/**
 * SERTONE REST API
 * This is the SERTONE REST API server for the  Sertone IOT Developers.  You can find out more about IOT at [http://www.sertone.com](http://www.sertone.com) or about the API on [API Reference](http://dev.sertone.com/public-rest-api).
 *
 * OpenAPI spec version: 0.0.1
 * Contact: email@sertone.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.SertoneRestApi) {
      root.SertoneRestApi = {};
    }
    root.SertoneRestApi.Gateways = factory(root.SertoneRestApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The Gateways model module.
   * @module model/Gateways
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>Gateways</code>.
   * @alias module:model/Gateways
   * @class
   */
  var exports = function() {
    var _this = this;



















  };

  /**
   * Constructs a <code>Gateways</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Gateways} obj Optional instance to populate.
   * @return {module:model/Gateways} The populated <code>Gateways</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'Integer');
      }
      if (data.hasOwnProperty('owner')) {
        obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
      }
      if (data.hasOwnProperty('gateway_eui')) {
        obj['gateway_eui'] = ApiClient.convertToType(data['gateway_eui'], 'String');
      }
      if (data.hasOwnProperty('gateway_status')) {
        obj['gateway_status'] = ApiClient.convertToType(data['gateway_status'], 'String');
      }
      if (data.hasOwnProperty('longitude')) {
        obj['longitude'] = ApiClient.convertToType(data['longitude'], 'String');
      }
      if (data.hasOwnProperty('latitude')) {
        obj['latitude'] = ApiClient.convertToType(data['latitude'], 'String');
      }
      if (data.hasOwnProperty('altitude')) {
        obj['altitude'] = ApiClient.convertToType(data['altitude'], 'String');
      }
      if (data.hasOwnProperty('address')) {
        obj['address'] = ApiClient.convertToType(data['address'], 'String');
      }
      if (data.hasOwnProperty('base_model')) {
        obj['base_model'] = ApiClient.convertToType(data['base_model'], 'String');
      }
      if (data.hasOwnProperty('city')) {
        obj['city'] = ApiClient.convertToType(data['city'], 'String');
      }
      if (data.hasOwnProperty('concentrator')) {
        obj['concentrator'] = ApiClient.convertToType(data['concentrator'], 'String');
      }
      if (data.hasOwnProperty('country')) {
        obj['country'] = ApiClient.convertToType(data['country'], 'String');
      }
      if (data.hasOwnProperty('freq_plan')) {
        obj['freq_plan'] = ApiClient.convertToType(data['freq_plan'], 'String');
      }
      if (data.hasOwnProperty('region')) {
        obj['region'] = ApiClient.convertToType(data['region'], 'String');
      }
      if (data.hasOwnProperty('rel_customer_uid')) {
        obj['rel_customer_uid'] = ApiClient.convertToType(data['rel_customer_uid'], 'String');
      }
      if (data.hasOwnProperty('gateway_title')) {
        obj['gateway_title'] = ApiClient.convertToType(data['gateway_title'], 'String');
      }
      if (data.hasOwnProperty('zip_code')) {
        obj['zip_code'] = ApiClient.convertToType(data['zip_code'], 'String');
      }
      if (data.hasOwnProperty('created_on')) {
        obj['created_on'] = ApiClient.convertToType(data['created_on'], 'String');
      }
    }
    return obj;
  }

  /**
   * @member {Integer} id
   */
  exports.prototype['id'] = undefined;
  /**
   * @member {String} owner
   */
  exports.prototype['owner'] = undefined;
  /**
   * @member {String} gateway_eui
   */
  exports.prototype['gateway_eui'] = undefined;
  /**
   * Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated
   * @member {String} gateway_status
   */
  exports.prototype['gateway_status'] = undefined;
  /**
   * @member {String} longitude
   */
  exports.prototype['longitude'] = undefined;
  /**
   * @member {String} latitude
   */
  exports.prototype['latitude'] = undefined;
  /**
   * @member {String} altitude
   */
  exports.prototype['altitude'] = undefined;
  /**
   * @member {String} address
   */
  exports.prototype['address'] = undefined;
  /**
   * @member {String} base_model
   */
  exports.prototype['base_model'] = undefined;
  /**
   * @member {String} city
   */
  exports.prototype['city'] = undefined;
  /**
   * @member {String} concentrator
   */
  exports.prototype['concentrator'] = undefined;
  /**
   * @member {String} country
   */
  exports.prototype['country'] = undefined;
  /**
   * @member {String} freq_plan
   */
  exports.prototype['freq_plan'] = undefined;
  /**
   * @member {String} region
   */
  exports.prototype['region'] = undefined;
  /**
   * @member {String} rel_customer_uid
   */
  exports.prototype['rel_customer_uid'] = undefined;
  /**
   * @member {String} gateway_title
   */
  exports.prototype['gateway_title'] = undefined;
  /**
   * @member {String} zip_code
   */
  exports.prototype['zip_code'] = undefined;
  /**
   * @member {String} created_on
   */
  exports.prototype['created_on'] = undefined;




  return exports;
}));


