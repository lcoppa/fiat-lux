#
# Copyright (c) 2013 Echelon Corporation.  All rights reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
Pilon IP-C Server REST API Device serializer.
"""

__version__ = "$Revision: #13 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/serializers/device.py $


from rest_framework             import serializers

from api.models.device          import Device
from api.query_params           import QUERY_DEPTH, QUERY_REFTYPE
from api.serializers.datapoint  import DatapointSerializer


__all__ = ['DeviceSerializer']


# DOC: <http://django-rest-framework.org/api-guide/serializers.html#hyperlinkedmodelserializer>
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    """
    'ModelSerializer' for the 'Device' model.
    """

    # serialize 'datapoints' dynamically based on the
    # value of the 'depth' and 'ref_type' query parameters
    # DOC: <http://django-rest-framework.org/api-guide/serializers.html#dynamically-modifiying-fields>
    # DOC: <http://stackoverflow.com/questions/17337843/how-to-implement-a-hierarchy-of-resources-eg-parents-id-children-in-django/17453277>
    datapoints = serializers.SerializerMethodField('get_device_datapoints')
    
    
    def get_device_datapoints(self, obj):
        """
        Get the (serialized) value of the dependent 'datapoints'
        (based on 'depth' and 'ref_type' parameters).
        """
        
        # Retrieve the 'depth' query parameter,
        # or its default value (0) if not specified.
        #
        # NOTE: It is not easy (possible at all?) to modify QUERY_PARAMS,
        #       so instead we will use an additional field, 'current_depth',
        #       to track our current nesting level.
        #
        # NOTE: We need to be careful to restore depth for subsequent calls in
        #       the case where this serializer is being called in list context.
        current_depth = self.context.get('current_depth', 0)
        query_params  = self.context['request'].QUERY_PARAMS
        depth = int(query_params.get(QUERY_DEPTH['PARAM'], QUERY_DEPTH['DEFAULT'])) - current_depth

        # fetch the (dynamically determined) serializer Field instance
        serializer_field = self.get_datapoints_serializer_field(depth)
        
        # initialize it (sets 'parent', 'root' and 'context')
        serializer_field.initialize(self, 'datapoints')
        
        # before potentially serializing any nested fields,
        # adjust the current depth
        if depth > 1:
            self.context['current_depth'] = current_depth + 2

        # use it to serialize the value
        value = serializer_field.field_to_native(obj, 'datapoints')
        
        # restore the current depth
        self.context['current_depth'] = current_depth
        
        return value
    
    
    def get_datapoints_serializer_field(self, depth):
        """
        Dynamically retrieve a serializer Field instance for the 'datapoints'
        field (based on 'depth' and 'ref_type' parameters).
        """
        
        # determine the type of serialization based on 'depth' and 'ref_type'
        if depth <= 0:
            # serialize 'datapoints' as a hyperlink to the 'device-datapoints'
            # API URL that will retrieve this device's datapoints (e.g. .../devices/2/datapoints/)
            return serializers.HyperlinkedIdentityField(view_name='device-datapoints')

        elif depth == 1:
            # partial expansion of 'datapoints' by URL or ID

            # retrieve the 'ref_type' query parameter,
            # or its default value ('url') if not specified
            query_params = self.context['request'].QUERY_PARAMS
            ref_type = query_params.get(QUERY_REFTYPE['PARAM'], QUERY_REFTYPE['DEFAULT'])
            if ref_type == QUERY_REFTYPE['ID']:
                # serialize 'datapoints' as a list of IDs
                return serializers.PrimaryKeyRelatedField(many=True, read_only=True)
            else:
                # serialize 'datapoints' as a list of hyperlinks
                return serializers.HyperlinkedRelatedField(
                           view_name='datapoint-detail',
                           many=True,
                           read_only=True)

        else:
            # full nested expansion of 'datapoints'
            return DatapointSerializer(context=self.context,
                                       many=True,
                                       read_only=True)
    
    
    # NOTE: only fields listed in 'fields' below are validated
    #       (which makes some sense, as these are the only fields
    #       that are serialized)
    def validate(self, attrs):
        return attrs


    # DOC: <http://django-rest-framework.org/api-guide/serializers.html#modelserializer>
    class Meta:
        # the corresponding Model class
        model = Device
        
        # NOTE: not exposing internal fields: source, devid
        fields = ('id', 'url', 'name', 'brand', 'type', 'categories', 'notes', 'active', 'datapoints', 'timestamp')
        #exclude = ('source', 'devid')

        # read-only fields ('id', 'url', 'datapoints', 'timestamp' are automatically read-only)
        read_only_fields = ('brand', 'type', 'active', 'source', 'devid')
