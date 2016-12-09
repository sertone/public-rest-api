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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DataApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_app_dev_data_payload(self, app_eui, dev_eui, **kwargs):
        """
        getAppDevDataPayload() - Gets payload data of given application and device.
        This can only be done by the logged in users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_dev_data_payload(app_eui, dev_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_eui: The appEui where payload will be retrieved (required)
        :param str dev_eui: The devEui where payload will be retrieved (required)
        :return: list[DataPayload]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_eui', 'dev_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_dev_data_payload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_eui' is set
        if ('app_eui' not in params) or (params['app_eui'] is None):
            raise ValueError("Missing the required parameter `app_eui` when calling `get_app_dev_data_payload`")
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params) or (params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `get_app_dev_data_payload`")

        resource_path = '/data/{appEui}/nodes/{devEui}'.replace('{format}', 'json')
        path_params = {}
        if 'app_eui' in params:
            path_params['appEui'] = params['app_eui']
        if 'dev_eui' in params:
            path_params['devEui'] = params['dev_eui']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = ['server_token', 'client_id']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DataPayload]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_app_dev_last_data_timestamp(self, app_eui, dev_eui, **kwargs):
        """
        getAppDevLastDataTimestamp() - Gets last data timestamp for a given application and device.
        This can only be done by the logged in users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_dev_last_data_timestamp(app_eui, dev_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_eui: The appEui whom to get last timestamp (required)
        :param str dev_eui: The devEui whom to get last timestamp (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_eui', 'dev_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_dev_last_data_timestamp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_eui' is set
        if ('app_eui' not in params) or (params['app_eui'] is None):
            raise ValueError("Missing the required parameter `app_eui` when calling `get_app_dev_last_data_timestamp`")
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params) or (params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `get_app_dev_last_data_timestamp`")

        resource_path = '/data/{appEui}/nodes/{devEui}/timestamp'.replace('{format}', 'json')
        path_params = {}
        if 'app_eui' in params:
            path_params['appEui'] = params['app_eui']
        if 'dev_eui' in params:
            path_params['devEui'] = params['dev_eui']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = ['server_token', 'client_id']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_app_dev_latest_counter(self, app_eui, dev_eui, **kwargs):
        """
        getAppDevLatestCounter() - Gets the latest counter for a given application and device.
        This can only be done by the logged in users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_dev_latest_counter(app_eui, dev_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_eui: The appEui whom to get last timestamp (required)
        :param str dev_eui: The devEui whom to get last timestamp (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_eui', 'dev_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_dev_latest_counter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_eui' is set
        if ('app_eui' not in params) or (params['app_eui'] is None):
            raise ValueError("Missing the required parameter `app_eui` when calling `get_app_dev_latest_counter`")
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params) or (params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `get_app_dev_latest_counter`")

        resource_path = '/data/{appEui}/nodes/{devEui}/count'.replace('{format}', 'json')
        path_params = {}
        if 'app_eui' in params:
            path_params['appEui'] = params['app_eui']
        if 'dev_eui' in params:
            path_params['devEui'] = params['dev_eui']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = ['server_token', 'client_id']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_app_last_data_method(self, app_eui, **kwargs):
        """
        getAppLastDataMethod() - Gets last data delivery method for a given application.
        This can only be done by the logged in users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_last_data_method(app_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_eui: The appEui whom to get last timestamp (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_last_data_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_eui' is set
        if ('app_eui' not in params) or (params['app_eui'] is None):
            raise ValueError("Missing the required parameter `app_eui` when calling `get_app_last_data_method`")

        resource_path = '/data/{appEui}/method'.replace('{format}', 'json')
        path_params = {}
        if 'app_eui' in params:
            path_params['appEui'] = params['app_eui']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = ['server_token', 'client_id']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_app_last_data_timestamp(self, app_eui, **kwargs):
        """
        getAppLastDataTimestamp() - Gets last data timestamp for a given application.
        This can only be done by the logged in users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_last_data_timestamp(app_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_eui: The appEui whom to get last timestamp (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_last_data_timestamp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_eui' is set
        if ('app_eui' not in params) or (params['app_eui'] is None):
            raise ValueError("Missing the required parameter `app_eui` when calling `get_app_last_data_timestamp`")

        resource_path = '/data/{appEui}/timestamp'.replace('{format}', 'json')
        path_params = {}
        if 'app_eui' in params:
            path_params['appEui'] = params['app_eui']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = ['server_token', 'client_id']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
