from __future__ import annotations

import re
from datetime import datetime, timezone
from functools import partial
from pathlib import Path

import pymongo
import yaml
from beanie import Document, Indexed
from deepdiff import DeepDiff
from pydantic import Field

from app.config import (
    EXPERIMENT_TEMPLATE_DIR_PREFIX,
    REPOSITORY_NAME,
    RESERVED_ENV_VARS,
    RUN_TEMP_OUTPUT_FOLDER,
    settings,
)
from app.schemas.env_vars import EnvironmentVar, EnvironmentVarDef
from app.schemas.experiment_template import (
    AssetSchema,
    ExperimentTemplateCreate,
    ExperimentTemplateResponse,
    TaskType,
)
from app.schemas.states import TemplateState
from app.services.aiod import get_dataset_name, get_model_name


class ExperimentTemplate(Document):
    name: Indexed(str, index_type=pymongo.TEXT)  # type: ignore
    description: str
    task: TaskType
    datasets_schema: AssetSchema
    models_schema: AssetSchema
    envs_required: list[EnvironmentVarDef]
    envs_optional: list[EnvironmentVarDef]
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=timezone.utc))
    updated_at: datetime = Field(default_factory=partial(datetime.now, tz=timezone.utc))
    state: TemplateState = TemplateState.CREATED
    retry_count: int = 0
    approved: bool = False
    created_by: str
    archived: bool = False
    public: bool = True

    @property
    def environment_attribute_names(self) -> list[str]:
        return [
            "task",
            "datasets_schema",
            "models_schema",
            "envs_required",
            "envs_optional",
            "base_image",
            "pip_requirements",
            "script",
        ]

    @property
    def experiment_template_path(self) -> Path:
        return settings.get_experiment_template_path(template_id=self.id)

    @property
    def base_image(self) -> str:
        if self.dockerfile == "":
            return ""

        first_line = self.dockerfile.split("\n")[0]
        if re.fullmatch(r"FROM \S+", first_line) is None:
            return ""

        return first_line[5:]

    @property
    def dockerfile(self) -> str:
        path = self.experiment_template_path.joinpath("Dockerfile")
        if path.exists():
            return path.read_text()
        return ""

    @property
    def pip_requirements(self) -> str:
        path = self.experiment_template_path.joinpath("requirements.txt")
        if path.exists():
            return path.read_text()
        return ""

    @property
    def script(self) -> str:
        path = self.experiment_template_path.joinpath("script.py")
        if path.exists():
            return path.read_text()
        return ""

    @property
    def image_name(self) -> str:
        image_tag = f"{EXPERIMENT_TEMPLATE_DIR_PREFIX}{self.id}"
        return f"{settings.DOCKER_REGISTRY_URL}/{REPOSITORY_NAME}:{image_tag}"

    @property
    def allows_experiment_creation(self) -> bool:
        return self.state == TemplateState.FINISHED and self.archived is False

    class Settings:
        name = "experimentTemplates"

    def is_valid(self) -> bool:
        env_names = [e.name for e in self.envs_required + self.envs_optional]
        allowed_names = [name not in RESERVED_ENV_VARS for name in env_names]

        return sum(allowed_names) == len(env_names)

    def initialize_files(self, base_image, pip_requirements, script):
        base_path = self.experiment_template_path
        base_path.mkdir(exist_ok=True, parents=True)

        # TODO check https://docs.bentoml.org/en/latest/guides/containerization.html#dockerfile-template
        # for working with dockerfile templates
        with open("app/data/template-Dockerfile") as f:
            dockerfile_template_lines = f.readlines()
            dockerfile_template_lines[0] = f"FROM {base_image}\n"
            dockerfile = "".join(dockerfile_template_lines)

        base_path.joinpath("Dockerfile").write_text(dockerfile)
        base_path.joinpath("requirements.txt").write_text(pip_requirements)
        base_path.joinpath("script.py").write_text(script)

        reana_cfg = yaml.safe_load(open("app/data/template-reana.yaml"))
        reana_cfg["workflow"]["specification"]["steps"][0][
            "environment"
        ] = self.image_name
        reana_cfg["outputs"]["directories"][0] = RUN_TEMP_OUTPUT_FOLDER

        with base_path.joinpath("reana.yaml").open("w") as fp:
            yaml.safe_dump(reana_cfg, fp)

    def map_to_response(self, user: dict | None = None) -> ExperimentTemplateResponse:
        mine = user is not None and self.created_by == user["email"]
        return ExperimentTemplateResponse(
            **self.dict(),
            dockerfile=self.dockerfile,
            pip_requirements=self.pip_requirements,
            script=self.script,
            mine=mine,
        )

    def update_state(self, state: TemplateState) -> None:
        self.state = state
        self.updated_at = datetime.now(tz=timezone.utc)

    async def validate_models(self, model_ids: list[int]) -> bool:
        model_names = [await get_model_name(x) for x in model_ids]

        checks = [
            all(model_name is not None for model_name in model_names),
            self.models_schema.cardinality.is_valid(len(model_names)),
        ]

        return all(checks)

    async def validate_datasets(self, dataset_ids: list[int]) -> bool:
        dataset_names = [await get_dataset_name(x) for x in dataset_ids]

        checks = [
            all(dataset_name is not None for dataset_name in dataset_names),
            self.datasets_schema.cardinality.is_valid(len(dataset_names)),
        ]

        return all(checks)

    def validate_env_vars(self, env_vars: list[EnvironmentVar]) -> bool:
        experiment_environment_var_names = set([env.key for env in env_vars])
        required_environment_var_names = set([env.name for env in self.envs_required])

        return required_environment_var_names.issubset(experiment_environment_var_names)

    def is_same_environment(
        self, experiment_template_req: ExperimentTemplateCreate
    ) -> bool:
        return sum(
            [
                bool(
                    DeepDiff(
                        getattr(self, attr_name),
                        getattr(experiment_template_req, attr_name),
                        ignore_order=True,
                    )
                )
                is False
                for attr_name in self.environment_attribute_names
            ]
        ) == len(self.environment_attribute_names)

    @classmethod
    async def update_template(
        cls,
        original_template: ExperimentTemplate,
        experiment_template_req: ExperimentTemplateCreate,
        editable_environment: bool,
        editable_visibility: bool,
    ) -> ExperimentTemplate | None:
        new_template = ExperimentTemplate(
            **experiment_template_req.dict(), created_by=original_template.created_by
        )
        if new_template.is_valid() is False:
            return None

        same_environment = original_template.is_same_environment(
            experiment_template_req
        )
        same_visibility = original_template.public == experiment_template_req.public

        template_to_return = None
        if same_environment and (same_visibility or editable_visibility):
            # We modify only name & descr (+ maybe visibility)
            original_template.name = new_template.name
            original_template.description = new_template.description
            original_template.public = new_template.public

            original_template.updated_at = new_template.updated_at
            template_to_return = original_template

        elif editable_environment:
            # If there are no experiments tied to this template,
            # we can modify everything
            new_template.created_at = original_template.created_at
            new_template.id = original_template.id

            new_template.initialize_files(
                base_image=experiment_template_req.base_image,
                pip_requirements=experiment_template_req.pip_requirements,
                script=experiment_template_req.script,
            )
            template_to_return = new_template

        return template_to_return
