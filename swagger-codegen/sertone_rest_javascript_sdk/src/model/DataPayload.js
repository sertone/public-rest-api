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
    root.SertoneRestApi.DataPayload = factory(root.SertoneRestApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The DataPayload model module.
   * @module model/DataPayload
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>DataPayload</code>.
   * @alias module:model/DataPayload
   * @class
   */
  var exports = function() {
    var _this = this;






  };

  /**
   * Constructs a <code>DataPayload</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/DataPayload} obj Optional instance to populate.
   * @return {module:model/DataPayload} The populated <code>DataPayload</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('devEui')) {
        obj['devEui'] = ApiClient.convertToType(data['devEui'], 'String');
      }
      if (data.hasOwnProperty('appEui')) {
        obj['appEui'] = ApiClient.convertToType(data['appEui'], 'String');
      }
      if (data.hasOwnProperty('seqNum')) {
        obj['seqNum'] = ApiClient.convertToType(data['seqNum'], 'Integer');
      }
      if (data.hasOwnProperty('lastDataReceived')) {
        obj['lastDataReceived'] = ApiClient.convertToType(data['lastDataReceived'], 'String');
      }
      if (data.hasOwnProperty('payload')) {
        obj['payload'] = ApiClient.convertToType(data['payload'], 'String');
      }
    }
    return obj;
  }

  /**
   * @member {String} devEui
   */
  exports.prototype['devEui'] = undefined;
  /**
   * @member {String} appEui
   */
  exports.prototype['appEui'] = undefined;
  /**
   * @member {Integer} seqNum
   */
  exports.prototype['seqNum'] = undefined;
  /**
   * @member {String} lastDataReceived
   */
  exports.prototype['lastDataReceived'] = undefined;
  /**
   * @member {String} payload
   */
  exports.prototype['payload'] = undefined;




  return exports;
}));


