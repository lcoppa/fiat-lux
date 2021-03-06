"""railcarAudioSensor standard profile, originally defined in resource file
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
import pylon.resources.datapoints.rac_ctrl
import pylon.resources.datapoints.rac_req
import pylon.resources.properties.location
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class railcarAudioSensor(pylon.resources.base.Profile):
    """railcarAudioSensor standard profile.  Railcar Audio Sensor.  Used to
    interface to Railcar Audio Controllers to allow use of different audio
    sources (defined by the Sensors) to be sent to different parts of a
    railcar."""

    def __init__(self):
        super().__init__(
            key=9112,
            scope=0
        )
        self.datapoints['nviAudCntCmdCar'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Audio Control Command from a Car.  This network variable
            receives audio command from Audio Controller Object
            (nvoAudioCntCmdCar), and uses it for internal set-up.""",
            name='nviAudCntCmdCar',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.rac_ctrl.rac_ctrl,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAudReq'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Audio Request Output.  This network variable is the audio
            request output which is sent to the Audio Controller Object in
            the car.""",
            name='nvoAudReq',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.rac_req.rac_req,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTrailcarAudioSensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = railcarAudioSensor()
    pass
