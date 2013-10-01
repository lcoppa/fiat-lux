"""variableAirVolume standard profile, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.hvac_status
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.hvac_overid
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.datapoints.flow
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.ppm
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.minSendTime
import pylon.resources.properties.location
import pylon.resources.properties.ductArea
import pylon.resources.properties.minFlow
import pylon.resources.properties.maxFlow
import pylon.resources.properties.minFlowHeat
import pylon.resources.properties.minFlowStby
import pylon.resources.properties.nomAirFlow
import pylon.resources.properties.gainVAV
import pylon.resources.properties.setPnts


class variableAirVolume(pylon.resources.base.Profile):
    """variableAirVolume standard profile.  Variable Air-Volume Controller
    (VAV) nciSetPnts is not defined in the profile due to its type inheriting
    from the Principal NV of the profile.  No mandatory NVs are of
    SNVT_temp_setpt, and therefore it cannot inherit the correct type."""

    def __init__(self):
        super().__init__(
            key=8010,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            minimum=b'\x03\xe8',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN01',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetPoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input.  This input network variable
            is used to allow the temperature setpoint for the occupied and
            standby mode to be changed via network.""",
            name='nviSetPoint',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSpaceTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to send the value of the controlled space temperature to
            other nodes.""",
            name='nvoSpaceTemp',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV03',
                    profile=self,
                    number=25,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Unit Status Output.  """,
            name='nvoUnitStatus',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_status.hvac_status,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            maximum=b'\xff\x4e\x20\x4e\x20\x4e\x20\x4e\x20\x4e\x20\xff',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV04':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV04',
                    profile=self,
                    number=26,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviApplicMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the VAV object with the air handler control or
            any other supervisory controller or intelligent human interface
            device.""",
            name='nviApplicMode',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN05',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviManOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""VAV Manual Override Input.  This input network variable is
            used for commanding the controller into a manual mode.""",
            name='nviManOverride',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.hvac_overid.hvac_overid,
            mandatory=False,
            maximum=b'\xff\x4e\x20\xff\xff',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetpointOffset'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the temperature setpoint via the network by adding
            nviSetpointOffset to the current setpoint.""",
            name='nviSetpointOffset',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x03\xe8',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN07':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN07',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy Input.  This input network variable is used to
            command the VAV objectinto different occupancy modes.""",
            name='nviOccCmd',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency Command Input.  This input network variable is
            used to command the VAV object into different emergency
            modes.""",
            name='nviEmergCmd',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviBoxFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Box Flow Input.  This variable represents the input to a
            VAV controller object from a flow sensor on the network.""",
            name='nviBoxFlow',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            minimum=b'\x00\x00',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN10':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN10',
                    profile=self,
                    number=20,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold-Off Input.  This input is from a device such
            as a window contact sensor.""",
            name='nviEnergyHoldOff',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN11':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN11',
                    profile=self,
                    number=21,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFanSpeedCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fan-Speed Command Input.  This input network variable is
            used to connect an external fan speed switch to the node or to
            allow any supervisory device to override the fan speed controlled
            by the node's control algorithm.""",
            name='nviFanSpeedCmd',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCO2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""CO2 Sensor Input.  This input network variable measures
            the CO2 levels in PPM.""",
            name='nviCO2',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.ppm.ppm,
            mandatory=False,
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN13':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN13',
                    profile=self,
                    number=22,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviHeaterOverid'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heater Override Input.  This input disables to be turned
            on by the VAV controller.""",
            name='nviHeaterOverid',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDuctInTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Duct-Inlet Temperature Input.  If the duct inlet air
            temperature sensor is a LONMARK device, the VAV controller object
            obtains its value through this network variable.""",
            name='nviDuctInTemp',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfc\x18',
            maximum=b'\x13\x88',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtN15':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtN15',
                    profile=self,
                    number=23,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectSetPt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  The output network variable is
            used to inform the effective setpoint temperature when the
            setpoint is changed by local means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x03\xe8',
            maximum=b'\x0d\xac',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV16':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV16',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFlowControlPt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective-Flow Control-Point Output.  The output network
            variable is used to inform the effective control point used by
            the flow control loop.""",
            name='nvoFlowControlPt',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoBoxFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Box Flow Output.  The output network variable is used to
            provide the flow in the box.""",
            name='nvoBoxFlow',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV18':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV18',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTerminalLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Terminal Load Output.  The output network variable is used
            to provide the demand for supply energy.""",
            name='nvoTerminalLoad',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV19':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV19',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEnergyHoldOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Energy Hold-Off Output.  This output is used to convey to
            other devices the state of an EnergyHoldOff device that is
            hardwired to the controller.""",
            name='nvoEnergyHoldOff',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\xc8\x01',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV20':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV20',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            array_size_max=65500,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Receive heartbeat.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            array_size_max=65500,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinOutTm',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            array_size_max=65500,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciDuctArea'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Duct area or size.  The duct area used to calculate the
            air flow, relevant only for VAV actuators / controllers.""",
            name='nciDuctArea',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.ductArea.ductArea,
            maximum=b'\xff\xfe',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinFlow'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum flow.  The minimum flow.""",
            name='nciMinFlow',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.minFlow.minFlow,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxFlow'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum flow.  The maximum flow.""",
            name='nciMaxFlow',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.maxFlow.maxFlow,
            maximum=b'\xff\xff',
            default=b'\xff\xff',
            mandatory=True
        )
        self.properties['nciMinFlowHeat'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum heating airflow.  The minimum airflow setpoint of
            a VAV terminal while heating.""",
            name='nciMinFlowHeat',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.minFlowHeat.minFlowHeat,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinFlowStand'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum flow for standby.  The minimum flow through the
            VAV box in standby mode.""",
            name='nciMinFlowStand',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.minFlowStby.minFlowStby,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciNomFlow'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal air flow.  Value used in calculating the air flow
            in an airflow control actuator.""",
            name='nciNomFlow',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.nomAirFlow.nomAirFlow,
            minimum=b'\x00\x00',
            maximum=b'\x12\x8e',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciVAVgain'] = pylon.resources.base.Profile.PropertyMember(
            doc="""VAV gain.  The gain of the VAV controller object.""",
            name='nciVAVgain',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.gainVAV.gainVAV,
            default=b'\x07\xd0',
            mandatory=False
        )
        self.properties['nciSetPnts'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=24,
            datatype=pylon.resources.properties.setPnts.setPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self._original_name = 'SFPTvariableAirVolume'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = variableAirVolume()
    pass
