"""fanCoilUnit standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.power
import pylon.resources.datapoints.hvac_status
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.setPnts
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.location
import pylon.resources.properties.numValves


class fanCoilUnit(pylon.resources.base.Profile):
    """fanCoilUnit standard profile.  Fan Coil Unit (FCU) Used to control the
    room temperature by controlling one heat and one cool actuator output, or
    a single actuator for heat and cool, and a fan with multiple fan-speed
    stages."""

    def __init__(self):
        super().__init__(
            key=8020,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space temperature input.  Optional input from a sensor
            node if the fan coil unit controller node itself provides a
            locally-wired space temperature sensor.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetPoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature setpoint input.  Allows the temperature
            setpoint for the occupied and standby mode to be changed via the
            network.""",
            name='nviSetPoint',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoHeatOutput'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heat control output.  Current position of the heat
            actuator;  can be used as part of a control loop and for
            monitoring purposes.""",
            name='nvoHeatOutput',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCoolOutput'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cool control output.  Current position of the cool
            actuator;  can be used as part of a control loop and for
            monitoring purposes.""",
            name='nvoCoolOutput',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFanSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan speed output.  Current fan speed of a multi-speed
            (n-speed) fan;  can be used as part of a control loop and for
            monitoring purposes.""",
            name='nvoFanSpeed',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviFanSpeedCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan speed command.  Used to connect an external fan speed
            switch to the node.""",
            name='nviFanSpeedCmd',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy input.  Commands the fan coil unit controller
            object into different occupancy modes.""",
            name='nviOccCmd',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application mode input.  Coordinates this object with any
            supervisory controller providing the supply energy.""",
            name='nviApplicMode',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetPtOffset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint offset input.  This setpoint shifting operates
            only on occupied and standby setpoints.  It does not affect the
            unoccupied setpoint.""",
            name='nviSetPtOffset',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x03\xe8',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviWaterTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Water temperature input.  Automatic heat/cool switchover
            dependent on the supply temperature.""",
            name='nviWaterTemp',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x23\x28',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoTerminalLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Terminal load output.  Present heat/cool energy demand of
            the FCU controller.""",
            name='nvoTerminalLoad',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLoadAbs'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Absolute power consumption output.  Present heat/cool
            power consumption of the FCU controller.""",
            name='nvoLoadAbs',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.power.power,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDischAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air temperature output.  Temperature of the air
            that leaves the fan coil.""",
            name='nvoDischAirTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoReheat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Reheat output.  Present state of an multi-stage (n-stage)
            reheat output.""",
            name='nvoReheat',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space temperature output.  Space temperature, if this
            temperature is locally measured.""",
            name='nvoSpaceTemp',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectSetPt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective setpoint output.  May depend on nciSetPnts,
            nviOccCmd, nviSetPoint, nviSetPtOffset, any local setpoint
            means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDischAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air temperature input.  The network value takes
            precedence over the physical value if both are available.""",
            name='nviDischAirTemp',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy hold-off input.  Input from a device such as a
            window contact sensor.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy output.  May derive from an occupancy sensor or
            any other means affecting the occupancy mode.""",
            name='nvoOccCmd',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy hold-off output.  Provides other devices the state
            of an EnergyHoldOff device that is hardwired to the
            controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit status output.  Combines operating mode, capacity of
            heating/cooling used, and an indication if any alarms are present
            in the object.""",
            name='nvoUnitStatus',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
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
        self.properties['nciSetPnts'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.setPnts.setPnts,
            minimum=b'\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciNumValve'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Number of output valves.  The value 1 implies one output
            valve (two pipe system) and the value 2 implies two output valves
            (four pipe system).""",
            name='nciNumValve',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.numValves.numValves,
            minimum=b'\x00\x01',
            maximum=b'\x00\x02',
            default=b'\x00\x02',
            mandatory=False
        )
        self._original_name = 'SFPTfanCoilUnit'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = fanCoilUnit()
    pass
