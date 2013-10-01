"""refrigDisplayCaseControllerThermostat standard profile, originally defined
in resource file set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.state
import pylon.resources.datapoints.lev_disc
import pylon.resources.datapoints.defr_state
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.location
import pylon.resources.properties.thermMode
import pylon.resources.properties.cutOutValue
import pylon.resources.properties.diffValue
import pylon.resources.properties.dayNightCntrl
import pylon.resources.properties.airTemp1Day
import pylon.resources.properties.airTemp1Night
import pylon.resources.properties.deltaNight
import pylon.resources.properties.diffNight
import pylon.resources.properties.airTemp1Alrm
import pylon.resources.properties.highLimTemp
import pylon.resources.properties.lowLimTemp
import pylon.resources.properties.highLimDefrDly
import pylon.resources.properties.lowLimDly
import pylon.resources.properties.highLimDly


class refrigDisplayCaseControllerThermostat(pylon.resources.base.Profile):
    """refrigDisplayCaseControllerThermostat standard profile.  Refrigerated
    Display-Case Thermostat Controller.  Used to control the thermostatic
    functions of a refigerated display case."""

    def __init__(self):
        super().__init__(
            key=10012,
            scope=0
        )
        self.datapoints['nvoAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Calculated Air Temperature.  This NV is the calculated
            case air temperature.  An error on the sensor is indicated with
            the error value for SNVT_temp_p (0x7fff).""",
            name='nvoAirTemp',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoThermostatState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Thermostat State.  This NV indicates the current state of
            the Thermostat Object.  There are currently three different
            control methods supported by the Thermostat Object (See PDF)""",
            name='nvoThermostatState',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.state.state,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviAirTemp1'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Measured Air Temperature 1.  This NV is to be assigned to
            discharge or return air as required.  An error on the sensor is
            indicated with the error value for SNVT_temp_p (0x7fff).""",
            name='nviAirTemp1',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDayNight'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discrete level.  This SNVT is obsolete.  Use SNVT_switch
            instead.""",
            name='nviDayNight',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.lev_disc.lev_disc,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoCutoutTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cut out Temperature.  This NV indicates the current cut
            out limit used by the thermostat object in its agorithms.""",
            name='nvoCutoutTemp',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviAirTemp2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Measured Air Temperature 2.  This NV is to be assigned to
            discharge or return air as required.  An error on the sensor is
            indicated with the error value for SNVT_temp_p (0x7fff).""",
            name='nviAirTemp2',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDifference'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Difference Temperature.  This NV indicates the value to be
            added to the nviCutoutTemp to get the thermostat cut in limit if
            cut in / out control is selected.""",
            name='nvoDifference',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDefrostState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Defrost state.  This NV indicates the current state of the
            defrost object.""",
            name='nviDefrostState',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.defr_state.defr_state,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAlarmAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm Air Temperature.  The nvoAlarmAirTemp indicates the
            current air temperature used by the alarm section of the
            thermostat object.""",
            name='nvoAlarmAirTemp',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDischargeTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge Air Temperature.  The nvoDischargeTemp indicates
            the current evaporator discharge air temperature used by the
            thermostat object.""",
            name='nvoDischargeTemp',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoReturnTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return Air Temperature.  The nvoReturnTemp indicates the
            current evaporator return air temperature used by the thermostat
            object.""",
            name='nvoReturnTemp',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActuatorValve'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator Valve.  This output can be used to drive a
            refrigeration valve or compressor.""",
            name='nvoActuatorValve',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.lev_disc.lev_disc,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciLocationLabel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocationLabel',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciThermostatMode'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Thermostat mode.  The thermostat control strategy.""",
            name='nciThermostatMode',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.thermMode.thermMode,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciCutoutValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cut-out value.  The cut-out limit.""",
            name='nciCutoutValue',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.cutOutValue.cutOutValue,
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciDifferenceValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Difference value.  The value to be added to the cut-out
            value to get the cut-in limit.""",
            name='nciDifferenceValue',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.diffValue.diffValue,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciDayNightControl'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Day/night control.  Configures the day/night function.""",
            name='nciDayNightControl',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.dayNightCntrl.dayNightCntrl,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentDay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Air temperature 1 percent day.  The air temperature
            weighting used during day control.""",
            name='nciAirTemp1PercentDay',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.airTemp1Day.airTemp1Day,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentNight'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Air temperature 1 percent night.  The air temperature
            weighting used during night control.""",
            name='nciAirTemp1PercentNight',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.airTemp1Night.airTemp1Night,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDeltaNight'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Delta night.  The value to be added to the cut-out value
            to get the cut-out limit during night control.""",
            name='nciDeltaNight',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.deltaNight.deltaNight,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciDifferenceNight'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Difference night.  The value to be added to the cut-out
            value to get the cut-in limit during night control.""",
            name='nciDifferenceNight',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.diffNight.diffNight,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Air temperature 1 percent alarm.  The weighting of the air
            temp 1 sensor when calculating the air temp alarm.""",
            name='nciAirTemp1PercentAlarm',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.airTemp1Alrm.airTemp1Alrm,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciHighLimitTemp'] = pylon.resources.base.Profile.PropertyMember(
            doc="""High limit temperature.  The high alarm set point for the
            alarm air temp network variable.""",
            name='nciHighLimitTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.highLimTemp.highLimTemp,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLowLimitTemp'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Low limit temperature.  The low alarm set point for the
            alarm air temp network variable.""",
            name='nciLowLimitTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.properties.lowLimTemp.lowLimTemp,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciHighLimitPdDly'] = pylon.resources.base.Profile.PropertyMember(
            doc="""High limit defrost delay.  The time limit before high air
            temp alarm during pull-down.""",
            name='nciHighLimitPdDly',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.highLimDefrDly.highLimDefrDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLowLimitDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Low limit delay.  The time limit during normal operation
            before the alarm air temp low alarm is recognized.""",
            name='nciLowLimitDelay',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.lowLimDly.lowLimDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciHighLimitDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""High limit delay.  The time limit during normal operation
            before the alarm air temp high alarm is recognized.""",
            name='nciHighLimitDelay',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.highLimDly.highLimDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTrefrigDisplayCaseControllerThermostat'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = refrigDisplayCaseControllerThermostat()
    pass
