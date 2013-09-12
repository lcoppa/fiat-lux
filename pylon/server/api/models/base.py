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
Pilon IP-C Server REST API model base class.

All Pilon model classes derive from this abstract `BaseModel` class.
"""

__version__ = "$Revision: #4 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/models/base.py $


from django.conf            import settings
from django.db              import models


__all__ = ['BaseModel']


# choices for the 'source' field of the 'BaseModel' class
# generated from the names of the COLLECTORS setting under PILON
SOURCE_CHOICES = [(name, name) for name in settings.PILON['COLLECTORS']]


# DOC: <https://docs.djangoproject.com/en/1.5/ref/models/>
# DOC: <https://docs.djangoproject.com/en/1.5/topics/db/models/#abstract-base-classes>
class BaseModel(models.Model):
    """
    'BaseModel' includes common fields for all Pilon models.
    """
    
    # NOTE: Beware that 'editable=False' means that the field
    #       can't be displayed at all (e.g. in Forms and the Admin).
    #       This should be saved for completely internal fields.
    #       Instead, use 'read_only_fields' in Serializer or ModelAdmin classes.
    # DOC: <https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields>
    
    # NOTE: Base classes include the following fields:
    #    id
    
    name = models.CharField(max_length=30,
                            blank=False,
                            unique=False,
                            #verbose_name="resource's name",
                            help_text="name of the resource")
    
    categories = models.CharField(max_length=100,
                                  blank=True,
                                  unique=False,
                                  #verbose_name="resource's categories",
                                  help_text="categories of the resource")
    
    # optional user-supplied notes field
    notes = models.TextField(blank=True,
                             default="",
                             unique=False,
                             #verbose_name="resource's notes",
                             help_text="(optional) user-supplied notes for the resource")

    timestamp = models.DateTimeField(auto_now=True,
                                     auto_now_add=True,
                                     #verbose_name="resource's last modification time",
                                     help_text="timestamp when the resource was last modified")
    
    # internal field used to correlate resource with its `Collector`
    source = models.SlugField(max_length=30,
                              choices=SOURCE_CHOICES,
                              blank=False,
                              unique=False,
                              #verbose_name="resource's source",
                              help_text="source of the resource's data")
    

    # names of search/filter fields
    # (used by 'search' and '{field}' filter parameters)
    search_fields = ('name', 'categories', 'notes')
    filter_fields = search_fields + ('id', 'timestamp', 'source')

    
    class Meta:
        abstract = True
        
