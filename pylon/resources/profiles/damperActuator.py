"""damperActuator standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.switch
import pylon.resources.properties.maxRnge
import pylon.resources.properties.minRnge
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.datapoints.hvac_overid
import pylon.resources.datapoints.angle_deg
import pylon.resources.properties.minDeltaAngl
import pylon.resources.datapoints.flow
import pylon.resources.properties.minDeltaFlow
import pylon.resources.datapoints.temp_p
import pylon.resources.properties.minDeltaTemp
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.direction
import pylon.resources.properties.actuatorType
import pylon.resources.properties.oemType
import pylon.resources.properties.location
import pylon.resources.properties.driveTime
import pylon.resources.properties.nomAngle
import pylon.resources.properties.nomAirFlow
import pylon.resources.properties.ductArea
import pylon.resources.properties.sensConstVAV
import pylon.resources.properties.sensConstTmp


class damperActuator(pylon.resources.base.Profile):
    """damperActuator standard profile.  Damper Actuator.  Three sub types of
    HVAC actuators can be handled by this object:  general purpose, fire &
    smoke, and airflow control."""

    def __init__(self):
        super().__init__(
            key=8110,
            scope=0
        )
        self.datapoints['nviRelStpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator setpoint input.  Controls the relative actuator
            setpoint.""",
            name='nviRelStpt',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviActuatState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator state input.  Used where the actuator is
            connected to a switch that forces the actuator to a predefined
            set of positions or air volumes.""",
            name='nviActuatState',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActualValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actual position output.  Present position of the
            actuator.""",
            name='nvoActualValue',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSetpoint':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum range.  The maximum limit of the value of
                    the primary output network variable for the object.""",
                    name='nciMaxSetpoint',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.maxRnge.maxRnge,
                    default=b'\x00\x00\x4e\x20',
                    mandatory=False
                ),
                'nciMinSetpoint':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum range.  The minimum limit of the value of
                    the primary output network variable for the object.""",
                    name='nciMinSetpoint',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.minRnge.minRnge,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEmergOvrd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency override input.  Used in fire and smoke
            applications to open and close an actuator with maximum speed;
            this input has highest priority.""",
            name='nviEmergOvrd',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviManOvrd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Manual override input.  Command the actuator into a manual
            mode (mainly used during balancing)""",
            name='nviManOvrd',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.hvac_overid.hvac_overid,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActuatStateFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator state feedback output.  Mirrors the actual value
            of nviActuatState.""",
            name='nvoActuatStateFb',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRelStptFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator setpoint feedback output.  Mirrors the actual
            value of nviRelStpt.""",
            name='nvoRelStptFb',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAbsAngle'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Damper angle output.  Present position of the actuator's
            shaft or damper blade.""",
            name='nvoAbsAngle',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.angle_deg.angle_deg,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltAngl':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Damper angle send on delta.  The minimum change in
                    damper actuator angle required to be treated as
                    significant.""",
                    name='nciSendOnDltAngl',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.minDeltaAngl.minDeltaAngl,
                    minimum=b'\x00\x00',
                    default=b'\x00\xfa',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAbsAirFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Air flow output.  Airflow through the associated VAV
            box.""",
            name='nvoAbsAirFlow',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltFlow':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Flow send on delta.  The minimum change in airflow
                    required to be treated as significant.""",
                    name='nciSendOnDltFlow',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.minDeltaFlow.minDeltaFlow,
                    default=b'\x00\x0a',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDuctTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Inside duct temperature output.  Present temperature
            inside the duct.""",
            name='nvoDuctTemp',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xec\x78',
            maximum=b'\x3a\x98',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltTemp':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum delta temperature.  The minimum change in
                    temperature required to be treated as significant.""",
                    name='nciSendOnDltTemp',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.minDeltaTemp.minDeltaTemp,
                    minimum=b'\x00\x00',
                    default=b'\x00\x64',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergOvrdFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency override feedback output.  Mirrors the value of
            nviEmergOvrd.""",
            name='nvoEmergOvrdFb',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x01\x2c',
            mandatory=True
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciDirection'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Direction / Safety position.  The actuator sense of
            rotation and safety position;  bit 0 set => counterclockwise, bit
            1 set => damper open.""",
            name='nciDirection',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.direction.direction,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciActuatType'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciActuatType',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.actuatorType.actuatorType,
            flags=pylon.resources.base.PropertyFlags.MFG,
            mandatory=False
        )
        self.properties['nciOemType'] = pylon.resources.base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOemType',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.oemType.oemType,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciDriveTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveTime',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.driveTime.driveTime,
            default=b'\x05\xdc',
            mandatory=False
        )
        self.properties['nciNomAngle'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal angle.  The nominal angle for an actuator.""",
            name='nciNomAngle',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.nomAngle.nomAngle,
            minimum=b'\x00\x00',
            maximum=b'\x12\x8e',
            default=b'\x11\x94',
            mandatory=False
        )
        self.properties['nciNomAirFlow'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal air flow.  Value used in calculating the air flow
            in an airflow control actuator.""",
            name='nciNomAirFlow',
            profile=self,
            number=13,
            datatype=pylon.resources.properties.nomAirFlow.nomAirFlow,
            mandatory=False
        )
        self.properties['nciDuctSize'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Duct area or size.  The duct area used to calculate the
            air flow, relevant only for VAV actuators / controllers.""",
            name='nciDuctSize',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.ductArea.ductArea,
            mandatory=False
        )
        self.properties['nciVavSensConst'] = pylon.resources.base.Profile.PropertyMember(
            doc="""VAV sensor constant.  Calibration constant used to
            calculate airflow.""",
            name='nciVavSensConst',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.sensConstVAV.sensConstVAV,
            mandatory=False
        )
        self.properties['nciTempSensConst'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Temperature sensor constant.  Calibration value for a duct
            temperature sensor.""",
            name='nciTempSensConst',
            profile=self,
            number=18,
            datatype=pylon.resources.properties.sensConstTmp.sensConstTmp,
            mandatory=False
        )
        self._original_name = 'SFPTdamperActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = damperActuator()
    pass
