"""SFPTrailcarAudioController standard profile, originally defined in
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
from pylon.resources.SNVT_rac_req import SNVT_rac_req
from pylon.resources.SNVT_rac_ctrl import SNVT_rac_ctrl
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer


class SFPTrailcarAudioController(base.Profile):
    """SFPTrailcarAudioController standard profile.  Railcar Audio
    Controller.  Used to interface to Railcar Audio Sensors to allow use of
    different audio sources to be sent to different parts of a railcar."""

    def __init__(self):
        super().__init__(
            key=9111,
            scope=0
        )
        self.datapoints['nviAudReq'] = base.Profile.DatapointMember(
            doc="""Audio Request Input.  This network variable is the audio
            request received from the Audio Sensor Object in the car.""",
            name='nviAudReq',
            profile=self,
            number=1,
            datatype=SNVT_rac_req,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAudCntCmdReq'] = base.Profile.DatapointMember(
            doc="""Audio Control Command Request Output.  This network
            variable is the audio control command sent to the Audio
            Controller Object in the system.""",
            name='nvoAudCntCmdReq',
            profile=self,
            number=2,
            datatype=SNVT_rac_ctrl,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV2':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV2',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV2':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV2',
                    profile=self,
                    number=4,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviAudCntCmdReq'] = base.Profile.DatapointMember(
            doc="""Audio Control Command Request Input.  These network
            variables are the audio control commands received from other
            Audio Controller Objects in the system.""",
            name='nviAudCntCmdReq',
            profile=self,
            number=3,
            datatype=SNVT_rac_ctrl,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAudCntCmdCont'] = base.Profile.DatapointMember(
            doc="""Audio Control Command from this Controller.  This network
            variable is the audio control command sent to the Audio
            Controller Object in the system.""",
            name='nvoAudCntCmdCont',
            profile=self,
            number=4,
            datatype=SNVT_rac_ctrl,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV4':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV4',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV4':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV4',
                    profile=self,
                    number=5,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviAudCntCmdCont'] = base.Profile.DatapointMember(
            doc="""Audio Control Command from another Controller.  These
            network variables are the audio control commands received from
            other Audio Controller Objects in the system.""",
            name='nviAudCntCmdCont',
            profile=self,
            number=5,
            datatype=SNVT_rac_ctrl,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAudCntCmdCar'] = base.Profile.DatapointMember(
            doc="""Audio Control Command to a Car.  This network variable is
            the audio control command sent to the Audio Sensor functional
            block (nviAudioCntCmdCar) of the audio unit.""",
            name='nvoAudCntCmdCar',
            profile=self,
            number=6,
            datatype=SNVT_rac_ctrl,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV6':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV6',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV6':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV6',
                    profile=self,
                    number=6,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=7,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=8,
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
            number=9,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTrailcarAudioController()
    pass
