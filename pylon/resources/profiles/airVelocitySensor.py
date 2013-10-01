"""airVelocitySensor standard profile, originally defined in resource file
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
import pylon.resources.datapoints.speed_mil
import pylon.resources.properties.ductArea
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.sndDelta
import pylon.resources.datapoints.flow
import pylon.resources.datapoints.flow_f
import pylon.resources.properties.offset
import pylon.resources.properties.gain


class airVelocitySensor(pylon.resources.base.Profile):
    """airVelocitySensor standard profile.  Air-Velocity Sensor.  Used to
    measure the speed of a gas, typically for HVAC applications."""

    def __init__(self):
        super().__init__(
            key=1083,
            scope=0,
            principal='nvoAirVelocity'
        )
        self.datapoints['nvoAirVelocity'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Air Velocity.  This output network variable reports the
            velocity detected by the sensor.""",
            name='nvoAirVelocity',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.speed_mil.speed_mil,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciDuctAreaNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Duct area or size.  The duct area used to
                    calculate the air flow, relevant only for VAV actuators /
                    controllers.""",
                    name='nciDuctAreaNV01',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.ductArea.ductArea,
                    default=b'\xff\xff',
                    mandatory=False
                ),
                'nciMaxSendTimeNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV01',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV01',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciSendOnDeltaNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciSendOnDeltaNV01',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAirFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Duct Flow Rate.  This output network variable provides the
            flow volume flowing through the duct.""",
            name='nvoAirFlow',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.flow.flow,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciDuctAreaNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Duct area or size.  The duct area used to
                    calculate the air flow, relevant only for VAV actuators /
                    controllers.""",
                    name='nciDuctAreaNV02',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.ductArea.ductArea,
                    default=b'\xff\xff',
                    mandatory=False
                ),
                'nciMaxSendTimeNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV02',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV02',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciSendOnDeltaNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciSendOnDeltaNV02',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAirFlowFloat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Flow Rate.  This output network variable provides the flow
            volume flowing through the duct.""",
            name='nvoAirFlowFloat',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.flow_f.flow_f,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV03',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciSendOnDeltaNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciSendOnDeltaNV03',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciSendOnDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send on delta.  The minimum change required to force
            transmission of the output value.""",
            name='nciSendOnDelta',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.sndDelta.sndDelta,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciVelocityOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Generic offset.  Used to calibrate the level that the
            associated output network variable should adopt after any
            translation table or gain factor.""",
            name='nciVelocityOffset',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.offset.offset,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciVelocityGain'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Gain This parameter is used to calibrate the external
            hardware.""",
            name='nciVelocityGain',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.gain.gain,
            default=b'\x00\x01\x00\x01',
            mandatory=False
        )
        self.properties['nciDuctArea'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Duct area or size.  The duct area used to calculate the
            air flow, relevant only for VAV actuators / controllers.""",
            name='nciDuctArea',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.ductArea.ductArea,
            default=b'\xff\xff',
            mandatory=False
        )
        self._original_name = 'SFPTairVelocitySensor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = airVelocitySensor()
    pass
