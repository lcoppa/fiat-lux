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
Pilon IP-C Server root URL dispatcher.
"""

__version__ = "$Revision: #5 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/project/urls.py $


from django.conf            import settings
from django.conf.urls       import patterns, include, url

# enable the Django administration interface
from django.contrib         import admin
admin.autodiscover()

from project.views          import home, hello, time, time_plus


urlpatterns = patterns('',
    # enable admin documentation:
    url(r'^admin/doc/',             include('django.contrib.admindocs.urls')),

    # the Django administration site
    url(r'^admin/',                 include(admin.site.urls),   name='admin'),

    # the Django REST Framework login/logout views
    url(r'^auth/',                  include('rest_framework.urls', namespace='rest_framework'), name='auth'),

    # the project home page
    url(r'^$',                      home,                       name='home'),
    
    # a few simple example Django views
    url(r'^hello/$',                hello,                      name='hello'),
    url(r'^time/$',                 time,                       name='time'),
    url(r'^time/([+-]?\d{1,2})/$',  time_plus,                  name='time_plus'),
    
    # Pilon IP-C Server REST API
    url(r'^api/',                   include('api.urls'),        name='api'),
)

# serve the following relative file paths from the root directory's static folder
# NOTE: this only works in DEBUG mode (see <https://docs.djangoproject.com/en/1.5/howto/static-files/>)
if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^(?P<path>(css|img|js)/.*)$', serve, {'document_root': settings.ROOT_DIR + '/static'}),
    )
