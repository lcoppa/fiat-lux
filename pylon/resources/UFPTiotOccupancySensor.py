"""UFPTiotOccupancySensor userdefined profile, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1."""


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
# Generated at 12-Sep-2013 11:24.

from pylon.resources import base
from pylon.resources.userdefined import userdefined
from pylon.resources.UNVT_iot_load_control import UNVT_iot_load_control
from pylon.resources.SCPTdebounce import SCPTdebounce
from pylon.resources.UCPTiotDescription import UCPTiotDescription
from pylon.resources.UCPTeventAlgorithmInhibit import UCPTeventAlgorithmInhibit
from pylon.resources.UCPTeventDetectionEnable import UCPTeventDetectionEnable
from pylon.resources.UCPTiotFeedbackDelay import UCPTiotFeedbackDelay
from pylon.resources.SCPTholdTime import SCPTholdTime
from pylon.resources.UCPTiotLoadGroupMembership import UCPTiotLoadGroupMembership
from pylon.resources.UCPToccupancyMode import UCPToccupancyMode
from pylon.resources.UCPToccupancyModeTimeout import UCPToccupancyModeTimeout
from pylon.resources.UCPTiotLocation import UCPTiotLocation
from pylon.resources.UCPTiotName import UCPTiotName
from pylon.resources.UCPTreliabilityEvaluationInhibit import UCPTreliabilityEvaluationInhibit
from pylon.resources.UCPTnetworkTiming import UCPTnetworkTiming


class UFPTiotOccupancySensor(base.Profile):
    """UFPTiotOccupancySensor userdefined profile.  IoT occupancy sensor.
    IoT occupancy sensor reporting occupancy based on detected motion or
    presence, and inputs from other occupancy sensors ."""

    def __init__(self):
        super().__init__(
            key=20004,
            scope=1,
            principal='nvoOccupancy'
        )
        self.datapoints['nvoOccupancy'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Occupancy sensor reading;  includes a
            field that reports local occupancy reported by the sensor with a
            hold time, and a second field that reports calculated occupancy
            based on local occupancy plus occupancy inputs from all connected
            occupancy sensors.""",
            name='nvoOccupancy',
            profile=self,
            number=1,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDebounce':
                base.Profile.PropertyMember(
                    doc="""Debounce time.  The interval after a change to the
                    occupied state that the occupancy sensor input is
                    ignored.""",
                    name='cpDebounce',
                    profile=self,
                    number=1,
                    datatype=SCPTdebounce,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviOccupancyIn'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Occupancy input from all connected
            occupancy sensors.""",
            name='nviOccupancyIn',
            profile=self,
            number=2,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['cpDescription'] = base.Profile.PropertyMember(
            doc="""IoT description.  Text descripton of the occupancy
            sensor.""",
            name='cpDescription',
            profile=self,
            number=2,
            datatype=UCPTiotDescription,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpEventAlgorithmInhibit'] = base.Profile.PropertyMember(
            doc="""Event algorithm inhibit.  Inhibit the event algorithm if
            true.""",
            name='cpEventAlgorithmInhibit',
            profile=self,
            number=3,
            datatype=UCPTeventAlgorithmInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpEventDetectionEnable'] = base.Profile.PropertyMember(
            doc="""Event detection enable.  Enable event detection if
            true.""",
            name='cpEventDetectionEnable',
            profile=self,
            number=4,
            datatype=UCPTeventDetectionEnable,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpFeedbackDelay'] = base.Profile.PropertyMember(
            doc="""Feedback delay.  The time period after the last update in
            a succession of changes to the input, before the feedback output
            is updated.""",
            name='cpFeedbackDelay',
            profile=self,
            number=5,
            datatype=UCPTiotFeedbackDelay,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpHoldTime'] = base.Profile.PropertyMember(
            doc="""Hold time.  Hold time for the nvoOccupancy occupied state
            after there is no occupancy detected;  the hold time timer is
            retriggered each time the sensor reports the area as
            occupied.""",
            name='cpHoldTime',
            profile=self,
            number=6,
            datatype=SCPTholdTime,
            minimum=b'\x00\x0a',
            default=b'\x01\x2c',
            mandatory=True
        )
        self.properties['cpLoadGroups'] = base.Profile.PropertyMember(
            doc="""Load group membership.  Active load groups for the
            occupancy sensor.""",
            name='cpLoadGroups',
            profile=self,
            number=7,
            datatype=UCPTiotLoadGroupMembership,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpMode'] = base.Profile.PropertyMember(
            doc="""Occupancy mode.  """,
            name='cpMode',
            profile=self,
            number=8,
            datatype=UCPToccupancyMode,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpModeTimeout'] = base.Profile.PropertyMember(
            doc="""Occupancy mode timeout.  Maximum time to hold an occupancy
            mode before returning to Auto mode.""",
            name='cpModeTimeout',
            profile=self,
            number=9,
            datatype=UCPToccupancyModeTimeout,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLocation'] = base.Profile.PropertyMember(
            doc="""Text location name.  Location of the occupancy sensor.""",
            name='cpLocation',
            profile=self,
            number=10,
            datatype=UCPTiotLocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName'] = base.Profile.PropertyMember(
            doc="""Text name.  Text name of the occupancy sensor.""",
            name='cpName',
            profile=self,
            number=11,
            datatype=UCPTiotName,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpReliabilityEvaluationInhibit'] = base.Profile.PropertyMember(
            doc="""Reliability evaluation inhibit.  Inhibit reliability
            evaluation if true.""",
            name='cpReliabilityEvaluationInhibit',
            profile=self,
            number=12,
            datatype=UCPTreliabilityEvaluationInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpnOccupancy'] = base.Profile.PropertyMember(
            doc="""Network timing.  Application-layer network timing
            parameters for the nvoOccupancy output.""",
            name='cpnOccupancy',
            profile=self,
            number=13,
            datatype=UCPTnetworkTiming,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = UFPTiotOccupancySensor()
    pass
