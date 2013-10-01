"""dischargeAirController standard profile, originally defined in resource
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
import pylon.resources.datapoints.tod_event
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.datapoints.press_p
import pylon.resources.datapoints.temp_p
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.flow
import pylon.resources.datapoints.enthalpy
import pylon.resources.datapoints.hvac_status
import pylon.resources.properties.minRnge
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.dischargeAirCoolingSetpoint
import pylon.resources.properties.dischargeAirHeatingSetpoint
import pylon.resources.properties.setPnts
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.location
import pylon.resources.properties.bypassTime
import pylon.resources.properties.maxSupplyFanCapacity
import pylon.resources.properties.minSupplyFanCapacity
import pylon.resources.properties.maxReturnExhaustFanCapacity
import pylon.resources.properties.minReturnExhaustFanCapacity
import pylon.resources.properties.ductStaticPressureSetpoint
import pylon.resources.properties.maxDuctStaticPressureSetpoint
import pylon.resources.properties.minDuctStaticPressureSetpoint
import pylon.resources.properties.ductStaticPressureLimit
import pylon.resources.properties.buildingStaticPressureSetpoint
import pylon.resources.properties.returnFanStaticPressureSetpoint
import pylon.resources.properties.fanDifferentialSetpoint
import pylon.resources.properties.mixedAirLowLimitSetpoint
import pylon.resources.properties.mixedAirTempSetpoint
import pylon.resources.properties.minOutdoorAirFlowSetpoint
import pylon.resources.properties.sensConstVAV
import pylon.resources.properties.ductArea
import pylon.resources.properties.outdoorAirTempSetpoint
import pylon.resources.properties.outdoorAirEnthalpySetpoint
import pylon.resources.properties.diffTempSetpoint
import pylon.resources.properties.exhaustEnablePosition
import pylon.resources.properties.spaceHumSetpoint
import pylon.resources.properties.humSetpt
import pylon.resources.properties.dischargeAirDewpointSetpoint
import pylon.resources.properties.maxDischargeAirCoolingSetpoint
import pylon.resources.properties.minDischargeAirCoolingSetpoint
import pylon.resources.properties.maxDischargeAirHeatingSetpoint
import pylon.resources.properties.minDischargeAirHeatingSetpoint
import pylon.resources.properties.coolingLockout
import pylon.resources.properties.heatingLockout
import pylon.resources.properties.coolingResetEnable
import pylon.resources.properties.heatingResetEnable


class dischargeAirController(pylon.resources.base.Profile):
    """dischargeAirController standard profile.  Discharge-Air Controller
    (DAC) Used to control duct static pressure and discharge-air
    temperature."""

    def __init__(self):
        super().__init__(
            key=8610,
            scope=0
        )
        self.datapoints['nviOccSchedule'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy scheduler input.  Commands the Discharge-Air
            Controller into different occupancy modes typically sent by
            scheduler or supervisory node.""",
            name='nviOccSchedule',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.tod_event.tod_event,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccManCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy override input.  Commands the Discharge-Air
            Controller into different occupancy modes.""",
            name='nviOccManCmd',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application mode input.  Coordinates the Discharge-Air
            Controller with any supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency override input.  Commands the device into
            different emergency modes.""",
            name='nviEmergOverride',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctStatPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Duct static pressure input.  Connects a duct static
            pressure sensor or network output from another controller.""",
            name='nviDuctStatPress',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x04\xe2',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctStaticSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Duct static pressure setpoint input.  Sets duct static
            pressure setpoint of the controller via the network.""",
            name='nviDuctStaticSP',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x04\xe2',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDAClSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air cooling setpoint input.  Sets discharge-air
            cooling setpoint of the controller via the network.""",
            name='nviDAClSP',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x0b\xb8',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDAHtSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge-Air heating setpoint input.  Sets discharge-air
            heating setpoint of the controller via the network.""",
            name='nviDAHtSP',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x1b\x58',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSupFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply fan capacity input.  Commands override of the
            supply fan capacity from another controller.""",
            name='nviSupFanCap',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviExhFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Exhaust fan capacity input.  Connects network output from
            another controller to override the local exhaust fan capacity
            control.""",
            name='nviExhFanCap',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRetFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return fan capacity input.  Commands an override of return
            fan capacity from another controller.""",
            name='nviRetFanCap',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFanDiffSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan differential setpoint input.  Setpoint for the percent
            capacity difference between the supply and return fans.""",
            name='nviFanDiffSP',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x27\x10',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBldgStatPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Building static pressure input.  Connects network building
            static pressure sensor or network output from another
            controller.""",
            name='nviBldgStatPress',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            minimum=b'\xff\x83',
            maximum=b'\x00\x7d',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBldgStaticSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Building static pressure setpoint input.  Connects network
            output from another controller to provide the building static
            pressure setpoint.""",
            name='nviBldgStaticSP',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            minimum=b'\xff\x9c',
            maximum=b'\x00\x64',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPriCoolEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary cool enable input.  Connect network output from
            another controller to enable/disable the primary cooling output
            of the unit.""",
            name='nviPriCoolEnable',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPriHeatEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary heat enable input.  Connects network output from
            another controller to enable/disable the primary heating outputs
            of the unit.""",
            name='nviPriHeatEnable',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEconEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Economizer enable input.  Enables and disables economizer
            operation.""",
            name='nviEconEnable',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOAMinPos'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air minimum position input.  Sets minimum outdoor
            air damper position of controller via the network.""",
            name='nviOAMinPos',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMinOAFlowSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Minimum outdoor airflow setpoint input.  Commands a
            minimum outdoor airflow rate setpoint from the network.""",
            name='nviMinOAFlowSP',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\xc3\x50',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air temperature input.  Measured outdoor air dry
            bulb temperature.""",
            name='nviOutdoorTemp',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xf0\x60',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air humidity input.  Measured outdoor air humidity
            in percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOAEnthalpy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air enthalpy input.  Connects a network outdoor
            air enthalpy sensor or network controller output.""",
            name='nviOAEnthalpy',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.enthalpy.enthalpy,
            mandatory=False,
            minimum=b'\x07\xd0',
            maximum=b'\x27\x10',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMATSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Mixed air temperature setpoint input.  Commands a mixed
            air temperature setpoint from the network.""",
            name='nviMATSP',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRATemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return air temperature input.  Connects a network return
            air temperature sensor or network output from another
            controller.""",
            name='nviRATemp',
            profile=self,
            number=24,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceEnthalpy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space enthalpy input.  Connects a network return air or
            space enthalpy sensor or network output from another
            controller.""",
            name='nviSpaceEnthalpy',
            profile=self,
            number=25,
            datatype=pylon.resources.datapoints.enthalpy.enthalpy,
            mandatory=False,
            minimum=b'\x07\xd0',
            maximum=b'\x27\x10',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space temperature input.  Connects a network space
            temperature sensor or network output from another controller.""",
            name='nviSpaceTemp',
            profile=self,
            number=26,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space humidity input.  Connects a network return air or
            space relative humidity sensor or network output from another
            controller.""",
            name='nviSpaceRH',
            profile=self,
            number=27,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHumEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Humidification enable input.  Enables humidification
            function in the controller.""",
            name='nviHumEnable',
            profile=self,
            number=28,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceHumSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space humidification setpoint input.  Connects a network
            space humidity setpoint or network output from another
            controller.""",
            name='nviSpaceHumSP',
            profile=self,
            number=29,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDehumEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dehumidification enable input.  Enables dehumidification
            function in the controller.""",
            name='nviDehumEnable',
            profile=self,
            number=30,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceDehumSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space dehumidification setpoint input.  Connects a network
            space dehumidification setpoint or network output from another
            controller.""",
            name='nviSpaceDehumSP',
            profile=self,
            number=31,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDADewPointSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air dewpoint setpoint input.  Commands a
            discharge-air dewpoint setpoint from the network.""",
            name='nviDADewPointSP',
            profile=self,
            number=32,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xf8\x30',
            maximum=b'\x0b\xb8',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser water temperature input.  Connects a network
            condenser water temperature sensor or network output from another
            controller.""",
            name='nviCWTemp',
            profile=self,
            number=33,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCWFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser water flow input.  System condenser flow
            status.""",
            name='nviCWFlow',
            profile=self,
            number=34,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDischAirTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air temperature output.  Monitors discharge-air
            temperature measured by a hardwired sensor.""",
            name='nvoDischAirTemp',
            profile=self,
            number=35,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit status output.  Reports the Discharge-Air Controller
            status.""",
            name='nvoUnitStatus',
            profile=self,
            number=36,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDATempSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective discharge-air temperature setpoint output.
            Monitors the effective discharge-air temperature setpoint the
            Discharge-Air Controller is using for control.""",
            name='nvoEffDATempSP',
            profile=self,
            number=37,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDuctStatPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Duct static pressure output.  Monitors the effective duct
            static pressure the controller is using for control.""",
            name='nvoDuctStatPress',
            profile=self,
            number=38,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDuctStatSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective duct static pressure setpoint output.  Monitors
            the effective duct static pressure setpoint the Discharge-Air
            Controller is using for control.""",
            name='nvoEffDuctStatSP',
            profile=self,
            number=39,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatCool'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective heat/cool output.  Actual heat/cool mode of the
            unit.""",
            name='nvoHeatCool',
            profile=self,
            number=40,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application mode output.  Used to control the mode of
            other controllers such as a VAV box controller.""",
            name='nvoApplicMode',
            profile=self,
            number=41,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectOccup'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective occupancy output.  Transmits the current
            occupancy mode of the Discharge-Air Controller for
            monitoring.""",
            name='nvoEffectOccup',
            profile=self,
            number=42,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply fan status output.  Actual status of the supply fan
            for monitoring.""",
            name='nvoSupFanStatus',
            profile=self,
            number=43,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanOnOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply fan on/off control output.  Used to start and stop
            the supply fan.""",
            name='nvoSupFanOnOff',
            profile=self,
            number=44,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Supply fan capacity output.  Used to command the supply
            fan speed or capacity.""",
            name='nvoSupFanCap',
            profile=self,
            number=45,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Exhaust fan status output.  Actual status of the exhaust
            fan for monitoring.""",
            name='nvoExhFanStatus',
            profile=self,
            number=46,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanOnOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Exhaust fan on/off control output.  Used to start and stop
            the exhaust fan.""",
            name='nvoExhFanOnOff',
            profile=self,
            number=47,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Exhaust fan capacity output.  Used to command the exhaust
            fan speed or capacity.""",
            name='nvoExhFanCap',
            profile=self,
            number=48,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhDamper'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Exhaust damper control output.  Present status of Exhaust
            Damper output for monitoring or control.""",
            name='nvoExhDamper',
            profile=self,
            number=49,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return fan status output.  Actual status of the return fan
            for monitoring.""",
            name='nvoRetFanStatus',
            profile=self,
            number=50,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanOnOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return fan on/off control output.  Used to start and stop
            the return fan.""",
            name='nvoRetFanOnOff',
            profile=self,
            number=51,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return fan capacity output.  Used to command the return
            fan speed or capacity.""",
            name='nvoRetFanCap',
            profile=self,
            number=52,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return fan pressure output.  Present value of return fan
            static pressure for monitoring.""",
            name='nvoRetFanPress',
            profile=self,
            number=53,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoBldgStatPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Building static pressure output.  Present value of the
            building static pressure for monitoring.""",
            name='nvoBldgStatPress',
            profile=self,
            number=54,
            datatype=pylon.resources.datapoints.press_p.press_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEconEnabled'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Economizer enabled output.  Present enable/disable status
            of economizer for monitoring.""",
            name='nvoEconEnabled',
            profile=self,
            number=55,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOADamper'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air damper output.  Present level of the outdoor
            air damper or injection fan capacity output for monitoring or
            control.""",
            name='nvoOADamper',
            profile=self,
            number=56,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciOAMinPos':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Outdoor air damper minimum position.  Default
                    minimum outdoor air damper position setpoint for the
                    Discharge-Air Controller.""",
                    name='nciOAMinPos',
                    profile=self,
                    number=22,
                    datatype=pylon.resources.properties.minRnge.minRnge,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOAFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor airflow output.  Present value of the outdoor
            airflow for monitoring.""",
            name='nvoOAFlow',
            profile=self,
            number=57,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalOATemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local outdoor air temperature output.  Indicates value of
            a hardwired outdoor air temperature sensor.""",
            name='nvoLocalOATemp',
            profile=self,
            number=58,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air temperature output.  Present value of outdoor
            air temperature for monitoring.""",
            name='nvoOutdoorTemp',
            profile=self,
            number=59,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalOARH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local outdoor air humidity output.  Indicates value of
            hardwired outdoor air relative humidity sensor.""",
            name='nvoLocalOARH',
            profile=self,
            number=60,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air humidity output.  Present value of outdoor air
            humidity for monitoring.""",
            name='nvoOutdoorRH',
            profile=self,
            number=61,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOAEnthalpy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air enthalpy output.  Present value of the outdoor
            air enthalpy.""",
            name='nvoOAEnthalpy',
            profile=self,
            number=62,
            datatype=pylon.resources.datapoints.enthalpy.enthalpy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCoolPrimary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary Cooling Output.  Present level of the primary
            cooling capacity.""",
            name='nvoCoolPrimary',
            profile=self,
            number=63,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatPrimary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary heating output.  Present value of the primary
            heating capacity.""",
            name='nvoHeatPrimary',
            profile=self,
            number=64,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMATemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Mixed air temperature output.  Present value of the mixed
            air dry bulb temperature.""",
            name='nvoMATemp',
            profile=self,
            number=65,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space temperature output.  Present value of the space
            temperature for monitoring.""",
            name='nvoSpaceTemp',
            profile=self,
            number=66,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRATemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Return air temperature output.  Present value of return
            air temperature for monitoring.""",
            name='nvoRATemp',
            profile=self,
            number=67,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space humidity output.  Present value of the space
            relative humidity for monitoring.""",
            name='nvoSpaceRH',
            profile=self,
            number=68,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceEnthalpy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space enthalpy output.  Present value of the space
            enthalpy.""",
            name='nvoSpaceEnthalpy',
            profile=self,
            number=69,
            datatype=pylon.resources.datapoints.enthalpy.enthalpy,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffSpaceHumSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective space humidification setpoint output.  Effective
            space low limit humidity setpoint for monitoring.""",
            name='nvoEffSpaceHumSP',
            profile=self,
            number=70,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHumidifier'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Humidification status output.  Present level of the
            humidifier output for monitoring.""",
            name='nvoHumidifier',
            profile=self,
            number=71,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffSpaceDHSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective space dehumidification setpoint output.
            Effective space high limit humidity setpoint for monitoring.""",
            name='nvoEffSpaceDHSP',
            profile=self,
            number=72,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDehumidifier'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dehumidification status output.  Present status of
            dehumidification control for monitoring.""",
            name='nvoDehumidifier',
            profile=self,
            number=73,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDADewPtSP'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective discharge-air dewpoint setpoint output.
            Monitors the effective discharge-air dewpoint setpoint that the
            discharge-air controller is using for control.""",
            name='nvoEffDADewPtSP',
            profile=self,
            number=74,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDADewPoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Discharge air dewpoint temperature output.  Present value
            of the discharge-air dewpoint temperature.""",
            name='nvoDADewPoint',
            profile=self,
            number=75,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCondCap'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser capacity output.  Present value of the condenser
            capacity control output for monitoring.""",
            name='nvoCondCap',
            profile=self,
            number=76,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalCWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local condenser water temperature output.  Transmits value
            of hardwired condenser water temperature sensor.""",
            name='nvoLocalCWTemp',
            profile=self,
            number=77,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser water temperature output.  Present value of
            condenser water temperature for monitoring.""",
            name='nvoCWTemp',
            profile=self,
            number=78,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser water flow output.  Transmits current status of
            condenser water flow sensor for monitoring.""",
            name='nvoCWFlow',
            profile=self,
            number=79,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWPump'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Condenser water pump output.  Transmits the current state
            of condenser water pump output for monitoring or control.""",
            name='nvoCWPump',
            profile=self,
            number=80,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before specified NV outputs will be automatically updated.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            mandatory=True
        )
        self.properties['nciDAClSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Discharge air cooling setpoint.  Default discharge-air
            cooling setpoint for the Discharge-Air Controller.""",
            name='nciDAClSP',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.dischargeAirCoolingSetpoint.dischargeAirCoolingSetpoint,
            mandatory=True
        )
        self.properties['nciDAHtSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Discharge air heating setpoint.  Default discharge-air
            heating setpoint for the Discharge-Air Controller.""",
            name='nciDAHtSP',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.dischargeAirHeatingSetpoint.dischargeAirHeatingSetpoint,
            mandatory=True
        )
        self.properties['nciSetpoints'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  Space temperature
            setpoints for various heat, cool and occupancy modes.""",
            name='nciSetpoints',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.setPnts.setPnts,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum time between automatic NV
            output transmissions.""",
            name='nciMinOutTm',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Receive heartbeat.  Controls maximum time after last
            update before default values are used.""",
            name='nciRcvHrtBt',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciBypassTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Local bypass time.  Maximum time the controller can be in
            bypass mode following request.""",
            name='nciBypassTime',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.bypassTime.bypassTime,
            mandatory=False
        )
        self.properties['nciMaxSupFanCap'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum supply fan capacity.  Maximum supply fan capacity
            setpoint for the Discharge-Air Controller.""",
            name='nciMaxSupFanCap',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.maxSupplyFanCapacity.maxSupplyFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMinSupFanCap'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum supply fan capacity.  Minimum supply fan capacity
            setpoint for the Discharge-Air Controller.""",
            name='nciMinSupFanCap',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.minSupplyFanCapacity.minSupplyFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMaxREFanCap'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum return/exhaust fan capacity.  Maximum
            return/exhaust fan capacity setpoint for the Discharge-Air
            Controller.""",
            name='nciMaxREFanCap',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.maxReturnExhaustFanCapacity.maxReturnExhaustFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMinREFanCap'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum return/exhaust fan capacity.  Minimum
            return/exhaust fan capacity setpoint for the Discharge-Air
            Controller.""",
            name='nciMinREFanCap',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.minReturnExhaustFanCapacity.minReturnExhaustFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDuctStatSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Duct static pressure setpoint.  Default duct static
            pressure setpoint for the Discharge-Air Controller.""",
            name='nciDuctStatSP',
            profile=self,
            number=13,
            datatype=pylon.resources.properties.ductStaticPressureSetpoint.ductStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDuctStatSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum duct static pressure setpoint.  Maximum duct
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciMaxDuctStatSP',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.maxDuctStaticPressureSetpoint.maxDuctStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciMinDuctStatSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum duct static pressure setpoint.  Minimum duct
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciMinDuctStatSP',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.minDuctStaticPressureSetpoint.minDuctStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciDuctStatLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Duct static pressure limit.  Duct static pressure limit,
            used for equipment protection.""",
            name='nciDuctStatLim',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.ductStaticPressureLimit.ductStaticPressureLimit,
            mandatory=False
        )
        self.properties['nciBldgStaticSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Building static pressure setpoint.  Default building
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciBldgStaticSP',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.buildingStaticPressureSetpoint.buildingStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciRetFanPressSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Return fan pressure setpoint.  Return fan static pressure
            setpoint for the Discharge-Air Controller.""",
            name='nciRetFanPressSP',
            profile=self,
            number=18,
            datatype=pylon.resources.properties.returnFanStaticPressureSetpoint.returnFanStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciFanDiffSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fan differential setpoint.  Default for percent capacity
            difference between supply and return fans.""",
            name='nciFanDiffSP',
            profile=self,
            number=19,
            datatype=pylon.resources.properties.fanDifferentialSetpoint.fanDifferentialSetpoint,
            mandatory=False
        )
        self.properties['nciMALowLimitSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Mixed air low limit setpoint.  Mixed air low limit
            setpoint for the Discharge-Air Controller.""",
            name='nciMALowLimitSP',
            profile=self,
            number=20,
            datatype=pylon.resources.properties.mixedAirLowLimitSetpoint.mixedAirLowLimitSetpoint,
            mandatory=False
        )
        self.properties['nciMATSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Mixed air temperature setpoint.  Default mixed air
            temperature setpoint for the Discharge-Air Controller.""",
            name='nciMATSP',
            profile=self,
            number=21,
            datatype=pylon.resources.properties.mixedAirTempSetpoint.mixedAirTempSetpoint,
            mandatory=False
        )
        self.properties['nciMinOAFlowSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum outdoor airflow setpoint.  Default minimum outdoor
            airflow setpoint for the Discharge-Air Controller.""",
            name='nciMinOAFlowSP',
            profile=self,
            number=23,
            datatype=pylon.resources.properties.minOutdoorAirFlowSetpoint.minOutdoorAirFlowSetpoint,
            mandatory=False
        )
        self.properties['nciOAFlowCalib'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Outdoor airflow calibration.  Gain for the outdoor airflow
            calibration for the Discharge-Air Controller.""",
            name='nciOAFlowCalib',
            profile=self,
            number=24,
            datatype=pylon.resources.properties.sensConstVAV.sensConstVAV,
            mandatory=False
        )
        self.properties['nciOAInletArea'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Outdoor air inlet area.  Area of the outdoor air inlet for
            the Discharge-Air Controller.""",
            name='nciOAInletArea',
            profile=self,
            number=25,
            datatype=pylon.resources.properties.ductArea.ductArea,
            mandatory=False
        )
        self.properties['nciOATSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Outdoor air temperature setpoint.  Airside economizer
            outdoor air temperature enable setpoint for the Discharge-Air
            Controller.""",
            name='nciOATSP',
            profile=self,
            number=26,
            datatype=pylon.resources.properties.outdoorAirTempSetpoint.outdoorAirTempSetpoint,
            mandatory=False
        )
        self.properties['nciOAEnthSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Outdoor air enthalpy setpoint.  Default airside economizer
            outdoor air enthalpy enable setpoint for the Discharge-Air
            Controller.""",
            name='nciOAEnthSP',
            profile=self,
            number=27,
            datatype=pylon.resources.properties.outdoorAirEnthalpySetpoint.outdoorAirEnthalpySetpoint,
            mandatory=False
        )
        self.properties['nciTempDiff'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Economizer enable differential temperature setpoint.
            Differential between entering air temp and entering condenser
            water temp to enable economizer operation.""",
            name='nciTempDiff',
            profile=self,
            number=28,
            datatype=pylon.resources.properties.diffTempSetpoint.diffTempSetpoint,
            mandatory=False
        )
        self.properties['nciExhStartPos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Exhaust enable position.  Exhaust enable outdoor air
            damper position setpoint for the Discharge-Air Controller.""",
            name='nciExhStartPos',
            profile=self,
            number=29,
            datatype=pylon.resources.properties.exhaustEnablePosition.exhaustEnablePosition,
            mandatory=False
        )
        self.properties['nciSpaceHumSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Space humidification setpoint.  Default space
            humidification setpoint for the Discharge-Air Controller.""",
            name='nciSpaceHumSP',
            profile=self,
            number=30,
            datatype=pylon.resources.properties.spaceHumSetpoint.spaceHumSetpoint,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciSpaceDehumSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Space dehumidification setpoint.  Default space
            dehumidification setpoint for the Discharge-Air Controller.""",
            name='nciSpaceDehumSP',
            profile=self,
            number=31,
            datatype=pylon.resources.properties.humSetpt.humSetpt,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDADewPointSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Discharge air dewpoint setpoint.  Default discharge-air
            dewpoint setpoint for the Discharge-Air Controller.""",
            name='nciDADewPointSP',
            profile=self,
            number=32,
            datatype=pylon.resources.properties.dischargeAirDewpointSetpoint.dischargeAirDewpointSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDAClSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum discharge air cooling setpoint.  Maximum
            discharge-air cooling setpoint for the Discharge-Air
            Controller.""",
            name='nciMaxDAClSP',
            profile=self,
            number=33,
            datatype=pylon.resources.properties.maxDischargeAirCoolingSetpoint.maxDischargeAirCoolingSetpoint,
            mandatory=False
        )
        self.properties['nciMinDAClSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum discharge air cooling setpoint.  Minimum
            discharge-air cooling setpoint for the Discharge-Air
            Controller.""",
            name='nciMinDAClSP',
            profile=self,
            number=34,
            datatype=pylon.resources.properties.minDischargeAirCoolingSetpoint.minDischargeAirCoolingSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDAHtSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum discharge air heating setpoint.  Maximum discharge
            heating setpoint for the Discharge-Air Controller.""",
            name='nciMaxDAHtSP',
            profile=self,
            number=35,
            datatype=pylon.resources.properties.maxDischargeAirHeatingSetpoint.maxDischargeAirHeatingSetpoint,
            mandatory=False
        )
        self.properties['nciMinDAHtSP'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum discharge air heating setpoint.  Minimum discharge
            heating setpoint for the Discharge-Air Controller.""",
            name='nciMinDAHtSP',
            profile=self,
            number=36,
            datatype=pylon.resources.properties.minDischargeAirHeatingSetpoint.minDischargeAirHeatingSetpoint,
            mandatory=False
        )
        self.properties['nciCoolLockout'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cooling lockout temperature setpoint.  Outdoor air
            temperature cooling lockout setpoint for the Discharge-Air
            Controller.""",
            name='nciCoolLockout',
            profile=self,
            number=37,
            datatype=pylon.resources.properties.coolingLockout.coolingLockout,
            mandatory=False
        )
        self.properties['nciHeatLockout'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating lockout temperature setpoint.  Outdoor air
            temperature heating lockout setpoint for the Discharge-Air
            Controller.""",
            name='nciHeatLockout',
            profile=self,
            number=38,
            datatype=pylon.resources.properties.heatingLockout.heatingLockout,
            mandatory=False
        )
        self.properties['nciCoolResetEn'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cooling reset enable.  Enables/disables the discharge-air
            temperature cooling reset control for the Discharge-Air
            Controller.""",
            name='nciCoolResetEn',
            profile=self,
            number=39,
            datatype=pylon.resources.properties.coolingResetEnable.coolingResetEnable,
            mandatory=False
        )
        self.properties['nciHeatResetEn'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating reset enable.  Enables/disables the discharge-air
            temperature heating reset control for the Discharge-Air
            Controller.""",
            name='nciHeatResetEn',
            profile=self,
            number=40,
            datatype=pylon.resources.properties.heatingResetEnable.heatingResetEnable,
            mandatory=False
        )
        self._original_name = 'SFPTdischargeAirController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = dischargeAirController()
    pass
