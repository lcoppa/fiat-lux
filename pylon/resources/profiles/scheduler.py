"""scheduler standard profile, originally defined in resource file set
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
import pylon.resources.properties.defOutput
import pylon.resources.properties.delayTime
import pylon.resources.properties.maxNVLength
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.nvType
import pylon.resources.properties.valueName
import pylon.resources.properties.ovrBehave
import pylon.resources.properties.ovrValue
import pylon.resources.properties.valueDefinition
import pylon.resources.datapoints.switch
import pylon.resources.properties.effectivePeriod
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.schedule
import pylon.resources.properties.scheduleTimeValue
import pylon.resources.properties.weeklySchedule
import pylon.resources.properties.scheduleName


class scheduler(pylon.resources.base.Profile):
    """scheduler standard profile.  Scheduler Standardized interface for
    describing daily schedules.  Schedules may become active on specified
    days of the week, or based on active schedules defined by a Calendar
    functional block."""

    def __init__(self):
        super().__init__(
            key=7,
            scope=0
        )
        self.datapoints['nvoPresentValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Present value.  Indicates the current value of the
            schedule.  The output is determined by the current time as well
            as the currently active schedules.""",
            name='nvoPresentValue',
            profile=self,
            number=1,
            datatype=pylon.resources.base.xxx,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDefOutput':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default output.  Specifies the nvoPresentValue
                    output when no schedules are active, or when an override
                    request is received for the functional block.  The
                    override behavior may be defined by the optional Override
                    Behavior and Override Value configuration properties.""",
                    name='cpDefOutput',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.defOutput.defOutput,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=True
                ),
                'cpDelayTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Delay time.  Specifies a delay from the scheduled
                    time.  This allows multiple outputs within a Scheduler
                    functional block, or multiple Scheduler functional blocks
                    on a device, to share a common schedule but stagger on
                    and off times to reduce peak load.""",
                    name='cpDelayTime',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.delayTime.delayTime,
                    mandatory=False
                ),
                'cpMaxNVLength':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum network variable length.  Maximum length
                    of a type that may be assigned to the nvoPresentValue
                    network variable.""",
                    name='cpMaxNVLength',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxNVLength.maxNVLength,
                    flags=pylon.resources.base.PropertyFlags.CONST,
                    mandatory=False
                ),
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    mandatory=False
                ),
                'cpNVType':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Network variable type.  Assigns the network
                    variable type for the nvoPresentValue network
                    variable.""",
                    name='cpNVType',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.nvType.nvType,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=False
                ),
                'cpValueName':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Value name.  Used to create an array of value
                    names for each of the values defined in a
                    SCPTvalueDefinition array.""",
                    name='cpValueName',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.valueName.valueName,
                    array_size_min=2,
                    array_size_max=65535,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=False
                ),
                'cpOvrBehave':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Override behavior.  Defines the behavior of the
                    nvoPresentValue output when an override request is
                    received.""",
                    name='cpOvrBehave',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.ovrBehave.ovrBehave,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=False
                ),
                'cpOvrValue':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Override value.  Sets the value the
                    nvoPresentValue output should adopt when it is overridden
                    and the value of Override Behavior is OV_SPECIFIED.""",
                    name='cpOvrValue',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.ovrValue.ovrValue,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=False
                ),
                'cpValueDef':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Value definition.  Used to create an array of
                    output values to be used for a schedule.  A schedule
                    time-value event specifies a value as an index into a
                    SCPTvalueDefinition array.""",
                    name='cpValueDef',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.valueDefinition.valueDefinition,
                    array_size_min=2,
                    array_size_max=65535,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    mandatory=True
                )
            }
        )
        self.datapoints['nviEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Enable Enables the scheduler.  The scheduler is enabled
            when the state value is one (1) and the level value is greater
            than zero (0)""",
            name='nviEnable',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['cpEffPeriod'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Effective period.  Time period during which a functional
            block is effective.""",
            name='cpEffPeriod',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.effectivePeriod.effectivePeriod,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['cpObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVer',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVer',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpSchedule'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Schedule Describes the attributes of a daily schedule
            definition.""",
            name='cpSchedule',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.schedule.schedule,
            array_size_min=2,
            array_size_max=65535,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['cpSchTimeValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Schedule time-value pair.  Specifies the time and value
            for a scheduled event.""",
            name='cpSchTimeValue',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.scheduleTimeValue.scheduleTimeValue,
            array_size_min=2,
            array_size_max=65535,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['cpWeeklySched'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Weekly schedule.  Identifies a schedule to be active for
            each day of the week.""",
            name='cpWeeklySched',
            profile=self,
            number=18,
            datatype=pylon.resources.properties.weeklySchedule.weeklySchedule,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['cpSchedName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Schedule name.  Used to create an array of schedule
            names.""",
            name='cpSchedName',
            profile=self,
            number=19,
            datatype=pylon.resources.properties.scheduleName.scheduleName,
            array_size_min=2,
            array_size_max=255,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self._original_name = 'SFPTscheduler'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = scheduler()
    pass
