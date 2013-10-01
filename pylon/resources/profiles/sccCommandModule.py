"""sccCommandModule standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.temp_p
import pylon.resources.properties.maxRcvTime
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.time_stamp
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_status
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.ppm
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.temp_setpt
import pylon.resources.properties.offsetTemp
import pylon.resources.properties.minDeltaTemp
import pylon.resources.properties.minSendTime
import pylon.resources.properties.setPnts
import pylon.resources.properties.location
import pylon.resources.properties.offsetCO2
import pylon.resources.properties.minDeltaCO2
import pylon.resources.properties.offsetRH
import pylon.resources.properties.minDeltaRH


class sccCommandModule(pylon.resources.base.Profile):
    """sccCommandModule standard profile.  Space-Comfort Command Module.
    Used to control the HVAC comfort in a given space."""

    def __init__(self):
        super().__init__(
            key=8090,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to display the value of an external space temperature
            sensor.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
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
                    number=11,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviUserLockout'] = pylon.resources.base.Profile.DatapointMember(
            doc="""User Lockout Input.  This input network variable is used
            by the supervisory device to restrict the occupant from making
            certain changes.""",
            name='nviUserLockout',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Time Input.  This input network variable is used to
            display the local time in the Command Module Device.""",
            name='nviTime',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
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
                    number=12,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEffectSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Temperature Setpoint Input.  This input network
            variable is from a controller object and is used to display in
            the Command Module Device the controller's Effective
            Setpoint.""",
            name='nviEffectSetpt',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
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
                    number=13,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEffectOccup'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Occupancy Input.  This input network variable is
            used to indicate the associated controller object's actual
            occupancy mode.""",
            name='nviEffectOccup',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit Status Input.  This input network variable is
            transmitted from the Controller object to inform the occupant of
            the status of the associated HVAC equipment, to be displayed in
            the Command Module Device.""",
            name='nviUnitStatus',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV06':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV06',
                    profile=self,
                    number=14,
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
            number=7,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
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
                    number=15,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor Air Humidity Input.  This input network variable
            is used to display outdoor humidity in percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
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
                    number=16,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Humidity Input.  This input network variable is used
            to display space humidity in percent.""",
            name='nviSpaceRH',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
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
                    number=17,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceCO2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Input.  This input network variable is
            used to display the space CO2 levels in PPM.""",
            name='nviSpaceCO2',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV10':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV10',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is from a space comfort
            controller device which monitors inputs such as a window contact
            sensor.""",
            name='nviEnergyHoldOff',
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
                    number=19,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature Setpoint Output.  This output network variable
            is used to allow the occupant to change the temperature setpoint
            for the occupied and standby mode from the Command Module
            Device.""",
            name='nvoSetpoint',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to transmit the space temperature that is hard wired to the
            Command Module Device.""",
            name='nvoSpaceTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV13':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV13',
                    profile=self,
                    number=25,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatCool'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heat/Cool Output.  This output network variable from the
            Command Module Device is used to transmit the user's command to
            the controller of the HVAC equipment.""",
            name='nvoHeatCool',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV14':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV14',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFanSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan Speed Output.  This output network variable reflects
            the requested speed of a remote fan.""",
            name='nvoFanSpeed',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOccSensor'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Sensor Output.  The Command Module Device object
            conveys to the network the occupancy state of a hard wired
            occupancy sensor.""",
            name='nvoOccSensor',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV16':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV16',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Humidity Output.  This output network variable is
            used to transmit the space relative humidity that is hard wired
            to the Command Module Device.""",
            name='nvoSpaceRH',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV17':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV17',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceCO2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Output.  This output network variable is
            used to transmit the space CO2 sensor value that is hard wired to
            the Command Module Device.""",
            name='nvoSpaceCO2',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV18':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV18',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOccManCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Manual Command Output.  The Command Module
            Device object conveys to the network the occupancy state as it is
            modified by the occupant.""",
            name='nvoOccManCmd',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetptOffset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature Setpoint Offset Output.  This output network
            variable is used to shift the temperature setpoint via the
            network, by adding nviSetPtOffset to the current setpoint.""",
            name='nvoSetptOffset',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV20':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV20',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoints'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Temperature Setpoints Output.  This output
            defines the occupancy temperature setpoints for heat and cool
            mode.""",
            name='nvoSetpoints',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.temp_setpt.temp_setpt,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceCO2Lim'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space CO2 Limit Output.  This network output property
            defines a high limit CO2 setpoint as requested by the occupant
            for ventilation functions.""",
            name='nvoSpaceCO2Lim',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceRHSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Humidity Setpoint Output.  This network output
            property defines the high limit humidity setpoint for the
            controlled space.""",
            name='nvoSpaceRHSetpt',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTmpOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Temperature offset.  Used to calibrate external hardware
            with additive offset after transformation.""",
            name='nciTmpOffset',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.offsetTemp.offsetTemp,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTmpMinDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum delta temperature.  The minimum change in
            temperature required to be treated as significant.""",
            name='nciTmpMinDelta',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.minDeltaTemp.minDeltaTemp,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSetPnts'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.setPnts.setPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=20,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCO2Offset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""CO2 level offset.  Used to calibrate external hardware
            with additive offset after transformation.""",
            name='nciCO2Offset',
            profile=self,
            number=21,
            datatype=pylon.resources.properties.offsetCO2.offsetCO2,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciCO2MinDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum delta CO2 level.  The minimum change in CO2 level
            required to be treated as significant.""",
            name='nciCO2MinDelta',
            profile=self,
            number=22,
            datatype=pylon.resources.properties.minDeltaCO2.minDeltaCO2,
            default=b'\x00\x0a',
            mandatory=False
        )
        self.properties['nciRHOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Relative humidity offset.  Used to calibrate external
            hardware with additive offset after transformation.""",
            name='nciRHOffset',
            profile=self,
            number=23,
            datatype=pylon.resources.properties.offsetRH.offsetRH,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRHMinDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum delta relative humidity.  The minimum change in RH
            level required to be treated as significant.""",
            name='nciRHMinDelta',
            profile=self,
            number=24,
            datatype=pylon.resources.properties.minDeltaRH.minDeltaRH,
            minimum=b'\x00\x00',
            default=b'\x00\xc8',
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=26,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTsccCommandModule'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = sccCommandModule()
    pass
