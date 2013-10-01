"""globalSolarRadiation standard profile, originally defined in resource file
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
import pylon.resources.datapoints.Wm2_p
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.sndDelta
import pylon.resources.properties.offset
import pylon.resources.properties.gain


class globalSolarRadiation(pylon.resources.base.Profile):
    """globalSolarRadiation standard profile.  Global Solar Radiation sensor
    object.  Typically Global Solar Radiation sensor object output is
    connected to the input of a controller.  The Global Solar Radiation value
    can e.g.  be used to estimate the energy input into a building by the
    sun."""

    def __init__(self):
        super().__init__(
            key=1015,
            scope=0
        )
        self.datapoints['nvoGlobalRad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Watts per square meter.  This output network variable
            reports the Solar Global Radiation with W/m2.""",
            name='nvoGlobalRad',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.Wm2_p.Wm2_p,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMinSendTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x32',
                    mandatory=True
                ),
                'cpMinDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='cpMinDelta',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x03',
                    mandatory=True
                ),
                'cpRadiationOffset':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Generic offset.  Used to calibrate the level that
                    the associated output network variable should adopt after
                    any translation table or gain factor.""",
                    name='cpRadiationOffset',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.offset.offset,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpRadiationGain':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Gain This parameter is used to calibrate the
                    external hardware.""",
                    name='cpRadiationGain',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.gain.gain,
                    default=b'\x00\x01\x00\x01',
                    mandatory=False
                )
            }
        )
        self._original_name = 'SFPTglobalSolarRadiation'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = globalSolarRadiation()
    pass
