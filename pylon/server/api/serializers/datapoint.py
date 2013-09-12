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
Pilon IP-C Server REST API Datapoint serializer.
"""

__version__ = "$Revision: #11 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/serializers/datapoint.py $


from rest_framework             import serializers

from api.models.datapoint       import Datapoint
from api.query_params           import QUERY_REFTYPE


__all__ = ['DatapointSerializer']


# DOC: <http://django-rest-framework.org/api-guide/serializers.html#hyperlinkedmodelserializer>
class DatapointSerializer(serializers.HyperlinkedModelSerializer):
    """
    'ModelSerializer' for the 'Datapoint' model.
    """

    # dynamically adjust the serializer
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        
        # make the `value` field read-only
        # if the `Datapoint`'s `read_only` field is set
        # NOTE: doesn't apply if this is e.g. a QuerySet
        if isinstance(instance, Datapoint) and instance.read_only:
            self.opts.read_only_fields += ('value',)
    
    
    # serialize 'device' dynamically based on the
    # value of the 'ref_type' query parameter
    # DOC: <http://django-rest-framework.org/api-guide/serializers.html#dynamically-modifiying-fields>
    # DOC: <http://stackoverflow.com/questions/17337843/how-to-implement-a-hierarchy-of-resources-eg-parents-id-children-in-django/17453277>
    device = serializers.SerializerMethodField('get_device')
    
    
    def get_device(self, obj):
        """
        Get the (serialized) value of the related 'device'
        (based on 'ref_type' parameter).
        """
        
        # fetch the (dynamically determined) serializer Field instance
        serializer_field = self.get_device_serializer_field()
        
        # initialize it (sets 'parent', 'root' and 'context')
        serializer_field.initialize(self, 'device')
        
        # use it to serialize the value
        return serializer_field.field_to_native(obj, 'device')
    
    
    def get_device_serializer_field(self):
        """
        Dynamically retrieve a serializer Field instance for the 'device'
        field (based on 'ref_type' parameter).
        """
        
        # Retrieve the 'ref_type' query parameter,
        # or its default values ('url') if not specified.
        query_params = self.context['request'].QUERY_PARAMS
        
        # Determine the type of serialization based on 'ref_type'.
        # NOTE: We ignore 'depth' here, because we don't want to expand the
        #       'parent' object (this could lead to cyclic expansion).
        ref_type = query_params.get(QUERY_REFTYPE['PARAM'], QUERY_REFTYPE['DEFAULT'])
        if ref_type == QUERY_REFTYPE['ID']:
            # serialize 'device' as an ID
            return serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        else:
            # serialize 'device' as a hyperlink
            return serializers.HyperlinkedRelatedField(view_name='device-detail', many=False, read_only=True)
    
    
    # DOC: <http://django-rest-framework.org/api-guide/serializers.html#modelserializer>
    class Meta:
        # the corresponding Model class
        model = Datapoint

        # NOTE: not exposing internal fields: source, read_only
        fields = ('id', 'url', 'name', 'value', 'notes', 'device', 'timestamp')
        #exclude = ('source', 'read_only')

        # read-only fields ('id', 'url', 'device', 'timestamp' are automatically read-only)
        read_only_fields = ('name', 'source', 'read_only')
