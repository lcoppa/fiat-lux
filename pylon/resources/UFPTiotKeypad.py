"""UFPTiotKeypad userdefined profile, originally defined in resource file set
iot 90:00:00:05:00:00:00:00-1."""


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
from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.UCPTnetworkTiming import UCPTnetworkTiming
from pylon.resources.UCPTiotButtonAction import UCPTiotButtonAction
from pylon.resources.UCPTiotDescription import UCPTiotDescription
from pylon.resources.UCPTeventAlgorithmInhibit import UCPTeventAlgorithmInhibit
from pylon.resources.UCPTeventDetectionEnable import UCPTeventDetectionEnable
from pylon.resources.UCPTiotFeedbackDelay import UCPTiotFeedbackDelay
from pylon.resources.UCPTiotLoadGroupMembership import UCPTiotLoadGroupMembership
from pylon.resources.UCPTiotLocation import UCPTiotLocation
from pylon.resources.UCPTiotName import UCPTiotName
from pylon.resources.UCPTreliabilityEvaluationInhibit import UCPTreliabilityEvaluationInhibit
from pylon.resources.UCPTiotScene import UCPTiotScene


class UFPTiotKeypad(base.Profile):
    """UFPTiotKeypad userdefined profile.  IoT keypad.  IoT keypad providing
    user control of lighting, blinds, fans, motors, and other loads ."""

    def __init__(self):
        super().__init__(
            key=20002,
            scope=1,
            principal='nvoLoadControl'
        )
        self.datapoints['nvoLoadControl'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Keypad load control output value.""",
            name='nvoLoadControl',
            profile=self,
            number=1,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDefaultOutput':
                base.Profile.PropertyMember(
                    doc="""Default output.  The level the load control output
                    should adopt at power-on reset.""",
                    name='cpDefaultOutput',
                    profile=self,
                    number=2,
                    datatype=SCPTdefOutput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpnLoadControl':
                base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nvoLoadControl output.""",
                    name='cpnLoadControl',
                    profile=self,
                    number=12,
                    datatype=UCPTnetworkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviLoadStatus'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Load control status from all connected
            load controls, keypads, occupancy sensors, and other load control
            devices.""",
            name='nviLoadStatus',
            profile=self,
            number=2,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['cpButtonAction'] = base.Profile.PropertyMember(
            doc="""IoT button action.  Actions to be executed when buttons
            are pressed, held, and released.""",
            name='cpButtonAction',
            profile=self,
            number=1,
            datatype=UCPTiotButtonAction,
            array_size_min=2,
            array_size_max=1000,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpDescription'] = base.Profile.PropertyMember(
            doc="""IoT description.  Text description of the keypad.""",
            name='cpDescription',
            profile=self,
            number=3,
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
            number=4,
            datatype=UCPTeventAlgorithmInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpEventDetectionEnable'] = base.Profile.PropertyMember(
            doc="""Event detection enable.  Enable event detection if
            true.""",
            name='cpEventDetectionEnable',
            profile=self,
            number=5,
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
            number=6,
            datatype=UCPTiotFeedbackDelay,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLoadGroups'] = base.Profile.PropertyMember(
            doc="""Load group membership.  Active load groups for the
            keypad.""",
            name='cpLoadGroups',
            profile=self,
            number=7,
            datatype=UCPTiotLoadGroupMembership,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLocation'] = base.Profile.PropertyMember(
            doc="""Text location name.  Location of the keypad.""",
            name='cpLocation',
            profile=self,
            number=8,
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
            doc="""Text name.  Text name for the keypad.""",
            name='cpName',
            profile=self,
            number=9,
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
            number=10,
            datatype=UCPTreliabilityEvaluationInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpScene'] = base.Profile.PropertyMember(
            doc="""IoT scene.  Scene table defining the scenes that map a
            scene number to keypad output.""",
            name='cpScene',
            profile=self,
            number=11,
            datatype=UCPTiotScene,
            array_size_min=2,
            array_size_max=1000,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = UFPTiotKeypad()
    pass
