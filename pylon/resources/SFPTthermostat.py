"""SFPTthermostat standard profile, originally defined in resource file set
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTminDeltaTemp import SCPTminDeltaTemp
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTheatUpperSP import SCPTheatUpperSP
from pylon.resources.SCPTheatLowerSP import SCPTheatLowerSP
from pylon.resources.SCPTcoolUpperSP import SCPTcoolUpperSP
from pylon.resources.SCPTcoolLowerSP import SCPTcoolLowerSP


class SFPTthermostat(base.Profile):
    """SFPTthermostat standard profile.  Thermostat Use to adjust HVAC
    setpoints for one or more heating/cooling units, and act upon temperature
    inputs for automated loop control."""

    def __init__(self):
        super().__init__(
            key=8060,
            scope=0
        )
        self.datapoints['nviSetPoint'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input.  This input network variable
            is used to allow the temperature setpoint for the occupied and
            standby mode being changed via the network.""",
            name='nviSetPoint',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoHeatOutput'] = base.Profile.DatapointMember(
            doc="""Heat Control Output.  This output network variable
            reflects the current position of the heat actuator and can be
            used as part of a control loop and for monitoring purposes.""",
            name='nvoHeatOutput',
            profile=self,
            number=2,
            datatype=SNVT_lev_percent,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV02':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV02',
                    profile=self,
                    number=17,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCoolOutput'] = base.Profile.DatapointMember(
            doc="""Cool Control Output.  This output network variable
            reflects the current position of the cool actuator and can be
            used as part of a control loop and for monitoring purposes.""",
            name='nvoCoolOutput',
            profile=self,
            number=3,
            datatype=SNVT_lev_percent,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV03',
                    profile=self,
                    number=18,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to send the value of a locally connected space temperature
            sensor to other nodes.  It is mandatory to the profile.""",
            name='nvoSpaceTemp',
            profile=self,
            number=4,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV04':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV04',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit Status Output.  This output network variable is
            available to report the object status.""",
            name='nvoUnitStatus',
            profile=self,
            number=5,
            datatype=SNVT_hvac_status,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV05',
                    profile=self,
                    number=20,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=6,
            datatype=SNVT_temp_p,
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
                    number=6,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy Input.  This input network variable is used to
            command the thermostat object into different occupancy modes.""",
            name='nviOccCmd',
            profile=self,
            number=7,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the thermostat object with any supervisory
            controller providing the supply energy, e.g.  hot or cold
            water.""",
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
                    number=7,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetPtOffset'] = base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the temperature setpoint via network by adding
            nviSetPtOffset to the current setpoint.""",
            name='nviSetPtOffset',
            profile=self,
            number=9,
            datatype=SNVT_temp_p,
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
                    number=8,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold Off Input.  This input is from a device such
            as a door/window contact sensor.""",
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
                    number=9,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Terminal Load Output.  This output network variable
            reflects the current heat/cool energy demand of the Thermostat
            Device which is typically bound to an energy providing node.""",
            name='nvoTerminalLoad',
            profile=self,
            number=11,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectSetPt'] = base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  The output network variable is
            used to report the effective setpoint temperature when the
            setpoint is changed through nciSetPnts, nviSetPoint,
            nviSetPtOffset or by local means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV12':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV12',
                    profile=self,
                    number=23,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalFan'] = base.Profile.DatapointMember(
            doc="""Terminal Fan.  This output network variable reflects the
            current fan speed of a multi-speed (n-speed) fan.  It can be used
            as part of a control loop and for monitoring purposes.""",
            name='nvoTerminalFan',
            profile=self,
            number=13,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold Off Output.  This output is used to convey to
            other devices the state of an EnergyHoldOff device that is
            hardwired to the controller.  Refer to EnergyHoldOff Input.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=14,
            datatype=SNVT_switch,
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
                    number=22,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSetPnts'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=5,
            datatype=SCPTsetPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciMinDelta'] = base.Profile.PropertyMember(
            doc="""Minimum delta temperature.  The minimum change in
            temperature required to be treated as significant.""",
            name='nciMinDelta',
            profile=self,
            number=10,
            datatype=SCPTminDeltaTemp,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=11,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciUpSPHeat'] = base.Profile.PropertyMember(
            doc="""Heating setpoint upper limit.  Limits the upper extent of
            the permitted range for the heating setpoint.""",
            name='nciUpSPHeat',
            profile=self,
            number=12,
            datatype=SCPTheatUpperSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x0d\xac',
            mandatory=False
        )
        self.properties['nciLrSPHeat'] = base.Profile.PropertyMember(
            doc="""Heating setpoint lower limit.  Limits the lower extent of
            the permitted range for the heating setpoint.""",
            name='nciLrSPHeat',
            profile=self,
            number=13,
            datatype=SCPTheatLowerSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciUpSPCool'] = base.Profile.PropertyMember(
            doc="""Cooling setpoint upper limit.  Limits the upper extent of
            the permitted range for the cooling setpoint.""",
            name='nciUpSPCool',
            profile=self,
            number=14,
            datatype=SCPTcoolUpperSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciLrSPCool'] = base.Profile.PropertyMember(
            doc="""Cooling setpoint lower limit.  Limits the lower extent of
            the permitted range for the cooling setpoint.""",
            name='nciLrSPCool',
            profile=self,
            number=15,
            datatype=SCPTcoolLowerSP,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=16,
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
            number=21,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTthermostat()
    pass
