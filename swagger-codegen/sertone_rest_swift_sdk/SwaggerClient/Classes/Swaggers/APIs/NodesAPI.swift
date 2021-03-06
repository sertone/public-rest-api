//
// NodesAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Alamofire



public class NodesAPI: APIBase {
    /**
     getNodesByUserId() - Gets all nodes owned by given user.
     
     - parameter userId: (path) The userId whom to get owned nodes 
     - parameter completion: completion handler to receive the data and the error objects
     */
    public class func getNodesByUserId(userId userId: String, completion: ((data: [Nodes]?, error: ErrorType?) -> Void)) {
        getNodesByUserIdWithRequestBuilder(userId: userId).execute { (response, error) -> Void in
            completion(data: response?.body, error: error);
        }
    }


    /**
     getNodesByUserId() - Gets all nodes owned by given user.
     - GET /users/{userId}/nodes
     - 
     - API Key:
       - type: apiKey Authorization 
       - name: server_token
     - API Key:
       - type: apiKey ClientID 
       - name: client_id
     - examples: [{contentType=application/xml, example=<Sensor>
  <regType>string</regType>
  <devEui>string</devEui>
  <appEui>string</appEui>
  <appKey>string</appKey>
  <appSKey>string</appSKey>
  <devAddr>string</devAddr>
  <nwkSKey>string</nwkSKey>
  <fcntUp>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntUp>
  <fcntDown>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntDown>
  <flags>string</flags>
</Sensor>}, {contentType=application/json, example=[ {
  "devAddr" : "aeiou",
  "appSKey" : "aeiou",
  "nwkSKey" : "aeiou",
  "flags" : "aeiou",
  "appKey" : "aeiou",
  "fcntUp" : "",
  "appEui" : "aeiou",
  "fcntDown" : "",
  "regType" : "aeiou",
  "devEui" : "aeiou"
} ]}]
     - examples: [{contentType=application/xml, example=<Sensor>
  <regType>string</regType>
  <devEui>string</devEui>
  <appEui>string</appEui>
  <appKey>string</appKey>
  <appSKey>string</appSKey>
  <devAddr>string</devAddr>
  <nwkSKey>string</nwkSKey>
  <fcntUp>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntUp>
  <fcntDown>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntDown>
  <flags>string</flags>
</Sensor>}, {contentType=application/json, example=[ {
  "devAddr" : "aeiou",
  "appSKey" : "aeiou",
  "nwkSKey" : "aeiou",
  "flags" : "aeiou",
  "appKey" : "aeiou",
  "fcntUp" : "",
  "appEui" : "aeiou",
  "fcntDown" : "",
  "regType" : "aeiou",
  "devEui" : "aeiou"
} ]}]
     
     - parameter userId: (path) The userId whom to get owned nodes 

     - returns: RequestBuilder<[Nodes]> 
     */
    public class func getNodesByUserIdWithRequestBuilder(userId userId: String) -> RequestBuilder<[Nodes]> {
        var path = "/users/{userId}/nodes"
        path = path.stringByReplacingOccurrencesOfString("{userId}", withString: "\(userId)", options: .LiteralSearch, range: nil)
        let URLString = SwaggerClientAPI.basePath + path

        let nillableParameters: [String:AnyObject?] = [:]
 
        let parameters = APIHelper.rejectNil(nillableParameters)
 
        let convertedParameters = APIHelper.convertBoolToString(parameters)
 
        let requestBuilder: RequestBuilder<[Nodes]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: URLString, parameters: convertedParameters, isBody: true)
    }

    /**
     getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user.
     
     - parameter userId: (path) The userId where node will be retrieved 
     - parameter devEui: (path) The sensorID to be retrieved 
     - parameter completion: completion handler to receive the data and the error objects
     */
    public class func getNodesByUserIdAndSensorId(userId userId: String, devEui: String, completion: ((data: NodeInfo?, error: ErrorType?) -> Void)) {
        getNodesByUserIdAndSensorIdWithRequestBuilder(userId: userId, devEui: devEui).execute { (response, error) -> Void in
            completion(data: response?.body, error: error);
        }
    }


    /**
     getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user.
     - GET /users/{userId}/nodes/{devEui}
     - 
     - API Key:
       - type: apiKey Authorization 
       - name: server_token
     - API Key:
       - type: apiKey ClientID 
       - name: client_id
     - examples: [{contentType=application/xml, example=<NodeInfo>
  <regType>string</regType>
  <devEui>string</devEui>
  <appEui>string</appEui>
  <appKey>string</appKey>
  <appSKey>string</appSKey>
  <devAddr>string</devAddr>
  <nwkSKey>string</nwkSKey>
  <fcntUp>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntUp>
  <fcntDown>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntDown>
  <flags>string</flags>
  <activated>true</activated>
</NodeInfo>}, {contentType=application/json, example={
  "devAddr" : "aeiou",
  "appSKey" : "aeiou",
  "nwkSKey" : "aeiou",
  "flags" : "aeiou",
  "appKey" : "aeiou",
  "fcntUp" : "",
  "appEui" : "aeiou",
  "fcntDown" : "",
  "regType" : "aeiou",
  "devEui" : "aeiou",
  "activated" : true
}}]
     - examples: [{contentType=application/xml, example=<NodeInfo>
  <regType>string</regType>
  <devEui>string</devEui>
  <appEui>string</appEui>
  <appKey>string</appKey>
  <appSKey>string</appSKey>
  <devAddr>string</devAddr>
  <nwkSKey>string</nwkSKey>
  <fcntUp>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntUp>
  <fcntDown>not implemented io.swagger.models.properties.BaseIntegerProperty@1121aa4d</fcntDown>
  <flags>string</flags>
  <activated>true</activated>
</NodeInfo>}, {contentType=application/json, example={
  "devAddr" : "aeiou",
  "appSKey" : "aeiou",
  "nwkSKey" : "aeiou",
  "flags" : "aeiou",
  "appKey" : "aeiou",
  "fcntUp" : "",
  "appEui" : "aeiou",
  "fcntDown" : "",
  "regType" : "aeiou",
  "devEui" : "aeiou",
  "activated" : true
}}]
     
     - parameter userId: (path) The userId where node will be retrieved 
     - parameter devEui: (path) The sensorID to be retrieved 

     - returns: RequestBuilder<NodeInfo> 
     */
    public class func getNodesByUserIdAndSensorIdWithRequestBuilder(userId userId: String, devEui: String) -> RequestBuilder<NodeInfo> {
        var path = "/users/{userId}/nodes/{devEui}"
        path = path.stringByReplacingOccurrencesOfString("{userId}", withString: "\(userId)", options: .LiteralSearch, range: nil)
        path = path.stringByReplacingOccurrencesOfString("{devEui}", withString: "\(devEui)", options: .LiteralSearch, range: nil)
        let URLString = SwaggerClientAPI.basePath + path

        let nillableParameters: [String:AnyObject?] = [:]
 
        let parameters = APIHelper.rejectNil(nillableParameters)
 
        let convertedParameters = APIHelper.convertBoolToString(parameters)
 
        let requestBuilder: RequestBuilder<NodeInfo>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: URLString, parameters: convertedParameters, isBody: true)
    }

}
