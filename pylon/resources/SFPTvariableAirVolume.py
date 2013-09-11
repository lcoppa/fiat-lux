"""SFPTvariableAirVolume standard profile, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_hvac_overid import SNVT_hvac_overid
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SNVT_flow import SNVT_flow
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_ppm import SNVT_ppm
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTductArea import SCPTductArea
from pylon.resources.SCPTminFlow import SCPTminFlow
from pylon.resources.SCPTmaxFlow import SCPTmaxFlow
from pylon.resources.SCPTminFlowHeat import SCPTminFlowHeat
from pylon.resources.SCPTminFlowStby import SCPTminFlowStby
from pylon.resources.SCPTnomAirFlow import SCPTnomAirFlow
from pylon.resources.SCPTgainVAV import SCPTgainVAV
from pylon.resources.SCPTsetPnts import SCPTsetPnts


class SFPTvariableAirVolume(base.Profile):
    """SFPTvariableAirVolume standard profile.  Variable Air-Volume
    Controller (VAV) nciSetPnts is not defined in the profile due to its type
    inheriting from the Principal NV of the profile.  No mandatory NVs are of
    SNVT_temp_setpt, and therefore it cannot inherit the correct type."""

    def __init__(self):
        super().__init__(
            key=8010,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            minimum=b'\x03\xe8',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN01':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN01',
                    profile=self,
                    number=17,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetPoint'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input.  This input network variable
            is used to allow the temperature setpoint for the occupied and
            standby mode to be changed via network.""",
            name='nviSetPoint',
            profile=self,
            number=2,
            datatype=SNVT_temp_p,
            mandatory=True,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to send the value of the controlled space temperature to
            other nodes.""",
            name='nvoSpaceTemp',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV03',
                    profile=self,
                    number=25,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit Status Output.  """,
            name='nvoUnitStatus',
            profile=self,
            number=4,
            datatype=SNVT_hvac_status,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            maximum=b'\xff\x4e\x20\x4e\x20\x4e\x20\x4e\x20\x4e\x20\xff',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV04':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV04',
                    profile=self,
                    number=26,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the VAV object with the air handler control or
            any other supervisory controller or intelligent human interface
            device.""",
            name='nviApplicMode',
            profile=self,
            number=5,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN05':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN05',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviManOverride'] = base.Profile.DatapointMember(
            doc="""VAV Manual Override Input.  This input network variable is
            used for commanding the controller into a manual mode.""",
            name='nviManOverride',
            profile=self,
            number=6,
            datatype=SNVT_hvac_overid,
            mandatory=False,
            maximum=b'\xff\x4e\x20\xff\xff',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetpointOffset'] = base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the temperature setpoint via the network by adding
            nviSetpointOffset to the current setpoint.""",
            name='nviSetpointOffset',
            profile=self,
            number=7,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x03\xe8',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN07':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN07',
                    profile=self,
                    number=18,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy Input.  This input network variable is used to
            command the VAV objectinto different occupancy modes.""",
            name='nviOccCmd',
            profile=self,
            number=8,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergCmd'] = base.Profile.DatapointMember(
            doc="""Emergency Command Input.  This input network variable is
            used to command the VAV object into different emergency
            modes.""",
            name='nviEmergCmd',
            profile=self,
            number=9,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBoxFlow'] = base.Profile.DatapointMember(
            doc="""Box Flow Input.  This variable represents the input to a
            VAV controller object from a flow sensor on the network.""",
            name='nviBoxFlow',
            profile=self,
            number=10,
            datatype=SNVT_flow,
            mandatory=False,
            minimum=b'\x00\x00',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN10':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN10',
                    profile=self,
                    number=20,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold-Off Input.  This input is from a device such
            as a window contact sensor.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=11,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN11':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN11',
                    profile=self,
                    number=21,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFanSpeedCmd'] = base.Profile.DatapointMember(
            doc="""Fan-Speed Command Input.  This input network variable is
            used to connect an external fan speed switch to the node or to
            allow any supervisory device to override the fan speed controlled
            by the node's control algorithm.""",
            name='nviFanSpeedCmd',
            profile=self,
            number=12,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCO2'] = base.Profile.DatapointMember(
            doc="""CO2 Sensor Input.  This input network variable measures
            the CO2 levels in PPM.""",
            name='nviCO2',
            profile=self,
            number=13,
            datatype=SNVT_ppm,
            mandatory=False,
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN13':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN13',
                    profile=self,
                    number=22,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeaterOverid'] = base.Profile.DatapointMember(
            doc="""Heater Override Input.  This input disables to be turned
            on by the VAV controller.""",
            name='nviHeaterOverid',
            profile=self,
            number=14,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctInTemp'] = base.Profile.DatapointMember(
            doc="""Duct-Inlet Temperature Input.  If the duct inlet air
            temperature sensor is a LONMARK device, the VAV controller object
            obtains its value through this network variable.""",
            name='nviDuctInTemp',
            profile=self,
            number=15,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN15':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN15',
                    profile=self,
                    number=23,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectSetPt'] = base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  The output network variable is
            used to inform the effective setpoint temperature when the
            setpoint is changed by local means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=16,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV16':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV16',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFlowControlPt'] = base.Profile.DatapointMember(
            doc="""Effective-Flow Control-Point Output.  The output network
            variable is used to inform the effective control point used by
            the flow control loop.""",
            name='nvoFlowControlPt',
            profile=self,
            number=17,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoBoxFlow'] = base.Profile.DatapointMember(
            doc="""Box Flow Output.  The output network variable is used to
            provide the flow in the box.""",
            name='nvoBoxFlow',
            profile=self,
            number=18,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV18':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV18',
                    profile=self,
                    number=13,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Terminal Load Output.  The output network variable is used
            to provide the demand for supply energy.""",
            name='nvoTerminalLoad',
            profile=self,
            number=19,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV19':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV19',
                    profile=self,
                    number=14,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHoldOff'] = base.Profile.DatapointMember(
            doc="""Energy Hold-Off Output.  This output is used to convey to
            other devices the state of an EnergyHoldOff device that is
            hardwired to the controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=20,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\xc8\x01',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV20':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV20',
                    profile=self,
                    number=16,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Send heartbeat.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Receive heartbeat.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=2,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=3,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=4,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciDuctArea'] = base.Profile.PropertyMember(
            doc="""Duct area or size.  The duct area used to calculate the
            air flow, relevant only for VAV actuators / controllers.""",
            name='nciDuctArea',
            profile=self,
            number=5,
            datatype=SCPTductArea,
            maximum=b'\xff\xfe',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinFlow'] = base.Profile.PropertyMember(
            doc="""Minimum flow.  The minimum flow.""",
            name='nciMinFlow',
            profile=self,
            number=6,
            datatype=SCPTminFlow,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxFlow'] = base.Profile.PropertyMember(
            doc="""Maximum flow.  The maximum flow.""",
            name='nciMaxFlow',
            profile=self,
            number=7,
            datatype=SCPTmaxFlow,
            maximum=b'\xff\xff',
            default=b'\xff\xff',
            mandatory=True
        )
        self.properties['nciMinFlowHeat'] = base.Profile.PropertyMember(
            doc="""Minimum heating airflow.  The minimum airflow setpoint of
            a VAV terminal while heating.""",
            name='nciMinFlowHeat',
            profile=self,
            number=8,
            datatype=SCPTminFlowHeat,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinFlowStand'] = base.Profile.PropertyMember(
            doc="""Minimum flow for standby.  The minimum flow through the
            VAV box in standby mode.""",
            name='nciMinFlowStand',
            profile=self,
            number=9,
            datatype=SCPTminFlowStby,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciNomFlow'] = base.Profile.PropertyMember(
            doc="""Nominal air flow.  Value used in calculating the air flow
            in an airflow control actuator.""",
            name='nciNomFlow',
            profile=self,
            number=10,
            datatype=SCPTnomAirFlow,
            minimum=b'\x00\x00',
            maximum=b'\x12\x8e',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciVAVgain'] = base.Profile.PropertyMember(
            doc="""VAV gain.  The gain of the VAV controller object.""",
            name='nciVAVgain',
            profile=self,
            number=11,
            datatype=SCPTgainVAV,
            default=b'\x07\xd0',
            mandatory=False
        )
        self.properties['nciSetPnts'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=24,
            datatype=SCPTsetPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTvariableAirVolume()
    pass
