"""SFPTfireSmokeDamperActuator standard profile, originally defined in
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTdriveTime import SCPTdriveTime
from pylon.resources.SCPTdirection import SCPTdirection
from pylon.resources.SCPToffDely import SCPToffDely
from pylon.resources.SCPTzoneNum import SCPTzoneNum
from pylon.resources.SCPTactuatorType import SCPTactuatorType
from pylon.resources.SCPTinstallDate import SCPTinstallDate
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTmaintDate import SCPTmaintDate
from pylon.resources.SCPTmanfDate import SCPTmanfDate
from pylon.resources.SCPToemType import SCPToemType


class SFPTfireSmokeDamperActuator(base.Profile):
    """SFPTfireSmokeDamperActuator standard profile.  Fire Smoke Damper
    Actuator.  Used to expell smoke or control fire-spread by manipulating
    the actuator position on a damper."""

    def __init__(self):
        super().__init__(
            key=11001,
            scope=0
        )
        self.datapoints['nviActuDrive'] = base.Profile.DatapointMember(
            doc="""Actuator Drive.  Controls the actuator position.""",
            name='nviActuDrive',
            profile=self,
            number=1,
            datatype=SNVT_hvac_emerg,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvrHrtBt':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvrHrtBt',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoActuDriveFb'] = base.Profile.DatapointMember(
            doc="""Actuator Drive Feedback.  Reflects the actuator value of
            nviActuDrive.  Used to synchronize source objects in multiple
            relationships.""",
            name='nvoActuDriveFb',
            profile=self,
            number=3,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActuPosn'] = base.Profile.DatapointMember(
            doc="""HVAC emergency mode.  """,
            name='nvoActuPosn',
            profile=self,
            number=2,
            datatype=SNVT_hvac_emerg,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=12,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciDriveT'] = base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveT',
            profile=self,
            number=1,
            datatype=SCPTdriveTime,
            default=b'\x05\xdc',
            mandatory=True
        )
        self.properties['nciSafetyPosn'] = base.Profile.PropertyMember(
            doc="""Direction / Safety position.  The actuator sense of
            rotation and safety position;  bit 0 set => counterclockwise, bit
            1 set => damper open.""",
            name='nciSafetyPosn',
            profile=self,
            number=3,
            datatype=SCPTdirection,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTurnOffT'] = base.Profile.PropertyMember(
            doc="""Turn-off delay.  The length of time that the load remains
            energized after a change from ON to OFF has been received.""",
            name='nciTurnOffT',
            profile=self,
            number=4,
            datatype=SCPToffDely,
            maximum=b'\x00\x00\x11\x3b\x3b\x03\xe7',
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciZoneNum'] = base.Profile.PropertyMember(
            doc="""Zone number.  The zone number for the device.""",
            name='nciZoneNum',
            profile=self,
            number=5,
            datatype=SCPTzoneNum,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciActuLabel'] = base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciActuLabel',
            profile=self,
            number=6,
            datatype=SCPTactuatorType,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=7,
            datatype=SCPTinstallDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=8,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaintDate'] = base.Profile.PropertyMember(
            doc="""Maintenance date.  The date of last maintenance for the
            device.""",
            name='nciMaintDate',
            profile=self,
            number=9,
            datatype=SCPTmaintDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciManfDate'] = base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciManfDate',
            profile=self,
            number=10,
            datatype=SCPTmanfDate,
            flags=base.PropertyFlags.MFG,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciOEMLable'] = base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOEMLable',
            profile=self,
            number=11,
            datatype=SCPToemType,
            flags=base.PropertyFlags.MFG,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTfireSmokeDamperActuator()
    pass
