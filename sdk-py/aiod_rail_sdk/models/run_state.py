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
from enum import Enum

from typing_extensions import Self


class RunState(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    CRASHED = "CRASHED"
    FINISHED = "FINISHED"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RunState from a JSON string"""
        return cls(json.loads(json_str))
