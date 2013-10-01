"""boilerController standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.temp_p
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.pwrUpState
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.heatSetpt
import pylon.resources.properties.location
import pylon.resources.properties.minSendTime
import pylon.resources.properties.pumpDownDelay


class boilerController(pylon.resources.base.Profile):
    """boilerController standard profile.  Boiler Controller.  Can be used as
    an interface to a staged or a modulating boiler."""

    def __init__(self):
        super().__init__(
            key=8301,
            scope=0
        )
        self.datapoints['nviBoilerEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Boiler enable input.  Used to disable (stop) boiler
            operation, or to enable (automatic, local, or remote) boiler
            operation.""",
            name='nviBoilerEnable',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoBoilerState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Boiler state output.  Boiler's present level of heat
            output, as well as the requested firing rate of a remote
            boiler.""",
            name='nvoBoilerState',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective setpoint output.  Used to monitor the effective
            temperature setpoint.""",
            name='nvoEffectSetpt',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application mode input.  Used to coordinate the boiler
            controller node with any supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPumpSpeedCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump speed command input.  Used to connect an external
            pump control to the node or to allow an override of the pump
            speed.""",
            name='nviPumpSpeedCmd',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSupplyTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply temperature input.  Used to connect an external
            supply temperature sensor to the node.""",
            name='nviSupplyTemp',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outside air temperature input.  Represents information
            from an outdoor air temperature sensor.""",
            name='nviOutdoorTemp',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xf0\x60',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviReturnTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return temperature input.  Used to connect an external
            return temperature sensor to the node.""",
            name='nviReturnTemp',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetpoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature setpoint input (absolute) Used to allow the
            heating setpoint for the boiler water temperature to be changed
            via the network.""",
            name='nviSetpoint',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBoilerCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Boiler command input.  Used to command the boiler state
            and firing rate of the boiler controller (e.g., to disable the
            boiler, or allow automatic control)""",
            name='nviBoilerCmd',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoBoilerLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Boiler load output.  Present heat/cool energy demand of
            the unit.  Negative values indicate that heating energy is
            required (or in use) by the boiler controller.""",
            name='nvoBoilerLoad',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            maximum=b'\x00\x00',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupplyTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply temperature output.  Used to monitor the supply
            water temperature that the boiler controller is using for
            control.""",
            name='nvoSupplyTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalSupTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local supply temperature output.  Present value of a
            locally wired supply water temperature sensor.""",
            name='nvoLocalSupTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xf0\x60',
            maximum=b'\x1b\x58',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoReturnTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return temperature output.  Used to monitor the return
            water temperature that the boiler controller is using for
            control.""",
            name='nvoReturnTemp',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalRetTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local return temperature output.  Present value of a
            locally wired return water temperature sensor.""",
            name='nvoLocalRetTemp',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xf0\x60',
            maximum=b'\x1b\x58',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPumpSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump speed output.  Actual pump speed of a local
            multi-speed pump, as well as the requested speed of a remote
            pump.""",
            name='nvoPumpSpeed',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoBypassValve'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Bypass valve output.  Present value of the bypass control
            valve position (if hardwired) or can be used to control a remote
            bypass valve.""",
            name='nvoBypassValve',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air temperature output.  Used to monitor the
            outdoor air temperature that the boiler controller is using for
            control.""",
            name='nvoOutdoorTemp',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xf0\x60',
            maximum=b'\x1b\x58',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalOATemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local outdoor air temperature output.  Present value of a
            locally wired outdoor air temperature sensor.""",
            name='nvoLocalOATemp',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xf0\x60',
            maximum=b'\x1b\x58',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before the specified network variable outputs will automatically
            be updated.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            mandatory=True
        )
        self.properties['nciPowerUp'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Power-up enable.  Default power-up and restart modes of
            the boiler controller.""",
            name='nciPowerUp',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.pwrUpState.pwrUpState,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Receive heartbeat.  Maximum time that elapses after the
            last update to a specified network variable input before the
            boiler controller starts to use its default values.""",
            name='nciRcvHrtBt',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            mandatory=False
        )
        self.properties['nciHeatSetpt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating setpoint.  This applies to the setpoint NV input
            if one exists;  otherwise, it applies to the hardwired input.""",
            name='nciHeatSetpt',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.heatSetpt.heatSetpt,
            minimum=b'\x00\x00',
            maximum=b'\x3a\x98',
            default=b'\x0d\xac',
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum period of time between
            automatic network variable output transmissions.""",
            name='nciMinOutTm',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            mandatory=False
        )
        self.properties['nciOffDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Turn-off delay time.  Used to control the time delay that
            the pump remains "on" after a new command to turn the pump "off"
            is issued.""",
            name='nciOffDelay',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.pumpDownDelay.pumpDownDelay,
            mandatory=False
        )
        self._original_name = 'SFPTboilerController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = boilerController()
    pass
