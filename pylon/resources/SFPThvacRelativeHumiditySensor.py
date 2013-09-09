"""SFPThvacRelativeHumiditySensor standard profile, originally defined in
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
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTminDeltaRH import SCPTminDeltaRH
from pylon.resources.SCPToffsetRH import SCPToffsetRH
from pylon.resources.SNVT_lev_cont import SNVT_lev_cont
from pylon.resources.SNVT_lev_cont_f import SNVT_lev_cont_f
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime


class SFPThvacRelativeHumiditySensor(base.Profile):
    """SFPThvacRelativeHumiditySensor standard profile.  HVAC Relative
    Humidity Sensor.  Relative humidity sensor designed for HVAC
    applications."""

    def __init__(self):
        super().__init__(
            key=1050,
            scope=0,
            principal='nvoHVACRH'
        )
        self.datapoints['nvoHVACRH'] = base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using the
            level-percent data type.""",
            name='nvoHVACRH',
            profile=self,
            number=1,
            datatype=SNVT_lev_percent,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciRHMinDelta':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciRHMinDelta',
                    profile=self,
                    number=3,
                    datatype=SCPTminDeltaRH,
                    mandatory=True
                ),
                'nciRHOffset':
                base.Profile.PropertyMember(
                    doc="""Relative humidity offset.  Used to calibrate
                    external hardware with additive offset after
                    transformation.""",
                    name='nciRHOffset',
                    profile=self,
                    number=4,
                    datatype=SCPToffsetRH,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvo8bitRH'] = base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using the short
            fixed point data type.""",
            name='nvo8bitRH',
            profile=self,
            number=2,
            datatype=SNVT_lev_cont,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFloatRH'] = base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using floating
            point data type.""",
            name='nvoFloatRH',
            profile=self,
            number=3,
            datatype=SNVT_lev_cont_f,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  Controls the maximum period of time
            before the output values are transmitted.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x0b\xb8',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  Controls the minimum period of time
            between output value transmissions.""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=SCPTminSendTime,
            default=b'\x00\x32',
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPThvacRelativeHumiditySensor()
    pass
