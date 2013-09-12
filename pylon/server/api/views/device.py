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
Pilon IP-C Server REST API Device view.
"""

__version__ = "$Revision: #12 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/views/device.py $


from rest_framework             import permissions, viewsets
from rest_framework.decorators  import action, link
from rest_framework.response    import Response

from api.models.datapoint       import Datapoint
from api.models.device          import Device
from api.serializers.datapoint  import DatapointSerializer
from api.serializers.device     import DeviceSerializer
from collectors.collector       import Collector
from collectors.task            import DeviceUpdateTask, DeviceCommandTask


__all__ = ['DeviceViewSet']


# DOC: <http://django-rest-framework.org/api-guide/viewsets.html#modelviewset>
# DOC: <http://daringfireball.net/projects/markdown/syntax>
class DeviceViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents **devices**.
    
    ###Optional query parameters:
    
      + **`depth=`**{*nested_expansion_depth*} (default: **0**)
      + **`ref_type=`**(**`url`** | **`id`**) (default: **url**)
      + **`search=`**{*search_text*}
      + {*field_name*}**`=`**{*field_value*}
    
    Query parameters are added to the end of the URI, following a
    `?` character, and separated from other parameters with a `&` character.
    
    `depth` controls the expansion of dependent objects (e.g. **datapoints**),
    as follows:
    
    <table border=1>
        <tr><th>value</th><th>description</th></tr>
        <tr><td>0</td><td>the URI to retrieve the dependent objects (no expansion)</td></tr>
        <tr><td>1</td><td>a partially expanded list of references (see below)</td></tr>
        <tr><td>&gt;1</td><td>a fully expanded list of the dependent objects</td></tr>
    </table><br>
    
    `ref_type` controls the form in which related objects are returned,
    as follows:
    
    <table border=1>
        <tr><th>value</th><th>description</th></tr>
        <tr><td>url</td><td>a hyperlink (URI) to the related object</td></tr>
        <tr><td>id</td><td>the (unique) ID (primary key) of the related object</td></tr>
    </table><br>
    
    `search` searches across several text-related fields for a partial
    case-insensitive match with {*search_text*} and returns only the matching
    objects.  Multiple parameters may be specified.
    
    {*field_name*} searches the specified field name for an exact
    case-sensitive match with {*field_value*} and returns only the matching
    objects.  Multiple parameters may be specified.
    
    
    **NOTE:**  You must be logged in to make changes to devices.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_fields = Device.filter_fields
    search_fields = Device.search_fields
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     # CreateModelMixin override(s)
#     def create(self, request, *args, **kwargs):
#         return super().create(self, request, *args, **kwargs)
# 
#     # ListModelMixin override(s)
#     def list(self, request, *args, **kwargs):
#         return super().list(self, request, *args, **kwargs)
# 
#     # RetrieveModelMixin override(s)
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(self, request, *args, **kwargs)
# 
#     # UpdateModelMixin override(s)
#     def update(self, request, *args, **kwargs):
#         return super().update(self, request, *args, **kwargs)
# 
#     # DestroyModelMixin override(s)
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(self, request, *args, **kwargs)


    # NOTE: For hierarchical resources, e.g. /devices/{device_id}/datapoints/, see:
    # DOC: <http://stackoverflow.com/questions/17337843/how-to-implement-a-hierarchy-of-resources-eg-parents-id-children-in-django>
    # NOTE: This @link adds a view_name='device-datapoints' to the URL conf.
    @link()
    def datapoints(self, request, pk=None):
        queryset = Datapoint.objects.filter(device__pk=pk)
        serializer = DatapointSerializer(queryset,
                                         context={'request': request},
                                         many=True,
                                         read_only=True)
        #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        return Response(serializer.data)


    @action()
    def wink(self, request, pk=None):
        device = Device.objects.get(pk=pk)
        Collector.enqueue_task(device.source,
                               DeviceCommandTask(device, DeviceCommandTask.DEVICE_WINK),
                               join=False)
        return Response()


    @action()
    def reset(self, request, pk=None):
        device = Device.objects.get(pk=pk)
        Collector.enqueue_task(device.source,
                               DeviceCommandTask(device, DeviceCommandTask.DEVICE_RESET),
                               join=False)
        return Response()
    
    
    #def pre_save(self, obj):
    #    obj.owner = self.request.user


    def post_save(self, device, created=False):
        """
        Called after saving a Device object.
        """
        Collector.enqueue_task(device.source,
                               DeviceUpdateTask(device),
                               join=False)
