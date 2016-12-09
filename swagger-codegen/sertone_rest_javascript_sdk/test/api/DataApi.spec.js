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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SertoneRestApi);
  }
}(this, function(expect, SertoneRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SertoneRestApi.DataApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('DataApi', function() {
    describe('getAppDevDataPayload', function() {
      it('should call getAppDevDataPayload successfully', function(done) {
        //uncomment below and update the code to test getAppDevDataPayload
        //instance.getAppDevDataPayload(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getAppDevLastDataTimestamp', function() {
      it('should call getAppDevLastDataTimestamp successfully', function(done) {
        //uncomment below and update the code to test getAppDevLastDataTimestamp
        //instance.getAppDevLastDataTimestamp(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getAppDevLatestCounter', function() {
      it('should call getAppDevLatestCounter successfully', function(done) {
        //uncomment below and update the code to test getAppDevLatestCounter
        //instance.getAppDevLatestCounter(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getAppLastDataMethod', function() {
      it('should call getAppLastDataMethod successfully', function(done) {
        //uncomment below and update the code to test getAppLastDataMethod
        //instance.getAppLastDataMethod(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getAppLastDataTimestamp', function() {
      it('should call getAppLastDataTimestamp successfully', function(done) {
        //uncomment below and update the code to test getAppLastDataTimestamp
        //instance.getAppLastDataTimestamp(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
