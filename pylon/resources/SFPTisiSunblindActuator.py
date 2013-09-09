"""SFPTisiSunblindActuator standard profile, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch_2 import SNVT_switch_2
from pylon.resources.SCPTdefInput import SCPTdefInput
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SCPTmaxPower import SCPTmaxPower
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SNVT_angle_deg import SNVT_angle_deg
from pylon.resources.SCPTname1 import SCPTname1
from pylon.resources.SCPTname2 import SCPTname2
from pylon.resources.SCPTscene import SCPTscene
from pylon.resources.SCPTinFbDly import SCPTinFbDly
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTsceneTiming import SCPTsceneTiming
from pylon.resources.SCPTname3 import SCPTname3
from pylon.resources.SCPTsceneName import SCPTsceneName
from pylon.resources.SCPTlightingGroupEnable import SCPTlightingGroupEnable
from pylon.resources.SCPTloadControlOffset import SCPTloadControlOffset


class SFPTisiSunblindActuator(base.Profile):
    """SFPTisiSunblindActuator standard profile.  ISI Sunblind and Motor
    Control Actuator.  Controls the position and rotation angle of a
    sunblind.  Also reports sunblind status with integrated scene control.
    This profile provides additional required interfaces over the
    SFPTsunblindActuator profile to simplify use in self-installed
    networks."""

    def __init__(self):
        super().__init__(
            key=6112,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = base.Profile.DatapointMember(
            doc="""Sunblind input value.  Scene, setting and/or request input
            to the sunblind actuator.""",
            name='nviValue',
            profile=self,
            number=1,
            datatype=SNVT_switch_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'cpDefaultInput':
                base.Profile.PropertyMember(
                    doc="""Default input.  Input value when updates are not
                    received, at power-on reset, or when overridden.""",
                    name='cpDefaultInput',
                    profile=self,
                    number=4,
                    datatype=SCPTdefInput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValueFb'] = base.Profile.DatapointMember(
            doc="""Sunblind or appliance feedback output.  Reports the last
            requested scene and current setting.""",
            name='nvoValueFb',
            profile=self,
            number=2,
            datatype=SNVT_switch_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMinSendTime',
                    profile=self,
                    number=8,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current value.
                    ISI heartbeats are specified if this value is set to the
                    invalid value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=13,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPower'] = base.Profile.DatapointMember(
            doc="""Power Reports the current power level of the sunblind or
            appliance.  Power level may be measured or estimated to detect
            blocked motors.""",
            name='nvoPower',
            profile=self,
            number=3,
            datatype=SNVT_power,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpPowerLimit':
                base.Profile.PropertyMember(
                    doc="""Maximum power.  Power level at which the sunblind
                    actuator detects a blocked motor and switches off
                    automatically.""",
                    name='cpPowerLimit',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxPower,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOccupancyFB'] = base.Profile.DatapointMember(
            doc="""Occupancy feedback.  """,
            name='nvoOccupancyFB',
            profile=self,
            number=4,
            datatype=SNVT_occupancy,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRunHours'] = base.Profile.DatapointMember(
            doc="""Running hours output.  Reports total running hours.""",
            name='nvoRunHours',
            profile=self,
            number=5,
            datatype=SNVT_elapsed_tm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRotation'] = base.Profile.DatapointMember(
            doc="""Angular distance.  Report the rotation angle.""",
            name='nvoRotation',
            profile=self,
            number=6,
            datatype=SNVT_angle_deg,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpName1'] = base.Profile.PropertyMember(
            doc="""Name part 1.  Part 1 of the name of the functional block
            to be used by optional user interface applications.  May
            optionally used with SCPTname2 and SCPTname3.  Must be
            implemented as a configuration network variable.""",
            name='cpName1',
            profile=self,
            number=1,
            datatype=SCPTname1,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName2'] = base.Profile.PropertyMember(
            doc="""Name part 2.  Part 2 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and may optionally be used with SCPTname3.  This
            part is concatenated after part 1, and may optionally be followed
            by part 3.  Must be implemented as a configuration network
            variable.""",
            name='cpName2',
            profile=self,
            number=2,
            datatype=SCPTname2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpScene'] = base.Profile.PropertyMember(
            doc="""Scene configuration.  Scene definition used to create a
            scene table.  This SCPT defines the minimum entries required by
            the ISI profiles.  May be used in combination with
            SCPTsceneTiming.""",
            name='cpScene',
            profile=self,
            number=3,
            datatype=SCPTscene,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpInFbDelay'] = base.Profile.PropertyMember(
            doc="""Input value feedback delay.  The time period after the
            last update in a succession of changes to the input, before the
            feedback output is updated.""",
            name='cpInFbDelay',
            profile=self,
            number=5,
            datatype=SCPTinFbDly,
            maximum=b'\x00\x00\x00\x00\x3b\x03\xe7',
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpFbMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpFbMajVer',
            profile=self,
            number=6,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpFbMinVer',
            profile=self,
            number=7,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='cpLocation',
            profile=self,
            number=10,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSceneTiming'] = base.Profile.PropertyMember(
            doc="""Scene timing configuration.  Scene timing definition used
            to supplement a scene table created with a SCPTscene array.  This
            SCPT defines the optional scene table entries for the ISI
            profiles.  When used, it must be used in combination with a
            SCPTscene array.""",
            name='cpSceneTiming',
            profile=self,
            number=11,
            datatype=SCPTsceneTiming,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpName3'] = base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=12,
            datatype=SCPTname3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSceneName'] = base.Profile.PropertyMember(
            doc="""Scene name.  Name for a scene to be used by optional user
            interface applications.  Used to create an array that supplements
            a scene table created with a SCPTscene array.""",
            name='cpSceneName',
            profile=self,
            number=14,
            datatype=SCPTsceneName,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLightingGroupEn'] = base.Profile.PropertyMember(
            doc="""Lighting group enable.  Bit masks to enable or disable up
            to 64 ISI lighting groups.  Group 0 is not used.  Groups may also
            be enabled or disabled using a SNVT_switch_2 update.""",
            name='cpLightingGroupEn',
            profile=self,
            number=16,
            datatype=SCPTlightingGroupEnable,
            array_size_min=8,
            array_size_max=8,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLoadControlOffset'] = base.Profile.PropertyMember(
            doc="""Load control offsets.  Offsets to be used during standby
            (unoccupied state but home, or sleep mode) and demand-response
            modes.""",
            name='cpLoadControlOffset',
            profile=self,
            number=17,
            datatype=SCPTloadControlOffset,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTisiSunblindActuator()
    pass
