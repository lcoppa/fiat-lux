"""isiOccupancySensor standard profile, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.switch_2
import pylon.resources.properties.debounce
import pylon.resources.properties.holdTime
import pylon.resources.properties.inFbDly
import pylon.resources.datapoints.occupancy
import pylon.resources.properties.location
import pylon.resources.properties.name1
import pylon.resources.properties.name2
import pylon.resources.properties.name3
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.maxSendTime


class isiOccupancySensor(pylon.resources.base.Profile):
    """isiOccupancySensor standard profile.  ISI Occupancy Sensor.  Reports
    the occupancy state for a zone.  Occupancy is reported when detected.
    Feedback from other connected occupancy sensors within the zone is
    monitored--the unoccupied state is only propagated if no connected
    occupancy sensors are reporting occupancy."""

    def __init__(self):
        super().__init__(
            key=1061,
            scope=0
        )
        self.datapoints['nvoSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy state.  Reports the occupancy state for a zone.
            Occupancy is reported when detected.  Feedback from other
            connected occupancy sensors within the zone is monitored--the
            unoccupied state is only propagated if no connected occupancy
            sensors are reporting occupancy.""",
            name='nvoSwitch',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDebounce':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Debounce time.  The interval after a change to the
                    occupied state that the occupancy sensor input is
                    ignored.  Must be implemented as a configuration network
                    variable.""",
                    name='cpDebounce',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.debounce.debounce,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpHoldTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Hold time.  Hold time for the nvoSwitch occupied
                    state after there is no occupancy detected.  The hold
                    time timer is retriggered each time the sensor reports
                    the area as occupied.  Must be implemented as a
                    configuration network variable.""",
                    name='cpHoldTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.holdTime.holdTime,
                    minimum=b'\x00\x0a',
                    default=b'\x01\x2c',
                    mandatory=True
                ),
                'cpInFbDelay':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Input value feedback delay.  The time period after
                    a change in the calculated state from occupied to
                    unoccupied before the unoccupied state is reported.  Must
                    be implemented as a configuration network variable.""",
                    name='cpInFbDelay',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.inFbDly.inFbDly,
                    maximum=b'\x00\x00\x00\x00\x3b\x03\xe7',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviSwitchFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy feedback input.  Used to synchronise multiple
            occupancy sensors within a zone.""",
            name='nviSwitchFb',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccup'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Provides the qualified state of the hardware
            sensor output.""",
            name='nvoOccup',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviTest'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Test control.  Controls test mode.  Set to SW_SET_ON to
            enable test mode--turning off the hold time and ignoring the
            feedback input;  set to SW_SET_OCCUPIED to force the output to
            occupied;  set to SW_SET_UNOCCUPIED to force output to
            unoccupied;  set to SW_SET_OFF to enable normal operation.
            Default is SW_SET_OFF.""",
            name='nviTest',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='cpLocation',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpName1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 1.  Part 1 of the name of the functional block
            to be used by optional user interface applications.  May
            optionally used with SCPTname2 and SCPTname3.  Must be
            implemented as a configuration network variable.""",
            name='cpName1',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.name1.name1,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName2'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 2.  Part 2 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and may optionally be used with SCPTname3.  This
            part is concatenated after part 1, and may optionally be followed
            by part 3.  Must be implemented as a configuration network
            variable.""",
            name='cpName2',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.name2.name2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.name3.name3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpFbMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Functional block major version number.  Major version
            number for the associated functional block.  See also
            cpFbMinVer.""",
            name='cpFbMajVer',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Functional block minor version.  Minor version number for
            the associated functional block.  See also cpFbMajVer.""",
            name='cpFbMinVer',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time (heartbeat) The maximum period of time
            between consecutive transmissions of the current value.  If this
            value is set to the invalid value, the heartbeat interval will be
            two minutes when occupied and 20 minutes when unoccupied--this is
            the default behavior.  Must be implemented as a configuration
            network variable.""",
            name='cpMaxSendTime',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\xff\xff',
            mandatory=True
        )
        self._original_name = 'SFPTisiOccupancySensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = isiOccupancySensor()
    pass
