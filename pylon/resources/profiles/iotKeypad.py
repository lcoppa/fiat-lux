"""iotKeypad userdefined profile, originally defined in resource file set iot
90:00:00:05:00:00:00:00-1."""


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
from pylon.resources.userdefined import userdefined
import pylon.resources.datapoints.iot_load_control
import pylon.resources.properties.defOutput
import pylon.resources.properties.networkTiming
import pylon.resources.properties.iotButtonAction
import pylon.resources.properties.iotDescription
import pylon.resources.properties.eventAlgorithmInhibit
import pylon.resources.properties.eventDetectionEnable
import pylon.resources.properties.iotFeedbackDelay
import pylon.resources.properties.iotLoadGroupMembership
import pylon.resources.properties.iotLocation
import pylon.resources.properties.iotName
import pylon.resources.properties.reliabilityEvaluationInhibit
import pylon.resources.properties.iotScene


class iotKeypad(pylon.resources.base.Profile):
    """iotKeypad userdefined profile.  IoT keypad.  IoT keypad providing user
    control of lighting, blinds, fans, motors, and other loads ."""

    def __init__(self):
        super().__init__(
            key=20002,
            scope=1,
            principal='nvoLoadControl'
        )
        self.datapoints['nvoLoadControl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""IoT load control.  Keypad load control output value.""",
            name='nvoLoadControl',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.iot_load_control.iot_load_control,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDefaultOutput':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default output.  The level the load control output
                    should adopt at power-on reset.""",
                    name='cpDefaultOutput',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.defOutput.defOutput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpnLoadControl':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nvoLoadControl output.""",
                    name='cpnLoadControl',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.networkTiming.networkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviLoadStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""IoT load control.  Load control status from all connected
            load controls, keypads, occupancy sensors, and other load control
            devices.""",
            name='nviLoadStatus',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.iot_load_control.iot_load_control,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['cpButtonAction'] = pylon.resources.base.Profile.PropertyMember(
            doc="""IoT button action.  Actions to be executed when buttons
            are pressed, held, and released.""",
            name='cpButtonAction',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.iotButtonAction.iotButtonAction,
            array_size_min=2,
            array_size_max=1000,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpDescription'] = pylon.resources.base.Profile.PropertyMember(
            doc="""IoT description.  Text description of the keypad.""",
            name='cpDescription',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.iotDescription.iotDescription,
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
        self.properties['cpEventAlgorithmInhibit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Event algorithm inhibit.  Inhibit the event algorithm if
            true.""",
            name='cpEventAlgorithmInhibit',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.eventAlgorithmInhibit.eventAlgorithmInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpEventDetectionEnable'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Event detection enable.  Enable event detection if
            true.""",
            name='cpEventDetectionEnable',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.eventDetectionEnable.eventDetectionEnable,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpFeedbackDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Feedback delay.  The time period after the last update in
            a succession of changes to the input, before the feedback output
            is updated.""",
            name='cpFeedbackDelay',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.iotFeedbackDelay.iotFeedbackDelay,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLoadGroups'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Load group membership.  Active load groups for the
            keypad.""",
            name='cpLoadGroups',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.iotLoadGroupMembership.iotLoadGroupMembership,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text location name.  Location of the keypad.""",
            name='cpLocation',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.iotLocation.iotLocation,
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
        self.properties['cpName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text name.  Text name for the keypad.""",
            name='cpName',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.iotName.iotName,
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
        self.properties['cpReliabilityEvaluationInhibit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Reliability evaluation inhibit.  Inhibit reliability
            evaluation if true.""",
            name='cpReliabilityEvaluationInhibit',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.reliabilityEvaluationInhibit.reliabilityEvaluationInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpScene'] = pylon.resources.base.Profile.PropertyMember(
            doc="""IoT scene.  Scene table defining the scenes that map a
            scene number to keypad output.""",
            name='cpScene',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.iotScene.iotScene,
            array_size_min=2,
            array_size_max=1000,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self._original_name = 'UFPTiotKeypad'
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = iotKeypad()
    pass
