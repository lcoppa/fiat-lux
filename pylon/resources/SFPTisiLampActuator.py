"""SFPTisiLampActuator standard profile, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch_2 import SNVT_switch_2
from pylon.resources.SCPTdefInput import SCPTdefInput
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SCPTrunHrInit import SCPTrunHrInit
from pylon.resources.SCPTrunHrAlarm import SCPTrunHrAlarm
from pylon.resources.SNVT_elec_kwh import SNVT_elec_kwh
from pylon.resources.SCPTenergyCntInit import SCPTenergyCntInit
from pylon.resources.SCPTsndDelta import SCPTsndDelta
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SNVT_color_2 import SNVT_color_2
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_multiplier_s import SNVT_multiplier_s
from pylon.resources.SNVT_elec_whr import SNVT_elec_whr
from pylon.resources.SCPTname1 import SCPTname1
from pylon.resources.SCPTinFbDly import SCPTinFbDly
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTscene import SCPTscene
from pylon.resources.SCPTsceneTiming import SCPTsceneTiming
from pylon.resources.SCPTname2 import SCPTname2
from pylon.resources.SCPTname3 import SCPTname3
from pylon.resources.SCPTsceneName import SCPTsceneName
from pylon.resources.SCPTlightingGroupEnable import SCPTlightingGroupEnable
from pylon.resources.SCPTmeasurementInterval import SCPTmeasurementInterval
from pylon.resources.SCPTovrBehave import SCPTovrBehave
from pylon.resources.SCPTovrValue import SCPTovrValue
from pylon.resources.SCPTloadControlOffset import SCPTloadControlOffset


class SFPTisiLampActuator(base.Profile):
    """SFPTisiLampActuator standard profile.  ISI Lamp and Appliance
    Actuator.  Controls the illumination level of a lamp or state of an
    appliance.  Also reports lamp or appliance status with integrated scene
    control.  This profile provides additional required interfaces over the
    SFPTlampActuator profile to simplify use in self-installed networks."""

    def __init__(self):
        super().__init__(
            key=3041,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = base.Profile.DatapointMember(
            doc="""Lamp input value.  Scene, setting, occupancy, and/or
            request input to the lamp.""",
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
                    number=2,
                    datatype=SCPTdefInput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValueFb'] = base.Profile.DatapointMember(
            doc="""Lamp or appliance feedback output.  Reports the last
            requested scene, current setting, and power consumption for the
            lamp or appliance.  Power consumption may be measured or
            estimated.""",
            name='nvoValueFb',
            profile=self,
            number=2,
            datatype=SNVT_switch_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpValueMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time (throttle) The minimum period of
                    time between consecutive transmissions of the current
                    value.""",
                    name='cpValueMinSendTime',
                    profile=self,
                    number=6,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpValueMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time (heartbeat) The maximum period
                    of time between consecutive transmissions of the current
                    value.  If this value is set to the invalid value, the
                    heartbeat interval will be two minutes when occupied and
                    20 minutes when unoccupied--this is the default
                    behavior.  Must be implemented as a configuration network
                    variable.""",
                    name='cpValueMaxSendTime',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRunHours'] = base.Profile.DatapointMember(
            doc="""Running hours output.  Reports total running hours.""",
            name='nvoRunHours',
            profile=self,
            number=8,
            datatype=SNVT_elapsed_tm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpRunHrInit':
                base.Profile.PropertyMember(
                    doc="""Running hours counter initialization.  The initial
                    value of the running hours counter network variable.""",
                    name='cpRunHrInit',
                    profile=self,
                    number=8,
                    datatype=SCPTrunHrInit,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpRunHrAlarm':
                base.Profile.PropertyMember(
                    doc="""Running hours alarm threshold level.  The alarm
                    threshold for the running hours counter.""",
                    name='cpRunHrAlarm',
                    profile=self,
                    number=7,
                    datatype=SCPTrunHrAlarm,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHi'] = base.Profile.DatapointMember(
            doc="""Electrical energy upper portion.  The nvoEnergyHi reading
            is incremented and the nvoEnergyLo reading wraps to zero when 1
            kWh is reached for the nvoEnergyLo value.  May be an estimated
            value.""",
            name='nvoEnergyHi',
            profile=self,
            number=6,
            datatype=SNVT_elec_kwh,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpEnergyCntInit':
                base.Profile.PropertyMember(
                    doc="""Energy counter initialization.  The initial value
                    of the energy counter for the associated network
                    variable.""",
                    name='cpEnergyCntInit',
                    profile=self,
                    number=10,
                    datatype=SCPTenergyCntInit,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyHiMaxSendTime',
                    profile=self,
                    number=27,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyHiMinSendTime',
                    profile=self,
                    number=28,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiSendOnDelta':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpEnergyHiSendOnDelta',
                    profile=self,
                    number=29,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPower'] = base.Profile.DatapointMember(
            doc="""Power Reports power consumption.  May be an estimate.""",
            name='nvoPower',
            profile=self,
            number=4,
            datatype=SNVT_power,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpPowerSendOnDelta':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpPowerSendOnDelta',
                    profile=self,
                    number=16,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x05',
                    mandatory=False
                ),
                'cpPowerMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpPowerMaxSendTime',
                    profile=self,
                    number=22,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpPowerMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpPowerMinSendTime',
                    profile=self,
                    number=23,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviColor'] = base.Profile.DatapointMember(
            doc="""Color """,
            name='nviColor',
            profile=self,
            number=5,
            datatype=SNVT_color_2,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccupancyFb'] = base.Profile.DatapointMember(
            doc="""Occupancy Occupancy state feedback.""",
            name='nvoOccupancyFb',
            profile=self,
            number=3,
            datatype=SNVT_occupancy,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMultiplierFb'] = base.Profile.DatapointMember(
            doc="""Multiplier Level multiplier feedback.  Reset to one after
            60 minutes.""",
            name='nvoMultiplierFb',
            profile=self,
            number=7,
            datatype=SNVT_multiplier_s,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoColorFb'] = base.Profile.DatapointMember(
            doc="""Color feedback.  Color setting feedback;  required if
            nviColor is implemented.""",
            name='nvoColorFb',
            profile=self,
            number=9,
            datatype=SNVT_color_2,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyLo'] = base.Profile.DatapointMember(
            doc="""Electrical energy lower portion.  The nvoEnergyHi reading
            is incremented and the nvoEnergyLo reading wraps to zero when 1
            kWh is reached for the nvoEnergyLo value.  May be an estimated
            value.""",
            name='nvoEnergyLo',
            profile=self,
            number=10,
            datatype=SNVT_elec_whr,
            mandatory=False,
            maximum=b'\x27\x0f',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpEnergyLoMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyLoMaxSendTime',
                    profile=self,
                    number=24,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyLoMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyLoMinSendTime',
                    profile=self,
                    number=25,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyLoSendOnDelta':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpEnergyLoSendOnDelta',
                    profile=self,
                    number=26,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['cpName1'] = base.Profile.PropertyMember(
            doc="""Name part 1.  Name of the object that the CP applies to.
            This name can be used by optional user interface applications or
            display devices.""",
            name='cpName1',
            profile=self,
            number=1,
            datatype=SCPTname1,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
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
            doc="""Functional block major version number.  Major version
            number for the associated functional block.  See also
            cpFbMinVer.""",
            name='cpFbMajVer',
            profile=self,
            number=3,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = base.Profile.PropertyMember(
            doc="""Functional block minor version.  Minor version number for
            the associated functional block.  See also cpFbMajVer.""",
            name='cpFbMinVer',
            profile=self,
            number=4,
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
            number=9,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpScene'] = base.Profile.PropertyMember(
            doc="""Scene configuration.  Scene table defining the minimum
            required scene definition entries.  May be used in combination
            with cpSceneTiming.""",
            name='cpScene',
            profile=self,
            number=11,
            datatype=SCPTscene,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpSceneTiming'] = base.Profile.PropertyMember(
            doc="""Scene timing configuration.  Scene timing definition used
            to supplement a scene table created with cpScene.  This CP array
            defines the optional scene table entries for the ISI profiles.
            When used, it must be used in combination with a cpScene
            array.""",
            name='cpSceneTiming',
            profile=self,
            number=12,
            datatype=SCPTsceneTiming,
            default=b'\x00\x00\x00\x00',
            mandatory=False
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
            number=13,
            datatype=SCPTname2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName3'] = base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=14,
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
            number=17,
            datatype=SCPTsceneName,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLightingGroupEn'] = base.Profile.PropertyMember(
            doc="""Lighting group enable.  Bit masks to enable or disable up
            to 64 ISI lighting groups.  Group 0 is not used.  Groups may also
            be enabled or disabled using a SNVT_switch_2 update.""",
            name='cpLightingGroupEn',
            profile=self,
            number=18,
            datatype=SCPTlightingGroupEnable,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpPowerMeasurementInterval'] = base.Profile.PropertyMember(
            doc="""Power measurement interval.  Time period used for a power
            measurement;  may be used to calibrate a power or energy
            sensor.""",
            name='cpPowerMeasurementInterval',
            profile=self,
            number=19,
            datatype=SCPTmeasurementInterval,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.MFG,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['cpOvrBehave'] = base.Profile.PropertyMember(
            doc="""Override behavior.  This parameter is used to define the
            behavior when an override request is received via the Node
            Object.""",
            name='cpOvrBehave',
            profile=self,
            number=20,
            datatype=SCPTovrBehave,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpOvrValue'] = base.Profile.PropertyMember(
            doc="""Override value.  The value to be used for the input when
            the functional block is overriden, and the behavior is
            "SPECIFIED";  if there is no Node object, a non-invalid value for
            the cpOvrValue state field triggers the override to the specified
            value, and the normal value is restored when the cpOvrValue state
            field changes to the invalid value.""",
            name='cpOvrValue',
            profile=self,
            number=21,
            datatype=SCPTovrValue,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLoadControlOffset'] = base.Profile.PropertyMember(
            doc="""Load control offsets.  Offsets to be used during standby
            (unoccupied state but home, or sleep mode) and demand-response
            modes.""",
            name='cpLoadControlOffset',
            profile=self,
            number=30,
            datatype=SCPTloadControlOffset,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTisiLampActuator()
    pass
