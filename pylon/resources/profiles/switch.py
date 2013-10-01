"""switch standard profile, originally defined in resource file set standard
00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.setting
import pylon.resources.properties.location
import pylon.resources.properties.minSendTime
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.stepValue
import pylon.resources.properties.maxOut


class switch(pylon.resources.base.Profile):
    """switch standard profile.  Switch Used for all type of switches, with
    or without specific hardware."""

    def __init__(self):
        super().__init__(
            key=3200,
            scope=0,
            principal='nvoSwitch'
        )
        self.datapoints['nvoSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Switch output value.  """,
            name='nvoSwitch',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSwitchFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Switch feedback value.  """,
            name='nviSwitchFb',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setting output value.  """,
            name='nvoSetting',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
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
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum period between output NV
            transmissions (maximum transmission rate)""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            minimum=b'\x00\x01',
            maximum=b'\x00\x14',
            default=b'\x00\x01',
            mandatory=False
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat.  Maximum period of time that expires
            before the object automatically transmits the present value of
            the lux level output NV.""",
            name='nciMaxSendTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            mandatory=False
        )
        self.properties['nciStepValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Ramp step value.  When up/down pushbuttons are used, this
            parameter can be used to adjust the total ramp time from 0 to
            100%.""",
            name='nciStepValue',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.stepValue.stepValue,
            mandatory=False
        )
        self.properties['nciMaxOut'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum output value.  Used to limit the maximum value of
            the Switch output.""",
            name='nciMaxOut',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.maxOut.maxOut,
            minimum=b'\x00',
            maximum=b'\xc8',
            default=b'\xc8',
            mandatory=False
        )
        self._original_name = 'SFPTswitch'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = switch()
    pass
