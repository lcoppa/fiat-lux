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
Pylon IP-C Server REST API Device admin interaction.
"""

__version__ = "$Revision: #8 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/admin/device.py $


from django.contrib             import admin
from api.models.device          import Device

__all__ = ['DeviceAdmin']


# customized administration classes for our models
# DOC: <https://docs.djangoproject.com/en/1.5/ref/contrib/admin/#modeladmin-objects>
class DeviceAdmin(admin.ModelAdmin):    
    # order and fields displayed on item pages
    fields  = ('id', 'devid', 'name', 'brand', 'type', 'categories', 'notes', 'active', 'source', 'timestamp')

    # read-only fields (all except 'notes')
    readonly_fields = ('id', 'devid', 'name', 'brand', 'type', 'active', 'source', 'timestamp')
    
    # excluded fields
    #exclude = ('field',)

    # order and fields displayed on list pages (e.g. add, change)
    list_display  = fields
    
    # fields that can be searched (all except 'timestamp')
    search_fields = ('id', 'devid', 'name', 'brand', 'type', 'categories', 'notes', 'active', 'source')


# register our models in the Django administration site
admin.site.register(Device, DeviceAdmin)
