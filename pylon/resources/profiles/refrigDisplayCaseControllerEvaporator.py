"""refrigDisplayCaseControllerEvaporator standard profile, originally defined
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
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.evap_state
import pylon.resources.datapoints.temp_p
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.state
import pylon.resources.datapoints.defr_state
import pylon.resources.datapoints.press
import pylon.resources.properties.location
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.superHtRefMax
import pylon.resources.properties.superHtRefMin
import pylon.resources.properties.superHtRefInit
import pylon.resources.properties.strtupDelay
import pylon.resources.properties.strtupOpen
import pylon.resources.properties.refrigGlide
import pylon.resources.properties.refrigType


class refrigDisplayCaseControllerEvaporator(pylon.resources.base.Profile):
    """refrigDisplayCaseControllerEvaporator standard profile.  Refrigerated
    Display-Case Evaporation Controller.  Used to control the evaporation
    functions of a refigerated display case."""

    def __init__(self):
        super().__init__(
            key=10011,
            scope=0
        )
        self.datapoints['nvoAcuatorOpening'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve opening.  The current opening degree of the valve,
            in percent of fully open.""",
            name='nvoAcuatorOpening',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEvaporatorState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Evaporator state.  The current state of the evaporator
            object.""",
            name='nvoEvaporatorState',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.evap_state.evap_state,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviEvapInTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Evaporator Inlet Temperature.  These values indicate the
            current evaporator inlet (liquid line) temperature.  The input
            can be used if the sensor is external to the evaporator
            object.""",
            name='nviEvapInTemp',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoEvapInTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Evaporator Inlet Temperature.  These values indicate the
            current evaporator inlet (liquid line) temperature.  The output
            can be used if the sensor is internal to the evaporator
            object.""",
            name='nvoEvapInTemp',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviEvapOutTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Evaporator Outlet Temperature.  These values indicate the
            current evaporator outlet (suction line) temperature.  The input
            can be used if the sensor is external to the vaporator
            object.""",
            name='nviEvapOutTemp',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoEvapOutTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Evaporator Outlet Temperature.  These values indicate the
            current evaporator outlet (suction line) temperature.  The output
            can be used if the sensor is internal to the evaporator
            object.""",
            name='nvoEvapOutTemp',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviForcedValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Forced Value.  The nviForcedValve is used to force the
            valve to a given opening degree.  The evaporator object will stay
            in this forced mode as long as SNVT_switch.state equals TRUE.""",
            name='nviForcedValue',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSuperHeatTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Super Heat Temperature.  The nvoSuperHeatTemp indicates
            the true evaporator super heat temperature.  This variable should
            be used only when both pressure & emperature are used for
            calculation.  If only temperatures are used then the delta
            temperature output should be used.""",
            name='nvoSuperHeatTemp',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviThermostatState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Thermostat State.  This NV indicates the current state of
            the Thermostat Object.  There are currently three different
            control methods supported by the Thermostat Object (See PDF)""",
            name='nviThermostatState',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.state.state,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSuperHeatRef'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Super Heat Reference Temperature.  The nvoSuperHeatRef
            indicates the current target evaporator super heat
            temperature.""",
            name='nvoSuperHeatRef',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDefrostState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Defrost state.  This NV indicates the current state of the
            defrost object.""",
            name='nviDefrostState',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.defr_state.defr_state,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Calculated Air Temperature.  This NV is the calculated
            case air temperature.  An error on the sensor is indicated with
            the error value for SNVT_temp_p (0x7fff).""",
            name='nviAirTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCutoutTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cut out Temperature.  This NV indicates the current cut
            out limit used by the thermostat object in its agorithms.""",
            name='nviCutoutTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDifference'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Difference Temperature.  This NV indicates the value to be
            added to the nviCutoutTemp to get the thermostat cut in limit if
            cut in / out control is selected.""",
            name='nviDifference',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSuperHeatRef'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Super Heat Reference Temperature.  The nviSuperHeatRef is
            an override input for the target super heat reference.  This
            input should be used when the object is in override.""",
            name='nviSuperHeatRef',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPressure'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Liquid Line Pressure.  The input variable would be
            included on nodes without the hardware interface to read a
            pressure sensor, whereas the output variable would be included on
            nodes with pressure sensor hardware.""",
            name='nviPressure',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDeltaTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Delta Temperature.  This NV indicates the inferred
            evaporator super heat temperature.  This variable should be used
            when pressure is not taken into account in the calculation.""",
            name='nvoDeltaTemp',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPressure'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Liquid Line Pressure.  The pressure of the refrigerant in
            the liquid (evaporator feed) line.""",
            name='nvoPressure',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocationLabel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocationLabel',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSuperHtRefMax'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Super heat reference maximum.  Maximum value for the
            target super heat network variable.""",
            name='nciSuperHtRefMax',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.superHtRefMax.superHtRefMax,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSuperHtRefMin'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Super heat reference minimum.  Minimum value for the
            target super heat network variable.""",
            name='nciSuperHtRefMin',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.superHtRefMin.superHtRefMin,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSuperHtRefInit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Super heat reference initialization.  Default value for
            the super heat target network variable.""",
            name='nciSuperHtRefInit',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.superHtRefInit.superHtRefInit,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciStartUpDly'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Startup delay.  The time to delay after power-up, defrost,
            or pack fail.""",
            name='nciStartUpDly',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.strtupDelay.strtupDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciStartUpOpen'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Startup valve opening.  Maximum valve opening to use after
            power-up, defrost, or pack fail.""",
            name='nciStartUpOpen',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.strtupOpen.strtupOpen,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRefGlide'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Refrigerant glide.  Used to characterize the glide of the
            refrigerant used.""",
            name='nciRefGlide',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.refrigGlide.refrigGlide,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRefType'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Refrigerant type.  """,
            name='nciRefType',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.refrigType.refrigType,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTrefrigDisplayCaseControllerEvaporator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = refrigDisplayCaseControllerEvaporator()
    pass
