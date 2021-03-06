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


class Gateways(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, owner=None, gateway_eui=None, gateway_status=None, longitude=None, latitude=None, altitude=None, address=None, base_model=None, city=None, concentrator=None, country=None, freq_plan=None, region=None, rel_customer_uid=None, gateway_title=None, zip_code=None, created_on=None):
        """
        Gateways - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'owner': 'str',
            'gateway_eui': 'str',
            'gateway_status': 'str',
            'longitude': 'str',
            'latitude': 'str',
            'altitude': 'str',
            'address': 'str',
            'base_model': 'str',
            'city': 'str',
            'concentrator': 'str',
            'country': 'str',
            'freq_plan': 'str',
            'region': 'str',
            'rel_customer_uid': 'str',
            'gateway_title': 'str',
            'zip_code': 'str',
            'created_on': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'owner': 'owner',
            'gateway_eui': 'gateway_eui',
            'gateway_status': 'gateway_status',
            'longitude': 'longitude',
            'latitude': 'latitude',
            'altitude': 'altitude',
            'address': 'address',
            'base_model': 'base_model',
            'city': 'city',
            'concentrator': 'concentrator',
            'country': 'country',
            'freq_plan': 'freq_plan',
            'region': 'region',
            'rel_customer_uid': 'rel_customer_uid',
            'gateway_title': 'gateway_title',
            'zip_code': 'zip_code',
            'created_on': 'created_on'
        }

        self._id = id
        self._owner = owner
        self._gateway_eui = gateway_eui
        self._gateway_status = gateway_status
        self._longitude = longitude
        self._latitude = latitude
        self._altitude = altitude
        self._address = address
        self._base_model = base_model
        self._city = city
        self._concentrator = concentrator
        self._country = country
        self._freq_plan = freq_plan
        self._region = region
        self._rel_customer_uid = rel_customer_uid
        self._gateway_title = gateway_title
        self._zip_code = zip_code
        self._created_on = created_on

    @property
    def id(self):
        """
        Gets the id of this Gateways.


        :return: The id of this Gateways.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Gateways.


        :param id: The id of this Gateways.
        :type: int
        """

        self._id = id

    @property
    def owner(self):
        """
        Gets the owner of this Gateways.


        :return: The owner of this Gateways.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Gateways.


        :param owner: The owner of this Gateways.
        :type: str
        """

        self._owner = owner

    @property
    def gateway_eui(self):
        """
        Gets the gateway_eui of this Gateways.


        :return: The gateway_eui of this Gateways.
        :rtype: str
        """
        return self._gateway_eui

    @gateway_eui.setter
    def gateway_eui(self, gateway_eui):
        """
        Sets the gateway_eui of this Gateways.


        :param gateway_eui: The gateway_eui of this Gateways.
        :type: str
        """

        self._gateway_eui = gateway_eui

    @property
    def gateway_status(self):
        """
        Gets the gateway_status of this Gateways.
        Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated

        :return: The gateway_status of this Gateways.
        :rtype: str
        """
        return self._gateway_status

    @gateway_status.setter
    def gateway_status(self, gateway_status):
        """
        Sets the gateway_status of this Gateways.
        Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated

        :param gateway_status: The gateway_status of this Gateways.
        :type: str
        """

        self._gateway_status = gateway_status

    @property
    def longitude(self):
        """
        Gets the longitude of this Gateways.


        :return: The longitude of this Gateways.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Gateways.


        :param longitude: The longitude of this Gateways.
        :type: str
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """
        Gets the latitude of this Gateways.


        :return: The latitude of this Gateways.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Gateways.


        :param latitude: The latitude of this Gateways.
        :type: str
        """

        self._latitude = latitude

    @property
    def altitude(self):
        """
        Gets the altitude of this Gateways.


        :return: The altitude of this Gateways.
        :rtype: str
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """
        Sets the altitude of this Gateways.


        :param altitude: The altitude of this Gateways.
        :type: str
        """

        self._altitude = altitude

    @property
    def address(self):
        """
        Gets the address of this Gateways.


        :return: The address of this Gateways.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Gateways.


        :param address: The address of this Gateways.
        :type: str
        """

        self._address = address

    @property
    def base_model(self):
        """
        Gets the base_model of this Gateways.


        :return: The base_model of this Gateways.
        :rtype: str
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        """
        Sets the base_model of this Gateways.


        :param base_model: The base_model of this Gateways.
        :type: str
        """

        self._base_model = base_model

    @property
    def city(self):
        """
        Gets the city of this Gateways.


        :return: The city of this Gateways.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Gateways.


        :param city: The city of this Gateways.
        :type: str
        """

        self._city = city

    @property
    def concentrator(self):
        """
        Gets the concentrator of this Gateways.


        :return: The concentrator of this Gateways.
        :rtype: str
        """
        return self._concentrator

    @concentrator.setter
    def concentrator(self, concentrator):
        """
        Sets the concentrator of this Gateways.


        :param concentrator: The concentrator of this Gateways.
        :type: str
        """

        self._concentrator = concentrator

    @property
    def country(self):
        """
        Gets the country of this Gateways.


        :return: The country of this Gateways.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Gateways.


        :param country: The country of this Gateways.
        :type: str
        """

        self._country = country

    @property
    def freq_plan(self):
        """
        Gets the freq_plan of this Gateways.


        :return: The freq_plan of this Gateways.
        :rtype: str
        """
        return self._freq_plan

    @freq_plan.setter
    def freq_plan(self, freq_plan):
        """
        Sets the freq_plan of this Gateways.


        :param freq_plan: The freq_plan of this Gateways.
        :type: str
        """

        self._freq_plan = freq_plan

    @property
    def region(self):
        """
        Gets the region of this Gateways.


        :return: The region of this Gateways.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Gateways.


        :param region: The region of this Gateways.
        :type: str
        """

        self._region = region

    @property
    def rel_customer_uid(self):
        """
        Gets the rel_customer_uid of this Gateways.


        :return: The rel_customer_uid of this Gateways.
        :rtype: str
        """
        return self._rel_customer_uid

    @rel_customer_uid.setter
    def rel_customer_uid(self, rel_customer_uid):
        """
        Sets the rel_customer_uid of this Gateways.


        :param rel_customer_uid: The rel_customer_uid of this Gateways.
        :type: str
        """

        self._rel_customer_uid = rel_customer_uid

    @property
    def gateway_title(self):
        """
        Gets the gateway_title of this Gateways.


        :return: The gateway_title of this Gateways.
        :rtype: str
        """
        return self._gateway_title

    @gateway_title.setter
    def gateway_title(self, gateway_title):
        """
        Sets the gateway_title of this Gateways.


        :param gateway_title: The gateway_title of this Gateways.
        :type: str
        """

        self._gateway_title = gateway_title

    @property
    def zip_code(self):
        """
        Gets the zip_code of this Gateways.


        :return: The zip_code of this Gateways.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this Gateways.


        :param zip_code: The zip_code of this Gateways.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def created_on(self):
        """
        Gets the created_on of this Gateways.


        :return: The created_on of this Gateways.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Gateways.


        :param created_on: The created_on of this Gateways.
        :type: str
        """

        self._created_on = created_on

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
