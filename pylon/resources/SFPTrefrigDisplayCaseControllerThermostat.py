"""SFPTrefrigDisplayCaseControllerThermostat standard profile, originally
defined in resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_state import SNVT_state
from pylon.resources.SNVT_lev_disc import SNVT_lev_disc
from pylon.resources.SNVT_defr_state import SNVT_defr_state
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTthermMode import SCPTthermMode
from pylon.resources.SCPTcutOutValue import SCPTcutOutValue
from pylon.resources.SCPTdiffValue import SCPTdiffValue
from pylon.resources.SCPTdayNightCntrl import SCPTdayNightCntrl
from pylon.resources.SCPTairTemp1Day import SCPTairTemp1Day
from pylon.resources.SCPTairTemp1Night import SCPTairTemp1Night
from pylon.resources.SCPTdeltaNight import SCPTdeltaNight
from pylon.resources.SCPTdiffNight import SCPTdiffNight
from pylon.resources.SCPTairTemp1Alrm import SCPTairTemp1Alrm
from pylon.resources.SCPThighLimTemp import SCPThighLimTemp
from pylon.resources.SCPTlowLimTemp import SCPTlowLimTemp
from pylon.resources.SCPThighLimDefrDly import SCPThighLimDefrDly
from pylon.resources.SCPTlowLimDly import SCPTlowLimDly
from pylon.resources.SCPThighLimDly import SCPThighLimDly


class SFPTrefrigDisplayCaseControllerThermostat(base.Profile):
    """SFPTrefrigDisplayCaseControllerThermostat standard profile.
    Refrigerated Display-Case Thermostat Controller.  Used to control the
    thermostatic functions of a refigerated display case."""

    def __init__(self):
        super().__init__(
            key=10012,
            scope=0
        )
        self.datapoints['nvoAirTemp'] = base.Profile.DatapointMember(
            doc="""Calculated Air Temperature.  This NV is the calculated
            case air temperature.  An error on the sensor is indicated with
            the error value for SNVT_temp_p (0x7fff).""",
            name='nvoAirTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoThermostatState'] = base.Profile.DatapointMember(
            doc="""Thermostat State.  This NV indicates the current state of
            the Thermostat Object.  There are currently three different
            control methods supported by the Thermostat Object (See PDF)""",
            name='nvoThermostatState',
            profile=self,
            number=2,
            datatype=SNVT_state,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviAirTemp1'] = base.Profile.DatapointMember(
            doc="""Measured Air Temperature 1.  This NV is to be assigned to
            discharge or return air as required.  An error on the sensor is
            indicated with the error value for SNVT_temp_p (0x7fff).""",
            name='nviAirTemp1',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDayNight'] = base.Profile.DatapointMember(
            doc="""Discrete level.  This SNVT is obsolete.  Use SNVT_switch
            instead.""",
            name='nviDayNight',
            profile=self,
            number=4,
            datatype=SNVT_lev_disc,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoCutoutTemp'] = base.Profile.DatapointMember(
            doc="""Cut out Temperature.  This NV indicates the current cut
            out limit used by the thermostat object in its agorithms.""",
            name='nvoCutoutTemp',
            profile=self,
            number=5,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviAirTemp2'] = base.Profile.DatapointMember(
            doc="""Measured Air Temperature 2.  This NV is to be assigned to
            discharge or return air as required.  An error on the sensor is
            indicated with the error value for SNVT_temp_p (0x7fff).""",
            name='nviAirTemp2',
            profile=self,
            number=6,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDifference'] = base.Profile.DatapointMember(
            doc="""Difference Temperature.  This NV indicates the value to be
            added to the nviCutoutTemp to get the thermostat cut in limit if
            cut in / out control is selected.""",
            name='nvoDifference',
            profile=self,
            number=7,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDefrostState'] = base.Profile.DatapointMember(
            doc="""Defrost state.  This NV indicates the current state of the
            defrost object.""",
            name='nviDefrostState',
            profile=self,
            number=8,
            datatype=SNVT_defr_state,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAlarmAirTemp'] = base.Profile.DatapointMember(
            doc="""Alarm Air Temperature.  The nvoAlarmAirTemp indicates the
            current air temperature used by the alarm section of the
            thermostat object.""",
            name='nvoAlarmAirTemp',
            profile=self,
            number=9,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDischargeTemp'] = base.Profile.DatapointMember(
            doc="""Discharge Air Temperature.  The nvoDischargeTemp indicates
            the current evaporator discharge air temperature used by the
            thermostat object.""",
            name='nvoDischargeTemp',
            profile=self,
            number=10,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoReturnTemp'] = base.Profile.DatapointMember(
            doc="""Return Air Temperature.  The nvoReturnTemp indicates the
            current evaporator return air temperature used by the thermostat
            object.""",
            name='nvoReturnTemp',
            profile=self,
            number=11,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActuatorValve'] = base.Profile.DatapointMember(
            doc="""Actuator Valve.  This output can be used to drive a
            refrigeration valve or compressor.""",
            name='nvoActuatorValve',
            profile=self,
            number=12,
            datatype=SNVT_lev_disc,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciLocationLabel'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocationLabel',
            profile=self,
            number=2,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciThermostatMode'] = base.Profile.PropertyMember(
            doc="""Thermostat mode.  The thermostat control strategy.""",
            name='nciThermostatMode',
            profile=self,
            number=3,
            datatype=SCPTthermMode,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciCutoutValue'] = base.Profile.PropertyMember(
            doc="""Cut-out value.  The cut-out limit.""",
            name='nciCutoutValue',
            profile=self,
            number=4,
            datatype=SCPTcutOutValue,
            default=b'\x03\xe8',
            mandatory=False
        )
        self.properties['nciDifferenceValue'] = base.Profile.PropertyMember(
            doc="""Difference value.  The value to be added to the cut-out
            value to get the cut-in limit.""",
            name='nciDifferenceValue',
            profile=self,
            number=5,
            datatype=SCPTdiffValue,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciDayNightControl'] = base.Profile.PropertyMember(
            doc="""Day/night control.  Configures the day/night function.""",
            name='nciDayNightControl',
            profile=self,
            number=6,
            datatype=SCPTdayNightCntrl,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentDay'] = base.Profile.PropertyMember(
            doc="""Air temperature 1 percent day.  The air temperature
            weighting used during day control.""",
            name='nciAirTemp1PercentDay',
            profile=self,
            number=7,
            datatype=SCPTairTemp1Day,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentNight'] = base.Profile.PropertyMember(
            doc="""Air temperature 1 percent night.  The air temperature
            weighting used during night control.""",
            name='nciAirTemp1PercentNight',
            profile=self,
            number=8,
            datatype=SCPTairTemp1Night,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDeltaNight'] = base.Profile.PropertyMember(
            doc="""Delta night.  The value to be added to the cut-out value
            to get the cut-out limit during night control.""",
            name='nciDeltaNight',
            profile=self,
            number=9,
            datatype=SCPTdeltaNight,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciDifferenceNight'] = base.Profile.PropertyMember(
            doc="""Difference night.  The value to be added to the cut-out
            value to get the cut-in limit during night control.""",
            name='nciDifferenceNight',
            profile=self,
            number=10,
            datatype=SCPTdiffNight,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciAirTemp1PercentAlarm'] = base.Profile.PropertyMember(
            doc="""Air temperature 1 percent alarm.  The weighting of the air
            temp 1 sensor when calculating the air temp alarm.""",
            name='nciAirTemp1PercentAlarm',
            profile=self,
            number=11,
            datatype=SCPTairTemp1Alrm,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciHighLimitTemp'] = base.Profile.PropertyMember(
            doc="""High limit temperature.  The high alarm set point for the
            alarm air temp network variable.""",
            name='nciHighLimitTemp',
            profile=self,
            number=12,
            datatype=SCPThighLimTemp,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLowLimitTemp'] = base.Profile.PropertyMember(
            doc="""Low limit temperature.  The low alarm set point for the
            alarm air temp network variable.""",
            name='nciLowLimitTemp',
            profile=self,
            number=13,
            datatype=SCPTlowLimTemp,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciHighLimitPdDly'] = base.Profile.PropertyMember(
            doc="""High limit defrost delay.  The time limit before high air
            temp alarm during pull-down.""",
            name='nciHighLimitPdDly',
            profile=self,
            number=14,
            datatype=SCPThighLimDefrDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLowLimitDelay'] = base.Profile.PropertyMember(
            doc="""Low limit delay.  The time limit during normal operation
            before the alarm air temp low alarm is recognized.""",
            name='nciLowLimitDelay',
            profile=self,
            number=15,
            datatype=SCPTlowLimDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciHighLimitDelay'] = base.Profile.PropertyMember(
            doc="""High limit delay.  The time limit during normal operation
            before the alarm air temp high alarm is recognized.""",
            name='nciHighLimitDelay',
            profile=self,
            number=16,
            datatype=SCPThighLimDly,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTrefrigDisplayCaseControllerThermostat()
    pass
