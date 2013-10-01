"""isiLampActuator standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch_2
import pylon.resources.properties.defInput
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.properties.runHrInit
import pylon.resources.properties.runHrAlarm
import pylon.resources.datapoints.elec_kwh
import pylon.resources.properties.energyCntInit
import pylon.resources.properties.sndDelta
import pylon.resources.datapoints.power
import pylon.resources.datapoints.color_2
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.multiplier_s
import pylon.resources.datapoints.elec_whr
import pylon.resources.properties.name1
import pylon.resources.properties.inFbDly
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.location
import pylon.resources.properties.scene
import pylon.resources.properties.sceneTiming
import pylon.resources.properties.name2
import pylon.resources.properties.name3
import pylon.resources.properties.sceneName
import pylon.resources.properties.lightingGroupEnable
import pylon.resources.properties.measurementInterval
import pylon.resources.properties.ovrBehave
import pylon.resources.properties.ovrValue
import pylon.resources.properties.loadControlOffset


class isiLampActuator(pylon.resources.base.Profile):
    """isiLampActuator standard profile.  ISI Lamp and Appliance Actuator.
    Controls the illumination level of a lamp or state of an appliance.  Also
    reports lamp or appliance status with integrated scene control.  This
    profile provides additional required interfaces over the SFPTlampActuator
    profile to simplify use in self-installed networks."""

    def __init__(self):
        super().__init__(
            key=3041,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp input value.  Scene, setting, occupancy, and/or
            request input to the lamp.""",
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
                    number=2,
                    datatype=pylon.resources.properties.defInput.defInput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValueFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp or appliance feedback output.  Reports the last
            requested scene, current setting, and power consumption for the
            lamp or appliance.  Power consumption may be measured or
            estimated.""",
            name='nvoValueFb',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpValueMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time (throttle) The minimum period of
                    time between consecutive transmissions of the current
                    value.""",
                    name='cpValueMinSendTime',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpValueMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
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
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRunHours'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Running hours output.  Reports total running hours.""",
            name='nvoRunHours',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpRunHrInit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Running hours counter initialization.  The initial
                    value of the running hours counter network variable.""",
                    name='cpRunHrInit',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.runHrInit.runHrInit,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpRunHrAlarm':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Running hours alarm threshold level.  The alarm
                    threshold for the running hours counter.""",
                    name='cpRunHrAlarm',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.runHrAlarm.runHrAlarm,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHi'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Electrical energy upper portion.  The nvoEnergyHi reading
            is incremented and the nvoEnergyLo reading wraps to zero when 1
            kWh is reached for the nvoEnergyLo value.  May be an estimated
            value.""",
            name='nvoEnergyHi',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.elec_kwh.elec_kwh,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpEnergyCntInit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Energy counter initialization.  The initial value
                    of the energy counter for the associated network
                    variable.""",
                    name='cpEnergyCntInit',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.energyCntInit.energyCntInit,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyHiMaxSendTime',
                    profile=self,
                    number=27,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyHiMinSendTime',
                    profile=self,
                    number=28,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyHiSendOnDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpEnergyHiSendOnDelta',
                    profile=self,
                    number=29,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPower'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power Reports power consumption.  May be an estimate.""",
            name='nvoPower',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.power.power,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpPowerSendOnDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpPowerSendOnDelta',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x05',
                    mandatory=False
                ),
                'cpPowerMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpPowerMaxSendTime',
                    profile=self,
                    number=22,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpPowerMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpPowerMinSendTime',
                    profile=self,
                    number=23,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviColor'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Color """,
            name='nviColor',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.color_2.color_2,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccupancyFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Occupancy state feedback.""",
            name='nvoOccupancyFb',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMultiplierFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Multiplier Level multiplier feedback.  Reset to one after
            60 minutes.""",
            name='nvoMultiplierFb',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.multiplier_s.multiplier_s,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoColorFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Color feedback.  Color setting feedback;  required if
            nviColor is implemented.""",
            name='nvoColorFb',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.color_2.color_2,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyLo'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Electrical energy lower portion.  The nvoEnergyHi reading
            is incremented and the nvoEnergyLo reading wraps to zero when 1
            kWh is reached for the nvoEnergyLo value.  May be an estimated
            value.""",
            name='nvoEnergyLo',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.elec_whr.elec_whr,
            mandatory=False,
            maximum=b'\x27\x0f',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpEnergyLoMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyLoMaxSendTime',
                    profile=self,
                    number=24,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyLoMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpEnergyLoMinSendTime',
                    profile=self,
                    number=25,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpEnergyLoSendOnDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpEnergyLoSendOnDelta',
                    profile=self,
                    number=26,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['cpName1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 1.  Name of the object that the CP applies to.
            This name can be used by optional user interface applications or
            display devices.""",
            name='cpName1',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.name1.name1,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
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
            doc="""Functional block major version number.  Major version
            number for the associated functional block.  See also
            cpFbMinVer.""",
            name='cpFbMajVer',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Functional block minor version.  Minor version number for
            the associated functional block.  See also cpFbMajVer.""",
            name='cpFbMinVer',
            profile=self,
            number=4,
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
            number=9,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpScene'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene configuration.  Scene table defining the minimum
            required scene definition entries.  May be used in combination
            with cpSceneTiming.""",
            name='cpScene',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.scene.scene,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpSceneTiming'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene timing configuration.  Scene timing definition used
            to supplement a scene table created with cpScene.  This CP array
            defines the optional scene table entries for the ISI profiles.
            When used, it must be used in combination with a cpScene
            array.""",
            name='cpSceneTiming',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.sceneTiming.sceneTiming,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00',
            mandatory=False
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
            number=13,
            datatype=pylon.resources.properties.name2.name2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=14,
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
            number=17,
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
            number=18,
            datatype=pylon.resources.properties.lightingGroupEnable.lightingGroupEnable,
            array_size_min=8,
            array_size_max=8,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpPowerMeasurementInterval'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Power measurement interval.  Time period used for a power
            measurement;  may be used to calibrate a power or energy
            sensor.""",
            name='cpPowerMeasurementInterval',
            profile=self,
            number=19,
            datatype=pylon.resources.properties.measurementInterval.measurementInterval,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.MFG,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['cpOvrBehave'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Override behavior.  This parameter is used to define the
            behavior when an override request is received via the Node
            Object.""",
            name='cpOvrBehave',
            profile=self,
            number=20,
            datatype=pylon.resources.properties.ovrBehave.ovrBehave,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpOvrValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Override value.  The value to be used for the input when
            the functional block is overriden, and the behavior is
            "SPECIFIED";  if there is no Node object, a non-invalid value for
            the cpOvrValue state field triggers the override to the specified
            value, and the normal value is restored when the cpOvrValue state
            field changes to the invalid value.""",
            name='cpOvrValue',
            profile=self,
            number=21,
            datatype=pylon.resources.properties.ovrValue.ovrValue,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLoadControlOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Load control offsets.  Offsets to be used during standby
            (unoccupied state but home, or sleep mode) and demand-response
            modes.""",
            name='cpLoadControlOffset',
            profile=self,
            number=30,
            datatype=pylon.resources.properties.loadControlOffset.loadControlOffset,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTisiLampActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = isiLampActuator()
    pass
