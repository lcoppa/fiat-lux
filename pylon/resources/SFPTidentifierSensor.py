"""SFPTidentifierSensor standard profile, originally defined in resource file
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
from pylon.resources.SNVT_magcard import SNVT_magcard
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg


class SFPTidentifierSensor(base.Profile):
    """SFPTidentifierSensor standard profile.  Identifier Sensor.  An
    Identifier Sensor can be any kind of device used to identify a person who
    wants to access a controlled point/area."""

    def __init__(self):
        super().__init__(
            key=5035,
            scope=0
        )
        self.datapoints['nvoId'] = base.Profile.DatapointMember(
            doc="""ISO 7811.  This data item contains data according to the
            ISO 7811 standard for card stripes.""",
            name='nvoId',
            profile=self,
            number=1,
            datatype=SNVT_magcard,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Send heartbeat.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
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
            number=2,
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
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciNetworkConfig'] = base.Profile.PropertyMember(
            doc="""Network configuration source.  The value of this field
            determines the source of the node's network configuration.""",
            name='nciNetworkConfig',
            profile=self,
            number=5,
            datatype=SCPTnwrkCnfg,
            flags=base.PropertyFlags.RESET,
            default=b'\x01',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTidentifierSensor()
    pass
