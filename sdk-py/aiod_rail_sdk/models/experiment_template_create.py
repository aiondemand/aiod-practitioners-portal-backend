# coding: utf-8

"""
    AIoD - RAIL

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.20240507-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from aiod_rail_sdk.models.asset_schema import AssetSchema
from aiod_rail_sdk.models.environment_var_def import EnvironmentVarDef
from aiod_rail_sdk.models.task_type import TaskType
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing_extensions import Self


class ExperimentTemplateCreate(BaseModel):
    """
    ExperimentTemplateCreate
    """  # noqa: E501

    name: StrictStr
    description: StrictStr
    task: TaskType
    datasets_schema: AssetSchema
    models_schema: AssetSchema
    envs_required: List[EnvironmentVarDef]
    envs_optional: List[EnvironmentVarDef]
    script: StrictStr
    pip_requirements: StrictStr
    public: StrictBool
    base_image: StrictStr
    __properties: ClassVar[List[str]] = [
        "name",
        "description",
        "task",
        "datasets_schema",
        "models_schema",
        "envs_required",
        "envs_optional",
        "script",
        "pip_requirements",
        "public",
        "base_image",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ExperimentTemplateCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of datasets_schema
        if self.datasets_schema:
            _dict["datasets_schema"] = self.datasets_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of models_schema
        if self.models_schema:
            _dict["models_schema"] = self.models_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in envs_required (list)
        _items = []
        if self.envs_required:
            for _item in self.envs_required:
                if _item:
                    _items.append(_item.to_dict())
            _dict["envs_required"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in envs_optional (list)
        _items = []
        if self.envs_optional:
            for _item in self.envs_optional:
                if _item:
                    _items.append(_item.to_dict())
            _dict["envs_optional"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExperimentTemplateCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "task": obj.get("task"),
                "datasets_schema": (
                    AssetSchema.from_dict(obj["datasets_schema"])
                    if obj.get("datasets_schema") is not None
                    else None
                ),
                "models_schema": (
                    AssetSchema.from_dict(obj["models_schema"])
                    if obj.get("models_schema") is not None
                    else None
                ),
                "envs_required": (
                    [
                        EnvironmentVarDef.from_dict(_item)
                        for _item in obj["envs_required"]
                    ]
                    if obj.get("envs_required") is not None
                    else None
                ),
                "envs_optional": (
                    [
                        EnvironmentVarDef.from_dict(_item)
                        for _item in obj["envs_optional"]
                    ]
                    if obj.get("envs_optional") is not None
                    else None
                ),
                "script": obj.get("script"),
                "pip_requirements": obj.get("pip_requirements"),
                "public": obj.get("public"),
                "base_image": obj.get("base_image"),
            }
        )
        return _obj
