"""SFPTsccVAV standard profile, originally defined in resource file set
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_temp_setpt import SNVT_temp_setpt
from pylon.resources.SNVT_tod_event import SNVT_tod_event
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SCPTbypassTime import SCPTbypassTime
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_hvac_overid import SNVT_hvac_overid
from pylon.resources.SCPTmanOvrTime import SCPTmanOvrTime
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPThumSetpt import SCPThumSetpt
from pylon.resources.SNVT_ppm import SNVT_ppm
from pylon.resources.SCPTlimitCO2 import SCPTlimitCO2
from pylon.resources.SNVT_flow import SNVT_flow
from pylon.resources.SCPTminFlow import SCPTminFlow
from pylon.resources.SCPTmaxFlow import SCPTmaxFlow
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SNVT_power_kilo import SNVT_power_kilo
from pylon.resources.SCPTminRnge import SCPTminRnge
from pylon.resources.SCPTnomAirFlow import SCPTnomAirFlow
from pylon.resources.SNVT_hvac_satsts import SNVT_hvac_satsts
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTnumValves import SCPTnumValves
from pylon.resources.SCPTductArea import SCPTductArea
from pylon.resources.SCPTsensConstVAV import SCPTsensConstVAV
from pylon.resources.SCPTminFlowHeat import SCPTminFlowHeat
from pylon.resources.SCPTmaxFlowHeat import SCPTmaxFlowHeat
from pylon.resources.SCPTminFlowStby import SCPTminFlowStby
from pylon.resources.SCPThvacType import SCPThvacType
from pylon.resources.SCPTfanOperation import SCPTfanOperation
from pylon.resources.SCPTminFlowUnit import SCPTminFlowUnit
from pylon.resources.SCPTmaxFlowUnit import SCPTmaxFlowUnit
from pylon.resources.SCPTminFlowHeatStby import SCPTminFlowHeatStby
from pylon.resources.SCPTminFlowUnitStby import SCPTminFlowUnitStby
from pylon.resources.SCPToffsetFlow import SCPToffsetFlow
from pylon.resources.SCPTareaDuctHeat import SCPTareaDuctHeat
from pylon.resources.SCPTnomAirFlowHeat import SCPTnomAirFlowHeat
from pylon.resources.SCPTgainVAVHeat import SCPTgainVAVHeat
from pylon.resources.SCPTnumDampers import SCPTnumDampers
from pylon.resources.SCPTminFlowUnitHeat import SCPTminFlowUnitHeat
from pylon.resources.SCPTsaturationDelay import SCPTsaturationDelay


class SFPTsccVAV(base.Profile):
    """SFPTsccVAV standard profile.  Space Comfort Controller (SCC) -
    Variable Air Volume.  Type of HVAC unit controller that provides
    temperature control for a space within a building."""

    def __init__(self):
        super().__init__(
            key=8502,
            scope=0,
            principal='nvoUnitStatus'
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space temperature input.  Connects an external space
            temperature sensor to the node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetpoint'] = base.Profile.DatapointMember(
            doc="""Temperature setpoint input (absolute) Allows the
            temperature setpoints for the occupied and standby modes to be
            changed via the network.""",
            name='nviSetpoint',
            profile=self,
            number=2,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetptOffset'] = base.Profile.DatapointMember(
            doc="""Setpoint offset input.  Shifts the effective occupied and
            standby temperature setpoints by adding this NV's value to the
            present setpoints.""",
            name='nviSetptOffset',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x03\xe8',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetptShift'] = base.Profile.DatapointMember(
            doc="""Setpoint shift input.  Shifts the effective heat/cool
            setpoints by adding the corresponding value in this NV to the
            present setpoints.""",
            name='nviSetptShift',
            profile=self,
            number=4,
            datatype=SNVT_temp_setpt,
            mandatory=False,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccSchedule'] = base.Profile.DatapointMember(
            doc="""Occupancy scheduler input.  Commands the SCC into
            different occupancy modes.""",
            name='nviOccSchedule',
            profile=self,
            number=5,
            datatype=SNVT_tod_event,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccManCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy override input.  Commands the SCC into different
            occupancy modes.""",
            name='nviOccManCmd',
            profile=self,
            number=6,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciBypassTime':
                base.Profile.PropertyMember(
                    doc="""Local bypass time.  Maximum amount of time that
                    the SCC can be in the bypass (occupancy) mode following a
                    single bypass request.""",
                    name='nciBypassTime',
                    profile=self,
                    number=6,
                    datatype=SCPTbypassTime,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccSensor'] = base.Profile.DatapointMember(
            doc="""Occupancy sensor input.  Indicates the presence of
            occupants in the controlled space.""",
            name='nviOccSensor',
            profile=self,
            number=7,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application mode input.  Used to coordinate the SCC with
            any supervisory controller.""",
            name='nviApplicMode',
            profile=self,
            number=8,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHeatCool'] = base.Profile.DatapointMember(
            doc="""Heat/cool mode input.  Used to coordinate the SCC with any
            node that may need to control the heat/cool changeover of the
            unit.""",
            name='nviHeatCool',
            profile=self,
            number=9,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFanSpeedCmd'] = base.Profile.DatapointMember(
            doc="""Fan speed command input.  Enables connection of an
            external fan speed switch, or allows a supervisory device to
            override the fan speed.""",
            name='nviFanSpeedCmd',
            profile=self,
            number=10,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviComprEnable'] = base.Profile.DatapointMember(
            doc="""Compressor enable input.  This input is used to disable
            compressor operation.""",
            name='nviComprEnable',
            profile=self,
            number=11,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviAuxHeatEnable'] = base.Profile.DatapointMember(
            doc="""Auxiliary heat enable input.  This input is used to
            disable auxiliary heat operation.""",
            name='nviAuxHeatEnable',
            profile=self,
            number=12,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEconEnable'] = base.Profile.DatapointMember(
            doc="""Economizer enable input.  This input is used to enable and
            disable economizer operation.""",
            name='nviEconEnable',
            profile=self,
            number=13,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy hold-off input.  This input is used to stop heating
            and cooling while allowing the unit to protect the space from
            temperature extremes.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=14,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviValveOverride'] = base.Profile.DatapointMember(
            doc="""Water valve override input.  Commands the controller into
            a manual mode for overriding water valves.""",
            name='nviValveOverride',
            profile=self,
            number=15,
            datatype=SNVT_hvac_overid,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciManualTime':
                base.Profile.PropertyMember(
                    doc="""Manual override time.  Maximum time that the SCC
                    will stay in a manual mode that was requested by a NV
                    input, without receiving an update on that NV.""",
                    name='nciManualTime',
                    profile=self,
                    number=7,
                    datatype=SCPTmanOvrTime,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFlowOverride'] = base.Profile.DatapointMember(
            doc="""Airflow override input.  Commands the controller into a
            manual mode for overriding airflow control.""",
            name='nviFlowOverride',
            profile=self,
            number=16,
            datatype=SNVT_hvac_overid,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergOverride'] = base.Profile.DatapointMember(
            doc="""Emergency override input.  Commands the device into
            different emergency modes.""",
            name='nviEmergOverride',
            profile=self,
            number=17,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSourceTemp'] = base.Profile.DatapointMember(
            doc="""Source temperature input.  Indicates the temperature of
            the air or water being supplied to the unit for heating and/or
            cooling capacity.""",
            name='nviSourceTemp',
            profile=self,
            number=18,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x27\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor air temperature input.  Represents information
            from an outdoor air temperature sensor.""",
            name='nviOutdoorTemp',
            profile=self,
            number=19,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xf0\x60',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space humidity input.  Measured space humidity in
            percent.""",
            name='nviSpaceRH',
            profile=self,
            number=20,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciSpaceRHSetpt':
                base.Profile.PropertyMember(
                    doc="""Space humidity setpoint.  High-limit humidity
                    setpoint for the controlled space.""",
                    name='nciSpaceRHSetpt',
                    profile=self,
                    number=10,
                    datatype=SCPThumSetpt,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor air humidity input.  Measured outdoor humidity in
            percent.""",
            name='nviOutdoorRH',
            profile=self,
            number=21,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSpaceIAQ'] = base.Profile.DatapointMember(
            doc="""Space indoor air quality input.  Measured space CO2 or VOC
            levels in PPM.""",
            name='nviSpaceIAQ',
            profile=self,
            number=22,
            datatype=SNVT_ppm,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciSpaceCO2Lim':
                base.Profile.PropertyMember(
                    doc="""Space CO2 limit.  Maximum limit to allowable
                    carbon dioxide within a defined area.""",
                    name='nciSpaceCO2Lim',
                    profile=self,
                    number=9,
                    datatype=SCPTlimitCO2,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceDewPt'] = base.Profile.DatapointMember(
            doc="""Space dewpoint temperature input.  Measured space dewpoint
            temperature.""",
            name='nviSpaceDewPt',
            profile=self,
            number=23,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorDewPt'] = base.Profile.DatapointMember(
            doc="""Outdoor air dewpoint temperature input.  Measured outdoor
            dewpoint temperature.""",
            name='nviOutdoorDewPt',
            profile=self,
            number=24,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xf0\x60',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviAirflow'] = base.Profile.DatapointMember(
            doc="""Airflow input.  The measured supply airflow value is
            typically provided by a flow sensor on the network.""",
            name='nviAirflow',
            profile=self,
            number=25,
            datatype=SNVT_flow,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMinFlow':
                base.Profile.PropertyMember(
                    doc="""Minimum airflow.  Minimum airflow setpoint of a
                    VAV terminal.""",
                    name='nciMinFlow',
                    profile=self,
                    number=15,
                    datatype=SCPTminFlow,
                    mandatory=False
                ),
                'nciMaxFlow':
                base.Profile.PropertyMember(
                    doc="""Maximum airflow.  Maximum airflow setpoint of a
                    VAV terminal.""",
                    name='nciMaxFlow',
                    profile=self,
                    number=16,
                    datatype=SCPTmaxFlow,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Effective space temperature output.  Used to monitor the
            effective space temperature that the SCC is using for
            control.""",
            name='nvoSpaceTemp',
            profile=self,
            number=26,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit status output.  Reports the SCC status.""",
            name='nvoUnitStatus',
            profile=self,
            number=27,
            datatype=SNVT_hvac_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectSetpt'] = base.Profile.DatapointMember(
            doc="""Effective setpoint output.  Monitors the effective
            temperature setpoint.""",
            name='nvoEffectSetpt',
            profile=self,
            number=28,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectOccup'] = base.Profile.DatapointMember(
            doc="""Effective occupancy output.  Actual occupancy mode of the
            unit.""",
            name='nvoEffectOccup',
            profile=self,
            number=29,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatCool'] = base.Profile.DatapointMember(
            doc="""Effective heat/cool output.  Actual heat/cool mode of the
            unit.""",
            name='nvoHeatCool',
            profile=self,
            number=30,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetpoint'] = base.Profile.DatapointMember(
            doc="""Local setpoint output.  Space temperature setpoint value
            if a setpoint device is hardwired.""",
            name='nvoSetpoint',
            profile=self,
            number=31,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetptShift'] = base.Profile.DatapointMember(
            doc="""Local setpoint shift output.  Locally determined shift of
            the effective heat/cool setpoints.""",
            name='nvoSetptShift',
            profile=self,
            number=32,
            datatype=SNVT_temp_setpt,
            mandatory=False,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8\x03\xe8',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFanSpeed'] = base.Profile.DatapointMember(
            doc="""Fan speed output.  Actual fan speed of a local multi-speed
            fan as well as the requested speed of a remote fan.""",
            name='nvoFanSpeed',
            profile=self,
            number=33,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDischAirTemp'] = base.Profile.DatapointMember(
            doc="""Discharge air temperature output.  Monitors the
            temperature of the air that leaves the SCC.""",
            name='nvoDischAirTemp',
            profile=self,
            number=34,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLoadAbs'] = base.Profile.DatapointMember(
            doc="""Absolute power consumption output.  Present power
            consumption of the unit.""",
            name='nvoLoadAbs',
            profile=self,
            number=35,
            datatype=SNVT_power,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLoadAbsK'] = base.Profile.DatapointMember(
            doc="""Absolute power consumption (kW) output.  Present power
            consumption of the unit.""",
            name='nvoLoadAbsK',
            profile=self,
            number=36,
            datatype=SNVT_power_kilo,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Terminal load output.  Present heat/cool energy demand of
            the unit.""",
            name='nvoTerminalLoad',
            profile=self,
            number=37,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatPrimary'] = base.Profile.DatapointMember(
            doc="""Primary heat output.  Present level of the primary heat
            output.""",
            name='nvoHeatPrimary',
            profile=self,
            number=38,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHeatSecondary'] = base.Profile.DatapointMember(
            doc="""Secondary heat output.  Present level of the secondary
            heat output.""",
            name='nvoHeatSecondary',
            profile=self,
            number=39,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCoolPrimary'] = base.Profile.DatapointMember(
            doc="""Primary cool output.  Present level of the primary
            mechanical cooling output.""",
            name='nvoCoolPrimary',
            profile=self,
            number=40,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCoolSecondary'] = base.Profile.DatapointMember(
            doc="""Secondary cool output.  Present level of the secondary
            mechanical cooling output.""",
            name='nvoCoolSecondary',
            profile=self,
            number=41,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOADamper'] = base.Profile.DatapointMember(
            doc="""Outdoor air damper output.  Present position of the
            outdoor air damper (if hardwired) or as a request to a remote
            outdoor air damper.""",
            name='nvoOADamper',
            profile=self,
            number=42,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciOAMinPos':
                base.Profile.PropertyMember(
                    doc="""Outdoor air damper minimum position.  Minimum
                    position for the outdoor air damper.""",
                    name='nciOAMinPos',
                    profile=self,
                    number=8,
                    datatype=SCPTminRnge,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space humidity output.  Space humidity in percent, if the
            SCC Device has a hardwired humidity sensor.""",
            name='nvoSpaceRH',
            profile=self,
            number=43,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor air humidity output.  Outdoor air humidity in
            percent, if the SCC Device has a hardwired humidity sensor.""",
            name='nvoOutdoorRH',
            profile=self,
            number=44,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor air temperature output.  Monitors the outdoor air
            temperature if the unit controller provides a hardwired
            temperature sensor.""",
            name='nvoOutdoorTemp',
            profile=self,
            number=45,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceCO2'] = base.Profile.DatapointMember(
            doc="""Space CO2 sensor output.  Space CO2 concentration in ppm,
            if the SCC Device has a hardwired CO2 sensor.""",
            name='nvoSpaceCO2',
            profile=self,
            number=46,
            datatype=SNVT_ppm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpaceDewPt'] = base.Profile.DatapointMember(
            doc="""Space dewpoint temperature output.  Space dewpoint
            temperature.""",
            name='nvoSpaceDewPt',
            profile=self,
            number=47,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHumidifier'] = base.Profile.DatapointMember(
            doc="""Humidifier output.  Present value of the humidifier (if
            hardwired) or can be used to control a remote humidifier or
            control valve.""",
            name='nvoHumidifier',
            profile=self,
            number=48,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy hold-off output.  Present state of an energy
            hold-off device that is hardwired to the controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=49,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffectFlowSP'] = base.Profile.DatapointMember(
            doc="""Effective airflow setpoint output.  Active flow setpoint
            used by the flow control loop.""",
            name='nvoEffectFlowSP',
            profile=self,
            number=50,
            datatype=SNVT_flow,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFlowSetpoint'] = base.Profile.DatapointMember(
            doc="""Flow control damper setpoint output.  Active flow setpoint
            used by the flow control loop.""",
            name='nvoFlowSetpoint',
            profile=self,
            number=51,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x7f\x58',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciNomFlow':
                base.Profile.PropertyMember(
                    doc="""Nominal air flow.  Nominal airflow volume of a VAV
                    terminal.""",
                    name='nciNomFlow',
                    profile=self,
                    number=13,
                    datatype=SCPTnomAirFlow,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAirflow'] = base.Profile.DatapointMember(
            doc="""Airflow output.  Measured airflow in the unit.""",
            name='nvoAirflow',
            profile=self,
            number=52,
            datatype=SNVT_flow,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviHeatSrcTemp'] = base.Profile.DatapointMember(
            doc="""Heat source temperature input.  Temperature of the air or
            water being supplied to the unit for heating capacity.""",
            name='nviHeatSrcTemp',
            profile=self,
            number=53,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x27\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCoolSrcTemp'] = base.Profile.DatapointMember(
            doc="""Cool source temperature input.  Temperature of the air or
            water being supplied to the unit for cooling capacity.""",
            name='nviCoolSrcTemp',
            profile=self,
            number=54,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHeatPriSlave'] = base.Profile.DatapointMember(
            doc="""Primary heat input for slave operation.  This input NV is
            intended for slave operation.""",
            name='nviHeatPriSlave',
            profile=self,
            number=55,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHeatSecSlave'] = base.Profile.DatapointMember(
            doc="""Secondary heat input for slave operation.  This input NV
            is intended for slave operation.""",
            name='nviHeatSecSlave',
            profile=self,
            number=56,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCoolPriSlave'] = base.Profile.DatapointMember(
            doc="""Primary cool input for slave operation.  This input NV is
            intended for slave operation.""",
            name='nviCoolPriSlave',
            profile=self,
            number=57,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCoolSecSlave'] = base.Profile.DatapointMember(
            doc="""Secondary cool input for slave operation.  This input NV
            is intended for slave operation.""",
            name='nviCoolSecSlave',
            profile=self,
            number=58,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOAMinPos'] = base.Profile.DatapointMember(
            doc="""Minimum position OA damper input.  Dynamic minimum
            position setpoint for an outdoor air damper.  When valid it will
            supercede nciOAMinPos.""",
            name='nviOAMinPos',
            profile=self,
            number=59,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMinAirFlow'] = base.Profile.DatapointMember(
            doc="""Minimum air flow setpoint input.  Dynamic minimum cooling
            air flow setpoint for single or dual duct VAV terminal units.
            When valid it will supercede nciMinFlow.""",
            name='nviMinAirFlow',
            profile=self,
            number=60,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMinAirFlowHt'] = base.Profile.DatapointMember(
            doc="""Minimum heat air flow setpoint input.  Dynamic minimum
            heating air flow setpoint for single or dual duct VAV terminal
            units.  When valid it will supercede nciMinFlowHeat.""",
            name='nviMinAirFlowHt',
            profile=self,
            number=61,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviAirFlowSetpt'] = base.Profile.DatapointMember(
            doc="""Air flow setpoint input.  The controller will add this
            input with nciFlowOffset to derive the active flow setpoint.""",
            name='nviAirFlowSetpt',
            profile=self,
            number=62,
            datatype=SNVT_flow,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Terminal load input.  When used with nvoTerminalLoad from
            another controller can be used to coordinate master/salve
            operation.""",
            name='nviTerminalLoad',
            profile=self,
            number=63,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\xb1\xe0',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoMixedAirTemp'] = base.Profile.DatapointMember(
            doc="""Mixed air temperature output.  The temperature of the
            combined return and fresh airstreams in an AHU before they reach
            the water coils.""",
            name='nvoMixedAirTemp',
            profile=self,
            number=64,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLocalSpaceTmp'] = base.Profile.DatapointMember(
            doc="""Local space temperature output.  Local hardwired space
            temperature input.""",
            name='nvoLocalSpaceTmp',
            profile=self,
            number=65,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffFlowSPHeat'] = base.Profile.DatapointMember(
            doc="""Effective air flow heat setpoint output.  The hot or
            ventilation duct flow setpoint of a dual duct unit.""",
            name='nvoEffFlowSPHeat',
            profile=self,
            number=66,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFlowSPHeat'] = base.Profile.DatapointMember(
            doc="""Flow control damper heat setpoint output.  Active flow
            setpoint used by the flow control loop for a hot or ventilation
            deck in a dual duct unit.""",
            name='nvoFlowSPHeat',
            profile=self,
            number=67,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x7f\x58',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAirFlowHeat'] = base.Profile.DatapointMember(
            doc="""Air flow heat output.  Air flow of a hot or ventilation
            deck of a dual duct VAV terminal.""",
            name='nvoAirFlowHeat',
            profile=self,
            number=68,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSatStatus'] = base.Profile.DatapointMember(
            doc="""HVAC saturation status.  Indicates whether the control
            algorithm capacity limits, or end device physical limits, have
            been reached.""",
            name='nvoSatStatus',
            profile=self,
            number=69,
            datatype=SNVT_hvac_satsts,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before the specified NV outputs will automatically be
            updated.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            mandatory=True
        )
        self.properties['nciSetpoints'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  Space temperature
            setpoints for the various heat, cool, and occupancy modes.""",
            name='nciSetpoints',
            profile=self,
            number=2,
            datatype=SCPTsetPnts,
            mandatory=True
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum period of time between
            automatic NV output transmissions.""",
            name='nciMinOutTm',
            profile=self,
            number=3,
            datatype=SCPTminSendTime,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Receive heartbeat.  Maximum time that elapses after the
            last update to a specified NV input before the SCC starts to use
            its default values.""",
            name='nciRcvHrtBt',
            profile=self,
            number=4,
            datatype=SCPTmaxRcvTime,
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=5,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciNumValve'] = base.Profile.PropertyMember(
            doc="""Number of heating/cooling valves.  Selects whether the SCC
            is used in a two pipe (one valve) or four pipe (two valve)
            system.""",
            name='nciNumValve',
            profile=self,
            number=11,
            datatype=SCPTnumValves,
            mandatory=False
        )
        self.properties['nciDuctArea'] = base.Profile.PropertyMember(
            doc="""Duct area or size.  Nominal cross-sectional airflow area
            of a VAV terminal.""",
            name='nciDuctArea',
            profile=self,
            number=12,
            datatype=SCPTductArea,
            mandatory=False
        )
        self.properties['nciFlowGain'] = base.Profile.PropertyMember(
            doc="""Airflow measurement gain.  Calibrates the airflow reading
            of a VAV terminal.""",
            name='nciFlowGain',
            profile=self,
            number=14,
            datatype=SCPTsensConstVAV,
            mandatory=False
        )
        self.properties['nciMinFlowHeat'] = base.Profile.PropertyMember(
            doc="""Heating minimum airflow.  Minimum airflow setpoint of a
            VAV terminal while heating.""",
            name='nciMinFlowHeat',
            profile=self,
            number=17,
            datatype=SCPTminFlowHeat,
            mandatory=False
        )
        self.properties['nciMaxFlowHeat'] = base.Profile.PropertyMember(
            doc="""Heating maximum airflow.  Maximum airflow setpoint of a
            VAV terminal while heating.""",
            name='nciMaxFlowHeat',
            profile=self,
            number=18,
            datatype=SCPTmaxFlowHeat,
            mandatory=False
        )
        self.properties['nciMinFlowStdby'] = base.Profile.PropertyMember(
            doc="""Standby minimum airflow.  Minimum airflow setpoint of a
            VAV terminal in the Standby (occupancy) mode.""",
            name='nciMinFlowStdby',
            profile=self,
            number=19,
            datatype=SCPTminFlowStby,
            mandatory=False
        )
        self.properties['nciHvacType'] = base.Profile.PropertyMember(
            doc="""HVAC unit type identifier.  This value is set by the
            manufacturer to allow an integrator to know the function of this
            SCC device.""",
            name='nciHvacType',
            profile=self,
            number=20,
            datatype=SCPThvacType,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciFanOperation'] = base.Profile.PropertyMember(
            doc="""Fan operation.  Specifies fan operation during occupied
            and occupied standby.  Fan operation during unoccupied is
            manufacturer defined.""",
            name='nciFanOperation',
            profile=self,
            number=21,
            datatype=SCPTfanOperation,
            mandatory=False
        )
        self.properties['nciUnitMinFlow'] = base.Profile.PropertyMember(
            doc="""Unit minimum air flow.  Unit minimum air flow for dual
            duct VAV Terminal units.""",
            name='nciUnitMinFlow',
            profile=self,
            number=22,
            datatype=SCPTminFlowUnit,
            mandatory=False
        )
        self.properties['nciUnitMaxFlow'] = base.Profile.PropertyMember(
            doc="""Unit maximum air flow.  Unit maximum air flow for dual
            duct VAV Terminal units.""",
            name='nciUnitMaxFlow',
            profile=self,
            number=23,
            datatype=SCPTmaxFlowUnit,
            mandatory=False
        )
        self.properties['nciMnFlwStdbyHt'] = base.Profile.PropertyMember(
            doc="""Standby heating minimum air flow.  The heating or
            ventilated deck minimum flow of a dual duct VAV Terminal unit
            during occupied standby mode.""",
            name='nciMnFlwStdbyHt',
            profile=self,
            number=24,
            datatype=SCPTminFlowHeatStby,
            mandatory=False
        )
        self.properties['nciUntMnFlwStdby'] = base.Profile.PropertyMember(
            doc="""Standby unit minimum air flow.  Total unit minimum airflow
            for dual duct units during occupied standby mode.""",
            name='nciUntMnFlwStdby',
            profile=self,
            number=25,
            datatype=SCPTminFlowUnitStby,
            mandatory=False
        )
        self.properties['nciFlowOffset'] = base.Profile.PropertyMember(
            doc="""Air flow offset.  """,
            name='nciFlowOffset',
            profile=self,
            number=26,
            datatype=SCPToffsetFlow,
            mandatory=False
        )
        self.properties['nciDuctAreaHeat'] = base.Profile.PropertyMember(
            doc="""Heating duct area.  Nominal cross-sectional airflow area
            of the hot or ventilation deck of a dual duct VAV terminal
            unit.""",
            name='nciDuctAreaHeat',
            profile=self,
            number=27,
            datatype=SCPTareaDuctHeat,
            mandatory=False
        )
        self.properties['nciNomFlowHeat'] = base.Profile.PropertyMember(
            doc="""Heating nominal flow.  Value used to provide the nominal
            airflow volume of a hot or ventilation deck of a dual duct VAV
            terminal.""",
            name='nciNomFlowHeat',
            profile=self,
            number=28,
            datatype=SCPTnomAirFlowHeat,
            mandatory=False
        )
        self.properties['nciFlowGainHeat'] = base.Profile.PropertyMember(
            doc="""VAV sensor constant.  Calibration constant used to
            calculate airflow.""",
            name='nciFlowGainHeat',
            profile=self,
            number=29,
            datatype=SCPTgainVAVHeat,
            mandatory=False
        )
        self.properties['nciNumDampers'] = base.Profile.PropertyMember(
            doc="""Number of dampers.  Indicates to the controller if it is
            in a single or dual duct system.""",
            name='nciNumDampers',
            profile=self,
            number=30,
            datatype=SCPTnumDampers,
            mandatory=False
        )
        self.properties['nciMinFlowUnitHt'] = base.Profile.PropertyMember(
            doc="""Unit heating minimum flow.  Minimum airflow setpoint of a
            single duct, or the unit minimum airflow setpoint of a dual duct
            VAV terminal when using a unit (local) heating source.""",
            name='nciMinFlowUnitHt',
            profile=self,
            number=31,
            datatype=SCPTminFlowUnitHeat,
            mandatory=False
        )
        self.properties['nciSatTime'] = base.Profile.PropertyMember(
            doc="""Saturation time.  """,
            name='nciSatTime',
            profile=self,
            number=32,
            datatype=SCPTsaturationDelay,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTsccVAV()
    pass
