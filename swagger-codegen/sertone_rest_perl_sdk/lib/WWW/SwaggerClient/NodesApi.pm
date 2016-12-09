=begin comment

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

=end comment

=cut

#
# NOTE: This class is auto generated by the swagger code generator program. 
# Do not edit the class manually.
# Ref: https://github.com/swagger-api/swagger-codegen
#
package WWW::SwaggerClient::NodesApi;

require 5.6.0;
use strict;
use warnings;
use utf8; 
use Exporter;
use Carp qw( croak );
use Log::Any qw($log);

use WWW::SwaggerClient::ApiClient;
use WWW::SwaggerClient::Configuration;

use base "Class::Data::Inheritable";

__PACKAGE__->mk_classdata('method_documentation' => {});

sub new {
    my $class   = shift;
    my (%self) = (
        'api_client' => WWW::SwaggerClient::ApiClient->instance,
        @_
    );

    #my $self = {
    #    #api_client => $options->{api_client}
    #    api_client => $default_api_client
    #}; 

    bless \%self, $class;

}


#
# get_nodes_by_user_id
#
# getNodesByUserId() - Gets all nodes owned by given user.
# 
# @param string $user_id The userId whom to get owned nodes (required)
{
    my $params = {
    'user_id' => {
        data_type => 'string',
        description => 'The userId whom to get owned nodes',
        required => '1',
    },
    };
    __PACKAGE__->method_documentation->{ get_nodes_by_user_id } = { 
    	summary => 'getNodesByUserId() - Gets all nodes owned by given user.',
        params => $params,
        returns => 'ARRAY[Nodes]',
        };
}
# @return ARRAY[Nodes]
#
sub get_nodes_by_user_id {
    my ($self, %args) = @_;

    # verify the required parameter 'user_id' is set
    unless (exists $args{'user_id'}) {
      croak("Missing the required parameter 'user_id' when calling get_nodes_by_user_id");
    }

    # parse inputs
    my $_resource_path = '/users/{userId}/nodes';
    $_resource_path =~ s/{format}/json/; # default format to json

    my $_method = 'GET';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/xml', 'application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type('application/xml', 'application/json');

    # path params
    if ( exists $args{'user_id'}) {
        my $_base_variable = "{" . "userId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'user_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw(server_token client_id )];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('ARRAY[Nodes]', $response);
    return $_response_object;
}

#
# get_nodes_by_user_id_and_sensor_id
#
# getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user.
# 
# @param string $user_id The userId where node will be retrieved (required)
# @param string $dev_eui The sensorID to be retrieved (required)
{
    my $params = {
    'user_id' => {
        data_type => 'string',
        description => 'The userId where node will be retrieved',
        required => '1',
    },
    'dev_eui' => {
        data_type => 'string',
        description => 'The sensorID to be retrieved',
        required => '1',
    },
    };
    __PACKAGE__->method_documentation->{ get_nodes_by_user_id_and_sensor_id } = { 
    	summary => 'getNodesByUserIdAndSensorId() - Gets details of given node ID for this given user.',
        params => $params,
        returns => 'NodeInfo',
        };
}
# @return NodeInfo
#
sub get_nodes_by_user_id_and_sensor_id {
    my ($self, %args) = @_;

    # verify the required parameter 'user_id' is set
    unless (exists $args{'user_id'}) {
      croak("Missing the required parameter 'user_id' when calling get_nodes_by_user_id_and_sensor_id");
    }

    # verify the required parameter 'dev_eui' is set
    unless (exists $args{'dev_eui'}) {
      croak("Missing the required parameter 'dev_eui' when calling get_nodes_by_user_id_and_sensor_id");
    }

    # parse inputs
    my $_resource_path = '/users/{userId}/nodes/{devEui}';
    $_resource_path =~ s/{format}/json/; # default format to json

    my $_method = 'GET';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/xml', 'application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type('application/xml', 'application/json');

    # path params
    if ( exists $args{'user_id'}) {
        my $_base_variable = "{" . "userId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'user_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    # path params
    if ( exists $args{'dev_eui'}) {
        my $_base_variable = "{" . "devEui" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'dev_eui'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw(server_token client_id )];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('NodeInfo', $response);
    return $_response_object;
}

1;