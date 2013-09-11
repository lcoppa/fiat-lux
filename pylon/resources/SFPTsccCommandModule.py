"""SFPTsccCommandModule standard profile, originally defined in resource file
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
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_time_stamp import SNVT_time_stamp
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_ppm import SNVT_ppm
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_temp_setpt import SNVT_temp_setpt
from pylon.resources.SCPToffsetTemp import SCPToffsetTemp
from pylon.resources.SCPTminDeltaTemp import SCPTminDeltaTemp
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPToffsetCO2 import SCPToffsetCO2
from pylon.resources.SCPTminDeltaCO2 import SCPTminDeltaCO2
from pylon.resources.SCPToffsetRH import SCPToffsetRH
from pylon.resources.SCPTminDeltaRH import SCPTminDeltaRH


class SFPTsccCommandModule(base.Profile):
    """SFPTsccCommandModule standard profile.  Space-Comfort Command Module.
    Used to control the HVAC comfort in a given space."""

    def __init__(self):
        super().__init__(
            key=8090,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to display the value of an external space temperature
            sensor.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=False,
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
                    number=11,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviUserLockout'] = base.Profile.DatapointMember(
            doc="""User Lockout Input.  This input network variable is used
            by the supervisory device to restrict the occupant from making
            certain changes.""",
            name='nviUserLockout',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTime'] = base.Profile.DatapointMember(
            doc="""Time Input.  This input network variable is used to
            display the local time in the Command Module Device.""",
            name='nviTime',
            profile=self,
            number=3,
            datatype=SNVT_time_stamp,
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
                    number=12,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEffectSetpt'] = base.Profile.DatapointMember(
            doc="""Effective Temperature Setpoint Input.  This input network
            variable is from a controller object and is used to display in
            the Command Module Device the controller's Effective
            Setpoint.""",
            name='nviEffectSetpt',
            profile=self,
            number=4,
            datatype=SNVT_temp_p,
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
                    number=13,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEffectOccup'] = base.Profile.DatapointMember(
            doc="""Effective Occupancy Input.  This input network variable is
            used to indicate the associated controller object's actual
            occupancy mode.""",
            name='nviEffectOccup',
            profile=self,
            number=5,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit Status Input.  This input network variable is
            transmitted from the Controller object to inform the occupant of
            the status of the associated HVAC equipment, to be displayed in
            the Command Module Device.""",
            name='nviUnitStatus',
            profile=self,
            number=6,
            datatype=SNVT_hvac_status,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV06':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV06',
                    profile=self,
                    number=14,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor Air Temperature Input.  This input network
            variable represents information from an outdoor air temperature
            sensor.""",
            name='nviOutdoorTemp',
            profile=self,
            number=7,
            datatype=SNVT_temp_p,
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
                    number=15,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor Air Humidity Input.  This input network variable
            is used to display outdoor humidity in percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=8,
            datatype=SNVT_lev_percent,
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
                    number=16,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space Humidity Input.  This input network variable is used
            to display space humidity in percent.""",
            name='nviSpaceRH',
            profile=self,
            number=9,
            datatype=SNVT_lev_percent,
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
                    number=17,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceCO2'] = base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Input.  This input network variable is
            used to display the space CO2 levels in PPM.""",
            name='nviSpaceCO2',
            profile=self,
            number=10,
            datatype=SNVT_ppm,
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
                    number=18,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is from a space comfort
            controller device which monitors inputs such as a window contact
            sensor.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=11,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV11':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV11',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoint'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Output.  This output network variable
            is used to allow the occupant to change the temperature setpoint
            for the occupied and standby mode from the Command Module
            Device.""",
            name='nvoSetpoint',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to transmit the space temperature that is hard wired to the
            Command Module Device.""",
            name='nvoSpaceTemp',
            profile=self,
            number=13,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV13':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV13',
                    profile=self,
                    number=25,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoHeatCool'] = base.Profile.DatapointMember(
            doc="""Heat/Cool Output.  This output network variable from the
            Command Module Device is used to transmit the user's command to
            the controller of the HVAC equipment.""",
            name='nvoHeatCool',
            profile=self,
            number=14,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV14':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV14',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFanSpeed'] = base.Profile.DatapointMember(
            doc="""Fan Speed Output.  This output network variable reflects
            the requested speed of a remote fan.""",
            name='nvoFanSpeed',
            profile=self,
            number=15,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOccSensor'] = base.Profile.DatapointMember(
            doc="""Occupancy Sensor Output.  The Command Module Device object
            conveys to the network the occupancy state of a hard wired
            occupancy sensor.""",
            name='nvoOccSensor',
            profile=self,
            number=16,
            datatype=SNVT_occupancy,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV16':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV16',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space Humidity Output.  This output network variable is
            used to transmit the space relative humidity that is hard wired
            to the Command Module Device.""",
            name='nvoSpaceRH',
            profile=self,
            number=17,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV17':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV17',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceCO2'] = base.Profile.DatapointMember(
            doc="""Space CO2 Sensor Output.  This output network variable is
            used to transmit the space CO2 sensor value that is hard wired to
            the Command Module Device.""",
            name='nvoSpaceCO2',
            profile=self,
            number=18,
            datatype=SNVT_ppm,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV18':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV18',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOccManCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy Manual Command Output.  The Command Module
            Device object conveys to the network the occupancy state as it is
            modified by the occupant.""",
            name='nvoOccManCmd',
            profile=self,
            number=19,
            datatype=SNVT_occupancy,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetptOffset'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Offset Output.  This output network
            variable is used to shift the temperature setpoint via the
            network, by adding nviSetPtOffset to the current setpoint.""",
            name='nvoSetptOffset',
            profile=self,
            number=20,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV20':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV20',
                    profile=self,
                    number=6,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSetpoints'] = base.Profile.DatapointMember(
            doc="""Occupancy Temperature Setpoints Output.  This output
            defines the occupancy temperature setpoints for heat and cool
            mode.""",
            name='nvoSetpoints',
            profile=self,
            number=21,
            datatype=SNVT_temp_setpt,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceCO2Lim'] = base.Profile.DatapointMember(
            doc="""Space CO2 Limit Output.  This network output property
            defines a high limit CO2 setpoint as requested by the occupant
            for ventilation functions.""",
            name='nvoSpaceCO2Lim',
            profile=self,
            number=22,
            datatype=SNVT_ppm,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceRHSetpt'] = base.Profile.DatapointMember(
            doc="""Space Humidity Setpoint Output.  This network output
            property defines the high limit humidity setpoint for the
            controlled space.""",
            name='nvoSpaceRHSetpt',
            profile=self,
            number=23,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTmpOffset'] = base.Profile.PropertyMember(
            doc="""Temperature offset.  Used to calibrate external hardware
            with additive offset after transformation.""",
            name='nciTmpOffset',
            profile=self,
            number=7,
            datatype=SCPToffsetTemp,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTmpMinDelta'] = base.Profile.PropertyMember(
            doc="""Minimum delta temperature.  The minimum change in
            temperature required to be treated as significant.""",
            name='nciTmpMinDelta',
            profile=self,
            number=8,
            datatype=SCPTminDeltaTemp,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=9,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSetPnts'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=10,
            datatype=SCPTsetPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=20,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCO2Offset'] = base.Profile.PropertyMember(
            doc="""CO2 level offset.  Used to calibrate external hardware
            with additive offset after transformation.""",
            name='nciCO2Offset',
            profile=self,
            number=21,
            datatype=SCPToffsetCO2,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciCO2MinDelta'] = base.Profile.PropertyMember(
            doc="""Minimum delta CO2 level.  The minimum change in CO2 level
            required to be treated as significant.""",
            name='nciCO2MinDelta',
            profile=self,
            number=22,
            datatype=SCPTminDeltaCO2,
            default=b'\x00\x0a',
            mandatory=False
        )
        self.properties['nciRHOffset'] = base.Profile.PropertyMember(
            doc="""Relative humidity offset.  Used to calibrate external
            hardware with additive offset after transformation.""",
            name='nciRHOffset',
            profile=self,
            number=23,
            datatype=SCPToffsetRH,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRHMinDelta'] = base.Profile.PropertyMember(
            doc="""Minimum delta relative humidity.  The minimum change in RH
            level required to be treated as significant.""",
            name='nciRHMinDelta',
            profile=self,
            number=24,
            datatype=SCPTminDeltaRH,
            minimum=b'\x00\x00',
            default=b'\x00\xc8',
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=26,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTsccCommandModule()
    pass
