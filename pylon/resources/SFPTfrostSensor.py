"""SFPTfrostSensor standard profile, originally defined in resource file set
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime


class SFPTfrostSensor(base.Profile):
    """SFPTfrostSensor standard profile.  Frost Sensor.  Used to detect the
    presence of frost."""

    def __init__(self):
        super().__init__(
            key=1042,
            scope=0
        )
        self.datapoints['nvoFrost'] = base.Profile.DatapointMember(
            doc="""Frost Data.  This output network variable provides the
            state of the frost detector.""",
            name='nvoFrost',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTFrost':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTFrost',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTFrost':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTFrost',
                    profile=self,
                    number=4,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTfrostSensor()
    pass
