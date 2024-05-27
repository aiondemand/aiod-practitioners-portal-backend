import asyncio
import json
import shutil
from datetime import datetime, timezone
from functools import partial
from pathlib import Path

from beanie import Document, Indexed, PydanticObjectId
from pydantic import Field

from app.config import (
    EXPERIMENT_RUN_DIR_PREFIX,
    LOGS_FILENAME,
    METRICS_FILENAME,
    settings,
)
from app.schemas.experiment_run import ExperimentRunDetails, ExperimentRunResponse
from app.schemas.states import RunState


class ExperimentRun(Document):
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=timezone.utc))
    updated_at: datetime = Field(default_factory=partial(datetime.now, tz=timezone.utc))
    retry_count: int = 0
    state: RunState = RunState.CREATED
    created_by: str
    public: bool
    archived: bool = False
    experiment_id: Indexed(PydanticObjectId)  # type: ignore

    @property
    def logs(self) -> str:
        log_path = self.run_path / LOGS_FILENAME
        return log_path.read_text() if log_path.is_file() else ""

    @property
    def metrics(self) -> dict[str, float]:
        m_path = self.run_output_path / METRICS_FILENAME
        if m_path.exists() is False:
            return {}

        with open(m_path) as f:
            metrics = json.load(f)
        return metrics

    @property
    def workflow_name(self) -> str:
        return f"{EXPERIMENT_RUN_DIR_PREFIX}{str(self.id)}"

    @property
    def run_path(self) -> Path:
        return settings.get_experiment_run_path(self.id)

    @property
    def run_output_path(self) -> Path:
        return settings.get_experiment_run_output_path(self.id)

    class Settings:
        name = "experimentRuns"

    async def update_state_in_db(self, state: RunState) -> None:
        self.state = state
        self.updated_at = datetime.now(tz=timezone.utc)

        await self.set(
            {ExperimentRun.state: self.state, ExperimentRun.updated_at: self.updated_at}
        )

    def map_to_response(
        self, user: dict | None = None, return_detailed_response: bool = False
    ) -> ExperimentRunResponse | ExperimentRunDetails:
        mine = user is not None and self.created_by == user["email"]
        response = ExperimentRunResponse(**self.dict(), metrics=self.metrics, mine=mine)

        if return_detailed_response is False:
            return response
        return ExperimentRunDetails(**response.dict(), logs=self.logs)

    def retry_failed_run(self):
        return ExperimentRun(
            created_by=self.created_by,
            public=self.public,
            archived=self.archived,
            experiment_id=self.experiment_id,
            retry_count=self.retry_count + 1,
        )

    async def delete_files(self) -> None:
        await asyncio.to_thread(shutil.rmtree, self.run_path)
