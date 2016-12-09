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

from pprint import pformat
from six import iteritems
import re


class DataPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dev_eui=None, app_eui=None, seq_num=None, last_data_received=None, payload=None):
        """
        DataPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dev_eui': 'str',
            'app_eui': 'str',
            'seq_num': 'int',
            'last_data_received': 'str',
            'payload': 'str'
        }

        self.attribute_map = {
            'dev_eui': 'devEui',
            'app_eui': 'appEui',
            'seq_num': 'seqNum',
            'last_data_received': 'lastDataReceived',
            'payload': 'payload'
        }

        self._dev_eui = dev_eui
        self._app_eui = app_eui
        self._seq_num = seq_num
        self._last_data_received = last_data_received
        self._payload = payload

    @property
    def dev_eui(self):
        """
        Gets the dev_eui of this DataPayload.


        :return: The dev_eui of this DataPayload.
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """
        Sets the dev_eui of this DataPayload.


        :param dev_eui: The dev_eui of this DataPayload.
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def app_eui(self):
        """
        Gets the app_eui of this DataPayload.


        :return: The app_eui of this DataPayload.
        :rtype: str
        """
        return self._app_eui

    @app_eui.setter
    def app_eui(self, app_eui):
        """
        Sets the app_eui of this DataPayload.


        :param app_eui: The app_eui of this DataPayload.
        :type: str
        """

        self._app_eui = app_eui

    @property
    def seq_num(self):
        """
        Gets the seq_num of this DataPayload.


        :return: The seq_num of this DataPayload.
        :rtype: int
        """
        return self._seq_num

    @seq_num.setter
    def seq_num(self, seq_num):
        """
        Sets the seq_num of this DataPayload.


        :param seq_num: The seq_num of this DataPayload.
        :type: int
        """

        self._seq_num = seq_num

    @property
    def last_data_received(self):
        """
        Gets the last_data_received of this DataPayload.


        :return: The last_data_received of this DataPayload.
        :rtype: str
        """
        return self._last_data_received

    @last_data_received.setter
    def last_data_received(self, last_data_received):
        """
        Sets the last_data_received of this DataPayload.


        :param last_data_received: The last_data_received of this DataPayload.
        :type: str
        """

        self._last_data_received = last_data_received

    @property
    def payload(self):
        """
        Gets the payload of this DataPayload.


        :return: The payload of this DataPayload.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this DataPayload.


        :param payload: The payload of this DataPayload.
        :type: str
        """

        self._payload = payload

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
