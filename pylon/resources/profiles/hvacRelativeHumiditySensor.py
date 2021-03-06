"""hvacRelativeHumiditySensor standard profile, originally defined in
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.minDeltaRH
import pylon.resources.properties.offsetRH
import pylon.resources.datapoints.lev_cont
import pylon.resources.datapoints.lev_cont_f
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime


class hvacRelativeHumiditySensor(pylon.resources.base.Profile):
    """hvacRelativeHumiditySensor standard profile.  HVAC Relative Humidity
    Sensor.  Relative humidity sensor designed for HVAC applications."""

    def __init__(self):
        super().__init__(
            key=1050,
            scope=0,
            principal='nvoHVACRH'
        )
        self.datapoints['nvoHVACRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using the
            level-percent data type.""",
            name='nvoHVACRH',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciRHMinDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciRHMinDelta',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.minDeltaRH.minDeltaRH,
                    mandatory=True
                ),
                'nciRHOffset':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Relative humidity offset.  Used to calibrate
                    external hardware with additive offset after
                    transformation.""",
                    name='nciRHOffset',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.offsetRH.offsetRH,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvo8bitRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using the short
            fixed point data type.""",
            name='nvo8bitRH',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFloatRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Relative humidity.  The relative humidity using floating
            point data type.""",
            name='nvoFloatRH',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_cont_f.lev_cont_f,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  Controls the maximum period of time
            before the output values are transmitted.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x0b\xb8',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Controls the minimum period of time
            between output value transmissions.""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x32',
            mandatory=True
        )
        self._original_name = 'SFPThvacRelativeHumiditySensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = hvacRelativeHumiditySensor()
    pass
