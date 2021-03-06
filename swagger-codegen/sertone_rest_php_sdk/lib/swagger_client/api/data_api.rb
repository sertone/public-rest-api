=begin
SERTONE REST API

This is the SERTONE REST API server for the  Sertone IOT Developers.  You can find out more about IOT at [http://www.sertone.com](http://www.sertone.com) or about the API on [API Reference](http://dev.sertone.com/public-rest-api).

OpenAPI spec version: 0.0.1
Contact: email@sertone.com
Generated by: https://github.com/swagger-api/swagger-codegen.git

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

=end

require "uri"

module SwaggerClient
  class DataApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end

    # getAppDevDataPayload() - Gets payload data of given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui where payload will be retrieved
    # @param dev_eui The devEui where payload will be retrieved
    # @param [Hash] opts the optional parameters
    # @return [Array<DataPayload>]
    def get_app_dev_data_payload(app_eui, dev_eui, opts = {})
      data, _status_code, _headers = get_app_dev_data_payload_with_http_info(app_eui, dev_eui, opts)
      return data
    end

    # getAppDevDataPayload() - Gets payload data of given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui where payload will be retrieved
    # @param dev_eui The devEui where payload will be retrieved
    # @param [Hash] opts the optional parameters
    # @return [Array<(Array<DataPayload>, Fixnum, Hash)>] Array<DataPayload> data, response status code and response headers
    def get_app_dev_data_payload_with_http_info(app_eui, dev_eui, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DataApi.get_app_dev_data_payload ..."
      end
      # verify the required parameter 'app_eui' is set
      fail ArgumentError, "Missing the required parameter 'app_eui' when calling DataApi.get_app_dev_data_payload" if app_eui.nil?
      # verify the required parameter 'dev_eui' is set
      fail ArgumentError, "Missing the required parameter 'dev_eui' when calling DataApi.get_app_dev_data_payload" if dev_eui.nil?
      # resource path
      local_var_path = "/data/{appEui}/nodes/{devEui}".sub('{format}','json').sub('{' + 'appEui' + '}', app_eui.to_s).sub('{' + 'devEui' + '}', dev_eui.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}

      # HTTP header 'Accept' (if needed)
      local_header_accept = ['application/xml', 'application/json']
      local_header_accept_result = @api_client.select_header_accept(local_header_accept) and header_params['Accept'] = local_header_accept_result

      # HTTP header 'Content-Type'
      local_header_content_type = ['application/xml', 'application/json']
      header_params['Content-Type'] = @api_client.select_header_content_type(local_header_content_type)

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
            auth_names = ['server_token', 'client_id']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'Array<DataPayload>')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DataApi#get_app_dev_data_payload\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # getAppDevLastDataTimestamp() - Gets last data timestamp for a given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param dev_eui The devEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [String]
    def get_app_dev_last_data_timestamp(app_eui, dev_eui, opts = {})
      data, _status_code, _headers = get_app_dev_last_data_timestamp_with_http_info(app_eui, dev_eui, opts)
      return data
    end

    # getAppDevLastDataTimestamp() - Gets last data timestamp for a given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param dev_eui The devEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [Array<(String, Fixnum, Hash)>] String data, response status code and response headers
    def get_app_dev_last_data_timestamp_with_http_info(app_eui, dev_eui, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DataApi.get_app_dev_last_data_timestamp ..."
      end
      # verify the required parameter 'app_eui' is set
      fail ArgumentError, "Missing the required parameter 'app_eui' when calling DataApi.get_app_dev_last_data_timestamp" if app_eui.nil?
      # verify the required parameter 'dev_eui' is set
      fail ArgumentError, "Missing the required parameter 'dev_eui' when calling DataApi.get_app_dev_last_data_timestamp" if dev_eui.nil?
      # resource path
      local_var_path = "/data/{appEui}/nodes/{devEui}/timestamp".sub('{format}','json').sub('{' + 'appEui' + '}', app_eui.to_s).sub('{' + 'devEui' + '}', dev_eui.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}

      # HTTP header 'Accept' (if needed)
      local_header_accept = ['application/xml', 'application/json']
      local_header_accept_result = @api_client.select_header_accept(local_header_accept) and header_params['Accept'] = local_header_accept_result

      # HTTP header 'Content-Type'
      local_header_content_type = ['application/xml', 'application/json']
      header_params['Content-Type'] = @api_client.select_header_content_type(local_header_content_type)

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
            auth_names = ['server_token', 'client_id']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'String')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DataApi#get_app_dev_last_data_timestamp\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # getAppDevLatestCounter() - Gets the latest counter for a given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param dev_eui The devEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [Integer]
    def get_app_dev_latest_counter(app_eui, dev_eui, opts = {})
      data, _status_code, _headers = get_app_dev_latest_counter_with_http_info(app_eui, dev_eui, opts)
      return data
    end

    # getAppDevLatestCounter() - Gets the latest counter for a given application and device.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param dev_eui The devEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [Array<(Integer, Fixnum, Hash)>] Integer data, response status code and response headers
    def get_app_dev_latest_counter_with_http_info(app_eui, dev_eui, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DataApi.get_app_dev_latest_counter ..."
      end
      # verify the required parameter 'app_eui' is set
      fail ArgumentError, "Missing the required parameter 'app_eui' when calling DataApi.get_app_dev_latest_counter" if app_eui.nil?
      # verify the required parameter 'dev_eui' is set
      fail ArgumentError, "Missing the required parameter 'dev_eui' when calling DataApi.get_app_dev_latest_counter" if dev_eui.nil?
      # resource path
      local_var_path = "/data/{appEui}/nodes/{devEui}/count".sub('{format}','json').sub('{' + 'appEui' + '}', app_eui.to_s).sub('{' + 'devEui' + '}', dev_eui.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}

      # HTTP header 'Accept' (if needed)
      local_header_accept = ['application/xml', 'application/json']
      local_header_accept_result = @api_client.select_header_accept(local_header_accept) and header_params['Accept'] = local_header_accept_result

      # HTTP header 'Content-Type'
      local_header_content_type = ['application/xml', 'application/json']
      header_params['Content-Type'] = @api_client.select_header_content_type(local_header_content_type)

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
            auth_names = ['server_token', 'client_id']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'Integer')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DataApi#get_app_dev_latest_counter\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # getAppLastDataMethod() - Gets last data delivery method for a given application.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [String]
    def get_app_last_data_method(app_eui, opts = {})
      data, _status_code, _headers = get_app_last_data_method_with_http_info(app_eui, opts)
      return data
    end

    # getAppLastDataMethod() - Gets last data delivery method for a given application.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [Array<(String, Fixnum, Hash)>] String data, response status code and response headers
    def get_app_last_data_method_with_http_info(app_eui, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DataApi.get_app_last_data_method ..."
      end
      # verify the required parameter 'app_eui' is set
      fail ArgumentError, "Missing the required parameter 'app_eui' when calling DataApi.get_app_last_data_method" if app_eui.nil?
      # resource path
      local_var_path = "/data/{appEui}/method".sub('{format}','json').sub('{' + 'appEui' + '}', app_eui.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}

      # HTTP header 'Accept' (if needed)
      local_header_accept = ['application/xml', 'application/json']
      local_header_accept_result = @api_client.select_header_accept(local_header_accept) and header_params['Accept'] = local_header_accept_result

      # HTTP header 'Content-Type'
      local_header_content_type = ['application/xml', 'application/json']
      header_params['Content-Type'] = @api_client.select_header_content_type(local_header_content_type)

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
            auth_names = ['server_token', 'client_id']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'String')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DataApi#get_app_last_data_method\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # getAppLastDataTimestamp() - Gets last data timestamp for a given application.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [String]
    def get_app_last_data_timestamp(app_eui, opts = {})
      data, _status_code, _headers = get_app_last_data_timestamp_with_http_info(app_eui, opts)
      return data
    end

    # getAppLastDataTimestamp() - Gets last data timestamp for a given application.
    # This can only be done by the logged in users.
    # @param app_eui The appEui whom to get last timestamp
    # @param [Hash] opts the optional parameters
    # @return [Array<(String, Fixnum, Hash)>] String data, response status code and response headers
    def get_app_last_data_timestamp_with_http_info(app_eui, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DataApi.get_app_last_data_timestamp ..."
      end
      # verify the required parameter 'app_eui' is set
      fail ArgumentError, "Missing the required parameter 'app_eui' when calling DataApi.get_app_last_data_timestamp" if app_eui.nil?
      # resource path
      local_var_path = "/data/{appEui}/timestamp".sub('{format}','json').sub('{' + 'appEui' + '}', app_eui.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}

      # HTTP header 'Accept' (if needed)
      local_header_accept = ['application/xml', 'application/json']
      local_header_accept_result = @api_client.select_header_accept(local_header_accept) and header_params['Accept'] = local_header_accept_result

      # HTTP header 'Content-Type'
      local_header_content_type = ['application/xml', 'application/json']
      header_params['Content-Type'] = @api_client.select_header_content_type(local_header_content_type)

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
            auth_names = ['server_token', 'client_id']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'String')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DataApi#get_app_last_data_timestamp\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
