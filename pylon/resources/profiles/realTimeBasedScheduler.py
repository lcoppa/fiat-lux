"""realTimeBasedScheduler standard profile, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.scene
import pylon.resources.datapoints.setting
import pylon.resources.properties.modeHrtBt
import pylon.resources.properties.timeEvent
import pylon.resources.properties.dayDateIndex
import pylon.resources.properties.defWeekMask


class realTimeBasedScheduler(pylon.resources.base.Profile):
    """realTimeBasedScheduler standard profile.  Real-Time-Based Scheduler.
    Sends events over the network that are based on real time."""

    def __init__(self):
        super().__init__(
            key=3301,
            scope=0
        )
        self.datapoints['nvoScene'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Time event output.  Provides a time- and date-related
            event for the controller.""",
            name='nvoScene',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Mode output.  Provides real-time-related operational-mode
            information for the controller.""",
            name='nvoSetting',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciModeHeartBeat':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Heart beat, mode output.  The time that must pass
                    without an update for mode definitions to be
                    automatically retransmitted, zero disables.""",
                    name='nciModeHeartBeat',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.modeHrtBt.modeHrtBt,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciTimeEvent'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Time event entry.  Event or mode definitions to be
            transmitted if the time in the record is reached.""",
            name='nciTimeEvent',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.timeEvent.timeEvent,
            array_size_min=2,
            array_size_max=65535,
            mandatory=True
        )
        self.properties['nciDayDateIndex'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Day date index.  One or two dates for matching with a
            start index to the time-event array.""",
            name='nciDayDateIndex',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.dayDateIndex.dayDateIndex,
            array_size_min=2,
            array_size_max=65535,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciDefWeekMask'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Definition week mask.  Day type definition for every day
            of the week.""",
            name='nciDefWeekMask',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.defWeekMask.defWeekMask,
            mandatory=True
        )
        self._original_name = 'SFPTrealTimeBasedScheduler'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = realTimeBasedScheduler()
    pass
