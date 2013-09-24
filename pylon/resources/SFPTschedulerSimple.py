"""SFPTschedulerSimple standard profile, originally defined in resource file
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_time_offset import SNVT_time_offset
from pylon.resources.SNVT_tod_event import SNVT_tod_event
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_sched_val import SNVT_sched_val
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_sched_status import SNVT_sched_status
from pylon.resources.SCPTscheduleSunday import SCPTscheduleSunday
from pylon.resources.SCPTscheduleMonday import SCPTscheduleMonday
from pylon.resources.SCPTscheduleTuesday import SCPTscheduleTuesday
from pylon.resources.SCPTscheduleWednesday import SCPTscheduleWednesday
from pylon.resources.SCPTscheduleThursday import SCPTscheduleThursday
from pylon.resources.SCPTscheduleFriday import SCPTscheduleFriday
from pylon.resources.SCPTscheduleSaturday import SCPTscheduleSaturday
from pylon.resources.SCPToccupancyBehavior import SCPToccupancyBehavior
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTscheduleException import SCPTscheduleException
from pylon.resources.SCPTscheduleHoliday import SCPTscheduleHoliday
from pylon.resources.SCPTrandomizationInterval import SCPTrandomizationInterval
from pylon.resources.SCPTsunriseTime import SCPTsunriseTime
from pylon.resources.SCPTsunsetTime import SCPTsunsetTime
from pylon.resources.SCPTschedulerOptions import SCPTschedulerOptions
from pylon.resources.SCPToccupancyThresholds import SCPToccupancyThresholds


class SFPTschedulerSimple(base.Profile):
    """SFPTschedulerSimple standard profile.  """

    def __init__(self):
        super().__init__(
            key=17,
            scope=0,
            principal='nvoOccPri'
        )
        self.datapoints['nviStartOffset'] = base.Profile.DatapointMember(
            doc="""Start time offset.  Offset value applied to a scheduled
            start time for any scheduled Occupied event.  The value may be
            generated by another functional block such as an optimal
            start-stop functional block.  The value can be used to offset a
            scheduled start time to implement an optimal start or optimal
            stop algorithm, or to stagger start times to minimize demand
            spikes.""",
            name='nviStartOffset',
            profile=self,
            number=1,
            datatype=SNVT_time_offset,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviStopOffset'] = base.Profile.DatapointMember(
            doc="""Stop time offset.  Offset value applied to a scheduled
            stop time for any scheduled Unccupied event.  The value may be
            generated by another functional block such as an optimal
            start-stop functional block.  The valuet can be used to offset a
            scheduled stop time to implement an optimal stop algorithm, or to
            stagger stop times to minimize demand spikes.""",
            name='nviStopOffset',
            profile=self,
            number=2,
            datatype=SNVT_time_offset,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviManualOvr'] = base.Profile.DatapointMember(
            doc="""Manual schedule override.  Highest priority override--this
            input overrides the daily schedule, the Exception Override input,
            the Local Occupancy input, the Scheduled Exception Event input,
            and the Scheduled Vacation/Holiday Event input.  The Offset for
            Start and Offset for Stop values do not apply to this
            override.""",
            name='nviManualOvr',
            profile=self,
            number=3,
            datatype=SNVT_tod_event,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviExceptionOvr'] = base.Profile.DatapointMember(
            doc="""Exception schedule override.  Second highest priority
            override--does not override the Manual Override input.  This
            input overrides the daily schedule, the Local Occupancy input,
            the Scheduled Exception Event input, and the Scheduled
            Vacation/Holiday Event input.  The Offset for Start and Offset
            for Stop values do not apply to this override.""",
            name='nviExceptionOvr',
            profile=self,
            number=4,
            datatype=SNVT_tod_event,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccPriTOD'] = base.Profile.DatapointMember(
            doc="""Primary time-of-day occupancy.  Primary scheduled
            occupancy event, which includes current and next state values
            that are the result of the normal schedule overlaid with any
            exceptions and/or overrides;  and where the Local Occupancy
            input(s) is/are considered in the determination of the output
            value (in contrast to the Secondary Time-of-Day Occupancy, which
            does not consider Local Occupancy).""",
            name='nvoOccPriTOD',
            profile=self,
            number=5,
            datatype=SNVT_tod_event,
            mandatory=True,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOccSecTOD'] = base.Profile.DatapointMember(
            doc="""Secondary time-of-day occupancy.  Secondary scheduled
            occupancy event, which includes current and next state values
            that are the result of the normal schedule overlaid with any
            exceptions and/or overrides;  but where the Local Occupancy
            input(s) is/are excluded from consideration in the determination
            of the output value (in contrast to the Primary Time-of-Day
            Occupancy, which always considers Local Occupancy).""",
            name='nvoOccSecTOD',
            profile=self,
            number=6,
            datatype=SNVT_tod_event,
            mandatory=True,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOccPri'] = base.Profile.DatapointMember(
            doc="""Primary occupancy.  Primary scheduled occupancy value
            which is the result of the normal schedule overlaid with any
            exceptions and/or overrides;  and where the Local Occupancy
            input(s) is/are considered in the determination of the output
            value (in contrast to the Secondary Time-of-Day Occupancy, which
            does not consider Local Occupancy).  Matches the value of the
            nvoOccPriTOD current_state field.""",
            name='nvoOccPri',
            profile=self,
            number=7,
            datatype=SNVT_occupancy,
            mandatory=True,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOccSec'] = base.Profile.DatapointMember(
            doc="""Secondary occupancy.  Secondary scheduled occupancy value
            which is the result of the normal schedule overlaid with any
            exceptions and/or overrides;  but where the Local Occupancy
            input(s) is/are excluded from consideration in the determination
            of the output value (in contrast to the Primary Time-of-Day
            Occupancy, which always considers Local Occupancy).  Matches the
            value of the nvoOccSecTOD current_state field.""",
            name='nvoOccSec',
            profile=self,
            number=8,
            datatype=SNVT_occupancy,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSchedValue'] = base.Profile.DatapointMember(
            doc="""General-purpose scheduler output value.  Index from
            scheduler that selects entry in SCPTvalueDefinition array, or is
            a direct value output.""",
            name='nvoSchedValue',
            profile=self,
            number=11,
            datatype=SNVT_sched_val,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviLocalOcc'] = base.Profile.DatapointMember(
            doc="""Local occupancy.  Local occupancy from one or more
            occupancy sensors and occupancy sensor managers.  The Default
            Occupancy Behavior CP determines the functional block response to
            this input.  This input is the third highest prioirty override
            after the Manual Override and Exception Override inputs.  It
            overrides the daily schedule, the Scheduled Exception Event
            input, and the Scheduled Vacation/Holiday Event input.  The
            functional block must manage inputs from up to 50 devices
            reporting occupancy or bypass, tracking the time since last
            occupancy or bypass report of each device by source address;  a
            device is dropped from the active list if it reports an
            unoccupied, standby, or invalid value, or if there is no update
            from the device in the time interval specified by the Occupancy
            Maximum Receive Time CP.  If 50 devices are reporting occupied or
            bypass status and an occupied or bypass input is received from a
            device that is not on the list, the oldest device on the list is
            dropped and the new device is added.""",
            name='nviLocalOcc',
            profile=self,
            number=9,
            datatype=SNVT_occupancy,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'cpOccTimeout':
                base.Profile.PropertyMember(
                    doc="""Occupancy maximum receive time.  The maximum
                    period of time that may expire with no updates from an
                    individual source address that reported occupancy before
                    the value is assumed to be unoccupied.  A zero value
                    disables occupancy fan-in.""",
                    name='cpOccTimeout',
                    profile=self,
                    number=20,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoSchedStat'] = base.Profile.DatapointMember(
            doc="""Scheduler status.  Type of schedule that is active.""",
            name='nvoSchedStat',
            profile=self,
            number=10,
            datatype=SNVT_sched_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpScheduleSunday'] = base.Profile.PropertyMember(
            doc="""Sunday schedule.  A structure containing an array of seven
            time-value pairs that specify the daily schedule for Sunday;
            unused time-value pairs have an invalid value (31) for the hour;
            if two time-value pairs specify the same time, the first with a
            valid output value is used.""",
            name='cpScheduleSunday',
            profile=self,
            number=7,
            datatype=SCPTscheduleSunday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleMonday'] = base.Profile.PropertyMember(
            doc="""Monday schedule.  A structure containing an array of seven
            time-value pairs that specify the daily schedule for Monday;
            unused time-value pairs have an invalid value (31) for the hour;
            if two time-value pairs specify the same time, the first with a
            valid output value is used.""",
            name='cpScheduleMonday',
            profile=self,
            number=1,
            datatype=SCPTscheduleMonday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleTuesday'] = base.Profile.PropertyMember(
            doc="""Tuesday schedule.  A structure containing an array of
            seven time-value pairs that specify the daily schedule for
            Tuesday;  unused time-value pairs have an invalid value (31) for
            the hour;  if two time-value pairs specify the same time, the
            first with a valid output value is used.""",
            name='cpScheduleTuesday',
            profile=self,
            number=2,
            datatype=SCPTscheduleTuesday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleWednesday'] = base.Profile.PropertyMember(
            doc="""Wednesday schedule.  A structure containing an array of
            seven time-value pairs that specify the daily schedule for
            Wednesday;  unused time-value pairs have an invalid value (31)
            for the hour;  if two time-value pairs specify the same time, the
            first with a valid output value is used.""",
            name='cpScheduleWednesday',
            profile=self,
            number=3,
            datatype=SCPTscheduleWednesday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleThursday'] = base.Profile.PropertyMember(
            doc="""Thursday schedule.  A structure containing an array of
            seven time-value pairs that specify the daily schedule for
            Thursday;  unused time-value pairs have an invalid value (31) for
            the hour;  if two time-value pairs specify the same time, the
            first with a valid output value is used.""",
            name='cpScheduleThursday',
            profile=self,
            number=4,
            datatype=SCPTscheduleThursday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleFriday'] = base.Profile.PropertyMember(
            doc="""Friday schedule.  A structure containing an array of seven
            time-value pairs that specify the daily schedule for Friday;
            unused time-value pairs have an invalid value (31) for the hour;
            if two time-value pairs specify the same time, the first with a
            valid output value is used.""",
            name='cpScheduleFriday',
            profile=self,
            number=5,
            datatype=SCPTscheduleFriday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleSaturday'] = base.Profile.PropertyMember(
            doc="""Saturday schedule.  A structure containing an array of
            seven time-value pairs that specify the daily schedule for
            Saturday;  unused time-value pairs have an invalid value (31) for
            the hour;  if two time-value pairs specify the same time, the
            first with a valid output value is used.""",
            name='cpScheduleSaturday',
            profile=self,
            number=6,
            datatype=SCPTscheduleSaturday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00',
            mandatory=True
        )
        self.properties['cpOccBehavior'] = base.Profile.PropertyMember(
            doc="""Occupancy behavior.  Specifies mapping of scheduled
            occupancy values to primary occupancy states based on local
            occupancy inputs.""",
            name='cpOccBehavior',
            profile=self,
            number=8,
            datatype=SCPToccupancyBehavior,
            default=b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the four primary and secondary
            occupancy values (heartbeat);  the value 0 disables the
            heartbeat.""",
            name='cpMaxSendTime',
            profile=self,
            number=13,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the four primary and secondary
            occupancy values (throttle);  the value 0 disables the
            throttle.""",
            name='cpMinSendTime',
            profile=self,
            number=14,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpObjMajVer'] = base.Profile.PropertyMember(
            doc="""Functional block implementation major version number.  The
            major version of the functional block implementation.  It may be
            used to identify compatibility of programs with the functional
            block.  For example, if support for new features and functions
            are added to the functional block, a network tool can use this CP
            to detect that the functional block is an older version that does
            not support the new features, and a firmware upgrade is required
            before this program may be downloaded.""",
            name='cpObjMajVer',
            profile=self,
            number=15,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpObjMinVer'] = base.Profile.PropertyMember(
            doc="""Functional block implementation minor version number.  The
            minor version of the functional block.  It may be used to
            identify the version of the functional block, so that a
            configuration tool can present relevant information to a user.
            The Minor Version of the functional block is used to distinguish
            version changes that do not affect compatibility.  For example,
            if a functional block has some minor behavioral changes such as
            range checking added, the tool can decide whether or not to warn
            the user about this potential issue.  Any changes that affect
            compatibility of programs require a change to the Major version
            CP.""",
            name='cpObjMinVer',
            profile=self,
            number=16,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpScheduleException'] = base.Profile.PropertyMember(
            doc="""Scheduled exception event.  Specifies a scheduled event to
            override a daily schedule.  This input is the fourth highest
            priority override after the Manual Override, Exception Override,
            and Local Occupancy inputs.  It overrides the daily schedule and
            the Scheduled Vacation/Holiday Event input.""",
            name='cpScheduleException',
            profile=self,
            number=10,
            datatype=SCPTscheduleException,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpScheduleHoliday'] = base.Profile.PropertyMember(
            doc="""Holiday or vacation schedule.  Specifies a scheduled
            vacation or holiday event to override a daily schedule.  This
            input is the lowest priority override after the Manual Override,
            Exception Override, Local Occupancy, and Exception Schedule
            inputs.  It overrides the daily schedule.""",
            name='cpScheduleHoliday',
            profile=self,
            number=11,
            datatype=SCPTscheduleHoliday,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpRandomizationInterval'] = base.Profile.PropertyMember(
            doc="""Randomization interval.  Specifies an interval around a
            scheduled time that is used by a scheduler to calculate a random
            event time.  Used to reduce simultaneous startup and shutdown of
            many devices by multiple schedulers.""",
            name='cpRandomizationInterval',
            profile=self,
            number=12,
            datatype=SCPTrandomizationInterval,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpSunriseTime'] = base.Profile.PropertyMember(
            doc="""Sunrise time.  Time used for sunrise-relative scheduling;
            must be implemented as a configuration network variable;  only
            the time fields are used for scheduling--the date fields indicate
            the date used for the configured time.""",
            name='cpSunriseTime',
            profile=self,
            number=18,
            datatype=SCPTsunriseTime,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSunsetTime'] = base.Profile.PropertyMember(
            doc="""Sunset time.  Time used for sunset-relative scheduling;
            must be implemented as a configuration network variable;  only
            the time fields are used for scheduling--the date fields indicate
            the date used for the configured time.""",
            name='cpSunsetTime',
            profile=self,
            number=19,
            datatype=SCPTsunsetTime,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpSchedulerOptions'] = base.Profile.PropertyMember(
            doc="""Scheduler options.  Specifies optional features
            implemented by this scheduler;  all Simple Schedulers support
            time-of-day occupancy scheduling;  support for a general-purpose
            output and sunrise-sunset relative scheduling is optional.""",
            name='cpSchedulerOptions',
            profile=self,
            number=17,
            datatype=SCPTschedulerOptions,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpOccThresholds'] = base.Profile.PropertyMember(
            doc="""Occupancy thresholds.  Specifies the minimum number of
            occupancy sensors that must report the same value to override a
            scheduled output value.""",
            name='cpOccThresholds',
            profile=self,
            number=9,
            datatype=SCPToccupancyThresholds,
            default=b'\x00\x00\x00',
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTschedulerSimple()
    pass
