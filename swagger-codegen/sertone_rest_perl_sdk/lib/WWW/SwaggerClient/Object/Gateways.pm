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
package WWW::SwaggerClient::Object::Gateways;

require 5.6.0;
use strict;
use warnings;
use utf8;
use JSON qw(decode_json);
use Data::Dumper;
use Module::Runtime qw(use_module);
use Log::Any qw($log);
use Date::Parse;
use DateTime;

use base ("Class::Accessor", "Class::Data::Inheritable");


#
#
#
# NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
# REF: https://github.com/swagger-api/swagger-codegen
#

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
__PACKAGE__->mk_classdata('attribute_map' => {});
__PACKAGE__->mk_classdata('swagger_types' => {});
__PACKAGE__->mk_classdata('method_documentation' => {}); 
__PACKAGE__->mk_classdata('class_documentation' => {});

# new object
sub new { 
    my ($class, %args) = @_; 

	my $self = bless {}, $class;
	
	foreach my $attribute (keys %{$class->attribute_map}) {
		my $args_key = $class->attribute_map->{$attribute};
		$self->$attribute( $args{ $args_key } );
	}
	
	return $self;
}  

# return perl hash
sub to_hash {
    return decode_json(JSON->new->convert_blessed->encode( shift ));
}

# used by JSON for serialization
sub TO_JSON { 
    my $self = shift;
    my $_data = {};
    foreach my $_key (keys %{$self->attribute_map}) {
        if (defined $self->{$_key}) {
            $_data->{$self->attribute_map->{$_key}} = $self->{$_key};
        }
    }
    return $_data;
}

# from Perl hashref
sub from_hash {
    my ($self, $hash) = @_;

    # loop through attributes and use swagger_types to deserialize the data
    while ( my ($_key, $_type) = each %{$self->swagger_types} ) {
    	my $_json_attribute = $self->attribute_map->{$_key}; 
        if ($_type =~ /^array\[/i) { # array
            my $_subclass = substr($_type, 6, -1);
            my @_array = ();
            foreach my $_element (@{$hash->{$_json_attribute}}) {
                push @_array, $self->_deserialize($_subclass, $_element);
            }
            $self->{$_key} = \@_array;
        } elsif (exists $hash->{$_json_attribute}) { #hash(model), primitive, datetime
            $self->{$_key} = $self->_deserialize($_type, $hash->{$_json_attribute});
        } else {
        	$log->debugf("Warning: %s (%s) does not exist in input hash\n", $_key, $_json_attribute);
        }
    }
  
    return $self;
}

# deserialize non-array data
sub _deserialize {
    my ($self, $type, $data) = @_;
    $log->debugf("deserializing %s with %s",Dumper($data), $type);
        
    if ($type eq 'DateTime') {
        return DateTime->from_epoch(epoch => str2time($data));
    } elsif ( grep( /^$type$/, ('int', 'double', 'string', 'boolean'))) {
        return $data;
    } else { # hash(model)
        my $_instance = eval "WWW::SwaggerClient::Object::$type->new()";
        return $_instance->from_hash($data);
    }
}



__PACKAGE__->class_documentation({description => '',
                                  class => 'Gateways',
                                  required => [], # TODO
}                                 );

__PACKAGE__->method_documentation({
    'id' => {
    	datatype => 'int',
    	base_name => 'id',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'owner' => {
    	datatype => 'string',
    	base_name => 'owner',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'gateway_eui' => {
    	datatype => 'string',
    	base_name => 'gateway_eui',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'gateway_status' => {
    	datatype => 'string',
    	base_name => 'gateway_status',
    	description => 'Gateway status can be Planned, Active, Inactive, Maintenance, Deprecated',
    	format => '',
    	read_only => '',
    		},
    'longitude' => {
    	datatype => 'string',
    	base_name => 'longitude',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'latitude' => {
    	datatype => 'string',
    	base_name => 'latitude',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'altitude' => {
    	datatype => 'string',
    	base_name => 'altitude',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'address' => {
    	datatype => 'string',
    	base_name => 'address',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'base_model' => {
    	datatype => 'string',
    	base_name => 'base_model',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'city' => {
    	datatype => 'string',
    	base_name => 'city',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'concentrator' => {
    	datatype => 'string',
    	base_name => 'concentrator',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'country' => {
    	datatype => 'string',
    	base_name => 'country',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'freq_plan' => {
    	datatype => 'string',
    	base_name => 'freq_plan',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'region' => {
    	datatype => 'string',
    	base_name => 'region',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'rel_customer_uid' => {
    	datatype => 'string',
    	base_name => 'rel_customer_uid',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'gateway_title' => {
    	datatype => 'string',
    	base_name => 'gateway_title',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'zip_code' => {
    	datatype => 'string',
    	base_name => 'zip_code',
    	description => '',
    	format => '',
    	read_only => '',
    		},
    'created_on' => {
    	datatype => 'string',
    	base_name => 'created_on',
    	description => '',
    	format => '',
    	read_only => '',
    		},
});

__PACKAGE__->swagger_types( {
    'id' => 'int',
    'owner' => 'string',
    'gateway_eui' => 'string',
    'gateway_status' => 'string',
    'longitude' => 'string',
    'latitude' => 'string',
    'altitude' => 'string',
    'address' => 'string',
    'base_model' => 'string',
    'city' => 'string',
    'concentrator' => 'string',
    'country' => 'string',
    'freq_plan' => 'string',
    'region' => 'string',
    'rel_customer_uid' => 'string',
    'gateway_title' => 'string',
    'zip_code' => 'string',
    'created_on' => 'string'
} );

__PACKAGE__->attribute_map( {
    'id' => 'id',
    'owner' => 'owner',
    'gateway_eui' => 'gateway_eui',
    'gateway_status' => 'gateway_status',
    'longitude' => 'longitude',
    'latitude' => 'latitude',
    'altitude' => 'altitude',
    'address' => 'address',
    'base_model' => 'base_model',
    'city' => 'city',
    'concentrator' => 'concentrator',
    'country' => 'country',
    'freq_plan' => 'freq_plan',
    'region' => 'region',
    'rel_customer_uid' => 'rel_customer_uid',
    'gateway_title' => 'gateway_title',
    'zip_code' => 'zip_code',
    'created_on' => 'created_on'
} );

__PACKAGE__->mk_accessors(keys %{__PACKAGE__->attribute_map});


1;
