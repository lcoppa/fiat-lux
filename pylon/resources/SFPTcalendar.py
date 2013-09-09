"""SFPTcalendar standard profile, originally defined in resource file set
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_date_event import SNVT_date_event
from pylon.resources.SCPTovrBehave import SCPTovrBehave
from pylon.resources.SCPTovrValue import SCPTovrValue
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTeffectivePeriod import SCPTeffectivePeriod
from pylon.resources.SCPTscheduleDates import SCPTscheduleDates
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTscheduleName import SCPTscheduleName


class SFPTcalendar(base.Profile):
    """SFPTcalendar standard profile.  Calendar Standardized interface for
    identifying active and inactive schedules based on dates.  Schedules may
    become active on a particular date, on a range of dates, or on a
    repeating interval."""

    def __init__(self):
        super().__init__(
            key=6,
            scope=0
        )
        self.datapoints['nvoDateEvent'] = base.Profile.DatapointMember(
            doc="""Date event.  Reports the status of a schedule.""",
            name='nvoDateEvent',
            profile=self,
            number=1,
            datatype=SNVT_date_event,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpOvrBehavior':
                base.Profile.PropertyMember(
                    doc="""Override behavior.  Behavior of the nvoDateEvent
                    output when an override request is received for the
                    calendar.""",
                    name='cpOvrBehavior',
                    profile=self,
                    number=5,
                    datatype=SCPTovrBehave,
                    mandatory=False
                ),
                'cpOvrValue':
                base.Profile.PropertyMember(
                    doc="""Override value.  The value the nvoDateEvent output
                    should adopt when it is overridden and the value of
                    Override Behavior is OV_SPECIFIED.""",
                    name='cpOvrValue',
                    profile=self,
                    number=6,
                    datatype=SCPTovrValue,
                    default=b'\xff\xff\xff\xff',
                    mandatory=False
                ),
                'cpMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  Minimum period of time between
                    automatic transmissions of the nvoDateEvent output.  This
                    throttles the series of outputs that occur whenever
                    schedules are updated via nvoDateEvent.""",
                    name='cpMinSendTime',
                    profile=self,
                    number=8,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x02',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviDateResynch'] = base.Profile.DatapointMember(
            doc="""Resynchronization request.  Requests an update on the
            status of all defined schedules.""",
            name='nviDateResynch',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['cpEffPeriod'] = base.Profile.PropertyMember(
            doc="""Effective period.  Time period during which the calendar
            is effective.""",
            name='cpEffPeriod',
            profile=self,
            number=1,
            datatype=SCPTeffectivePeriod,
            flags=base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['cpSchedDates'] = base.Profile.PropertyMember(
            doc="""Schedule dates.  A range of dates with an optional
            qualifier that specifies when a schedule is active.""",
            name='cpSchedDates',
            profile=self,
            number=2,
            datatype=SCPTscheduleDates,
            array_size_min=2,
            array_size_max=65535,
            flags=base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['cpObjMajVersion'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVersion',
            profile=self,
            number=3,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpObjMinVersion'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVersion',
            profile=self,
            number=4,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpSchedName'] = base.Profile.PropertyMember(
            doc="""Schedule name.  Array of schedule names.""",
            name='cpSchedName',
            profile=self,
            number=7,
            datatype=SCPTscheduleName,
            array_size_min=2,
            array_size_max=255,
            flags=base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTcalendar()
    pass
