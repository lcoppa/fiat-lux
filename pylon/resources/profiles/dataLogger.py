"""dataLogger standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.alarm_2
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.switch
import pylon.resources.properties.fanInEnable
import pylon.resources.properties.logHighLimit
import pylon.resources.properties.logLowLimit
import pylon.resources.properties.maxFanIn
import pylon.resources.properties.logMinDeltaTime
import pylon.resources.properties.logMinDeltaValue
import pylon.resources.properties.nvType
import pylon.resources.properties.pollRate
import pylon.resources.properties.sourceAddress
import pylon.resources.properties.maxNVLength
import pylon.resources.datapoints.log_status
import pylon.resources.properties.logCapacity
import pylon.resources.properties.logNotificationThreshold
import pylon.resources.properties.logSize
import pylon.resources.properties.logType
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.logTimestampEnable
import pylon.resources.properties.logAlarmThreshold


class dataLogger(pylon.resources.base.Profile):
    """dataLogger standard profile.  """

    def __init__(self):
        super().__init__(
            key=9,
            scope=0
        )
        self.datapoints['nvoLevAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm status 2.  Transmits alarm data to a monitoring
            device.  The alarm type is set to AL_NO_CONDITION if the level
            set by cpLogAlarmThreshold is not reached and to AL_ALM_CONDITION
            if the level has been reached or exceeded.  The priority is set
            to PR_10.""",
            name='nvoLevAlarm',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.alarm_2.alarm_2,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxAlSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Alarm maximum send time.  The maximum period of
                    time between consecutive transmissions of the current
                    value.""",
                    name='cpMaxAlSendTime',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Enable Enables data collection for the data log.  Data
            collection is enabled when the state value is one (1).  The level
            value is not used.""",
            name='nviEnable',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDataValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Data value.  Receives data to be collected in the data
            log.  Optional because data sources may be internal to the
            device.""",
            name='nviDataValue',
            profile=self,
            number=1,
            datatype=pylon.resources.base.xxx,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'cpFanInEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Fan-in enable.  Enables fan-in of multiple data
                    sources.  When True, the application examines the source
                    address of each input value and uses it to determine the
                    data source of the update.""",
                    name='cpFanInEnable',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.fanInEnable.fanInEnable,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x01',
                    mandatory=False
                ),
                'cpLogHighLimit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Data log high limit.  Enables logging of data
                    greater or equal to the specified value.  All other data
                    is ignored, with the exception that data that is less
                    than or equal to a valid SCPTlogLowLimit value is also
                    logged.  All data is logged if the SCPTlogEnableHighLimit
                    and SCPTlogEnableLowLimit values are both invalid.""",
                    name='cpLogHighLimit',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.logHighLimit.logHighLimit,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpLogLowLimit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Data log low limit.  Enables logging of data less
                    than or equal to the specified value.  All other data is
                    ignored, with the exception that data that is greater
                    than or equal to a valid SCPTlogHighLimit value is also
                    logged.  All data is logged if the SCPTlogEnableHighLimit
                    and SCPTlogEnableLowLimit values are both invalid.""",
                    name='cpLogLowLimit',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.logLowLimit.logLowLimit,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpMaxFanIn':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum fan-in.  Specifies the maximum number of
                    data sources that may be connected to a network
                    variable.  The functional block determines data sources
                    by examining the source address of each update.""",
                    name='cpMaxFanIn',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.maxFanIn.maxFanIn,
                    flags=pylon.resources.base.PropertyFlags.CONST,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpLogMinDeltaTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Data log minimum delta time.  Minimum amount of
                    time between logged values.  This is used to throttle
                    data entry into a data log.  When a data value is logged,
                    a subsequent update to the data value is not logged until
                    the time specified by this value has elapsed.  If
                    additional updates are received during this time, the
                    older values are discarded and are not stored in the data
                    log.  Time of receipt is ignored if the value of this
                    configuration property is zero or invalid.""",
                    name='cpLogMinDeltaTime',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.logMinDeltaTime.logMinDeltaTime,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpLogMinDeltaValue':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Data log minimum delta time.  Minimum amount of
                    time between logged values.  This is used to throttle
                    data entry into a data log.  When a data value is logged,
                    a subsequent update to the data value is not logged until
                    the time specified by this value has elapsed.  If
                    additional updates are received during this time, the
                    older values are discarded and are not stored in the data
                    log.  Time of receipt is ignored if the value of this
                    configuration property is zero or invalid.""",
                    name='cpLogMinDeltaValue',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.logMinDeltaValue.logMinDeltaValue,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpNVType':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Network variable type.  Network variable type for
                    network variables that support changeable types.""",
                    name='cpNVType',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.nvType.nvType,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
                        b'\x00\x01\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpPollRate':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Poll rate.  Specifies the poll rate for each data
                    source.  When this value is greater than zero, the
                    functional block polls each of the data sources
                    identified in the source address array at the rate
                    specified by this value.""",
                    name='cpPollRate',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.pollRate.pollRate,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpSourceAddress':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Source address.  Specifies a source address or
                    element of an array of source addresses for and input to
                    a functional block.""",
                    name='cpSourceAddress',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.sourceAddress.sourceAddress,
                    array_size_min=2,
                    array_size_max=32385,
                    flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                        pylon.resources.base.PropertyFlags.CONST |
                        pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpMaxNVLength':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum network variable length.  Maximum length
                    of a type that may be assigned to the nviDataValue
                    input.  Also requires implementation of the cpNvType
                    configuration property.""",
                    name='cpMaxNVLength',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.maxNVLength.maxNVLength,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    default=b'\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviClear'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Clear Clears the contents of the data log.  The data log
            may also be cleared by a Node Object request.""",
            name='nviClear',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Log status.  Reports the current status of a data log.
            Updated based on the cpLogNotificationThreshold value.  Reports
            status only;  alarms reported via Node Object nvoAlarm2 output.
            Required if the Node Object does not include an nvoLogStat
            output.""",
            name='nvoStatus',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.log_status.log_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  Maximum period of time that
                    expires before the Data Logger functional block
                    automatically transmits the current value of the
                    nvoStatus output network variable.  This provides a
                    heartbeat output that can be used by destination
                    functional blocks to ensure that the functional block is
                    still healthy.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['cpLogCapacity'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Data log capacity.  Specifies the total capacity of all
            data logs on a device.  The size of each data log is specified by
            its cpLogSize value.  The value is specified in bytes.""",
            name='cpLogCapacity',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.logCapacity.logCapacity,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLogNotifyThreshold'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Data log notification threshold.  Specifies the percentage
            change in log level required to trigger an update to the Data Log
            Status (nvoStatus) output.""",
            name='cpLogNotifyThreshold',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.logNotificationThreshold.logNotificationThreshold,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpLogSize'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Log size.  Capacity of a data log.""",
            name='cpLogSize',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.logSize.logSize,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLogType'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Data log type.  Specifies the method used to store data in
            a data log.""",
            name='cpLogType',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.logType.logType,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            minimum=b'\x00',
            maximum=b'\x03',
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  Major version number for the
            data logger implementation.  This value is incremented when the
            network interface for the functional block changes.""",
            name='cpObjMajVer',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['cpObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  Minor version number for the
            data logger implementation.  This value is incremented when the
            functional block implementation changes without changing the
            functional block network interface.  The minor version is reset
            to zero and the cpObjMajVer value is incremented when the
            functional block network interface changes.""",
            name='cpObjMinVer',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpTimestampEnable'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Data log enable timestamp.  Enables time stamping of each
            data value.  When True, the data logger includes a timestamp of
            the receipt time for each value received by the data logger.""",
            name='cpTimestampEnable',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.logTimestampEnable.logTimestampEnable,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x01',
            mandatory=False
        )
        self.properties['cpLogAlarmThreshold'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Data log alarm threshold.  Specifies the log level
            required to trigger an alarm condition for the data logger.""",
            name='cpLogAlarmThreshold',
            profile=self,
            number=20,
            datatype=pylon.resources.properties.logAlarmThreshold.logAlarmThreshold,
            default=b'\xbf',
            mandatory=False
        )
        self._original_name = 'SFPTdataLogger'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = dataLogger()
    pass
