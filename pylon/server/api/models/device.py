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
Pilon IP-C Server REST API Device model.
"""

__version__ = "$Revision: #11 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/models/device.py $


import logging

from django.db              import models
from django.core            import validators
from django.core.exceptions import ValidationError

from api.models.base        import BaseModel
from collectors.collector   import Collector
from shared                 import NAMESPACE

# NOTE: To avoid a cyclic dependency, avoid adding this import here.
#       Instead, include it inside a (run-time executed) function, when needed.
#from api.models.datapoint   import Datapoint


__all__ = ['Device']


# choices for the 'active' field of the 'Device' model
ACTIVE_CHOICES = (
    ('true',     'Active'),
    ('pending',  'Pending'),
    ('marginal', 'Marginal'),
    ('false',    'Inactive')
)


# our logger
logger = logging.getLogger(NAMESPACE('models.device'))


# NOTE: When adding new fields to a model, also add the field names in:
#       serializers and admin; also, check: views.  You will also need to rebuild the
#       database, either from scratch, or by using South's migration feature.

# DOC: <https://docs.djangoproject.com/en/1.5/ref/models/>
class Device(BaseModel):
    """
    A 'Device' represents an IP-C or ISI device discovered on the network.
    """
    
    # NOTE: Beware that 'editable=False' means that the field
    #       can't be displayed at all (e.g. in Forms and the Admin).
    #       This should be saved for completely internal fields.
    #       Instead, use 'readonly_fields' in Serializer or ModelAdmin classes.
    # DOC: <https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields>
    
    # NOTE: Base classes include the following fields:
    #    id
    #    name
    #    categories
    #    notes
    #    timestamp
    #    source

    brand = models.CharField(max_length=30,
                             blank=True,
                             default="",
                             unique=False,
                             #verbose_name="device's brand",
                             help_text="brand of the device")
    
    type = models.CharField(max_length=30,
                            blank=False,
                            unique=False,
                            #verbose_name="device's type",
                            help_text="type of the device")
    
    active = models.CharField(max_length=10,
                              choices=ACTIVE_CHOICES,
                              default="pending",
                              blank=False,
                              unique=False,
                              #verbose_name="device's activity level",
                              #verbose_name="activity level",
                              help_text="activity level of the device")
    
    # internal field to correlate the device with the LonBridge device ID
    devid = models.CharField(max_length=30,
                             unique=False,      # see clean() below for further validation
                             blank=True,        # see clean() below for further validation
                             verbose_name="LonBridge ID",
                             help_text="LonBridge Server ID of the device")
    
    # there is an implicit one-to-many relationship with Datapoint objects
    # accessed as 'device.datapoints'
    # DOC: <https://docs.djangoproject.com/en/1.5/ref/models/relations/>

    search_fields = BaseModel.search_fields + ('brand', 'type', 'active')
    filter_fields = BaseModel.filter_fields + ('brand', 'type', 'active', 'devid')
    
    def __str__(self):
        return "%d: %s (%s)" % (self.id or 0, self.name, self.devid)
        

    # DOC: <https://docs.djangoproject.com/en/1.5/ref/models/instances/#django.db.models.Model.clean>
    def clean(self):
        """
        Extra model-wide validation after clean_fields() has been
        called on every field.  Any ValidationError raised
        by this method will not be associated with a particular field; it will
        have a special-case association with the field defined by NON_FIELD_ERRORS.
        """
        
        # some types of device (e.g. LonBridge-based devices) require a non-blank (and unique) device ID
        if self.devid in validators.EMPTY_VALUES:
            collector = Collector.collector(self.source)
            if collector and collector.requires_devid:
                raise ValidationError("This type of device requires a non-blank 'devid'.")
        
        # TODO: also verify uniqueness of a non-blank 'devid'


    @staticmethod
    def get_device(create=True, save=True, **kwargs):
        """
        Returns the `Device` matching the specified `kwargs`, if it exists,
        optionally creating it if it does not exist.
        
        Arguments:
            create -- whether to create a new `Device` if one does not already exist
            save -- whether to automatically save a newly created device 
            kwargs -- keyword arguments used as a filter and for initializing a new `Device` object
            
        Returns:
            A tuple (device, created) containing the device that was
            found or created, and whether a new `Device` was created.
        """

        # look for a matching Device object in our database
        # DOC: <https://docs.djangoproject.com/en/1.5/topics/db/queries/#retrieving-objects>
        logger.debug("Looking for device matching: %r...", kwargs)
        devs = Device.objects.filter(**kwargs)
        if devs:
            # device found (there should only be one)
            assert len(devs) == 1
            device = devs[0]
            logger.debug("Found device: %r", device)
            return (device, False)

        # device not found
        logger.debug("Did not find device matching: %r", kwargs)
        if not create:
            return (None, False)
        
        # create a new device
        # DOC: <https://docs.djangoproject.com/en/1.5/topics/db/queries/#creating-objects>
        logger.info("Creating new device with: %r...", kwargs)
        device = Device(**kwargs)
        
        # optionally, validate and save the new device
        if save:
            try:
                # NOTE: SQLite ignores 'max_length' and 'choices' are not enforced
                #       (except when creating them from forms),
                #       so use 'full_clean()' to validate the data before saving it.
                #       See <http://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work>
                #       and <http://stackoverflow.com/questions/2520598/check-if-django-model-field-choices-exists?rq=1>.
                device.full_clean()
                device.save()
                logger.info("Saved new device: %r", device)
                
            except ValidationError as e:
                # device creation/update failed
                logger.error("Data for new device (%r) failed validation: %s", device, e)
                return (None, False)
            
        return (device, True)
    
    
    # DOC: <https://docs.djangoproject.com/en/1.5/topics/db/queries/#retrieving-objects>
    def get_datapoint(self, name, create=True, read_only=False, save=True):
        """
        Returns the named `Datapoint`, if it exists,
        optionally creating it if it does not exist.
        
        Arguments:
            name -- name of the datapoint to be retrieved/created
            create -- whether to create a new `Datapoint` if one does not already exist (default: True)
            read_only -- whether a newly-created datapoint should have a read-only `value` (default: False)
            save -- whether to automatically save a newly created datapoint (default: True)
            
        Returns:
            A tuple (datapoint, created) containing the datapoint that was
            found or created, and whether a new `Datapoint` was created.
        """

        # look for a Datapoint object in our database (belonging to this device)
        # with a matching name and source
        logger.debug("Looking for datapoint: %s...", name)
        dps = self.datapoints.filter(name=name, source=self.source)
        if dps:
            # datapoint found (there should only be one)
            assert len(dps) == 1
            datapoint = dps[0]
            logger.debug("Found datapoint: %r", datapoint)
            assert datapoint.source == self.source
            assert datapoint.read_only == read_only
            return (dps[0], False)

        # datapoint not found
        logger.debug("Did not find datapoint: %s", name)
        if not create:
            return (None, False)
        
        # NOTE: To avoid a cyclic dependency, avoid adding this import at the top.
        #       Instead, include it here (where it executes at run-time).
        from api.models.datapoint import Datapoint

        # create a new datapoint
        # DOC: <https://docs.djangoproject.com/en/1.5/topics/db/queries/#creating-objects>
        logger.info("Creating new datapoint: %s...", name)
        datapoint = Datapoint(name=name, read_only=read_only, device=self, source=self.source)
        assert datapoint.source == self.source
        
        # optionally, validate and save the new datapoint
        if save:
            try:
                # NOTE: SQLite ignores 'max_length' and 'choices' are not enforced
                #       (except when creating them from forms),
                #       so use 'full_clean()' to validate the data before saving it.
                #       See <http://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work>
                #       and <http://stackoverflow.com/questions/2520598/check-if-django-model-field-choices-exists?rq=1>.
                datapoint.full_clean()
                datapoint.save()
                logger.info("Saved new datapoint: %r", datapoint)
                
            except ValidationError as e:
                # datapoint creation/update failed
                logger.error("Data for new datapoint (%r) failed validation: %s", datapoint, e)
                return (None, False)
            
        return (datapoint, True)


    # DOC: <https://docs.djangoproject.com/en/1.5/ref/models/options/>
    class Meta:
        app_label = 'api'
        
        #ordering = ['name', 'devid']
        ordering = ['id']

        #unique_together = ('source', 'devid')
