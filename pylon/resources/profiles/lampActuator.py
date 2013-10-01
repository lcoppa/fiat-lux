"""lampActuator standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch
import pylon.resources.properties.inFbDly
import pylon.resources.properties.defOutput
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.properties.runHrInit
import pylon.resources.properties.runHrAlarm
import pylon.resources.datapoints.elec_kwh
import pylon.resources.properties.energyCntInit
import pylon.resources.properties.location


class lampActuator(pylon.resources.base.Profile):
    """lampActuator standard profile.  Lamp Actuator.  Used within devices
    that can control the illumination level of a lamp."""

    def __init__(self):
        super().__init__(
            key=3040,
            scope=0,
            principal='nviLampValue'
        )
        self.datapoints['nviLampValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp input value.  Permits another device to pass data to
            the Lamp Actuator.""",
            name='nviLampValue',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLampValueFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp feedback output.  State of the Lamp Actuator (ON or
            OFF) and the percentage level of intensity.""",
            name='nvoLampValueFb',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciInFbDly':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Input-value feedback delay.  The time period after
                    the last update, in a succession of changes to the input,
                    before the feedback output is updated.""",
                    name='nciInFbDly',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.inFbDly.inFbDly,
                    default=b'\x00\x00\x00\x00\x00\x01\x2c',
                    mandatory=False
                ),
                'nciDefault':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default output.  The level the sensor should adopt
                    in certain default conditions.""",
                    name='nciDefault',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.defOutput.defOutput,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRunHours'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Running hours output.  Monitors the Lamp Actuator's
            running (ON) hours.""",
            name='nvoRunHours',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciRunHrInit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Initialization of running hours counter.  """,
                    name='nciRunHrInit',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.runHrInit.runHrInit,
                    mandatory=False
                ),
                'ncRunHrAlarm':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm threshold level for the running hours
                    counter.  """,
                    name='ncRunHrAlarm',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.runHrAlarm.runHrAlarm,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyCnt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy counter output.  Monitors the consumed energy in
            kiloWatt hours.""",
            name='nvoEnergyCnt',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.elec_kwh.elec_kwh,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciEnergyCntInit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Initialization of energy counter.  """,
                    name='nciEnergyCntInit',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.energyCntInit.energyCntInit,
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self._original_name = 'SFPTlampActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = lampActuator()
    pass
