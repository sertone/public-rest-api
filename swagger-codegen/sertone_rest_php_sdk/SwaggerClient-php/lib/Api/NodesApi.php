<?php
/**
 * NodesApi
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

namespace Swagger\Client\Api;

use \Swagger\Client\Configuration;
use \Swagger\Client\ApiClient;
use \Swagger\Client\ApiException;
use \Swagger\Client\ObjectSerializer;

/**
 * NodesApi Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   http://github.com/swagger-api/swagger-codegen
 * @license  http://www.apache.org/licenses/LICENSE-2.0 Apache Licene v2
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class NodesApi
{

    /**
     * API Client
     *
     * @var \Swagger\Client\ApiClient instance of the ApiClient
     */
    protected $apiClient;

    /**
     * Constructor
     *
     * @param \Swagger\Client\ApiClient|null $apiClient The api client to use
     */
    public function __construct(\Swagger\Client\ApiClient $apiClient = null)
    {
        if ($apiClient == null) {
            $apiClient = new ApiClient();
            $apiClient->getConfig()->setHost('http://api.dds.sertone.com/v1');
        }

        $this->apiClient = $apiClient;
    }

    /**
     * Get API client
     *
     * @return \Swagger\Client\ApiClient get the API client
     */
    public function getApiClient()
    {
        return $this->apiClient;
    }

    /**
     * Set the API client
     *
     * @param \Swagger\Client\ApiClient $apiClient set the API client
     *
     * @return NodesApi
     */
    public function setApiClient(\Swagger\Client\ApiClient $apiClient)
    {
        $this->apiClient = $apiClient;
        return $this;
    }

    /**
     * Operation getNodesByUserId
     *
     * getNodesByUserId() - Gets all nodes owned by given user..
     *
     * @param string $user_id The userId whom to get owned nodes (required)
     *
     * @return \Swagger\Client\Model\Nodes[]
     * @throws \Swagger\Client\ApiException on non-2xx response
     */
    public function getNodesByUserId($user_id)
    {
        list($response) = $this->getNodesByUserIdWithHttpInfo($user_id);
        return $response;
    }


    /**
     * Operation getNodesByUserIdWithHttpInfo
     *
     * getNodesByUserId() - Gets all nodes owned by given user..
     *
     * @param string $user_id The userId whom to get owned nodes (required)
     *
     * @return Array of \Swagger\Client\Model\Nodes[], HTTP status code, HTTP response headers (array of strings)
     * @throws \Swagger\Client\ApiException on non-2xx response
     */
    public function getNodesByUserIdWithHttpInfo($user_id)
    {
        
        // verify the required parameter 'user_id' is set
        if ($user_id === null) {
            throw new \InvalidArgumentException('Missing the required parameter $user_id when calling getNodesByUserId');
        }

        // parse inputs
        $resourcePath = "/users/{userId}/nodes";
        $httpBody = '';
        $queryParams = array();
        $headerParams = array();
        $formParams = array();
        $_header_accept = $this->apiClient->selectHeaderAccept(array('application/xml', 'application/json'));
        if (!is_null($_header_accept)) {
            $headerParams['Accept'] = $_header_accept;
        }
        $headerParams['Content-Type'] = $this->apiClient->selectHeaderContentType(array('application/xml','application/json'));

        
        
        // path params
        if ($user_id !== null) {
            $resourcePath = str_replace(
                "{" . "userId" . "}",
                $this->apiClient->getSerializer()->toPathValue($user_id),
                $resourcePath
            );
        }
        // default format to json
        $resourcePath = str_replace("{format}", "json", $resourcePath);

        
        

        // for model (json/xml)
        if (isset($_tempBody)) {
            $httpBody = $_tempBody; // $_tempBody is the method argument, if present
        } elseif (count($formParams) > 0) {
            $httpBody = $formParams; // for HTTP post (form)
        }
        
        // this endpoint requires API key authentication
        $apiKey = $this->apiClient->getApiKeyWithPrefix('Authorization');
        if (strlen($apiKey) !== 0) {
            $headerParams['Authorization'] = $apiKey;
        }
        

        // this endpoint requires API key authentication
        $apiKey = $this->apiClient->getApiKeyWithPrefix('ClientID');
        if (strlen($apiKey) !== 0) {
            $headerParams['ClientID'] = $apiKey;
        }
        
        // make the API Call
        try {
            list($response, $statusCode, $httpHeader) = $this->apiClient->callApi(
                $resourcePath,
                'GET',
                $queryParams,
                $httpBody,
                $headerParams,
                '\Swagger\Client\Model\Nodes[]'
            );

            return array($this->apiClient->getSerializer()->deserialize($response, '\Swagger\Client\Model\Nodes[]', $httpHeader), $statusCode, $httpHeader);
        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = $this->apiClient->getSerializer()->deserialize($e->getResponseBody(), '\Swagger\Client\Model\Nodes[]', $e->getResponseHeaders());
                    $e->setResponseObject($data);
                    break;
            }

            throw $e;
        }
    }
    /**
     * Operation getNodesByUserIdAndSensorId
     *
     * getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user..
     *
     * @param string $user_id The userId where node will be retrieved (required)
     * @param string $dev_eui The sensorID to be retrieved (required)
     *
     * @return \Swagger\Client\Model\NodeInfo
     * @throws \Swagger\Client\ApiException on non-2xx response
     */
    public function getNodesByUserIdAndSensorId($user_id, $dev_eui)
    {
        list($response) = $this->getNodesByUserIdAndSensorIdWithHttpInfo($user_id, $dev_eui);
        return $response;
    }


    /**
     * Operation getNodesByUserIdAndSensorIdWithHttpInfo
     *
     * getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user..
     *
     * @param string $user_id The userId where node will be retrieved (required)
     * @param string $dev_eui The sensorID to be retrieved (required)
     *
     * @return Array of \Swagger\Client\Model\NodeInfo, HTTP status code, HTTP response headers (array of strings)
     * @throws \Swagger\Client\ApiException on non-2xx response
     */
    public function getNodesByUserIdAndSensorIdWithHttpInfo($user_id, $dev_eui)
    {
        
        // verify the required parameter 'user_id' is set
        if ($user_id === null) {
            throw new \InvalidArgumentException('Missing the required parameter $user_id when calling getNodesByUserIdAndSensorId');
        }

        // verify the required parameter 'dev_eui' is set
        if ($dev_eui === null) {
            throw new \InvalidArgumentException('Missing the required parameter $dev_eui when calling getNodesByUserIdAndSensorId');
        }

        // parse inputs
        $resourcePath = "/users/{userId}/nodes/{devEui}";
        $httpBody = '';
        $queryParams = array();
        $headerParams = array();
        $formParams = array();
        $_header_accept = $this->apiClient->selectHeaderAccept(array('application/xml', 'application/json'));
        if (!is_null($_header_accept)) {
            $headerParams['Accept'] = $_header_accept;
        }
        $headerParams['Content-Type'] = $this->apiClient->selectHeaderContentType(array('application/xml','application/json'));

        
        
        // path params
        if ($user_id !== null) {
            $resourcePath = str_replace(
                "{" . "userId" . "}",
                $this->apiClient->getSerializer()->toPathValue($user_id),
                $resourcePath
            );
        }// path params
        if ($dev_eui !== null) {
            $resourcePath = str_replace(
                "{" . "devEui" . "}",
                $this->apiClient->getSerializer()->toPathValue($dev_eui),
                $resourcePath
            );
        }
        // default format to json
        $resourcePath = str_replace("{format}", "json", $resourcePath);

        
        

        // for model (json/xml)
        if (isset($_tempBody)) {
            $httpBody = $_tempBody; // $_tempBody is the method argument, if present
        } elseif (count($formParams) > 0) {
            $httpBody = $formParams; // for HTTP post (form)
        }
        
        // this endpoint requires API key authentication
        $apiKey = $this->apiClient->getApiKeyWithPrefix('Authorization');
        if (strlen($apiKey) !== 0) {
            $headerParams['Authorization'] = $apiKey;
        }
        

        // this endpoint requires API key authentication
        $apiKey = $this->apiClient->getApiKeyWithPrefix('ClientID');
        if (strlen($apiKey) !== 0) {
            $headerParams['ClientID'] = $apiKey;
        }
        
        // make the API Call
        try {
            list($response, $statusCode, $httpHeader) = $this->apiClient->callApi(
                $resourcePath,
                'GET',
                $queryParams,
                $httpBody,
                $headerParams,
                '\Swagger\Client\Model\NodeInfo'
            );

            return array($this->apiClient->getSerializer()->deserialize($response, '\Swagger\Client\Model\NodeInfo', $httpHeader), $statusCode, $httpHeader);
        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = $this->apiClient->getSerializer()->deserialize($e->getResponseBody(), '\Swagger\Client\Model\NodeInfo', $e->getResponseHeaders());
                    $e->setResponseObject($data);
                    break;
            }

            throw $e;
        }
    }
}
