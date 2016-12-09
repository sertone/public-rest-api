<?php
/**
 * Gateways
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   http://github.com/swagger-api/swagger-codegen
 * @license  http://www.apache.org/licenses/LICENSE-2.0 Apache Licene v2
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * SERTONE REST API
 *
 * This is the SERTONE REST API server for the  Sertone IOT Developers.  You can find out more about IOT at [http://www.sertone.com](http://www.sertone.com) or about the API on [API Reference](http://dev.sertone.com/public-rest-api).
 *
 * OpenAPI spec version: 0.0.1
 * Contact: email@sertone.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;

/**
 * Gateways Class Doc Comment
 *
 * @category    Class
 * @package     Swagger\Client
 * @author      http://github.com/swagger-api/swagger-codegen
 * @license     http://www.apache.org/licenses/LICENSE-2.0 Apache Licene v2
 * @link        https://github.com/swagger-api/swagger-codegen
 */
class Gateways implements ArrayAccess
{
    /**
      * The original name of the model.
      * @var string
      */
    protected static $swaggerModelName = 'Gateways';

    /**
      * Array of property to type mappings. Used for (de)serialization
      * @var string[]
      */
    protected static $swaggerTypes = array(
        'id' => 'int',
        'owner' => 'string',
        'gateway_eui' => 'string',
        'gateway_status' => 'string',
        'longitude' => 'string',
        'latitude' => 'string',
        'altitude' => 'string',
        'address' => 'string',
        'base_model' => 'string',
        'city' => 'string',
        'concentrator' => 'string',
        'country' => 'string',
        'freq_plan' => 'string',
        'region' => 'string',
        'rel_customer_uid' => 'string',
        'gateway_title' => 'string',
        'zip_code' => 'string',
        'created_on' => 'string'
    );

    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of attributes where the key is the local name, and the value is the original name
     * @var string[]
     */
    protected static $attributeMap = array(
        'id' => 'id',
        'owner' => 'owner',
        'gateway_eui' => 'gateway_eui',
        'gateway_status' => 'gateway_status',
        'longitude' => 'longitude',
        'latitude' => 'latitude',
        'altitude' => 'altitude',
        'address' => 'address',
        'base_model' => 'base_model',
        'city' => 'city',
        'concentrator' => 'concentrator',
        'country' => 'country',
        'freq_plan' => 'freq_plan',
        'region' => 'region',
        'rel_customer_uid' => 'rel_customer_uid',
        'gateway_title' => 'gateway_title',
        'zip_code' => 'zip_code',
        'created_on' => 'created_on'
    );

    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     * @var string[]
     */
    protected static $setters = array(
        'id' => 'setId',
        'owner' => 'setOwner',
        'gateway_eui' => 'setGatewayEui',
        'gateway_status' => 'setGatewayStatus',
        'longitude' => 'setLongitude',
        'latitude' => 'setLatitude',
        'altitude' => 'setAltitude',
        'address' => 'setAddress',
        'base_model' => 'setBaseModel',
        'city' => 'setCity',
        'concentrator' => 'setConcentrator',
        'country' => 'setCountry',
        'freq_plan' => 'setFreqPlan',
        'region' => 'setRegion',
        'rel_customer_uid' => 'setRelCustomerUid',
        'gateway_title' => 'setGatewayTitle',
        'zip_code' => 'setZipCode',
        'created_on' => 'setCreatedOn'
    );

    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     * @var string[]
     */
    protected static $getters = array(
        'id' => 'getId',
        'owner' => 'getOwner',
        'gateway_eui' => 'getGatewayEui',
        'gateway_status' => 'getGatewayStatus',
        'longitude' => 'getLongitude',
        'latitude' => 'getLatitude',
        'altitude' => 'getAltitude',
        'address' => 'getAddress',
        'base_model' => 'getBaseModel',
        'city' => 'getCity',
        'concentrator' => 'getConcentrator',
        'country' => 'getCountry',
        'freq_plan' => 'getFreqPlan',
        'region' => 'getRegion',
        'rel_customer_uid' => 'getRelCustomerUid',
        'gateway_title' => 'getGatewayTitle',
        'zip_code' => 'getZipCode',
        'created_on' => 'getCreatedOn'
    );

    public static function getters()
    {
        return self::$getters;
    }

    

    

    /**
     * Associative array for storing property values
     * @var mixed[]
     */
    protected $container = array();

    /**
     * Constructor
     * @param mixed[] $data Associated array of property value initalizing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['owner'] = isset($data['owner']) ? $data['owner'] : null;
        $this->container['gateway_eui'] = isset($data['gateway_eui']) ? $data['gateway_eui'] : null;
        $this->container['gateway_status'] = isset($data['gateway_status']) ? $data['gateway_status'] : null;
        $this->container['longitude'] = isset($data['longitude']) ? $data['longitude'] : null;
        $this->container['latitude'] = isset($data['latitude']) ? $data['latitude'] : null;
        $this->container['altitude'] = isset($data['altitude']) ? $data['altitude'] : null;
        $this->container['address'] = isset($data['address']) ? $data['address'] : null;
        $this->container['base_model'] = isset($data['base_model']) ? $data['base_model'] : null;
        $this->container['city'] = isset($data['city']) ? $data['city'] : null;
        $this->container['concentrator'] = isset($data['concentrator']) ? $data['concentrator'] : null;
        $this->container['country'] = isset($data['country']) ? $data['country'] : null;
        $this->container['freq_plan'] = isset($data['freq_plan']) ? $data['freq_plan'] : null;
        $this->container['region'] = isset($data['region']) ? $data['region'] : null;
        $this->container['rel_customer_uid'] = isset($data['rel_customer_uid']) ? $data['rel_customer_uid'] : null;
        $this->container['gateway_title'] = isset($data['gateway_title']) ? $data['gateway_title'] : null;
        $this->container['zip_code'] = isset($data['zip_code']) ? $data['zip_code'] : null;
        $this->container['created_on'] = isset($data['created_on']) ? $data['created_on'] : null;
    }

    /**
     * show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalid_properties = array();
        return $invalid_properties;
    }

    /**
     * validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properteis are valid
     */
    public function valid()
    {
        return true;
    }


    /**
     * Gets id
     * @return int
     */
    public function getId()
    {
        return $this->container['id'];
    }

    /**
     * Sets id
     * @param int $id
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets owner
     * @return string
     */
    public function getOwner()
    {
        return $this->container['owner'];
    }

    /**
     * Sets owner
     * @param string $owner
     * @return $this
     */
    public function setOwner($owner)
    {
        $this->container['owner'] = $owner;

        return $this;
    }

    /**
     * Gets gateway_eui
     * @return string
     */
    public function getGatewayEui()
    {
        return $this->container['gateway_eui'];
    }

    /**
     * Sets gateway_eui
     * @param string $gateway_eui
     * @return $this
     */
    public function setGatewayEui($gateway_eui)
    {
        $this->container['gateway_eui'] = $gateway_eui;

        return $this;
    }

    /**
     * Gets gateway_status
     * @return string
     */
    public function getGatewayStatus()
    {
        return $this->container['gateway_status'];
    }

    /**
     * Sets gateway_status
     * @param string $gateway_status Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated
     * @return $this
     */
    public function setGatewayStatus($gateway_status)
    {
        $this->container['gateway_status'] = $gateway_status;

        return $this;
    }

    /**
     * Gets longitude
     * @return string
     */
    public function getLongitude()
    {
        return $this->container['longitude'];
    }

    /**
     * Sets longitude
     * @param string $longitude
     * @return $this
     */
    public function setLongitude($longitude)
    {
        $this->container['longitude'] = $longitude;

        return $this;
    }

    /**
     * Gets latitude
     * @return string
     */
    public function getLatitude()
    {
        return $this->container['latitude'];
    }

    /**
     * Sets latitude
     * @param string $latitude
     * @return $this
     */
    public function setLatitude($latitude)
    {
        $this->container['latitude'] = $latitude;

        return $this;
    }

    /**
     * Gets altitude
     * @return string
     */
    public function getAltitude()
    {
        return $this->container['altitude'];
    }

    /**
     * Sets altitude
     * @param string $altitude
     * @return $this
     */
    public function setAltitude($altitude)
    {
        $this->container['altitude'] = $altitude;

        return $this;
    }

    /**
     * Gets address
     * @return string
     */
    public function getAddress()
    {
        return $this->container['address'];
    }

    /**
     * Sets address
     * @param string $address
     * @return $this
     */
    public function setAddress($address)
    {
        $this->container['address'] = $address;

        return $this;
    }

    /**
     * Gets base_model
     * @return string
     */
    public function getBaseModel()
    {
        return $this->container['base_model'];
    }

    /**
     * Sets base_model
     * @param string $base_model
     * @return $this
     */
    public function setBaseModel($base_model)
    {
        $this->container['base_model'] = $base_model;

        return $this;
    }

    /**
     * Gets city
     * @return string
     */
    public function getCity()
    {
        return $this->container['city'];
    }

    /**
     * Sets city
     * @param string $city
     * @return $this
     */
    public function setCity($city)
    {
        $this->container['city'] = $city;

        return $this;
    }

    /**
     * Gets concentrator
     * @return string
     */
    public function getConcentrator()
    {
        return $this->container['concentrator'];
    }

    /**
     * Sets concentrator
     * @param string $concentrator
     * @return $this
     */
    public function setConcentrator($concentrator)
    {
        $this->container['concentrator'] = $concentrator;

        return $this;
    }

    /**
     * Gets country
     * @return string
     */
    public function getCountry()
    {
        return $this->container['country'];
    }

    /**
     * Sets country
     * @param string $country
     * @return $this
     */
    public function setCountry($country)
    {
        $this->container['country'] = $country;

        return $this;
    }

    /**
     * Gets freq_plan
     * @return string
     */
    public function getFreqPlan()
    {
        return $this->container['freq_plan'];
    }

    /**
     * Sets freq_plan
     * @param string $freq_plan
     * @return $this
     */
    public function setFreqPlan($freq_plan)
    {
        $this->container['freq_plan'] = $freq_plan;

        return $this;
    }

    /**
     * Gets region
     * @return string
     */
    public function getRegion()
    {
        return $this->container['region'];
    }

    /**
     * Sets region
     * @param string $region
     * @return $this
     */
    public function setRegion($region)
    {
        $this->container['region'] = $region;

        return $this;
    }

    /**
     * Gets rel_customer_uid
     * @return string
     */
    public function getRelCustomerUid()
    {
        return $this->container['rel_customer_uid'];
    }

    /**
     * Sets rel_customer_uid
     * @param string $rel_customer_uid
     * @return $this
     */
    public function setRelCustomerUid($rel_customer_uid)
    {
        $this->container['rel_customer_uid'] = $rel_customer_uid;

        return $this;
    }

    /**
     * Gets gateway_title
     * @return string
     */
    public function getGatewayTitle()
    {
        return $this->container['gateway_title'];
    }

    /**
     * Sets gateway_title
     * @param string $gateway_title
     * @return $this
     */
    public function setGatewayTitle($gateway_title)
    {
        $this->container['gateway_title'] = $gateway_title;

        return $this;
    }

    /**
     * Gets zip_code
     * @return string
     */
    public function getZipCode()
    {
        return $this->container['zip_code'];
    }

    /**
     * Sets zip_code
     * @param string $zip_code
     * @return $this
     */
    public function setZipCode($zip_code)
    {
        $this->container['zip_code'] = $zip_code;

        return $this;
    }

    /**
     * Gets created_on
     * @return string
     */
    public function getCreatedOn()
    {
        return $this->container['created_on'];
    }

    /**
     * Sets created_on
     * @param string $created_on
     * @return $this
     */
    public function setCreatedOn($created_on)
    {
        $this->container['created_on'] = $created_on;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     * @param  integer $offset Offset
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     * @param  integer $offset Offset
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     * @param  integer $offset Offset
     * @param  mixed   $value  Value to be set
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     * @param  integer $offset Offset
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(\Swagger\Client\ObjectSerializer::sanitizeForSerialization($this), JSON_PRETTY_PRINT);
        }

        return json_encode(\Swagger\Client\ObjectSerializer::sanitizeForSerialization($this));
    }
}
