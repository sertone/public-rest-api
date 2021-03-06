//
// GatewaysStatus.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public class GatewaysStatus: JSONEncodable {
    public var gatewayEui: String?
    /** Gateway activity can be Active, Inactive, Not Found */
    public var gatewayActivity: String?
    public var lastPullData: String?
    public var lastPushData: String?
    public var pullDataCount: String?
    public var pushDataCount: String?

    public init() {}

    // MARK: JSONEncodable
    func encodeToJSON() -> AnyObject {
        var nillableDictionary = [String:AnyObject?]()
        nillableDictionary["gateway_eui"] = self.gatewayEui
        nillableDictionary["gateway_activity"] = self.gatewayActivity
        nillableDictionary["last_pull_data"] = self.lastPullData
        nillableDictionary["last_push_data"] = self.lastPushData
        nillableDictionary["pull_data_count"] = self.pullDataCount
        nillableDictionary["push_data_count"] = self.pushDataCount
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}
