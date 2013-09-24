"""SFPTdamperActuator standard profile, originally defined in resource file
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTmaxRnge import SCPTmaxRnge
from pylon.resources.SCPTminRnge import SCPTminRnge
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SNVT_hvac_overid import SNVT_hvac_overid
from pylon.resources.SNVT_angle_deg import SNVT_angle_deg
from pylon.resources.SCPTminDeltaAngl import SCPTminDeltaAngl
from pylon.resources.SNVT_flow import SNVT_flow
from pylon.resources.SCPTminDeltaFlow import SCPTminDeltaFlow
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTminDeltaTemp import SCPTminDeltaTemp
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTdirection import SCPTdirection
from pylon.resources.SCPTactuatorType import SCPTactuatorType
from pylon.resources.SCPToemType import SCPToemType
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTdriveTime import SCPTdriveTime
from pylon.resources.SCPTnomAngle import SCPTnomAngle
from pylon.resources.SCPTnomAirFlow import SCPTnomAirFlow
from pylon.resources.SCPTductArea import SCPTductArea
from pylon.resources.SCPTsensConstVAV import SCPTsensConstVAV
from pylon.resources.SCPTsensConstTmp import SCPTsensConstTmp


class SFPTdamperActuator(base.Profile):
    """SFPTdamperActuator standard profile.  Damper Actuator.  Three sub
    types of HVAC actuators can be handled by this object:  general purpose,
    fire & smoke, and airflow control."""

    def __init__(self):
        super().__init__(
            key=8110,
            scope=0
        )
        self.datapoints['nviRelStpt'] = base.Profile.DatapointMember(
            doc="""Actuator setpoint input.  Controls the relative actuator
            setpoint.""",
            name='nviRelStpt',
            profile=self,
            number=1,
            datatype=SNVT_lev_percent,
            mandatory=True,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviActuatState'] = base.Profile.DatapointMember(
            doc="""Actuator state input.  Used where the actuator is
            connected to a switch that forces the actuator to a predefined
            set of positions or air volumes.""",
            name='nviActuatState',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActualValue'] = base.Profile.DatapointMember(
            doc="""Actual position output.  Present position of the
            actuator.""",
            name='nvoActualValue',
            profile=self,
            number=3,
            datatype=SNVT_lev_percent,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSetpoint':
                base.Profile.PropertyMember(
                    doc="""Maximum range.  The maximum limit of the value of
                    the primary output network variable for the object.""",
                    name='nciMaxSetpoint',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxRnge,
                    default=b'\x00\x00\x4e\x20',
                    mandatory=False
                ),
                'nciMinSetpoint':
                base.Profile.PropertyMember(
                    doc="""Minimum range.  The minimum limit of the value of
                    the primary output network variable for the object.""",
                    name='nciMinSetpoint',
                    profile=self,
                    number=16,
                    datatype=SCPTminRnge,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEmergOvrd'] = base.Profile.DatapointMember(
            doc="""Emergency override input.  Used in fire and smoke
            applications to open and close an actuator with maximum speed;
            this input has highest priority.""",
            name='nviEmergOvrd',
            profile=self,
            number=4,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviManOvrd'] = base.Profile.DatapointMember(
            doc="""Manual override input.  Command the actuator into a manual
            mode (mainly used during balancing)""",
            name='nviManOvrd',
            profile=self,
            number=5,
            datatype=SNVT_hvac_overid,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActuatStateFb'] = base.Profile.DatapointMember(
            doc="""Actuator state feedback output.  Mirrors the actual value
            of nviActuatState.""",
            name='nvoActuatStateFb',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRelStptFb'] = base.Profile.DatapointMember(
            doc="""Actuator setpoint feedback output.  Mirrors the actual
            value of nviRelStpt.""",
            name='nvoRelStptFb',
            profile=self,
            number=7,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAbsAngle'] = base.Profile.DatapointMember(
            doc="""Damper angle output.  Present position of the actuator's
            shaft or damper blade.""",
            name='nvoAbsAngle',
            profile=self,
            number=8,
            datatype=SNVT_angle_deg,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltAngl':
                base.Profile.PropertyMember(
                    doc="""Damper angle send on delta.  The minimum change in
                    damper actuator angle required to be treated as
                    significant.""",
                    name='nciSendOnDltAngl',
                    profile=self,
                    number=7,
                    datatype=SCPTminDeltaAngl,
                    minimum=b'\x00\x00',
                    default=b'\x00\xfa',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAbsAirFlow'] = base.Profile.DatapointMember(
            doc="""Air flow output.  Airflow through the associated VAV
            box.""",
            name='nvoAbsAirFlow',
            profile=self,
            number=9,
            datatype=SNVT_flow,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltFlow':
                base.Profile.PropertyMember(
                    doc="""Flow send on delta.  The minimum change in airflow
                    required to be treated as significant.""",
                    name='nciSendOnDltFlow',
                    profile=self,
                    number=5,
                    datatype=SCPTminDeltaFlow,
                    default=b'\x00\x0a',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDuctTemp'] = base.Profile.DatapointMember(
            doc="""Inside duct temperature output.  Present temperature
            inside the duct.""",
            name='nvoDuctTemp',
            profile=self,
            number=10,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xec\x78',
            maximum=b'\x3a\x98',
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDltTemp':
                base.Profile.PropertyMember(
                    doc="""Minimum delta temperature.  The minimum change in
                    temperature required to be treated as significant.""",
                    name='nciSendOnDltTemp',
                    profile=self,
                    number=6,
                    datatype=SCPTminDeltaTemp,
                    minimum=b'\x00\x00',
                    default=b'\x00\x64',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergOvrdFb'] = base.Profile.DatapointMember(
            doc="""Emergency override feedback output.  Mirrors the value of
            nviEmergOvrd.""",
            name='nvoEmergOvrdFb',
            profile=self,
            number=11,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=1,
            datatype=SCPTminSendTime,
            default=b'\x01\x2c',
            mandatory=True
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvTime'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvTime',
            profile=self,
            number=3,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciDirection'] = base.Profile.PropertyMember(
            doc="""Direction / Safety position.  The actuator sense of
            rotation and safety position;  bit 0 set => counterclockwise, bit
            1 set => damper open.""",
            name='nciDirection',
            profile=self,
            number=4,
            datatype=SCPTdirection,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciActuatType'] = base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciActuatType',
            profile=self,
            number=8,
            datatype=SCPTactuatorType,
            flags=base.PropertyFlags.MFG,
            mandatory=False
        )
        self.properties['nciOemType'] = base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOemType',
            profile=self,
            number=9,
            datatype=SCPToemType,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=10,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciDriveTime'] = base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveTime',
            profile=self,
            number=11,
            datatype=SCPTdriveTime,
            default=b'\x05\xdc',
            mandatory=False
        )
        self.properties['nciNomAngle'] = base.Profile.PropertyMember(
            doc="""Nominal angle.  The nominal angle for an actuator.""",
            name='nciNomAngle',
            profile=self,
            number=12,
            datatype=SCPTnomAngle,
            minimum=b'\x00\x00',
            maximum=b'\x12\x8e',
            default=b'\x11\x94',
            mandatory=False
        )
        self.properties['nciNomAirFlow'] = base.Profile.PropertyMember(
            doc="""Nominal air flow.  Value used in calculating the air flow
            in an airflow control actuator.""",
            name='nciNomAirFlow',
            profile=self,
            number=13,
            datatype=SCPTnomAirFlow,
            mandatory=False
        )
        self.properties['nciDuctSize'] = base.Profile.PropertyMember(
            doc="""Duct area or size.  The duct area used to calculate the
            air flow, relevant only for VAV actuators / controllers.""",
            name='nciDuctSize',
            profile=self,
            number=14,
            datatype=SCPTductArea,
            mandatory=False
        )
        self.properties['nciVavSensConst'] = base.Profile.PropertyMember(
            doc="""VAV sensor constant.  Calibration constant used to
            calculate airflow.""",
            name='nciVavSensConst',
            profile=self,
            number=17,
            datatype=SCPTsensConstVAV,
            mandatory=False
        )
        self.properties['nciTempSensConst'] = base.Profile.PropertyMember(
            doc="""Temperature sensor constant.  Calibration value for a duct
            temperature sensor.""",
            name='nciTempSensConst',
            profile=self,
            number=18,
            datatype=SCPTsensConstTmp,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTdamperActuator()
    pass
