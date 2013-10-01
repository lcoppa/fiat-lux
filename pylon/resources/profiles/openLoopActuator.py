"""openLoopActuator standard profile, originally defined in resource file set
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
import pylon.resources.properties.maxRcvT
import pylon.resources.properties.highLimit1
import pylon.resources.properties.highLimit2
import pylon.resources.properties.lowLimit1
import pylon.resources.properties.lowLimit2
import pylon.resources.properties.alrmSetT1
import pylon.resources.properties.alrmSetT2
import pylon.resources.properties.alrmClrT1
import pylon.resources.properties.alrmClrT2
import pylon.resources.properties.hystHigh1
import pylon.resources.properties.hystHigh2
import pylon.resources.properties.hystLow1
import pylon.resources.properties.hystLow2
import pylon.resources.properties.alrmIhbT
import pylon.resources.properties.ovrValue
import pylon.resources.datapoints.preset
import pylon.resources.properties.actFbDly
import pylon.resources.properties.defOutput
import pylon.resources.properties.driveT
import pylon.resources.properties.location
import pylon.resources.properties.offDely
import pylon.resources.properties.ovrBehave
import pylon.resources.properties.trnsTblX
import pylon.resources.properties.trnsTblY


class openLoopActuator(pylon.resources.base.Profile):
    """openLoopActuator standard profile.  Open-Loop Actuator (OLA) A basic
    object without feedback, used with any form of actuator."""

    def __init__(self):
        super().__init__(
            key=3,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Value input.  Dictates the desired state of the actuator,
            determined by the specific application.""",
            name='nviValue',
            profile=self,
            number=1,
            datatype=pylon.resources.base.xxx,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveT':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  Maximum time that elapses
                    after the last update to the input NV before actuator
                    adopts the default output.""",
                    name='nciMaxReceiveT',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxRcvT.maxRcvT,
                    mandatory=False
                ),
                'nciHighLim1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 1.  Used to remotely set the alarm high
                    limit 1.""",
                    name='nciHighLim1',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    mandatory=False
                ),
                'nciHighLim2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 2.  Used to remotely set the alarm high
                    limit 2.""",
                    name='nciHighLim2',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.highLimit2.highLimit2,
                    mandatory=False
                ),
                'nciLowLim1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 1.  Used to remotely set the alarm low
                    limit 1.""",
                    name='nciLowLim1',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.lowLimit1.lowLimit1,
                    mandatory=False
                ),
                'nciLowLim2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 2.  Used to remotely set the alarm low
                    limit 2.""",
                    name='nciLowLim2',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.lowLimit2.lowLimit2,
                    mandatory=False
                ),
                'nciAlarmSetT1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm set time 1.  The time period that an alarm 2
                    condition must exist before it is regarded as a valid
                    alarm.""",
                    name='nciAlarmSetT1',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.alrmSetT1.alrmSetT1,
                    mandatory=False
                ),
                'nciAlarmSetT2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm set time 2.  The time period that an alarm 2
                    condition must exist before it is regarded as a valid
                    alarm.""",
                    name='nciAlarmSetT2',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.alrmSetT2.alrmSetT2,
                    mandatory=False
                ),
                'nciAlarmClearT1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm clear time 1.  The time period that an alarm
                    1 condition must not exist before it is regarded as a
                    valid cleared alarm.""",
                    name='nciAlarmClearT1',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.alrmClrT1.alrmClrT1,
                    mandatory=False
                ),
                'nciAlarmClearT2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm clear time 2.  The time period that an alarm
                    2 condition must not exist before it is regarded as a
                    valid cleared alarm.""",
                    name='nciAlarmClearT2',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.alrmClrT2.alrmClrT2,
                    mandatory=False
                ),
                'nciLimHystHi1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Hysteresis high 1.  The hysteresis level for the
                    value field of the alarm high 1 comparison threshold.""",
                    name='nciLimHystHi1',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.hystHigh1.hystHigh1,
                    mandatory=False
                ),
                'nciLimHystHi2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Hysteresis high 2.  The hysteresis level for the
                    value field of the alarm high 2 comparison threshold.""",
                    name='nciLimHystHi2',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.hystHigh2.hystHigh2,
                    mandatory=False
                ),
                'nciLimHystLow1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Hysteresis low 1.  The hysteresis level for the
                    value field of the alarm low 1 comparison threshold.""",
                    name='nciLimHystLow1',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.hystLow1.hystLow1,
                    mandatory=False
                ),
                'nciLimHystLow2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Hysteresis low 2.  The hysteresis level for the
                    value field of the alarm low 2 comparison threshold.""",
                    name='nciLimHystLow2',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.hystLow2.hystLow2,
                    mandatory=False
                ),
                'nciOutInhT':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm output inhibit time.  Time period for which
                    alarms are inhibited after enabling, node reset, or node
                    is put on line.""",
                    name='nciOutInhT',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.alrmIhbT.alrmIhbT,
                    mandatory=False
                ),
                'nciOverValue':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Override value.  Sets the value an actuator should
                    adopt when an object is overridden and behavior is
                    OV_SPECIFIED.""",
                    name='nciOverValue',
                    profile=self,
                    number=21,
                    datatype=pylon.resources.properties.ovrValue.ovrValue,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviPreset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Preset input.  Used to program or control the preset
            function.""",
            name='nviPreset',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.preset.preset,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActPosnFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actual position feedback output.  Present position of the
            actuator, can be used as part of a control loop and for
            monitoring purposes.""",
            name='nvoActPosnFb',
            profile=self,
            number=3,
            datatype=pylon.resources.base.xxx,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciActFbDly':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Actual position feedback delay.  The period for
                    updating the feedback output when the actuator position
                    does not match the requested position.""",
                    name='nciActFbDly',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.actFbDly.actFbDly,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPresetFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Preset feedback output.  Transmits the setting associated
            with the current recalled or programmed preset.""",
            name='nvoPresetFb',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.preset.preset,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciDefault'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Default output.  The level the actuator should adopt in
            certain default conditions.""",
            name='nciDefault',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.defOutput.defOutput,
            mandatory=False
        )
        self.properties['nciDriveT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Drive time.  Time to be taken by the actuator to move from
            one extreme to the other.""",
            name='nciDriveT',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.driveT.driveT,
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciOffDly'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Turn-off delay.  Used for SNVT_switch or SNVT_lev_disc to
            determine the length of time the load remains energized after a
            change from ON to OFF is received.""",
            name='nciOffDly',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.offDely.offDely,
            mandatory=False
        )
        self.properties['nciOverBehave'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Override behavior.  The behavior of an actuator when an
            override request is received.""",
            name='nciOverBehave',
            profile=self,
            number=20,
            datatype=pylon.resources.properties.ovrBehave.ovrBehave,
            mandatory=False
        )
        self.properties['nciTransTblX'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Translation table X.  Used in conjunction with Translation
            table Y to create a linearization table.""",
            name='nciTransTblX',
            profile=self,
            number=22,
            datatype=pylon.resources.properties.trnsTblX.trnsTblX,
            mandatory=False
        )
        self.properties['nciTransTblY'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Translation table Y.  Used in conjunction with Translation
            table X to create a linearization table.""",
            name='nciTransTblY',
            profile=self,
            number=23,
            datatype=pylon.resources.properties.trnsTblY.trnsTblY,
            mandatory=False
        )
        self._original_name = 'SFPTopenLoopActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = openLoopActuator()
    pass
