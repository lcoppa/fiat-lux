"""fireSmokeDamperActuator standard profile, originally defined in resource
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
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.driveTime
import pylon.resources.properties.direction
import pylon.resources.properties.offDely
import pylon.resources.properties.zoneNum
import pylon.resources.properties.actuatorType
import pylon.resources.properties.installDate
import pylon.resources.properties.location
import pylon.resources.properties.maintDate
import pylon.resources.properties.manfDate
import pylon.resources.properties.oemType


class fireSmokeDamperActuator(pylon.resources.base.Profile):
    """fireSmokeDamperActuator standard profile.  Fire Smoke Damper
    Actuator.  Used to expell smoke or control fire-spread by manipulating
    the actuator position on a damper."""

    def __init__(self):
        super().__init__(
            key=11001,
            scope=0
        )
        self.datapoints['nviActuDrive'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator Drive.  Controls the actuator position.""",
            name='nviActuDrive',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvrHrtBt':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvrHrtBt',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoActuDriveFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actuator Drive Feedback.  Reflects the actuator value of
            nviActuDrive.  Used to synchronize source objects in multiple
            relationships.""",
            name='nvoActuDriveFb',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActuPosn'] = pylon.resources.base.Profile.DatapointMember(
            doc="""HVAC emergency mode.  """,
            name='nvoActuPosn',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciDriveT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveT',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.driveTime.driveTime,
            default=b'\x05\xdc',
            mandatory=True
        )
        self.properties['nciSafetyPosn'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Direction / Safety position.  The actuator sense of
            rotation and safety position;  bit 0 set => counterclockwise, bit
            1 set => damper open.""",
            name='nciSafetyPosn',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.direction.direction,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciTurnOffT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Turn-off delay.  The length of time that the load remains
            energized after a change from ON to OFF has been received.""",
            name='nciTurnOffT',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.offDely.offDely,
            maximum=b'\x00\x00\x11\x3b\x3b\x03\xe7',
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciZoneNum'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Zone number.  The zone number for the device.""",
            name='nciZoneNum',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.zoneNum.zoneNum,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciActuLabel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciActuLabel',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.actuatorType.actuatorType,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.installDate.installDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaintDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maintenance date.  The date of last maintenance for the
            device.""",
            name='nciMaintDate',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.maintDate.maintDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciManfDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciManfDate',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.manfDate.manfDate,
            flags=pylon.resources.base.PropertyFlags.MFG,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciOEMLable'] = pylon.resources.base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOEMLable',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.oemType.oemType,
            flags=pylon.resources.base.PropertyFlags.MFG,
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
        self._original_name = 'SFPTfireSmokeDamperActuator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = fireSmokeDamperActuator()
    pass
