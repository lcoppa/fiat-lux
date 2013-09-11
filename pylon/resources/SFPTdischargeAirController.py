"""SFPTdischargeAirController standard profile, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_tod_event import SNVT_tod_event
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SNVT_press_p import SNVT_press_p
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_flow import SNVT_flow
from pylon.resources.SNVT_enthalpy import SNVT_enthalpy
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SCPTminRnge import SCPTminRnge
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTdischargeAirCoolingSetpoint import SCPTdischargeAirCoolingSetpoint
from pylon.resources.SCPTdischargeAirHeatingSetpoint import SCPTdischargeAirHeatingSetpoint
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTbypassTime import SCPTbypassTime
from pylon.resources.SCPTmaxSupplyFanCapacity import SCPTmaxSupplyFanCapacity
from pylon.resources.SCPTminSupplyFanCapacity import SCPTminSupplyFanCapacity
from pylon.resources.SCPTmaxReturnExhaustFanCapacity import SCPTmaxReturnExhaustFanCapacity
from pylon.resources.SCPTminReturnExhaustFanCapacity import SCPTminReturnExhaustFanCapacity
from pylon.resources.SCPTductStaticPressureSetpoint import SCPTductStaticPressureSetpoint
from pylon.resources.SCPTmaxDuctStaticPressureSetpoint import SCPTmaxDuctStaticPressureSetpoint
from pylon.resources.SCPTminDuctStaticPressureSetpoint import SCPTminDuctStaticPressureSetpoint
from pylon.resources.SCPTductStaticPressureLimit import SCPTductStaticPressureLimit
from pylon.resources.SCPTbuildingStaticPressureSetpoint import SCPTbuildingStaticPressureSetpoint
from pylon.resources.SCPTreturnFanStaticPressureSetpoint import SCPTreturnFanStaticPressureSetpoint
from pylon.resources.SCPTfanDifferentialSetpoint import SCPTfanDifferentialSetpoint
from pylon.resources.SCPTmixedAirLowLimitSetpoint import SCPTmixedAirLowLimitSetpoint
from pylon.resources.SCPTmixedAirTempSetpoint import SCPTmixedAirTempSetpoint
from pylon.resources.SCPTminOutdoorAirFlowSetpoint import SCPTminOutdoorAirFlowSetpoint
from pylon.resources.SCPTsensConstVAV import SCPTsensConstVAV
from pylon.resources.SCPTductArea import SCPTductArea
from pylon.resources.SCPToutdoorAirTempSetpoint import SCPToutdoorAirTempSetpoint
from pylon.resources.SCPToutdoorAirEnthalpySetpoint import SCPToutdoorAirEnthalpySetpoint
from pylon.resources.SCPTdiffTempSetpoint import SCPTdiffTempSetpoint
from pylon.resources.SCPTexhaustEnablePosition import SCPTexhaustEnablePosition
from pylon.resources.SCPTspaceHumSetpoint import SCPTspaceHumSetpoint
from pylon.resources.SCPThumSetpt import SCPThumSetpt
from pylon.resources.SCPTdischargeAirDewpointSetpoint import SCPTdischargeAirDewpointSetpoint
from pylon.resources.SCPTmaxDischargeAirCoolingSetpoint import SCPTmaxDischargeAirCoolingSetpoint
from pylon.resources.SCPTminDischargeAirCoolingSetpoint import SCPTminDischargeAirCoolingSetpoint
from pylon.resources.SCPTmaxDischargeAirHeatingSetpoint import SCPTmaxDischargeAirHeatingSetpoint
from pylon.resources.SCPTminDischargeAirHeatingSetpoint import SCPTminDischargeAirHeatingSetpoint
from pylon.resources.SCPTcoolingLockout import SCPTcoolingLockout
from pylon.resources.SCPTheatingLockout import SCPTheatingLockout
from pylon.resources.SCPTcoolingResetEnable import SCPTcoolingResetEnable
from pylon.resources.SCPTheatingResetEnable import SCPTheatingResetEnable


class SFPTdischargeAirController(base.Profile):
    """SFPTdischargeAirController standard profile.  Discharge-Air Controller
    (DAC) Used to control duct static pressure and discharge-air
    temperature."""

    def __init__(self):
        super().__init__(
            key=8610,
            scope=0
        )
        self.datapoints['nviOccSchedule'] = base.Profile.DatapointMember(
            doc="""Occupancy scheduler input.  Commands the Discharge-Air
            Controller into different occupancy modes typically sent by
            scheduler or supervisory node.""",
            name='nviOccSchedule',
            profile=self,
            number=1,
            datatype=SNVT_tod_event,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccManCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy override input.  Commands the Discharge-Air
            Controller into different occupancy modes.""",
            name='nviOccManCmd',
            profile=self,
            number=2,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application mode input.  Coordinates the Discharge-Air
            Controller with any supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=3,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergOverride'] = base.Profile.DatapointMember(
            doc="""Emergency override input.  Commands the device into
            different emergency modes.""",
            name='nviEmergOverride',
            profile=self,
            number=4,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctStatPress'] = base.Profile.DatapointMember(
            doc="""Duct static pressure input.  Connects a duct static
            pressure sensor or network output from another controller.""",
            name='nviDuctStatPress',
            profile=self,
            number=5,
            datatype=SNVT_press_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x04\xe2',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctStaticSP'] = base.Profile.DatapointMember(
            doc="""Duct static pressure setpoint input.  Sets duct static
            pressure setpoint of the controller via the network.""",
            name='nviDuctStaticSP',
            profile=self,
            number=6,
            datatype=SNVT_press_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x04\xe2',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDAClSP'] = base.Profile.DatapointMember(
            doc="""Discharge air cooling setpoint input.  Sets discharge-air
            cooling setpoint of the controller via the network.""",
            name='nviDAClSP',
            profile=self,
            number=7,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x0b\xb8',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDAHtSP'] = base.Profile.DatapointMember(
            doc="""Discharge-Air heating setpoint input.  Sets discharge-air
            heating setpoint of the controller via the network.""",
            name='nviDAHtSP',
            profile=self,
            number=8,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x1b\x58',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSupFanCap'] = base.Profile.DatapointMember(
            doc="""Supply fan capacity input.  Commands override of the
            supply fan capacity from another controller.""",
            name='nviSupFanCap',
            profile=self,
            number=9,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviExhFanCap'] = base.Profile.DatapointMember(
            doc="""Exhaust fan capacity input.  Connects network output from
            another controller to override the local exhaust fan capacity
            control.""",
            name='nviExhFanCap',
            profile=self,
            number=10,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRetFanCap'] = base.Profile.DatapointMember(
            doc="""Return fan capacity input.  Commands an override of return
            fan capacity from another controller.""",
            name='nviRetFanCap',
            profile=self,
            number=11,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFanDiffSP'] = base.Profile.DatapointMember(
            doc="""Fan differential setpoint input.  Setpoint for the percent
            capacity difference between the supply and return fans.""",
            name='nviFanDiffSP',
            profile=self,
            number=12,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x27\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBldgStatPress'] = base.Profile.DatapointMember(
            doc="""Building static pressure input.  Connects network building
            static pressure sensor or network output from another
            controller.""",
            name='nviBldgStatPress',
            profile=self,
            number=13,
            datatype=SNVT_press_p,
            mandatory=False,
            minimum=b'\xff\x83',
            maximum=b'\x00\x7d',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBldgStaticSP'] = base.Profile.DatapointMember(
            doc="""Building static pressure setpoint input.  Connects network
            output from another controller to provide the building static
            pressure setpoint.""",
            name='nviBldgStaticSP',
            profile=self,
            number=14,
            datatype=SNVT_press_p,
            mandatory=False,
            minimum=b'\xff\x9c',
            maximum=b'\x00\x64',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPriCoolEnable'] = base.Profile.DatapointMember(
            doc="""Primary cool enable input.  Connect network output from
            another controller to enable/disable the primary cooling output
            of the unit.""",
            name='nviPriCoolEnable',
            profile=self,
            number=15,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPriHeatEnable'] = base.Profile.DatapointMember(
            doc="""Primary heat enable input.  Connects network output from
            another controller to enable/disable the primary heating outputs
            of the unit.""",
            name='nviPriHeatEnable',
            profile=self,
            number=16,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEconEnable'] = base.Profile.DatapointMember(
            doc="""Economizer enable input.  Enables and disables economizer
            operation.""",
            name='nviEconEnable',
            profile=self,
            number=17,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOAMinPos'] = base.Profile.DatapointMember(
            doc="""Outdoor air minimum position input.  Sets minimum outdoor
            air damper position of controller via the network.""",
            name='nviOAMinPos',
            profile=self,
            number=18,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMinOAFlowSP'] = base.Profile.DatapointMember(
            doc="""Minimum outdoor airflow setpoint input.  Commands a
            minimum outdoor airflow rate setpoint from the network.""",
            name='nviMinOAFlowSP',
            profile=self,
            number=19,
            datatype=SNVT_flow,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\xc3\x50',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor air temperature input.  Measured outdoor air dry
            bulb temperature.""",
            name='nviOutdoorTemp',
            profile=self,
            number=20,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xf0\x60',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor air humidity input.  Measured outdoor air humidity
            in percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=21,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOAEnthalpy'] = base.Profile.DatapointMember(
            doc="""Outdoor air enthalpy input.  Connects a network outdoor
            air enthalpy sensor or network controller output.""",
            name='nviOAEnthalpy',
            profile=self,
            number=22,
            datatype=SNVT_enthalpy,
            mandatory=False,
            minimum=b'\x07\xd0',
            maximum=b'\x27\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMATSP'] = base.Profile.DatapointMember(
            doc="""Mixed air temperature setpoint input.  Commands a mixed
            air temperature setpoint from the network.""",
            name='nviMATSP',
            profile=self,
            number=23,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRATemp'] = base.Profile.DatapointMember(
            doc="""Return air temperature input.  Connects a network return
            air temperature sensor or network output from another
            controller.""",
            name='nviRATemp',
            profile=self,
            number=24,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceEnthalpy'] = base.Profile.DatapointMember(
            doc="""Space enthalpy input.  Connects a network return air or
            space enthalpy sensor or network output from another
            controller.""",
            name='nviSpaceEnthalpy',
            profile=self,
            number=25,
            datatype=SNVT_enthalpy,
            mandatory=False,
            minimum=b'\x07\xd0',
            maximum=b'\x27\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space temperature input.  Connects a network space
            temperature sensor or network output from another controller.""",
            name='nviSpaceTemp',
            profile=self,
            number=26,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space humidity input.  Connects a network return air or
            space relative humidity sensor or network output from another
            controller.""",
            name='nviSpaceRH',
            profile=self,
            number=27,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHumEnable'] = base.Profile.DatapointMember(
            doc="""Humidification enable input.  Enables humidification
            function in the controller.""",
            name='nviHumEnable',
            profile=self,
            number=28,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceHumSP'] = base.Profile.DatapointMember(
            doc="""Space humidification setpoint input.  Connects a network
            space humidity setpoint or network output from another
            controller.""",
            name='nviSpaceHumSP',
            profile=self,
            number=29,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDehumEnable'] = base.Profile.DatapointMember(
            doc="""Dehumidification enable input.  Enables dehumidification
            function in the controller.""",
            name='nviDehumEnable',
            profile=self,
            number=30,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceDehumSP'] = base.Profile.DatapointMember(
            doc="""Space dehumidification setpoint input.  Connects a network
            space dehumidification setpoint or network output from another
            controller.""",
            name='nviSpaceDehumSP',
            profile=self,
            number=31,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDADewPointSP'] = base.Profile.DatapointMember(
            doc="""Discharge air dewpoint setpoint input.  Commands a
            discharge-air dewpoint setpoint from the network.""",
            name='nviDADewPointSP',
            profile=self,
            number=32,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xf8\x30',
            maximum=b'\x0b\xb8',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCWTemp'] = base.Profile.DatapointMember(
            doc="""Condenser water temperature input.  Connects a network
            condenser water temperature sensor or network output from another
            controller.""",
            name='nviCWTemp',
            profile=self,
            number=33,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCWFlow'] = base.Profile.DatapointMember(
            doc="""Condenser water flow input.  System condenser flow
            status.""",
            name='nviCWFlow',
            profile=self,
            number=34,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDischAirTemp'] = base.Profile.DatapointMember(
            doc="""Discharge air temperature output.  Monitors discharge-air
            temperature measured by a hardwired sensor.""",
            name='nvoDischAirTemp',
            profile=self,
            number=35,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit status output.  Reports the Discharge-Air Controller
            status.""",
            name='nvoUnitStatus',
            profile=self,
            number=36,
            datatype=SNVT_hvac_status,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDATempSP'] = base.Profile.DatapointMember(
            doc="""Effective discharge-air temperature setpoint output.
            Monitors the effective discharge-air temperature setpoint the
            Discharge-Air Controller is using for control.""",
            name='nvoEffDATempSP',
            profile=self,
            number=37,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDuctStatPress'] = base.Profile.DatapointMember(
            doc="""Duct static pressure output.  Monitors the effective duct
            static pressure the controller is using for control.""",
            name='nvoDuctStatPress',
            profile=self,
            number=38,
            datatype=SNVT_press_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDuctStatSP'] = base.Profile.DatapointMember(
            doc="""Effective duct static pressure setpoint output.  Monitors
            the effective duct static pressure setpoint the Discharge-Air
            Controller is using for control.""",
            name='nvoEffDuctStatSP',
            profile=self,
            number=39,
            datatype=SNVT_press_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatCool'] = base.Profile.DatapointMember(
            doc="""Effective heat/cool output.  Actual heat/cool mode of the
            unit.""",
            name='nvoHeatCool',
            profile=self,
            number=40,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoApplicMode'] = base.Profile.DatapointMember(
            doc="""Application mode output.  Used to control the mode of
            other controllers such as a VAV box controller.""",
            name='nvoApplicMode',
            profile=self,
            number=41,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectOccup'] = base.Profile.DatapointMember(
            doc="""Effective occupancy output.  Transmits the current
            occupancy mode of the Discharge-Air Controller for
            monitoring.""",
            name='nvoEffectOccup',
            profile=self,
            number=42,
            datatype=SNVT_occupancy,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanStatus'] = base.Profile.DatapointMember(
            doc="""Supply fan status output.  Actual status of the supply fan
            for monitoring.""",
            name='nvoSupFanStatus',
            profile=self,
            number=43,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanOnOff'] = base.Profile.DatapointMember(
            doc="""Supply fan on/off control output.  Used to start and stop
            the supply fan.""",
            name='nvoSupFanOnOff',
            profile=self,
            number=44,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSupFanCap'] = base.Profile.DatapointMember(
            doc="""Supply fan capacity output.  Used to command the supply
            fan speed or capacity.""",
            name='nvoSupFanCap',
            profile=self,
            number=45,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanStatus'] = base.Profile.DatapointMember(
            doc="""Exhaust fan status output.  Actual status of the exhaust
            fan for monitoring.""",
            name='nvoExhFanStatus',
            profile=self,
            number=46,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanOnOff'] = base.Profile.DatapointMember(
            doc="""Exhaust fan on/off control output.  Used to start and stop
            the exhaust fan.""",
            name='nvoExhFanOnOff',
            profile=self,
            number=47,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhFanCap'] = base.Profile.DatapointMember(
            doc="""Exhaust fan capacity output.  Used to command the exhaust
            fan speed or capacity.""",
            name='nvoExhFanCap',
            profile=self,
            number=48,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoExhDamper'] = base.Profile.DatapointMember(
            doc="""Exhaust damper control output.  Present status of Exhaust
            Damper output for monitoring or control.""",
            name='nvoExhDamper',
            profile=self,
            number=49,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanStatus'] = base.Profile.DatapointMember(
            doc="""Return fan status output.  Actual status of the return fan
            for monitoring.""",
            name='nvoRetFanStatus',
            profile=self,
            number=50,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanOnOff'] = base.Profile.DatapointMember(
            doc="""Return fan on/off control output.  Used to start and stop
            the return fan.""",
            name='nvoRetFanOnOff',
            profile=self,
            number=51,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanCap'] = base.Profile.DatapointMember(
            doc="""Return fan capacity output.  Used to command the return
            fan speed or capacity.""",
            name='nvoRetFanCap',
            profile=self,
            number=52,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRetFanPress'] = base.Profile.DatapointMember(
            doc="""Return fan pressure output.  Present value of return fan
            static pressure for monitoring.""",
            name='nvoRetFanPress',
            profile=self,
            number=53,
            datatype=SNVT_press_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoBldgStatPress'] = base.Profile.DatapointMember(
            doc="""Building static pressure output.  Present value of the
            building static pressure for monitoring.""",
            name='nvoBldgStatPress',
            profile=self,
            number=54,
            datatype=SNVT_press_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEconEnabled'] = base.Profile.DatapointMember(
            doc="""Economizer enabled output.  Present enable/disable status
            of economizer for monitoring.""",
            name='nvoEconEnabled',
            profile=self,
            number=55,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOADamper'] = base.Profile.DatapointMember(
            doc="""Outdoor air damper output.  Present level of the outdoor
            air damper or injection fan capacity output for monitoring or
            control.""",
            name='nvoOADamper',
            profile=self,
            number=56,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciOAMinPos':
                base.Profile.PropertyMember(
                    doc="""Outdoor air damper minimum position.  Default
                    minimum outdoor air damper position setpoint for the
                    Discharge-Air Controller.""",
                    name='nciOAMinPos',
                    profile=self,
                    number=22,
                    datatype=SCPTminRnge,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOAFlow'] = base.Profile.DatapointMember(
            doc="""Outdoor airflow output.  Present value of the outdoor
            airflow for monitoring.""",
            name='nvoOAFlow',
            profile=self,
            number=57,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalOATemp'] = base.Profile.DatapointMember(
            doc="""Local outdoor air temperature output.  Indicates value of
            a hardwired outdoor air temperature sensor.""",
            name='nvoLocalOATemp',
            profile=self,
            number=58,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor air temperature output.  Present value of outdoor
            air temperature for monitoring.""",
            name='nvoOutdoorTemp',
            profile=self,
            number=59,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalOARH'] = base.Profile.DatapointMember(
            doc="""Local outdoor air humidity output.  Indicates value of
            hardwired outdoor air relative humidity sensor.""",
            name='nvoLocalOARH',
            profile=self,
            number=60,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor air humidity output.  Present value of outdoor air
            humidity for monitoring.""",
            name='nvoOutdoorRH',
            profile=self,
            number=61,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOAEnthalpy'] = base.Profile.DatapointMember(
            doc="""Outdoor air enthalpy output.  Present value of the outdoor
            air enthalpy.""",
            name='nvoOAEnthalpy',
            profile=self,
            number=62,
            datatype=SNVT_enthalpy,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCoolPrimary'] = base.Profile.DatapointMember(
            doc="""Primary Cooling Output.  Present level of the primary
            cooling capacity.""",
            name='nvoCoolPrimary',
            profile=self,
            number=63,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatPrimary'] = base.Profile.DatapointMember(
            doc="""Primary heating output.  Present value of the primary
            heating capacity.""",
            name='nvoHeatPrimary',
            profile=self,
            number=64,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMATemp'] = base.Profile.DatapointMember(
            doc="""Mixed air temperature output.  Present value of the mixed
            air dry bulb temperature.""",
            name='nvoMATemp',
            profile=self,
            number=65,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space temperature output.  Present value of the space
            temperature for monitoring.""",
            name='nvoSpaceTemp',
            profile=self,
            number=66,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRATemp'] = base.Profile.DatapointMember(
            doc="""Return air temperature output.  Present value of return
            air temperature for monitoring.""",
            name='nvoRATemp',
            profile=self,
            number=67,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space humidity output.  Present value of the space
            relative humidity for monitoring.""",
            name='nvoSpaceRH',
            profile=self,
            number=68,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceEnthalpy'] = base.Profile.DatapointMember(
            doc="""Space enthalpy output.  Present value of the space
            enthalpy.""",
            name='nvoSpaceEnthalpy',
            profile=self,
            number=69,
            datatype=SNVT_enthalpy,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffSpaceHumSP'] = base.Profile.DatapointMember(
            doc="""Effective space humidification setpoint output.  Effective
            space low limit humidity setpoint for monitoring.""",
            name='nvoEffSpaceHumSP',
            profile=self,
            number=70,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHumidifier'] = base.Profile.DatapointMember(
            doc="""Humidification status output.  Present level of the
            humidifier output for monitoring.""",
            name='nvoHumidifier',
            profile=self,
            number=71,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffSpaceDHSP'] = base.Profile.DatapointMember(
            doc="""Effective space dehumidification setpoint output.
            Effective space high limit humidity setpoint for monitoring.""",
            name='nvoEffSpaceDHSP',
            profile=self,
            number=72,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDehumidifier'] = base.Profile.DatapointMember(
            doc="""Dehumidification status output.  Present status of
            dehumidification control for monitoring.""",
            name='nvoDehumidifier',
            profile=self,
            number=73,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffDADewPtSP'] = base.Profile.DatapointMember(
            doc="""Effective discharge-air dewpoint setpoint output.
            Monitors the effective discharge-air dewpoint setpoint that the
            discharge-air controller is using for control.""",
            name='nvoEffDADewPtSP',
            profile=self,
            number=74,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDADewPoint'] = base.Profile.DatapointMember(
            doc="""Discharge air dewpoint temperature output.  Present value
            of the discharge-air dewpoint temperature.""",
            name='nvoDADewPoint',
            profile=self,
            number=75,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCondCap'] = base.Profile.DatapointMember(
            doc="""Condenser capacity output.  Present value of the condenser
            capacity control output for monitoring.""",
            name='nvoCondCap',
            profile=self,
            number=76,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalCWTemp'] = base.Profile.DatapointMember(
            doc="""Local condenser water temperature output.  Transmits value
            of hardwired condenser water temperature sensor.""",
            name='nvoLocalCWTemp',
            profile=self,
            number=77,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWTemp'] = base.Profile.DatapointMember(
            doc="""Condenser water temperature output.  Present value of
            condenser water temperature for monitoring.""",
            name='nvoCWTemp',
            profile=self,
            number=78,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWFlow'] = base.Profile.DatapointMember(
            doc="""Condenser water flow output.  Transmits current status of
            condenser water flow sensor for monitoring.""",
            name='nvoCWFlow',
            profile=self,
            number=79,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCWPump'] = base.Profile.DatapointMember(
            doc="""Condenser water pump output.  Transmits the current state
            of condenser water pump output for monitoring or control.""",
            name='nvoCWPump',
            profile=self,
            number=80,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before specified NV outputs will be automatically updated.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            mandatory=True
        )
        self.properties['nciDAClSP'] = base.Profile.PropertyMember(
            doc="""Discharge air cooling setpoint.  Default discharge-air
            cooling setpoint for the Discharge-Air Controller.""",
            name='nciDAClSP',
            profile=self,
            number=2,
            datatype=SCPTdischargeAirCoolingSetpoint,
            mandatory=True
        )
        self.properties['nciDAHtSP'] = base.Profile.PropertyMember(
            doc="""Discharge air heating setpoint.  Default discharge-air
            heating setpoint for the Discharge-Air Controller.""",
            name='nciDAHtSP',
            profile=self,
            number=3,
            datatype=SCPTdischargeAirHeatingSetpoint,
            mandatory=True
        )
        self.properties['nciSetpoints'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  Space temperature
            setpoints for various heat, cool and occupancy modes.""",
            name='nciSetpoints',
            profile=self,
            number=4,
            datatype=SCPTsetPnts,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum time between automatic NV
            output transmissions.""",
            name='nciMinOutTm',
            profile=self,
            number=5,
            datatype=SCPTminSendTime,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Receive heartbeat.  Controls maximum time after last
            update before default values are used.""",
            name='nciRcvHrtBt',
            profile=self,
            number=6,
            datatype=SCPTmaxRcvTime,
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=7,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciBypassTime'] = base.Profile.PropertyMember(
            doc="""Local bypass time.  Maximum time the controller can be in
            bypass mode following request.""",
            name='nciBypassTime',
            profile=self,
            number=8,
            datatype=SCPTbypassTime,
            mandatory=False
        )
        self.properties['nciMaxSupFanCap'] = base.Profile.PropertyMember(
            doc="""Maximum supply fan capacity.  Maximum supply fan capacity
            setpoint for the Discharge-Air Controller.""",
            name='nciMaxSupFanCap',
            profile=self,
            number=9,
            datatype=SCPTmaxSupplyFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMinSupFanCap'] = base.Profile.PropertyMember(
            doc="""Minimum supply fan capacity.  Minimum supply fan capacity
            setpoint for the Discharge-Air Controller.""",
            name='nciMinSupFanCap',
            profile=self,
            number=10,
            datatype=SCPTminSupplyFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMaxREFanCap'] = base.Profile.PropertyMember(
            doc="""Maximum return/exhaust fan capacity.  Maximum
            return/exhaust fan capacity setpoint for the Discharge-Air
            Controller.""",
            name='nciMaxREFanCap',
            profile=self,
            number=11,
            datatype=SCPTmaxReturnExhaustFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciMinREFanCap'] = base.Profile.PropertyMember(
            doc="""Minimum return/exhaust fan capacity.  Minimum
            return/exhaust fan capacity setpoint for the Discharge-Air
            Controller.""",
            name='nciMinREFanCap',
            profile=self,
            number=12,
            datatype=SCPTminReturnExhaustFanCapacity,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDuctStatSP'] = base.Profile.PropertyMember(
            doc="""Duct static pressure setpoint.  Default duct static
            pressure setpoint for the Discharge-Air Controller.""",
            name='nciDuctStatSP',
            profile=self,
            number=13,
            datatype=SCPTductStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDuctStatSP'] = base.Profile.PropertyMember(
            doc="""Maximum duct static pressure setpoint.  Maximum duct
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciMaxDuctStatSP',
            profile=self,
            number=14,
            datatype=SCPTmaxDuctStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciMinDuctStatSP'] = base.Profile.PropertyMember(
            doc="""Minimum duct static pressure setpoint.  Minimum duct
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciMinDuctStatSP',
            profile=self,
            number=15,
            datatype=SCPTminDuctStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciDuctStatLim'] = base.Profile.PropertyMember(
            doc="""Duct static pressure limit.  Duct static pressure limit,
            used for equipment protection.""",
            name='nciDuctStatLim',
            profile=self,
            number=16,
            datatype=SCPTductStaticPressureLimit,
            mandatory=False
        )
        self.properties['nciBldgStaticSP'] = base.Profile.PropertyMember(
            doc="""Building static pressure setpoint.  Default building
            static pressure setpoint for the Discharge-Air Controller.""",
            name='nciBldgStaticSP',
            profile=self,
            number=17,
            datatype=SCPTbuildingStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciRetFanPressSP'] = base.Profile.PropertyMember(
            doc="""Return fan pressure setpoint.  Return fan static pressure
            setpoint for the Discharge-Air Controller.""",
            name='nciRetFanPressSP',
            profile=self,
            number=18,
            datatype=SCPTreturnFanStaticPressureSetpoint,
            mandatory=False
        )
        self.properties['nciFanDiffSP'] = base.Profile.PropertyMember(
            doc="""Fan differential setpoint.  Default for percent capacity
            difference between supply and return fans.""",
            name='nciFanDiffSP',
            profile=self,
            number=19,
            datatype=SCPTfanDifferentialSetpoint,
            mandatory=False
        )
        self.properties['nciMALowLimitSP'] = base.Profile.PropertyMember(
            doc="""Mixed air low limit setpoint.  Mixed air low limit
            setpoint for the Discharge-Air Controller.""",
            name='nciMALowLimitSP',
            profile=self,
            number=20,
            datatype=SCPTmixedAirLowLimitSetpoint,
            mandatory=False
        )
        self.properties['nciMATSP'] = base.Profile.PropertyMember(
            doc="""Mixed air temperature setpoint.  Default mixed air
            temperature setpoint for the Discharge-Air Controller.""",
            name='nciMATSP',
            profile=self,
            number=21,
            datatype=SCPTmixedAirTempSetpoint,
            mandatory=False
        )
        self.properties['nciMinOAFlowSP'] = base.Profile.PropertyMember(
            doc="""Minimum outdoor airflow setpoint.  Default minimum outdoor
            airflow setpoint for the Discharge-Air Controller.""",
            name='nciMinOAFlowSP',
            profile=self,
            number=23,
            datatype=SCPTminOutdoorAirFlowSetpoint,
            mandatory=False
        )
        self.properties['nciOAFlowCalib'] = base.Profile.PropertyMember(
            doc="""Outdoor airflow calibration.  Gain for the outdoor airflow
            calibration for the Discharge-Air Controller.""",
            name='nciOAFlowCalib',
            profile=self,
            number=24,
            datatype=SCPTsensConstVAV,
            mandatory=False
        )
        self.properties['nciOAInletArea'] = base.Profile.PropertyMember(
            doc="""Outdoor air inlet area.  Area of the outdoor air inlet for
            the Discharge-Air Controller.""",
            name='nciOAInletArea',
            profile=self,
            number=25,
            datatype=SCPTductArea,
            mandatory=False
        )
        self.properties['nciOATSP'] = base.Profile.PropertyMember(
            doc="""Outdoor air temperature setpoint.  Airside economizer
            outdoor air temperature enable setpoint for the Discharge-Air
            Controller.""",
            name='nciOATSP',
            profile=self,
            number=26,
            datatype=SCPToutdoorAirTempSetpoint,
            mandatory=False
        )
        self.properties['nciOAEnthSP'] = base.Profile.PropertyMember(
            doc="""Outdoor air enthalpy setpoint.  Default airside economizer
            outdoor air enthalpy enable setpoint for the Discharge-Air
            Controller.""",
            name='nciOAEnthSP',
            profile=self,
            number=27,
            datatype=SCPToutdoorAirEnthalpySetpoint,
            mandatory=False
        )
        self.properties['nciTempDiff'] = base.Profile.PropertyMember(
            doc="""Economizer enable differential temperature setpoint.
            Differential between entering air temp and entering condenser
            water temp to enable economizer operation.""",
            name='nciTempDiff',
            profile=self,
            number=28,
            datatype=SCPTdiffTempSetpoint,
            mandatory=False
        )
        self.properties['nciExhStartPos'] = base.Profile.PropertyMember(
            doc="""Exhaust enable position.  Exhaust enable outdoor air
            damper position setpoint for the Discharge-Air Controller.""",
            name='nciExhStartPos',
            profile=self,
            number=29,
            datatype=SCPTexhaustEnablePosition,
            mandatory=False
        )
        self.properties['nciSpaceHumSP'] = base.Profile.PropertyMember(
            doc="""Space humidification setpoint.  Default space
            humidification setpoint for the Discharge-Air Controller.""",
            name='nciSpaceHumSP',
            profile=self,
            number=30,
            datatype=SCPTspaceHumSetpoint,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciSpaceDehumSP'] = base.Profile.PropertyMember(
            doc="""Space dehumidification setpoint.  Default space
            dehumidification setpoint for the Discharge-Air Controller.""",
            name='nciSpaceDehumSP',
            profile=self,
            number=31,
            datatype=SCPThumSetpt,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDADewPointSP'] = base.Profile.PropertyMember(
            doc="""Discharge air dewpoint setpoint.  Default discharge-air
            dewpoint setpoint for the Discharge-Air Controller.""",
            name='nciDADewPointSP',
            profile=self,
            number=32,
            datatype=SCPTdischargeAirDewpointSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDAClSP'] = base.Profile.PropertyMember(
            doc="""Maximum discharge air cooling setpoint.  Maximum
            discharge-air cooling setpoint for the Discharge-Air
            Controller.""",
            name='nciMaxDAClSP',
            profile=self,
            number=33,
            datatype=SCPTmaxDischargeAirCoolingSetpoint,
            mandatory=False
        )
        self.properties['nciMinDAClSP'] = base.Profile.PropertyMember(
            doc="""Minimum discharge air cooling setpoint.  Minimum
            discharge-air cooling setpoint for the Discharge-Air
            Controller.""",
            name='nciMinDAClSP',
            profile=self,
            number=34,
            datatype=SCPTminDischargeAirCoolingSetpoint,
            mandatory=False
        )
        self.properties['nciMaxDAHtSP'] = base.Profile.PropertyMember(
            doc="""Maximum discharge air heating setpoint.  Maximum discharge
            heating setpoint for the Discharge-Air Controller.""",
            name='nciMaxDAHtSP',
            profile=self,
            number=35,
            datatype=SCPTmaxDischargeAirHeatingSetpoint,
            mandatory=False
        )
        self.properties['nciMinDAHtSP'] = base.Profile.PropertyMember(
            doc="""Minimum discharge air heating setpoint.  Minimum discharge
            heating setpoint for the Discharge-Air Controller.""",
            name='nciMinDAHtSP',
            profile=self,
            number=36,
            datatype=SCPTminDischargeAirHeatingSetpoint,
            mandatory=False
        )
        self.properties['nciCoolLockout'] = base.Profile.PropertyMember(
            doc="""Cooling lockout temperature setpoint.  Outdoor air
            temperature cooling lockout setpoint for the Discharge-Air
            Controller.""",
            name='nciCoolLockout',
            profile=self,
            number=37,
            datatype=SCPTcoolingLockout,
            mandatory=False
        )
        self.properties['nciHeatLockout'] = base.Profile.PropertyMember(
            doc="""Heating lockout temperature setpoint.  Outdoor air
            temperature heating lockout setpoint for the Discharge-Air
            Controller.""",
            name='nciHeatLockout',
            profile=self,
            number=38,
            datatype=SCPTheatingLockout,
            mandatory=False
        )
        self.properties['nciCoolResetEn'] = base.Profile.PropertyMember(
            doc="""Cooling reset enable.  Enables/disables the discharge-air
            temperature cooling reset control for the Discharge-Air
            Controller.""",
            name='nciCoolResetEn',
            profile=self,
            number=39,
            datatype=SCPTcoolingResetEnable,
            mandatory=False
        )
        self.properties['nciHeatResetEn'] = base.Profile.PropertyMember(
            doc="""Heating reset enable.  Enables/disables the discharge-air
            temperature heating reset control for the Discharge-Air
            Controller.""",
            name='nciHeatResetEn',
            profile=self,
            number=40,
            datatype=SCPTheatingResetEnable,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTdischargeAirController()
    pass
