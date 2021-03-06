//
// Applications.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public class Applications: JSONEncodable {
    public var id: Int64?
    public var appEui: String?
    /** Name or Title of the application */
    public var name: String?
    public var owner: String?
    public var accessKeys: String?
    public var valid: Bool?

    public init() {}

    // MARK: JSONEncodable
    func encodeToJSON() -> AnyObject {
        var nillableDictionary = [String:AnyObject?]()
        nillableDictionary["id"] = self.id?.encodeToJSON()
        nillableDictionary["appEui"] = self.appEui
        nillableDictionary["name"] = self.name
        nillableDictionary["owner"] = self.owner
        nillableDictionary["accessKeys"] = self.accessKeys
        nillableDictionary["valid"] = self.valid
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}
