"""calendar standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.date_event
import pylon.resources.properties.ovrBehave
import pylon.resources.properties.ovrValue
import pylon.resources.properties.minSendTime
import pylon.resources.datapoints.switch
import pylon.resources.properties.effectivePeriod
import pylon.resources.properties.scheduleDates
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.scheduleName


class calendar(pylon.resources.base.Profile):
    """calendar standard profile.  Calendar Standardized interface for
    identifying active and inactive schedules based on dates.  Schedules may
    become active on a particular date, on a range of dates, or on a
    repeating interval."""

    def __init__(self):
        super().__init__(
            key=6,
            scope=0
        )
        self.datapoints['nvoDateEvent'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Date event.  Reports the status of a schedule.""",
            name='nvoDateEvent',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.date_event.date_event,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpOvrBehavior':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Override behavior.  Behavior of the nvoDateEvent
                    output when an override request is received for the
                    calendar.""",
                    name='cpOvrBehavior',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.ovrBehave.ovrBehave,
                    mandatory=False
                ),
                'cpOvrValue':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Override value.  The value the nvoDateEvent output
                    should adopt when it is overridden and the value of
                    Override Behavior is OV_SPECIFIED.""",
                    name='cpOvrValue',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.ovrValue.ovrValue,
                    default=b'\xff\xff\xff\xff',
                    mandatory=False
                ),
                'cpMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  Minimum period of time between
                    automatic transmissions of the nvoDateEvent output.  This
                    throttles the series of outputs that occur whenever
                    schedules are updated via nvoDateEvent.""",
                    name='cpMinSendTime',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x02',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviDateResynch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Resynchronization request.  Requests an update on the
            status of all defined schedules.""",
            name='nviDateResynch',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['cpEffPeriod'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Effective period.  Time period during which the calendar
            is effective.""",
            name='cpEffPeriod',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.effectivePeriod.effectivePeriod,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['cpSchedDates'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Schedule dates.  A range of dates with an optional
            qualifier that specifies when a schedule is active.""",
            name='cpSchedDates',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.scheduleDates.scheduleDates,
            array_size_min=2,
            array_size_max=65535,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['cpObjMajVersion'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVersion',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpObjMinVersion'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVersion',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpSchedName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Schedule name.  Array of schedule names.""",
            name='cpSchedName',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.scheduleName.scheduleName,
            array_size_min=2,
            array_size_max=255,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self._original_name = 'SFPTcalendar'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = calendar()
    pass
