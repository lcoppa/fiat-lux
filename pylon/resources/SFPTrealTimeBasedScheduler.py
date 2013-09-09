"""SFPTrealTimeBasedScheduler standard profile, originally defined in
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
from pylon.resources.SNVT_scene import SNVT_scene
from pylon.resources.SNVT_setting import SNVT_setting
from pylon.resources.SCPTmodeHrtBt import SCPTmodeHrtBt
from pylon.resources.SCPTtimeEvent import SCPTtimeEvent
from pylon.resources.SCPTdayDateIndex import SCPTdayDateIndex
from pylon.resources.SCPTdefWeekMask import SCPTdefWeekMask


class SFPTrealTimeBasedScheduler(base.Profile):
    """SFPTrealTimeBasedScheduler standard profile.  Real-Time-Based
    Scheduler.  Sends events over the network that are based on real time."""

    def __init__(self):
        super().__init__(
            key=3301,
            scope=0
        )
        self.datapoints['nvoScene'] = base.Profile.DatapointMember(
            doc="""Time event output.  Provides a time- and date-related
            event for the controller.""",
            name='nvoScene',
            profile=self,
            number=1,
            datatype=SNVT_scene,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetting'] = base.Profile.DatapointMember(
            doc="""Mode output.  Provides real-time-related operational-mode
            information for the controller.""",
            name='nvoSetting',
            profile=self,
            number=2,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciModeHeartBeat':
                base.Profile.PropertyMember(
                    doc="""Heart beat, mode output.  The time that must pass
                    without an update for mode definitions to be
                    automatically retransmitted, zero disables.""",
                    name='nciModeHeartBeat',
                    profile=self,
                    number=4,
                    datatype=SCPTmodeHrtBt,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciTimeEvent'] = base.Profile.PropertyMember(
            doc="""Time event entry.  Event or mode definitions to be
            transmitted if the time in the record is reached.""",
            name='nciTimeEvent',
            profile=self,
            number=1,
            datatype=SCPTtimeEvent,
            array_size_min=2,
            array_size_max=65535,
            mandatory=True
        )
        self.properties['nciDayDateIndex'] = base.Profile.PropertyMember(
            doc="""Day date index.  One or two dates for matching with a
            start index to the time-event array.""",
            name='nciDayDateIndex',
            profile=self,
            number=2,
            datatype=SCPTdayDateIndex,
            array_size_min=2,
            array_size_max=65535,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciDefWeekMask'] = base.Profile.PropertyMember(
            doc="""Definition week mask.  Day type definition for every day
            of the week.""",
            name='nciDefWeekMask',
            profile=self,
            number=3,
            datatype=SCPTdefWeekMask,
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTrealTimeBasedScheduler()
    pass
