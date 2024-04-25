# coding: utf-8

"""
    AIoD - RAIL

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.20240209-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
from enum import Enum

from typing_extensions import Self


class TemplateState(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    CRASHED = "CRASHED"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TemplateState from a JSON string"""
        return cls(json.loads(json_str))
