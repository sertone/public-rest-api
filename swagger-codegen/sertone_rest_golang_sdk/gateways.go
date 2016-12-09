/* 
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

package swagger

type Gateways struct {

	Id int64 `json:"id,omitempty"`

	Owner string `json:"owner,omitempty"`

	GatewayEui string `json:"gateway_eui,omitempty"`

	// Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated
	GatewayStatus string `json:"gateway_status,omitempty"`

	Longitude string `json:"longitude,omitempty"`

	Latitude string `json:"latitude,omitempty"`

	Altitude string `json:"altitude,omitempty"`

	Address string `json:"address,omitempty"`

	BaseModel string `json:"base_model,omitempty"`

	City string `json:"city,omitempty"`

	Concentrator string `json:"concentrator,omitempty"`

	Country string `json:"country,omitempty"`

	FreqPlan string `json:"freq_plan,omitempty"`

	Region string `json:"region,omitempty"`

	RelCustomerUid string `json:"rel_customer_uid,omitempty"`

	GatewayTitle string `json:"gateway_title,omitempty"`

	ZipCode string `json:"zip_code,omitempty"`

	CreatedOn string `json:"created_on,omitempty"`
}