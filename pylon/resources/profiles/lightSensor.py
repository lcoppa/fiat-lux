"""lightSensor standard profile, originally defined in resource file set
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.lux
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minDeltaLevel
import pylon.resources.properties.location
import pylon.resources.properties.reflection
import pylon.resources.properties.fieldCalib


class lightSensor(pylon.resources.base.Profile):
    """lightSensor standard profile.  Light Sensor.  Used within devices that
    can measure ambient light levels."""

    def __init__(self):
        super().__init__(
            key=1010,
            scope=0,
            principal='nvoLuxLevel'
        )
        self.datapoints['nvoLuxLevel'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Light level output.  Monitors the value of the hardware
            input.""",
            name='nvoLuxLevel',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lux.lux,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendT':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  Minimum period between output
                    NV transmissions (maximum transmission rate)""",
                    name='nciMinSendT',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x0a',
                    mandatory=False
                ),
                'nciMaxSendT':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send heartbeat.  Maximum period of time that
                    expires before the object automatically transmits the
                    present value of the lux level output NV.""",
                    name='nciMaxSendT',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x02\x58',
                    mandatory=False
                ),
                'nciMinDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum change before output.  Used to control the
                    % amount by which the value must change before lux level
                    output NV is transmitted.""",
                    name='nciMinDelta',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.minDeltaLevel.minDeltaLevel,
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciReflection'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Reflection factor.  Adjusts the internal gain factor for
            the measured illumination level.""",
            name='nciReflection',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.reflection.reflection,
            mandatory=False
        )
        self.properties['nciFieldCalibr'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Ambient lux value for self-calibration.  Used by the light
            sensor to self-calibrate the hardware.""",
            name='nciFieldCalibr',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.fieldCalib.fieldCalib,
            mandatory=False
        )
        self._original_name = 'SFPTlightSensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = lightSensor()
    pass
