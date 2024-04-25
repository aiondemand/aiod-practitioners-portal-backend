# coding: utf-8

"""
    AIoD - RAIL

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.20240209-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from aiod_rail_sdk.models.geo import Geo


class TestGeo(unittest.TestCase):
    """Geo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Geo:
        """Test Geo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Geo`
        """
        model = Geo()
        if include_optional:
            return Geo(
                latitude = 37.42242,
                longitude = -122.08585,
                elevation_millimeters = 56
            )
        else:
            return Geo(
        )
        """

    def testGeo(self):
        """Test Geo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
