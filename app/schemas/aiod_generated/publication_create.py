# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublicationCreate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublicationCreate - a model defined in OpenAPI

        platform: The platform of this PublicationCreate [Optional].
        platform_identifier: The platform_identifier of this PublicationCreate [Optional].
        title: The title of this PublicationCreate.
        doi: The doi of this PublicationCreate [Optional].
        creators: The creators of this PublicationCreate [Optional].
        access_right: The access_right of this PublicationCreate [Optional].
        date_created: The date_created of this PublicationCreate [Optional].
        date_published: The date_published of this PublicationCreate [Optional].
        url: The url of this PublicationCreate [Optional].
        datasets: The datasets of this PublicationCreate.
        license: The license of this PublicationCreate [Optional].
        resource_type: The resource_type of this PublicationCreate [Optional].
    """

    platform: Optional[str] = Field(alias="platform", default=None)
    platform_identifier: Optional[str] = Field(
        alias="platform_identifier", default=None
    )
    title: str = Field(alias="title")
    doi: Optional[str] = Field(alias="doi", default=None)
    creators: Optional[str] = Field(alias="creators", default=None)
    access_right: Optional[str] = Field(alias="access_right", default=None)
    date_created: Optional[datetime] = Field(alias="date_created", default=None)
    date_published: Optional[datetime] = Field(alias="date_published", default=None)
    url: Optional[str] = Field(alias="url", default=None)
    datasets: List[int] = Field(alias="datasets")
    license: Optional[str] = Field(alias="license", default=None)
    resource_type: Optional[str] = Field(alias="resource_type", default=None)

    @validator("title")
    def title_max_length(cls, value):
        assert len(value) <= 250
        return value

    @validator("doi")
    def doi_max_length(cls, value):
        assert len(value) <= 150
        return value

    @validator("creators")
    def creators_max_length(cls, value):
        assert len(value) <= 450
        return value

    @validator("access_right")
    def access_right_max_length(cls, value):
        assert len(value) <= 150
        return value

    @validator("url")
    def url_max_length(cls, value):
        assert len(value) <= 250
        return value


PublicationCreate.update_forward_refs()
