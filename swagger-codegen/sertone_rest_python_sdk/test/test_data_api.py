# coding: utf-8

"""
    SERTONE REST API

    This is the SERTONE REST API server for the  Sertone IOT Developers.  You can find out more about IOT at [http://www.sertone.com](http://www.sertone.com) or about the API on [API Reference](http://dev.sertone.com/public-rest-api).

    OpenAPI spec version: 0.0.1
    Contact: email@sertone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.data_api import DataApi


class TestDataApi(unittest.TestCase):
    """ DataApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.data_api.DataApi()

    def tearDown(self):
        pass

    def test_get_app_dev_data_payload(self):
        """
        Test case for get_app_dev_data_payload

        getAppDevDataPayload() - Gets payload data of given application and device.
        """
        pass

    def test_get_app_dev_last_data_timestamp(self):
        """
        Test case for get_app_dev_last_data_timestamp

        getAppDevLastDataTimestamp() - Gets last data timestamp for a given application and device.
        """
        pass

    def test_get_app_dev_latest_counter(self):
        """
        Test case for get_app_dev_latest_counter

        getAppDevLatestCounter() - Gets the latest counter for a given application and device.
        """
        pass

    def test_get_app_last_data_method(self):
        """
        Test case for get_app_last_data_method

        getAppLastDataMethod() - Gets last data delivery method for a given application.
        """
        pass

    def test_get_app_last_data_timestamp(self):
        """
        Test case for get_app_last_data_timestamp

        getAppLastDataTimestamp() - Gets last data timestamp for a given application.
        """
        pass


if __name__ == '__main__':
    unittest.main()
