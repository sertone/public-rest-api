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

type NodeInfo struct {

	// Registration Type - OTAA or ABP
	RegType string `json:"regType,omitempty"`

	DevEui string `json:"devEui,omitempty"`

	AppEui string `json:"appEui,omitempty"`

	AppKey string `json:"appKey,omitempty"`

	AppSKey string `json:"appSKey,omitempty"`

	DevAddr string `json:"devAddr,omitempty"`

	NwkSKey string `json:"nwkSKey,omitempty"`

	FcntUp int32 `json:"fcntUp,omitempty"`

	FcntDown int32 `json:"fcntDown,omitempty"`

	Flags string `json:"flags,omitempty"`

	Activated bool `json:"activated,omitempty"`
}
