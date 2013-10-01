"""thermostat standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.hvac_status
import pylon.resources.properties.maxRcvTime
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.switch
import pylon.resources.properties.setPnts
import pylon.resources.properties.minDeltaTemp
import pylon.resources.properties.location
import pylon.resources.properties.heatUpperSP
import pylon.resources.properties.heatLowerSP
import pylon.resources.properties.coolUpperSP
import pylon.resources.properties.coolLowerSP


class thermostat(pylon.resources.base.Profile):
    """thermostat standard profile.  Thermostat Use to adjust HVAC setpoints
    for one or more heating/cooling units, and act upon temperature inputs
    for automated loop control."""

    def __init__(self):
        super().__init__(
            key=8060,
            scope=0
        )
        self.datapoints['nviSetPoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input.  This input network variable
            is used to allow the temperature setpoint for the occupied and
            standby mode being changed via the network.""",
            name='nviSetPoint',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoHeatOutput'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heat Control Output.  This output network variable
            reflects the current position of the heat actuator and can be
            used as part of a control loop and for monitoring purposes.""",
            name='nvoHeatOutput',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV02',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCoolOutput'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cool Control Output.  This output network variable
            reflects the current position of the cool actuator and can be
            used as part of a control loop and for monitoring purposes.""",
            name='nvoCoolOutput',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV03',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to send the value of a locally connected space temperature
            sensor to other nodes.  It is mandatory to the profile.""",
            name='nvoSpaceTemp',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV04':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV04',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit Status Output.  This output network variable is
            available to report the object status.""",
            name='nvoUnitStatus',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV05',
                    profile=self,
                    number=20,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
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
                    number=6,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Input.  This input network variable is used to
            command the thermostat object into different occupancy modes.""",
            name='nviOccCmd',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the thermostat object with any supervisory
            controller providing the supply energy, e.g.  hot or cold
            water.""",
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
                    number=7,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetPtOffset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the temperature setpoint via network by adding
            nviSetPtOffset to the current setpoint.""",
            name='nviSetPtOffset',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
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
                    number=8,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is from a device such
            as a door/window contact sensor.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.switch.switch,
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
                    number=9,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Terminal Load Output.  This output network variable
            reflects the current heat/cool energy demand of the Thermostat
            Device which is typically bound to an energy providing node.""",
            name='nvoTerminalLoad',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectSetPt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  The output network variable is
            used to report the effective setpoint temperature when the
            setpoint is changed through nciSetPnts, nviSetPoint,
            nviSetPtOffset or by local means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV12':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV12',
                    profile=self,
                    number=23,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalFan'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Terminal Fan.  This output network variable reflects the
            current fan speed of a multi-speed (n-speed) fan.  It can be used
            as part of a control loop and for monitoring purposes.""",
            name='nvoTerminalFan',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold Off Output.  This output is used to convey to
            other devices the state of an EnergyHoldOff device that is
            hardwired to the controller.  Refer to EnergyHoldOff Input.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.switch.switch,
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
                    number=22,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSetPnts'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.setPnts.setPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciMinDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum delta temperature.  The minimum change in
            temperature required to be treated as significant.""",
            name='nciMinDelta',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.minDeltaTemp.minDeltaTemp,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciUpSPHeat'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating setpoint upper limit.  Limits the upper extent of
            the permitted range for the heating setpoint.""",
            name='nciUpSPHeat',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.heatUpperSP.heatUpperSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x0d\xac',
            mandatory=False
        )
        self.properties['nciLrSPHeat'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating setpoint lower limit.  Limits the lower extent of
            the permitted range for the heating setpoint.""",
            name='nciLrSPHeat',
            profile=self,
            number=13,
            datatype=pylon.resources.properties.heatLowerSP.heatLowerSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciUpSPCool'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cooling setpoint upper limit.  Limits the upper extent of
            the permitted range for the cooling setpoint.""",
            name='nciUpSPCool',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.coolUpperSP.coolUpperSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciLrSPCool'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cooling setpoint lower limit.  Limits the lower extent of
            the permitted range for the cooling setpoint.""",
            name='nciLrSPCool',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.coolLowerSP.coolLowerSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=16,
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
            number=21,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTthermostat'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = thermostat()
    pass
