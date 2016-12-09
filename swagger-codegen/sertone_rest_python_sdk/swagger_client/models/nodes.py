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


class Nodes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, reg_type=None, dev_eui=None, app_eui=None, app_key=None, app_s_key=None, dev_addr=None, nwk_s_key=None, fcnt_up=None, fcnt_down=None, flags=None):
        """
        Nodes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'reg_type': 'str',
            'dev_eui': 'str',
            'app_eui': 'str',
            'app_key': 'str',
            'app_s_key': 'str',
            'dev_addr': 'str',
            'nwk_s_key': 'str',
            'fcnt_up': 'int',
            'fcnt_down': 'int',
            'flags': 'str'
        }

        self.attribute_map = {
            'reg_type': 'regType',
            'dev_eui': 'devEui',
            'app_eui': 'appEui',
            'app_key': 'appKey',
            'app_s_key': 'appSKey',
            'dev_addr': 'devAddr',
            'nwk_s_key': 'nwkSKey',
            'fcnt_up': 'fcntUp',
            'fcnt_down': 'fcntDown',
            'flags': 'flags'
        }

        self._reg_type = reg_type
        self._dev_eui = dev_eui
        self._app_eui = app_eui
        self._app_key = app_key
        self._app_s_key = app_s_key
        self._dev_addr = dev_addr
        self._nwk_s_key = nwk_s_key
        self._fcnt_up = fcnt_up
        self._fcnt_down = fcnt_down
        self._flags = flags

    @property
    def reg_type(self):
        """
        Gets the reg_type of this Nodes.
        Registration Type - OTAA or ABP

        :return: The reg_type of this Nodes.
        :rtype: str
        """
        return self._reg_type

    @reg_type.setter
    def reg_type(self, reg_type):
        """
        Sets the reg_type of this Nodes.
        Registration Type - OTAA or ABP

        :param reg_type: The reg_type of this Nodes.
        :type: str
        """

        self._reg_type = reg_type

    @property
    def dev_eui(self):
        """
        Gets the dev_eui of this Nodes.


        :return: The dev_eui of this Nodes.
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """
        Sets the dev_eui of this Nodes.


        :param dev_eui: The dev_eui of this Nodes.
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def app_eui(self):
        """
        Gets the app_eui of this Nodes.


        :return: The app_eui of this Nodes.
        :rtype: str
        """
        return self._app_eui

    @app_eui.setter
    def app_eui(self, app_eui):
        """
        Sets the app_eui of this Nodes.


        :param app_eui: The app_eui of this Nodes.
        :type: str
        """

        self._app_eui = app_eui

    @property
    def app_key(self):
        """
        Gets the app_key of this Nodes.


        :return: The app_key of this Nodes.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """
        Sets the app_key of this Nodes.


        :param app_key: The app_key of this Nodes.
        :type: str
        """

        self._app_key = app_key

    @property
    def app_s_key(self):
        """
        Gets the app_s_key of this Nodes.


        :return: The app_s_key of this Nodes.
        :rtype: str
        """
        return self._app_s_key

    @app_s_key.setter
    def app_s_key(self, app_s_key):
        """
        Sets the app_s_key of this Nodes.


        :param app_s_key: The app_s_key of this Nodes.
        :type: str
        """

        self._app_s_key = app_s_key

    @property
    def dev_addr(self):
        """
        Gets the dev_addr of this Nodes.


        :return: The dev_addr of this Nodes.
        :rtype: str
        """
        return self._dev_addr

    @dev_addr.setter
    def dev_addr(self, dev_addr):
        """
        Sets the dev_addr of this Nodes.


        :param dev_addr: The dev_addr of this Nodes.
        :type: str
        """

        self._dev_addr = dev_addr

    @property
    def nwk_s_key(self):
        """
        Gets the nwk_s_key of this Nodes.


        :return: The nwk_s_key of this Nodes.
        :rtype: str
        """
        return self._nwk_s_key

    @nwk_s_key.setter
    def nwk_s_key(self, nwk_s_key):
        """
        Sets the nwk_s_key of this Nodes.


        :param nwk_s_key: The nwk_s_key of this Nodes.
        :type: str
        """

        self._nwk_s_key = nwk_s_key

    @property
    def fcnt_up(self):
        """
        Gets the fcnt_up of this Nodes.


        :return: The fcnt_up of this Nodes.
        :rtype: int
        """
        return self._fcnt_up

    @fcnt_up.setter
    def fcnt_up(self, fcnt_up):
        """
        Sets the fcnt_up of this Nodes.


        :param fcnt_up: The fcnt_up of this Nodes.
        :type: int
        """

        self._fcnt_up = fcnt_up

    @property
    def fcnt_down(self):
        """
        Gets the fcnt_down of this Nodes.


        :return: The fcnt_down of this Nodes.
        :rtype: int
        """
        return self._fcnt_down

    @fcnt_down.setter
    def fcnt_down(self, fcnt_down):
        """
        Sets the fcnt_down of this Nodes.


        :param fcnt_down: The fcnt_down of this Nodes.
        :type: int
        """

        self._fcnt_down = fcnt_down

    @property
    def flags(self):
        """
        Gets the flags of this Nodes.


        :return: The flags of this Nodes.
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """
        Sets the flags of this Nodes.


        :param flags: The flags of this Nodes.
        :type: str
        """

        self._flags = flags

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
