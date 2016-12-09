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


package io.swagger.client.api;

import io.swagger.client.ApiException;
import io.swagger.client.model.Applications;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ApplicationsApi
 */
public class ApplicationsApiTest {

    private final ApplicationsApi api = new ApplicationsApi();

    
    /**
     * getApplicationsByUserId() - Gets all applications owned by given user.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getApplicationsByUserIdTest() throws ApiException {
        String userId = null;
        // List<Applications> response = api.getApplicationsByUserId(userId);

        // TODO: test validations
    }
    
    /**
     * getApplicationsByUserIdAndAppId() - Gets details of given application ID for this given user.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getApplicationsByUserIdAndAppIdTest() throws ApiException {
        String userId = null;
        String appEui = null;
        // Applications response = api.getApplicationsByUserIdAndAppId(userId, appEui);

        // TODO: test validations
    }
    
}
