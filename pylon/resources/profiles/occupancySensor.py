"""occupancySensor standard profile, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software" to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file is generated from device resource files using an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.  The machine-generated code may not meet
# compliance with PEP-8 and PEP-257 recommendations at all times.
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.occupancy
import pylon.resources.properties.location
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.debounce


class occupancySensor(pylon.resources.base.Profile):
    """occupancySensor standard profile.  Occupancy Sensor.  Used in a device
    with a hardware sensor whose output is either in an occupied or
    unoccupied state."""

    def __init__(self):
        super().__init__(
            key=1060,
            scope=0,
            principal='nvoOccup'
        )
        self.datapoints['nvoOccup'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Provides the qualified state of the hardware
            sensor output.""",
            name='nvoOccup',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciHeartBeat'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciHeartBeat',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x04\xb0',
            mandatory=False
        )
        self.properties['nciDebounce'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Debounce time.  The debouncing time to generate the
            detection envelope.""",
            name='nciDebounce',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.debounce.debounce,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPToccupancySensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = occupancySensor()
    pass
