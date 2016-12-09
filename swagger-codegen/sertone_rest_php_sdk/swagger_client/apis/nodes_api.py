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


class NodesApi(object):
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

    def get_nodes_by_user_id(self, user_id, **kwargs):
        """
        getNodesByUserId() - Gets all nodes owned by given user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_nodes_by_user_id(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The userId whom to get owned nodes (required)
        :return: list[Nodes]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_by_user_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_nodes_by_user_id`")

        resource_path = '/users/{userId}/nodes'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='list[Nodes]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_nodes_by_user_id_and_sensor_id(self, user_id, dev_eui, **kwargs):
        """
        getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_nodes_by_user_id_and_sensor_id(user_id, dev_eui, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The userId where node will be retrieved (required)
        :param str dev_eui: The sensorID to be retrieved (required)
        :return: NodeInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'dev_eui']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_by_user_id_and_sensor_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_nodes_by_user_id_and_sensor_id`")
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params) or (params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `get_nodes_by_user_id_and_sensor_id`")

        resource_path = '/users/{userId}/nodes/{devEui}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
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
                                            response_type='NodeInfo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
