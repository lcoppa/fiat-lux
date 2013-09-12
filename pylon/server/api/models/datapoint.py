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
Pilon IP-C Server REST API Datapoint model.
"""

__version__ = "$Revision: #9 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/models/datapoint.py $


from django.db              import models

from api.models.base        import BaseModel
from api.models.device      import Device


__all__ = ['Datapoint']


# NOTE: When adding new fields to a model, also add the field names in:
#       serializers and admin; also, check: views.  You will also need to
#       rebuild the database, either from scratch, or by using South's
#       migration feature.

# DOC: <https://docs.djangoproject.com/en/1.5/ref/models/>
class Datapoint(BaseModel):
    """
    A 'Datapoint' represents a datapoint belonging to an IP-C
    or ISI device discovered on the network.
    """
    
    # NOTE: Beware that 'editable=False' means that the field
    #       can't be displayed at all (e.g. in Forms and the Admin).
    #       This should be saved for completely internal fields.
    #       Instead, use 'read_only_fields' in Serializer or ModelAdmin classes.
    # DOC: <https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields>
    
    # NOTE: Base classes include the following fields:
    #    id
    #    name
    #    categories
    #    notes
    #    timestamp
    #    source
    
    value = models.TextField(blank=True,
                             unique=False,
                             #verbose_name="datapoint's value",
                             help_text="value of the datapoint")
    
    read_only = models.BooleanField(default=False,
                                    help_text="whether the `value` field is read-only")
    
    # DOC: <https://docs.djangoproject.com/en/1.5/ref/models/fields/#django.db.models.ForeignKey.related_name>
    # DOC: <https://docs.djangoproject.com/en/1.5/topics/db/queries/#following-relationships-backward>
    device = models.ForeignKey(Device,
                               related_name='datapoints',
                               blank=False,
                               unique=False,
                               verbose_name="associated device",
                               help_text="device to which datapoint belongs")

    search_fields = BaseModel.search_fields + ('value',)
    filter_fields = BaseModel.filter_fields + ('value', 'read_only')
    
    def __str__(self):
        return "%d: %s" % (self.id or 0, self.name)

    # DOC: <https://docs.djangoproject.com/en/1.5/ref/models/options/>
    class Meta:
        app_label = 'api'
        ordering = ['id']
