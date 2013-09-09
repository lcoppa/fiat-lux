"""SFPTpressureSensor standard profile, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_press import SNVT_press
from pylon.resources.SCPToffset import SCPToffset
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTsndDelta import SCPTsndDelta
from pylon.resources.SNVT_press_p import SNVT_press_p
from pylon.resources.SNVT_press_f import SNVT_press_f
from pylon.resources.SCPTlocation import SCPTlocation


class SFPTpressureSensor(base.Profile):
    """SFPTpressureSensor standard profile.  Pressure Sensor.  Used to
    acquire pressure readings and report them over the network."""

    def __init__(self):
        super().__init__(
            key=1030,
            scope=0,
            principal='nvoPress'
        )
        self.datapoints['nvoPress'] = base.Profile.DatapointMember(
            doc="""Standard Pressure Output.  This output variable reports
            the pressure of the sensor using the Kilo Pascal pressure
            SNVT_press.""",
            name='nvoPress',
            profile=self,
            number=1,
            datatype=SNVT_press,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciPressOffset1':
                base.Profile.PropertyMember(
                    doc="""Generic offset.  Used to calibrate the level that
                    the associated output network variable should adopt after
                    any translation table or gain factor.""",
                    name='nciPressOffset1',
                    profile=self,
                    number=4,
                    datatype=SCPToffset,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'nciMaxSendTimeNV01':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV01',
                    profile=self,
                    number=8,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV01':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV01',
                    profile=self,
                    number=11,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinDeltaNV01':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciMinDeltaNV01',
                    profile=self,
                    number=14,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPrecisePress'] = base.Profile.DatapointMember(
            doc="""High Precision Pressure Output.  This output variable
            reports the pressure of the sensor using the high precision
            pressure SNVT_press_p.""",
            name='nvoPrecisePress',
            profile=self,
            number=2,
            datatype=SNVT_press_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciPressOffset2':
                base.Profile.PropertyMember(
                    doc="""Generic offset.  Used to calibrate the level that
                    the associated output network variable should adopt after
                    any translation table or gain factor.""",
                    name='nciPressOffset2',
                    profile=self,
                    number=5,
                    datatype=SCPToffset,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'nciMaxSendTimeNV02':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV02',
                    profile=self,
                    number=9,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV02':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV02',
                    profile=self,
                    number=12,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinDeltaNV02':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciMinDeltaNV02',
                    profile=self,
                    number=15,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFloatPress'] = base.Profile.DatapointMember(
            doc="""Floating Point Pressure Output.  This output variable
            reports the pressure of the sensor using the Floating point
            pressure SNVT.""",
            name='nvoFloatPress',
            profile=self,
            number=3,
            datatype=SNVT_press_f,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciPressOffset3':
                base.Profile.PropertyMember(
                    doc="""Generic offset.  Used to calibrate the level that
                    the associated output network variable should adopt after
                    any translation table or gain factor.""",
                    name='nciPressOffset3',
                    profile=self,
                    number=6,
                    datatype=SCPToffset,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'nciMaxSendTimeNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=10,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV03':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV03',
                    profile=self,
                    number=13,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinDeltaNV03':
                base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciMinDeltaNV03',
                    profile=self,
                    number=16,
                    datatype=SCPTsndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinDelta'] = base.Profile.PropertyMember(
            doc="""Send on delta.  The minimum change required to force
            transmission of the output value.""",
            name='nciMinDelta',
            profile=self,
            number=3,
            datatype=SCPTsndDelta,
            default=b'\x00\x00\x00\x00',
            mandatory=True
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
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTpressureSensor()
    pass
