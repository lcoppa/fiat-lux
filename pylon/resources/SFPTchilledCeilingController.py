"""SFPTchilledCeilingController standard profile, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_temp_setpt import SNVT_temp_setpt
from pylon.resources.SNVT_tod_event import SNVT_tod_event
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_hvac_overid import SNVT_hvac_overid
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTbypassTime import SCPTbypassTime
from pylon.resources.SCPTmanOvrTime import SCPTmanOvrTime


class SFPTchilledCeilingController(base.Profile):
    """SFPTchilledCeilingController standard profile.  Chilled-Ceiling
    Controller.  Used to control an HVAC chilled-ceiling space-conditioning
    unit."""

    def __init__(self):
        super().__init__(
            key=8070,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV01':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV01',
                    profile=self,
                    number=14,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetpoint'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input (absolute) This input network
            variable is used to allow the temperature setpoints for the
            occupied and standby modes to be changed via the network.""",
            name='nviSetpoint',
            profile=self,
            number=2,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetptOffset'] = base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the effective occupied and standby temperature
            setpoints by adding nviSetptOffset to the current setpoints.""",
            name='nviSetptOffset',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV03',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetptShift'] = base.Profile.DatapointMember(
            doc="""Setpoint Shift Input.  This input network variable is used
            to shift the effective heat/cool setpoints by adding the
            corresponding value in nviSetptShift to the current
            setpoints.""",
            name='nviSetptShift',
            profile=self,
            number=4,
            datatype=SNVT_temp_setpt,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV04':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV04',
                    profile=self,
                    number=16,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccSchedule'] = base.Profile.DatapointMember(
            doc="""Occupancy Scheduler Input.  This input network variable is
            used to command the Chilled Ceiling Controller into different
            occupancy modes.""",
            name='nviOccSchedule',
            profile=self,
            number=5,
            datatype=SNVT_tod_event,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV05',
                    profile=self,
                    number=17,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccManCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy Override Input.  This input network variable is
            used to command the Chilled Ceiling Controller into different
            occupancy modes.""",
            name='nviOccManCmd',
            profile=self,
            number=6,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccSensor'] = base.Profile.DatapointMember(
            doc="""Occupancy Sensor Input.  This input network variable is
            used to indicate the presence of occupants in the controlled
            space.""",
            name='nviOccSensor',
            profile=self,
            number=7,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV07':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV07',
                    profile=self,
                    number=18,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the Chilled Ceiling Controller with any
            supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=8,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV08':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV08',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeatCool'] = base.Profile.DatapointMember(
            doc="""Heat/Cool Mode Input.  This network variable input is used
            to coordinate the Chilled Ceiling Controller with any node that
            may need to control the heat/cool changeover of the unit.""",
            name='nviHeatCool',
            profile=self,
            number=9,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV09':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV09',
                    profile=self,
                    number=20,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is used to stop heating
            and cooling while allowing the unit to protect the space from
            temperature extremes.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=10,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV10':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV10',
                    profile=self,
                    number=21,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviValveOverride'] = base.Profile.DatapointMember(
            doc="""Water Valve Override Input.  This input network variable
            is used for commanding the controller into a manual mode for
            overriding water valves controlled by the unit.""",
            name='nviValveOverride',
            profile=self,
            number=11,
            datatype=SNVT_hvac_overid,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSourceTemp'] = base.Profile.DatapointMember(
            doc="""Source Temperature Input.  This input network variable is
            used to indicate the temperature of the air or water being
            supplied to the unit for heating and/or cooling capacity.""",
            name='nviSourceTemp',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV12':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV12',
                    profile=self,
                    number=22,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeatSrcTemp'] = base.Profile.DatapointMember(
            doc="""Heat Source Temperature Input.  This input network
            variable is used to indicate the temperature of the air or water
            being supplied to the unit for heating capacity.""",
            name='nviHeatSrcTemp',
            profile=self,
            number=13,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV13':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV13',
                    profile=self,
                    number=23,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviCoolSrcTemp'] = base.Profile.DatapointMember(
            doc="""Cool Source Temperature Input.  This input network
            variable is used to indicate the temperature of the air or water
            being supplied to the unit for cooling capacity.""",
            name='nviCoolSrcTemp',
            profile=self,
            number=14,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV14':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV14',
                    profile=self,
                    number=24,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space Humidity Input.  This input network variable is the
            measured space humidity in percent.  This input is typically sent
            from a communicating humidity sensor.""",
            name='nviSpaceRH',
            profile=self,
            number=15,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV15':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV15',
                    profile=self,
                    number=25,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceDewPt'] = base.Profile.DatapointMember(
            doc="""Space Dew Point Temperature Input.  This input network
            variable is the measured space dew point temperature.""",
            name='nviSpaceDewPt',
            profile=self,
            number=16,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV16':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV16',
                    profile=self,
                    number=26,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorDewPt'] = base.Profile.DatapointMember(
            doc="""Outdoor Air Dew Point Temp.  Input.  This input network
            variable is the measured outdoor dew point temperature.""",
            name='nviOutdoorDewPt',
            profile=self,
            number=17,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV17':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV17',
                    profile=self,
                    number=27,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeatPriSlave'] = base.Profile.DatapointMember(
            doc="""Primary Heat Input for Slave Operation.  This input
            network variable is intended for slave operation.""",
            name='nviHeatPriSlave',
            profile=self,
            number=18,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV18':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV18',
                    profile=self,
                    number=28,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeatSecSlave'] = base.Profile.DatapointMember(
            doc="""Secondary Heat Input for Slave Operation.  This input
            network variable is intended for slave operation.""",
            name='nviHeatSecSlave',
            profile=self,
            number=19,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV19':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV19',
                    profile=self,
                    number=29,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviCoolPriSlave'] = base.Profile.DatapointMember(
            doc="""Primary Cool Input for Slave Operation.  This input
            network variable is intended for slave operation.""",
            name='nviCoolPriSlave',
            profile=self,
            number=20,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV20':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV20',
                    profile=self,
                    number=30,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviCoolSecSlave'] = base.Profile.DatapointMember(
            doc="""Secondary Cool Input for Slave Operation.  This input
            network variable is intended for slave operation.""",
            name='nviCoolSecSlave',
            profile=self,
            number=21,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV21':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV21',
                    profile=self,
                    number=31,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Effective Space Temperature Output.  This output network
            variable is used to monitor the effective space temperature that
            the Chilled Ceiling Controller is using for control.""",
            name='nvoSpaceTemp',
            profile=self,
            number=22,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV22':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV22',
                    profile=self,
                    number=40,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit Status Output.  This output network variable is
            available to report the Chilled Ceiling Controller status.""",
            name='nvoUnitStatus',
            profile=self,
            number=23,
            datatype=SNVT_hvac_status,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV23':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV23',
                    profile=self,
                    number=39,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectSetpt'] = base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  This output network variable
            is used to monitor the effective temperature setpoint.""",
            name='nvoEffectSetpt',
            profile=self,
            number=24,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV24':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV24',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectOccup'] = base.Profile.DatapointMember(
            doc="""Effective Occupancy Output.  This output network variable
            is used to indicate the actual occupancy mode of the unit.""",
            name='nvoEffectOccup',
            profile=self,
            number=25,
            datatype=SNVT_occupancy,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatCool'] = base.Profile.DatapointMember(
            doc="""Effective Heat/Cool Output.  This output network variable
            is used to indicate the actual heat/cool mode of the unit.""",
            name='nvoHeatCool',
            profile=self,
            number=26,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV26':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV26',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoint'] = base.Profile.DatapointMember(
            doc="""Local Setpoint Output.  This output network variable is
            used to monitor the space temperature setpoint if a setpoint
            device is locally wired.""",
            name='nvoSetpoint',
            profile=self,
            number=27,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetptShift'] = base.Profile.DatapointMember(
            doc="""Local Setpoint Shift Output.  This output network variable
            is used to report a locally-determined shift of the effective
            heat/cool setpoints.""",
            name='nvoSetptShift',
            profile=self,
            number=28,
            datatype=SNVT_temp_setpt,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV28':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV28',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoLoadAbs'] = base.Profile.DatapointMember(
            doc="""Absolute Power Consumption Output.  This output network
            variable can used to indicate the current power consumption of
            the unit.""",
            name='nvoLoadAbs',
            profile=self,
            number=29,
            datatype=SNVT_power,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Terminal Load Output.  This output indicates the current
            heat/cool energy demand of the unit.""",
            name='nvoTerminalLoad',
            profile=self,
            number=30,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV30':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV30',
                    profile=self,
                    number=6,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatPrimary'] = base.Profile.DatapointMember(
            doc="""Primary Heat Output.  This output network variable
            reflects the current level of the primary heat output or can be
            used to control a remote primary heat source.""",
            name='nvoHeatPrimary',
            profile=self,
            number=31,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV31':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV31',
                    profile=self,
                    number=7,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatSecondary'] = base.Profile.DatapointMember(
            doc="""Secondary Heat Output.  This output network variable
            reflects the current level of the secondary heat output or can be
            used to control a remote secondary heat source.""",
            name='nvoHeatSecondary',
            profile=self,
            number=32,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV32':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV32',
                    profile=self,
                    number=8,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCoolPrimary'] = base.Profile.DatapointMember(
            doc="""Primary Cool Output.  This output network variable
            reflects the current level of the primary mechanical cooling
            output or can be used to control a remote mechanical cooling
            source.""",
            name='nvoCoolPrimary',
            profile=self,
            number=33,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV33':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV33',
                    profile=self,
                    number=9,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCoolSecondary'] = base.Profile.DatapointMember(
            doc="""Secondary Cool Output.  This output network variable
            reflects the current level of the secondary mechanical cooling
            output or can be used to control a remote mechanical cooling
            source.""",
            name='nvoCoolSecondary',
            profile=self,
            number=34,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV34':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV34',
                    profile=self,
                    number=10,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space Humidity Output.  This output network variable
            indicates the space humidity in percent, if the Chilled Ceiling
            Controller Device has a locally wired humidity sensor.""",
            name='nvoSpaceRH',
            profile=self,
            number=35,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV35':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV35',
                    profile=self,
                    number=11,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceDewPt'] = base.Profile.DatapointMember(
            doc="""Space Dewpoint Temperature Output.  This output network
            variable indicates the space dew point temperature.  This value
            can be measured or calculated by the Chilled Ceiling
            Controller.""",
            name='nvoSpaceDewPt',
            profile=self,
            number=36,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV36':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV36',
                    profile=self,
                    number=12,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold Off Output.  This output indicates the state
            of an Energy Hold Off device that is hardwired to the
            controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=37,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV37':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV37',
                    profile=self,
                    number=13,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSetpoints'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetpoints',
            profile=self,
            number=32,
            datatype=SCPTsetPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=33,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=34,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciBypassTime'] = base.Profile.PropertyMember(
            doc="""Bypass time.  The maximum amount of time that the
            controller can be in the bypass (occupancy) mode following the
            last bypass request.  Zero disables the timer.""",
            name='nciBypassTime',
            profile=self,
            number=35,
            datatype=SCPTbypassTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciManualTime'] = base.Profile.PropertyMember(
            doc="""Manual override time.  The maximum time that the
            controller will stay in a manual mode following the last request
            by a network variable input.  Zero disables the timer.""",
            name='nciManualTime',
            profile=self,
            number=36,
            datatype=SCPTmanOvrTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=37,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=38,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTchilledCeilingController()
    pass
