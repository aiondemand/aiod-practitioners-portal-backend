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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self


class AIoDEntryRead(BaseModel):
    """
    AIoDEntryRead
    """  # noqa: E501

    editor: Optional[List[StrictInt]] = Field(
        default=None,
        description="Links to identifiers of persons responsible for maintaining the entry.",
    )
    status: Optional[StrictStr] = Field(
        default="draft", description="Status of the entry (published, draft, rejected)"
    )
    date_modified: Optional[datetime] = Field(
        default=None,
        description="The datetime on which the metadata was last updated in the AIoD platform,in UTC.  Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.",
    )
    date_created: Optional[datetime] = Field(
        default=None,
        description="The datetime on which the metadata was first published on the AIoD platform, in UTC.",
    )
    __properties: ClassVar[List[str]] = [
        "editor",
        "status",
        "date_modified",
        "date_created",
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
        """Create an instance of AIoDEntryRead from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AIoDEntryRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "editor": obj.get("editor"),
                "status": (
                    obj.get("status") if obj.get("status") is not None else "draft"
                ),
                "date_modified": obj.get("date_modified"),
                "date_created": obj.get("date_created"),
            }
        )
        return _obj
