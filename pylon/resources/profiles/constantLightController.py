"""constantLightController standard profile, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.lux
import pylon.resources.datapoints.setting
import pylon.resources.datapoints.switch
import pylon.resources.properties.luxSetpoint
import pylon.resources.properties.location
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.step
import pylon.resources.properties.minDeltaLevel
import pylon.resources.properties.onOffHysteresis
import pylon.resources.properties.clOffDelay
import pylon.resources.properties.clOnDelay
import pylon.resources.properties.powerupState


class constantLightController(pylon.resources.base.Profile):
    """constantLightController standard profile.  Constant Light Controller.
    The controller input is the ambient light level, and the output is the
    state and illumination level to the lamp actuator."""

    def __init__(self):
        super().__init__(
            key=3050,
            scope=0,
            principal='nviLuxLevel'
        )
        self.datapoints['nviLuxLevel'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Illumination level input value.  Ambient light level.""",
            name='nviLuxLevel',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lux.lux,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setting input.  Selects the operating mode, and adjusts
            the setpoint of the constant light controller.""",
            name='nviSetting',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLampValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp value output.  State for the lamp actuator (ON or
            OFF), and the percentage level of intensity.""",
            name='nvoLampValue',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviManOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Manual override input.  Provides enable of manual control
            for the lamp value output.""",
            name='nviManOverride',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciLuxSetpoint'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Illumination level setpoint.  Used to change the
            illumination level setpoint for the controller.""",
            name='nciLuxSetpoint',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.luxSetpoint.luxSetpoint,
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciMinSendT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum period between output NV
            transmissions (maximum transmission rate)""",
            name='nciMinSendT',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x05',
            mandatory=False
        )
        self.properties['nciMaxSendT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before the object automatically transmits the present value of
            the lux level output NV.""",
            name='nciMaxSendT',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x0b\xb8',
            mandatory=False
        )
        self.properties['nciStep'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Step Used to determine the maximum step that the constant
            light controller is allowed to take to approach the target
            illumination level.""",
            name='nciStep',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.step.step,
            mandatory=False
        )
        self.properties['nciSendOnDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum change.  Amount by which the lamp value output
            must change before the lamp value is transmitted.""",
            name='nciSendOnDelta',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.minDeltaLevel.minDeltaLevel,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciOnOffHyster'] = pylon.resources.base.Profile.PropertyMember(
            doc="""ON/OFF hysteresis.  Hysteresis for the illumination level
            setpoint.  The hysteresis is used in AUTO mode to switch-off and
            -on the lamp.""",
            name='nciOnOffHyster',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.onOffHysteresis.onOffHysteresis,
            mandatory=False
        )
        self.properties['nciClOffDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Light off delay.  Used to determine the delay after which
            the lamp value output is switched-off.""",
            name='nciClOffDelay',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.clOffDelay.clOffDelay,
            default=b'\x0b\xb8',
            mandatory=False
        )
        self.properties['nciClOnDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Light on delay.  Used to determine the delay after which
            the lamp value output is switched-on.""",
            name='nciClOnDelay',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.clOnDelay.clOnDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciPowerupSt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Power-up state.  Used to determine the state (mode) of the
            constant light controller object after power-up or reset.  The
            state ("function") can be either SET_ON or SET_OFF.""",
            name='nciPowerupSt',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.powerupState.powerupState,
            minimum=b'\x00\x00\xb9\xb1',
            maximum=b'\x01\xc8\x46\x50',
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTconstantLightController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = constantLightController()
    pass
