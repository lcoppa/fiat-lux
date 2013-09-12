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
Pilon IP-C Server REST API Datapoint view.
"""

__version__ = "$Revision: #13 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/views/datapoint.py $


from rest_framework             import permissions, viewsets

from api.models.datapoint       import Datapoint
from api.serializers.datapoint  import DatapointSerializer
from collectors.collector       import Collector
from collectors.task            import DatapointUpdateTask


__all__ = ['DatapointViewSet']


# DOC: <http://django-rest-framework.org/api-guide/viewsets.html#modelviewset>
# DOC: <http://daringfireball.net/projects/markdown/syntax>
class DatapointViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents **datapoints**.
    
    ###Optional query parameters:
    
      + **`ref_type=`**(**`url`** | **`id`**) (default: **url**)
      + **`search=`** {*search_text*}
      + {*field_name*}**`=`**{*field_value*}
    
    Query parameters are added to the end of the URI, following a
    `?` character, and separated from other parameters with a `&` character.
    
    `ref_type` controls the form in which related objects (e.g. **device**)
    are returned, as follows:
    
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
    
    **NOTE:**  You must be logged in to make changes to datapoints.
    """
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    filter_fields = Datapoint.filter_fields
    search_fields = Datapoint.search_fields
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def pre_save(self, obj):
    #    obj.owner = self.request.user

    def post_save(self, datapoint, created=False):
        """
        Called after saving a Datapoint object.
        """
        Collector.enqueue_task(datapoint.source,
                               DatapointUpdateTask(datapoint),
                               join=False)

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

# class DatapointsByDevice(generics.ListCreateAPIView):
#     queryset = Datapoint.objects.all()
#     serializer_class = DatapointSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#   
#     def get_queryset(self):
#         device_pk = self.kwargs['device_pk']
#         return self.queryset.filter(device__pk=device_pk)
# 
# 
# class DatapointsByDeviceViewSet(viewsets.ModelViewSet):
#     queryset = Datapoint.objects.all()
#     serializer_class = DatapointSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#   
#     def get_queryset(self):
#         device_pk = self.kwargs['device_pk']
#         return self.queryset.filter(device__pk=device_pk)
    