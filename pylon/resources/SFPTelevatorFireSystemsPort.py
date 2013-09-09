"""SFPTelevatorFireSystemsPort standard profile, originally defined in
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
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTzoneNum import SCPTzoneNum


class SFPTelevatorFireSystemsPort(base.Profile):
    """SFPTelevatorFireSystemsPort standard profile.  Elevator/Lift
    Fire-Systems Port.  Input for elevator/lift cars to accept fire-signal
    information from fire control panels."""

    def __init__(self):
        super().__init__(
            key=14041,
            scope=0
        )
        self.datapoints['nviCommonAlarm'] = base.Profile.DatapointMember(
            doc="""Primary fire-sensor input.  Master fire signal to the
            elevator group controller.""",
            name='nviCommonAlarm',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviLobbyAlarm'] = base.Profile.DatapointMember(
            doc="""Fire-in-lobby sensor.  Reports fire in lobby, so alternate
            elevator action can be taken.""",
            name='nviLobbyAlarm',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMachRoomSmoke'] = base.Profile.DatapointMember(
            doc="""Machine-room smoke sensor.  Indicates smoke or fire in the
            elevator machine room.""",
            name='nviMachRoomSmoke',
            profile=self,
            number=3,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOption1'] = base.Profile.DatapointMember(
            doc="""Optional sensor 1.  Optional input for
            installation/manufacturer-specific fire/smoke alarming
            connections.""",
            name='nviOption1',
            profile=self,
            number=4,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOption2'] = base.Profile.DatapointMember(
            doc="""Optional sensor 2.  Optional input for
            installation/manufacturer-specific fire/smoke alarming
            connections.""",
            name='nviOption2',
            profile=self,
            number=5,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoTrouble'] = base.Profile.DatapointMember(
            doc="""Elevator is unable to respond to fire sensors.  value>0
            and state=1 indicates trouble.""",
            name='nvoTrouble',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciTroubleHrtbt':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciTroubleHrtbt',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.properties['nciReceiveHrtbt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciReceiveHrtbt',
            profile=self,
            number=1,
            datatype=SCPTmaxRcvTime,
            maximum=b'\x8c\xa0',
            mandatory=True
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=2,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=3,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=4,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciZoneNumber'] = base.Profile.PropertyMember(
            doc="""Zone Number is for use by Fire System.  The zone number
            for the device.""",
            name='nciZoneNumber',
            profile=self,
            number=6,
            datatype=SCPTzoneNum,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTelevatorFireSystemsPort()
    pass
