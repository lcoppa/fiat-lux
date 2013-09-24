"""SFPTdataLogger standard profile, originally defined in resource file set
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_alarm_2 import SNVT_alarm_2
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_xxx import SNVT_xxx
from pylon.resources.SCPTfanInEnable import SCPTfanInEnable
from pylon.resources.SCPTlogHighLimit import SCPTlogHighLimit
from pylon.resources.SCPTlogLowLimit import SCPTlogLowLimit
from pylon.resources.SCPTmaxFanIn import SCPTmaxFanIn
from pylon.resources.SCPTlogMinDeltaTime import SCPTlogMinDeltaTime
from pylon.resources.SCPTlogMinDeltaValue import SCPTlogMinDeltaValue
from pylon.resources.SCPTnvType import SCPTnvType
from pylon.resources.SCPTpollRate import SCPTpollRate
from pylon.resources.SCPTsourceAddress import SCPTsourceAddress
from pylon.resources.SCPTmaxNVLength import SCPTmaxNVLength
from pylon.resources.SNVT_log_status import SNVT_log_status
from pylon.resources.SCPTlogCapacity import SCPTlogCapacity
from pylon.resources.SCPTlogNotificationThreshold import SCPTlogNotificationThreshold
from pylon.resources.SCPTlogSize import SCPTlogSize
from pylon.resources.SCPTlogType import SCPTlogType
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTlogTimestampEnable import SCPTlogTimestampEnable
from pylon.resources.SCPTlogAlarmThreshold import SCPTlogAlarmThreshold


class SFPTdataLogger(base.Profile):
    """SFPTdataLogger standard profile.  """

    def __init__(self):
        super().__init__(
            key=9,
            scope=0
        )
        self.datapoints['nvoLevAlarm'] = base.Profile.DatapointMember(
            doc="""Alarm status 2.  Transmits alarm data to a monitoring
            device.  The alarm type is set to AL_NO_CONDITION if the level
            set by cpLogAlarmThreshold is not reached and to AL_ALM_CONDITION
            if the level has been reached or exceeded.  The priority is set
            to PR_10.""",
            name='nvoLevAlarm',
            profile=self,
            number=5,
            datatype=SNVT_alarm_2,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxAlSendTime':
                base.Profile.PropertyMember(
                    doc="""Alarm maximum send time.  The maximum period of
                    time between consecutive transmissions of the current
                    value.""",
                    name='cpMaxAlSendTime',
                    profile=self,
                    number=18,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEnable'] = base.Profile.DatapointMember(
            doc="""Enable Enables data collection for the data log.  Data
            collection is enabled when the state value is one (1).  The level
            value is not used.""",
            name='nviEnable',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDataValue'] = base.Profile.DatapointMember(
            doc="""Data value.  Receives data to be collected in the data
            log.  Optional because data sources may be internal to the
            device.""",
            name='nviDataValue',
            profile=self,
            number=1,
            datatype=SNVT_xxx,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'cpFanInEnable':
                base.Profile.PropertyMember(
                    doc="""Fan-in enable.  Enables fan-in of multiple data
                    sources.  When True, the application examines the source
                    address of each input value and uses it to determine the
                    data source of the update.""",
                    name='cpFanInEnable',
                    profile=self,
                    number=5,
                    datatype=SCPTfanInEnable,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x01',
                    mandatory=False
                ),
                'cpLogHighLimit':
                base.Profile.PropertyMember(
                    doc="""Data log high limit.  Enables logging of data
                    greater or equal to the specified value.  All other data
                    is ignored, with the exception that data that is less
                    than or equal to a valid SCPTlogLowLimit value is also
                    logged.  All data is logged if the SCPTlogEnableHighLimit
                    and SCPTlogEnableLowLimit values are both invalid.""",
                    name='cpLogHighLimit',
                    profile=self,
                    number=9,
                    datatype=SCPTlogHighLimit,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpLogLowLimit':
                base.Profile.PropertyMember(
                    doc="""Data log low limit.  Enables logging of data less
                    than or equal to the specified value.  All other data is
                    ignored, with the exception that data that is greater
                    than or equal to a valid SCPTlogHighLimit value is also
                    logged.  All data is logged if the SCPTlogEnableHighLimit
                    and SCPTlogEnableLowLimit values are both invalid.""",
                    name='cpLogLowLimit',
                    profile=self,
                    number=10,
                    datatype=SCPTlogLowLimit,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpMaxFanIn':
                base.Profile.PropertyMember(
                    doc="""Maximum fan-in.  Specifies the maximum number of
                    data sources that may be connected to a network
                    variable.  The functional block determines data sources
                    by examining the source address of each update.""",
                    name='cpMaxFanIn',
                    profile=self,
                    number=11,
                    datatype=SCPTmaxFanIn,
                    flags=base.PropertyFlags.CONST,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpLogMinDeltaTime':
                base.Profile.PropertyMember(
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
                    datatype=SCPTlogMinDeltaTime,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpLogMinDeltaValue':
                base.Profile.PropertyMember(
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
                    datatype=SCPTlogMinDeltaValue,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpNVType':
                base.Profile.PropertyMember(
                    doc="""Network variable type.  Network variable type for
                    network variables that support changeable types.""",
                    name='cpNVType',
                    profile=self,
                    number=15,
                    datatype=SCPTnvType,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
                        b'\x00\x01\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpPollRate':
                base.Profile.PropertyMember(
                    doc="""Poll rate.  Specifies the poll rate for each data
                    source.  When this value is greater than zero, the
                    functional block polls each of the data sources
                    identified in the source address array at the rate
                    specified by this value.""",
                    name='cpPollRate',
                    profile=self,
                    number=16,
                    datatype=SCPTpollRate,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpSourceAddress':
                base.Profile.PropertyMember(
                    doc="""Source address.  Specifies a source address or
                    element of an array of source addresses for and input to
                    a functional block.""",
                    name='cpSourceAddress',
                    profile=self,
                    number=17,
                    datatype=SCPTsourceAddress,
                    array_size_min=2,
                    array_size_max=32385,
                    flags=base.PropertyFlags.DEVICE_SPECIFIC |
                        base.PropertyFlags.CONST |
                        base.PropertyFlags.DISABLE,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'cpMaxNVLength':
                base.Profile.PropertyMember(
                    doc="""Maximum network variable length.  Maximum length
                    of a type that may be assigned to the nviDataValue
                    input.  Also requires implementation of the cpNvType
                    configuration property.""",
                    name='cpMaxNVLength',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxNVLength,
                    flags=base.PropertyFlags.DISABLE,
                    default=b'\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviClear'] = base.Profile.DatapointMember(
            doc="""Clear Clears the contents of the data log.  The data log
            may also be cleared by a Node Object request.""",
            name='nviClear',
            profile=self,
            number=3,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoStatus'] = base.Profile.DatapointMember(
            doc="""Log status.  Reports the current status of a data log.
            Updated based on the cpLogNotificationThreshold value.  Reports
            status only;  alarms reported via Node Object nvoAlarm2 output.
            Required if the Node Object does not include an nvoLogStat
            output.""",
            name='nvoStatus',
            profile=self,
            number=4,
            datatype=SNVT_log_status,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                base.Profile.PropertyMember(
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
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['cpLogCapacity'] = base.Profile.PropertyMember(
            doc="""Data log capacity.  Specifies the total capacity of all
            data logs on a device.  The size of each data log is specified by
            its cpLogSize value.  The value is specified in bytes.""",
            name='cpLogCapacity',
            profile=self,
            number=1,
            datatype=SCPTlogCapacity,
            flags=base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLogNotifyThreshold'] = base.Profile.PropertyMember(
            doc="""Data log notification threshold.  Specifies the percentage
            change in log level required to trigger an update to the Data Log
            Status (nvoStatus) output.""",
            name='cpLogNotifyThreshold',
            profile=self,
            number=2,
            datatype=SCPTlogNotificationThreshold,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpLogSize'] = base.Profile.PropertyMember(
            doc="""Log size.  Capacity of a data log.""",
            name='cpLogSize',
            profile=self,
            number=3,
            datatype=SCPTlogSize,
            flags=base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLogType'] = base.Profile.PropertyMember(
            doc="""Data log type.  Specifies the method used to store data in
            a data log.""",
            name='cpLogType',
            profile=self,
            number=4,
            datatype=SCPTlogType,
            flags=base.PropertyFlags.DISABLE,
            minimum=b'\x00',
            maximum=b'\x03',
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  Major version number for the
            data logger implementation.  This value is incremented when the
            network interface for the functional block changes.""",
            name='cpObjMajVer',
            profile=self,
            number=6,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['cpObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  Minor version number for the
            data logger implementation.  This value is incremented when the
            functional block implementation changes without changing the
            functional block network interface.  The minor version is reset
            to zero and the cpObjMajVer value is incremented when the
            functional block network interface changes.""",
            name='cpObjMinVer',
            profile=self,
            number=7,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpTimestampEnable'] = base.Profile.PropertyMember(
            doc="""Data log enable timestamp.  Enables time stamping of each
            data value.  When True, the data logger includes a timestamp of
            the receipt time for each value received by the data logger.""",
            name='cpTimestampEnable',
            profile=self,
            number=8,
            datatype=SCPTlogTimestampEnable,
            flags=base.PropertyFlags.DISABLE,
            default=b'\x01',
            mandatory=False
        )
        self.properties['cpLogAlarmThreshold'] = base.Profile.PropertyMember(
            doc="""Data log alarm threshold.  Specifies the log level
            required to trigger an alarm condition for the data logger.""",
            name='cpLogAlarmThreshold',
            profile=self,
            number=20,
            datatype=SCPTlogAlarmThreshold,
            default=b'\xbf',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTdataLogger()
    pass
