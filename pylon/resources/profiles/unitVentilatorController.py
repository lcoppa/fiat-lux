"""unitVentilatorController standard profile, originally defined in resource
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
import pylon.resources.datapoints.temp_p
import pylon.resources.properties.maxRcvTime
import pylon.resources.datapoints.temp_setpt
import pylon.resources.datapoints.tod_event
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.hvac_overid
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.hvac_status
import pylon.resources.datapoints.power_kilo
import pylon.resources.datapoints.ppm
import pylon.resources.properties.setPnts
import pylon.resources.properties.minSendTime
import pylon.resources.properties.location
import pylon.resources.properties.bypassTime
import pylon.resources.properties.manOvrTime
import pylon.resources.properties.minRnge
import pylon.resources.properties.limitCO2
import pylon.resources.properties.humSetpt
import pylon.resources.properties.numValves


class unitVentilatorController(pylon.resources.base.Profile):
    """unitVentilatorController standard profile.  Unit-Ventilator
    Controller.  Used to control an HVAC unit ventilator."""

    def __init__(self):
        super().__init__(
            key=8080,
            scope=0,
            principal='nviSpaceTemp'
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV01',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetpoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input (absolute) This input network
            variable is used to allow the temperature setpoints for the
            occupied and standby modes to be changed via the network.""",
            name='nviSetpoint',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetptOffset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the effective occupied and standby temperature
            setpoints by adding nviSetptOffset to the current setpoints.""",
            name='nviSetptOffset',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV03',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetptShift'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint Shift Input.  This input network variable is used
            to shift the effective heat/cool setpoints by adding the
            corresponding value in nviSetptShift to the current
            setpoints.""",
            name='nviSetptShift',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.temp_setpt.temp_setpt,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV04':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV04',
                    profile=self,
                    number=20,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccSchedule'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Scheduler Input.  This input network variable is
            used to command the Unit Ventilator Controller into different
            occupancy modes.""",
            name='nviOccSchedule',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.tod_event.tod_event,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV05',
                    profile=self,
                    number=21,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccManCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Override Input.  This input network variable is
            used to command the Unit Ventilator Controller into different
            occupancy modes.""",
            name='nviOccManCmd',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccSensor'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Sensor Input.  This input network variable is
            used to indicate the presence of occupants in the controlled
            space.""",
            name='nviOccSensor',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV07':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV07',
                    profile=self,
                    number=22,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the Unit Ventilator Controller with any
            supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV08':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV08',
                    profile=self,
                    number=23,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeatCool'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heat/Cool Mode Input.  This network variable input is used
            to coordinate the Unit Ventilator Controller with any node that
            may need to control the heat/cool changeover of the unit.""",
            name='nviHeatCool',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV09':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV09',
                    profile=self,
                    number=24,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFanSpeedCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan Speed Command Input.  This input network variable is
            used to connect an external fan speed switch to the node or to
            allow any supervisory device to override the fan speed controlled
            by the node's control algorithm.""",
            name='nviFanSpeedCmd',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviComprEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Compressor Enable Input.  This input is used to disable
            compressor operation.  This input is typically sent from a system
            coordination panel.""",
            name='nviComprEnable',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV11':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV11',
                    profile=self,
                    number=25,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviAuxHeatEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Auxiliary Heat Enable Input.  This input is used to
            disable auxiliary heat operation.  This input is typically sent
            from a system supervisor panel.""",
            name='nviAuxHeatEnable',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV12':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV12',
                    profile=self,
                    number=26,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEconEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Economizer Enable Input.  This input is used to enable and
            disable economizer operation.""",
            name='nviEconEnable',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV13':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV13',
                    profile=self,
                    number=27,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is used to stop heating
            and cooling while allowing the unit to protect the space from
            temperature extremes.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV14':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV14',
                    profile=self,
                    number=28,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviValveOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Water Valve Override Input.  This input network variable
            is used for commanding the controller into a manual mode for
            overriding water valves controlled by the unit.""",
            name='nviValveOverride',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.hvac_overid.hvac_overid,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency Override Input.  This input network variable is
            used to command the device into different emergency modes.  It is
            typically set by a supervisory node.""",
            name='nviEmergOverride',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSourceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Source Temperature Input.  This input network variable is
            used to indicate the temperature of the air or water being
            supplied to the unit for heating and/or cooling capacity.""",
            name='nviSourceTemp',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV17':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV17',
                    profile=self,
                    number=29,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Temperature Input.  This input network
            variable represents information from an outdoor air temperature
            sensor.""",
            name='nviOutdoorTemp',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV18':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV18',
                    profile=self,
                    number=30,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Percentage level.  This input network variable is the
            measured space humidity in percent.  This input is typically sent
            from a communicating humidity sensor.""",
            name='nviSpaceRH',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV19':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV19',
                    profile=self,
                    number=31,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Humidity Input.  This input network variable
            is the measured outdoor humidity in percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV20':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV20',
                    profile=self,
                    number=32,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Space Temperature Output.  This output network
            variable is used to monitor the effective space temperature that
            the Chilled Ceiling Controller is using for control.""",
            name='nvoSpaceTemp',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV21':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV21',
                    profile=self,
                    number=43,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  This output network variable
            is used to monitor the effective temperature setpoint.""",
            name='nvoEffectSetpt',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV22':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV22',
                    profile=self,
                    number=44,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit Status Output.  This output network variable is
            available to report the Unit Ventilator Controller status.""",
            name='nvoUnitStatus',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV23':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV23',
                    profile=self,
                    number=45,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectOccup'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Occupancy Output.  This output network variable
            is used to indicate the actual occupancy mode of the unit.""",
            name='nvoEffectOccup',
            profile=self,
            number=24,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatCool'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Heat/Cool Output.  This output network variable
            is used to indicate the actual heat/cool mode of the unit.""",
            name='nvoHeatCool',
            profile=self,
            number=25,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV25':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV25',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local Setpoint Output.  This output network variable is
            used to monitor the space temperature setpoint if a setpoint
            device is locally wired.""",
            name='nvoSetpoint',
            profile=self,
            number=26,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetptShift'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local Setpoint Shift Output.  This output network variable
            is used to report a locally-determined shift of the effective
            heat/cool setpoints.""",
            name='nvoSetptShift',
            profile=self,
            number=27,
            datatype=pylon.resources.datapoints.temp_setpt.temp_setpt,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV27':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV27',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFanSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan Speed Output.  This output network variable reflects
            the actual fan speed of a local multi-speed fan as well as the
            requested speed of a remote fan.""",
            name='nvoFanSpeed',
            profile=self,
            number=28,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV28':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV28',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDischAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge Air Temperature Output.  This output network
            variable is used to monitor the temperature of the air that
            leaves the Unit Ventilator Controller, if the unit controller
            provides a hardwired temperature sensor for this purpose.""",
            name='nvoDischAirTemp',
            profile=self,
            number=29,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLoadAbsK'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Absolute Power Consumption KW Output.  This output network
            variable can used to indicate the current power consumption of
            the unit.""",
            name='nvoLoadAbsK',
            profile=self,
            number=30,
            datatype=pylon.resources.datapoints.power_kilo.power_kilo,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTerminalLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Terminal Load Output.  This output indicates the current
            heat/cool energy demand of the unit.""",
            name='nvoTerminalLoad',
            profile=self,
            number=31,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV31':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV31',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatPrimary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary Heat Output.  This output network variable
            reflects the current level of the primary heat output or can be
            used to control a remote primary heat source.""",
            name='nvoHeatPrimary',
            profile=self,
            number=32,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV32':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV32',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatSecondary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary Heat Output.  This output network variable
            reflects the current level of the secondary heat output or can be
            used to control a remote secondary heat source.""",
            name='nvoHeatSecondary',
            profile=self,
            number=33,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV33':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV33',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCoolPrimary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary Cool Output.  This output network variable
            reflects the current level of the primary mechanical cooling
            output or can be used to control a remote mechanical cooling
            source.""",
            name='nvoCoolPrimary',
            profile=self,
            number=34,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV34':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV34',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOADamper'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Damper Output.  This output network variable
            reflects the current position of the outdoor air damper or as a
            request to a remote outdoor air damper.""",
            name='nvoOADamper',
            profile=self,
            number=35,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV35':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV35',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Humidity Output.  This output network variable
            indicates the space humidity in percent, if the Chilled Ceiling
            Controller Device has a locally wired humidity sensor.""",
            name='nvoSpaceRH',
            profile=self,
            number=36,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV36':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV36',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Humidity Output.  This output network variable
            indicates the outdoor air humidity in percent, if the Unit
            Ventilator Controller Device has a locally wired humidity
            sensor.""",
            name='nvoOutdoorRH',
            profile=self,
            number=37,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV37':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV37',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Temperature Output.  This output network
            variable is used to monitor the outdoor air temperature if the
            unit controller provides a hardwired temperature sensor for this
            purpose.""",
            name='nvoOutdoorTemp',
            profile=self,
            number=38,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV38':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV38',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceCO2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Output.  This output network variable
            indicates the space CO2 concentration in ppm, if the Unit
            Ventilator Controller Device has a locally wired CO2 sensor.""",
            name='nvoSpaceCO2',
            profile=self,
            number=39,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV39':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV39',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold Off Output.  This output indicates the state
            of an Energy Hold Off device that is hardwired to the
            controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=40,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV40':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV40',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceCO2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Input.  This input network variable
            measures the space CO2 levels in PPM.""",
            name='nviSpaceCO2',
            profile=self,
            number=41,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV41':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV41',
                    profile=self,
                    number=47,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSetPoints'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPoints',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.setPnts.setPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=34,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=35,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciBypassTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Bypass time.  The maximum amount of time that the
            controller can be in the bypass (occupancy) mode following the
            last bypass request.  Zero disables the timer.""",
            name='nciBypassTime',
            profile=self,
            number=36,
            datatype=pylon.resources.properties.bypassTime.bypassTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciManualTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manual override time.  The maximum time that the
            controller will stay in a manual mode following the last request
            by a network variable input.  Zero disables the timer.""",
            name='nciManualTime',
            profile=self,
            number=37,
            datatype=pylon.resources.properties.manOvrTime.manOvrTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciOAMinPos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum range.  The minimum limit of the value of the
            primary output network variable for the object.""",
            name='nciOAMinPos',
            profile=self,
            number=38,
            datatype=pylon.resources.properties.minRnge.minRnge,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciSpaceCO2Lim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""CO2 limit.  CO2 threshold limit, controller to maintain
            concentration below this limit.""",
            name='nciSpaceCO2Lim',
            profile=self,
            number=39,
            datatype=pylon.resources.properties.limitCO2.limitCO2,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSpaceHRSetpt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Humidity high limit setpoint.  High limit humidity
            setpoint for the controlled space.  A zero value disables.""",
            name='nciSpaceHRSetpt',
            profile=self,
            number=40,
            datatype=pylon.resources.properties.humSetpt.humSetpt,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciNumValve'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Number of output valves.  Used to inform the controller
            whether it is in a one-valve or two-valve system.""",
            name='nciNumValve',
            profile=self,
            number=41,
            datatype=pylon.resources.properties.numValves.numValves,
            minimum=b'\x00\x01',
            maximum=b'\x00\x02',
            default=b'\x00\x02',
            mandatory=False
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=42,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=46,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTunitVentilatorController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = unitVentilatorController()
    pass
