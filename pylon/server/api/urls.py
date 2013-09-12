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
Pilon IP-C Server REST API URL dispatcher.
"""

__version__ = "$Revision: #8 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/urls.py $


from django.conf            import settings
from django.conf.urls       import include, patterns, url

from rest_framework.routers import DefaultRouter

from api.views              import DatapointViewSet, DeviceViewSet, UserViewSet
#from api.views.datapoint    import DatapointsByDevice, DatapointsByDeviceViewSet


# NOTE: For hierarchical resources, e.g. /devices/{device_id}/datapoints/, see:
# DOC: <http://stackoverflow.com/questions/17337843/how-to-implement-a-hierarchy-of-resources-eg-parents-id-children-in-django>

router = DefaultRouter()
router.register(r'datapoints', DatapointViewSet)
router.register(r'devices',    DeviceViewSet)
router.register(r'users',      UserViewSet)

urlpatterns = patterns('api',
    # the REST API webapp home page
    #url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    
    # NOTE: this works for just a simple list view
    #url(r'^devices/(?P<device_pk>[^/]+)/datapoints/$', DatapointsByDevice.as_view(), name='datapointsbydevice')
)

# serve the following relative file paths from the root directory's static folder
# NOTE: this only works in DEBUG mode (see <https://docs.djangoproject.com/en/1.5/howto/static-files/>)
if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('api',
        url(r'^(?P<path>(css|img|js)/.*)$', serve, {'document_root': settings.ROOT_DIR + '/static'}),
    )
