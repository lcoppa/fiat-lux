"""SFPTlampActuator standard profile, originally defined in resource file set
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTinFbDly import SCPTinFbDly
from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SCPTrunHrInit import SCPTrunHrInit
from pylon.resources.SCPTrunHrAlarm import SCPTrunHrAlarm
from pylon.resources.SNVT_elec_kwh import SNVT_elec_kwh
from pylon.resources.SCPTenergyCntInit import SCPTenergyCntInit
from pylon.resources.SCPTlocation import SCPTlocation


class SFPTlampActuator(base.Profile):
    """SFPTlampActuator standard profile.  Lamp Actuator.  Used within
    devices that can control the illumination level of a lamp."""

    def __init__(self):
        super().__init__(
            key=3040,
            scope=0,
            principal='nviLampValue'
        )
        self.datapoints['nviLampValue'] = base.Profile.DatapointMember(
            doc="""Lamp input value.  Permits another device to pass data to
            the Lamp Actuator.""",
            name='nviLampValue',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLampValueFb'] = base.Profile.DatapointMember(
            doc="""Lamp feedback output.  State of the Lamp Actuator (ON or
            OFF) and the percentage level of intensity.""",
            name='nvoLampValueFb',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciInFbDly':
                base.Profile.PropertyMember(
                    doc="""Input-value feedback delay.  The time period after
                    the last update, in a succession of changes to the input,
                    before the feedback output is updated.""",
                    name='nciInFbDly',
                    profile=self,
                    number=2,
                    datatype=SCPTinFbDly,
                    default=b'\x00\x00\x00\x00\x00\x01\x2c',
                    mandatory=False
                ),
                'nciDefault':
                base.Profile.PropertyMember(
                    doc="""Default output.  The level the sensor should adopt
                    in certain default conditions.""",
                    name='nciDefault',
                    profile=self,
                    number=3,
                    datatype=SCPTdefOutput,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRunHours'] = base.Profile.DatapointMember(
            doc="""Running hours output.  Monitors the Lamp Actuator's
            running (ON) hours.""",
            name='nvoRunHours',
            profile=self,
            number=3,
            datatype=SNVT_elapsed_tm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciRunHrInit':
                base.Profile.PropertyMember(
                    doc="""Initialization of running hours counter.  """,
                    name='nciRunHrInit',
                    profile=self,
                    number=4,
                    datatype=SCPTrunHrInit,
                    mandatory=False
                ),
                'ncRunHrAlarm':
                base.Profile.PropertyMember(
                    doc="""Alarm threshold level for the running hours
                    counter.  """,
                    name='ncRunHrAlarm',
                    profile=self,
                    number=5,
                    datatype=SCPTrunHrAlarm,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyCnt'] = base.Profile.DatapointMember(
            doc="""Energy counter output.  Monitors the consumed energy in
            kiloWatt hours.""",
            name='nvoEnergyCnt',
            profile=self,
            number=4,
            datatype=SNVT_elec_kwh,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciEnergyCntInit':
                base.Profile.PropertyMember(
                    doc="""Initialization of energy counter.  """,
                    name='nciEnergyCntInit',
                    profile=self,
                    number=6,
                    datatype=SCPTenergyCntInit,
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=SCPTlocation,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTlampActuator()
    pass
