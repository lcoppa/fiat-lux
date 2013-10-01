"""isiSunblindActuator standard profile, originally defined in resource file
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
import pylon.resources.properties.defInput
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.power
import pylon.resources.properties.maxPower
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.datapoints.angle_deg
import pylon.resources.properties.name1
import pylon.resources.properties.name2
import pylon.resources.properties.scene
import pylon.resources.properties.inFbDly
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.location
import pylon.resources.properties.sceneTiming
import pylon.resources.properties.name3
import pylon.resources.properties.sceneName
import pylon.resources.properties.lightingGroupEnable
import pylon.resources.properties.loadControlOffset


class isiSunblindActuator(pylon.resources.base.Profile):
    """isiSunblindActuator standard profile.  ISI Sunblind and Motor Control
    Actuator.  Controls the position and rotation angle of a sunblind.  Also
    reports sunblind status with integrated scene control.  This profile
    provides additional required interfaces over the SFPTsunblindActuator
    profile to simplify use in self-installed networks."""

    def __init__(self):
        super().__init__(
            key=6112,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Sunblind input value.  Scene, setting and/or request input
            to the sunblind actuator.""",
            name='nviValue',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'cpDefaultInput':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default input.  Input value when updates are not
                    received, at power-on reset, or when overridden.""",
                    name='cpDefaultInput',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.defInput.defInput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValueFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Sunblind or appliance feedback output.  Reports the last
            requested scene and current setting.""",
            name='nvoValueFb',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMinSendTime',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current value.
                    ISI heartbeats are specified if this value is set to the
                    invalid value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPower'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power Reports the current power level of the sunblind or
            appliance.  Power level may be measured or estimated to detect
            blocked motors.""",
            name='nvoPower',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.power.power,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpPowerLimit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum power.  Power level at which the sunblind
                    actuator detects a blocked motor and switches off
                    automatically.""",
                    name='cpPowerLimit',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.maxPower.maxPower,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOccupancyFB'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy feedback.  """,
            name='nvoOccupancyFB',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRunHours'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Running hours output.  Reports total running hours.""",
            name='nvoRunHours',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRotation'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Angular distance.  Report the rotation angle.""",
            name='nvoRotation',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.angle_deg.angle_deg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpName1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 1.  Part 1 of the name of the functional block
            to be used by optional user interface applications.  May
            optionally used with SCPTname2 and SCPTname3.  Must be
            implemented as a configuration network variable.""",
            name='cpName1',
            profile=self,
            number=1,
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
            number=2,
            datatype=pylon.resources.properties.name2.name2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpScene'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene configuration.  Scene definition used to create a
            scene table.  This SCPT defines the minimum entries required by
            the ISI profiles.  May be used in combination with
            SCPTsceneTiming.""",
            name='cpScene',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.scene.scene,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpInFbDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Input value feedback delay.  The time period after the
            last update in a succession of changes to the input, before the
            feedback output is updated.""",
            name='cpInFbDelay',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.inFbDly.inFbDly,
            maximum=b'\x00\x00\x00\x00\x3b\x03\xe7',
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpFbMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpFbMajVer',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpFbMinVer',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='cpLocation',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSceneTiming'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene timing configuration.  Scene timing definition used
            to supplement a scene table created with a SCPTscene array.  This
            SCPT defines the optional scene table entries for the ISI
            profiles.  When used, it must be used in combination with a
            SCPTscene array.""",
            name='cpSceneTiming',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.sceneTiming.sceneTiming,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpName3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.name3.name3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSceneName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene name.  Name for a scene to be used by optional user
            interface applications.  Used to create an array that supplements
            a scene table created with a SCPTscene array.""",
            name='cpSceneName',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.sceneName.sceneName,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLightingGroupEn'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Lighting group enable.  Bit masks to enable or disable up
            to 64 ISI lighting groups.  Group 0 is not used.  Groups may also
            be enabled or disabled using a SNVT_switch_2 update.""",
            name='cpLightingGroupEn',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.lightingGroupEnable.lightingGroupEnable,
            array_size_min=8,
            array_size_max=8,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLoadControlOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Load control offsets.  Offsets to be used during standby
            (unoccupied state but home, or sleep mode) and demand-response
            modes.""",
            name='cpLoadControlOffset',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.loadControlOffset.loadControlOffset,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTisiSunblindActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = isiSunblindActuator()
    pass
