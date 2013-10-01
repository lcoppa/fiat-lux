"""log_status standard datapoint type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0.  """


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
import pylon.resources.enumerations.log_status_t
import pylon.resources.datapoints.time_stamp_p


class log_status(pylon.resources.base.Structure):
    """log_status standard datapoint type.  Log status.  Reports the current
    status of a data log.  Updated based on the cpLogNotificationThreshold
    value.  Reports status only;  alarms reported via Node Object nvoAlarm2
    output.  Required if the Node Object does not include an nvoLogStat
    output.  (hundredths of second.)."""

    def __init__(self):
        super().__init__(
            key=191,
            scope=0
        )

        self.__status = pylon.resources.enumerations.log_status_t.log_status_t(
        )
        self._register(('status', self.__status))

        self.__log_number = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('log_number', self.__log_number))

        self.__level = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            scaling=(0.5, 0),
            invalid=127.5,
            minimum=0,
            maximum=100
        )
        self._register(('level', self.__level))

        self.__record_count = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('record_count', self.__record_count))

        self.__byte_count = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('byte_count', self.__byte_count))

        self.__total_record_count = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('total_record_count', self.__total_record_count))

        self.__records_since_notification = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('records_since_notification', self.__records_since_notification))

        self.__current_notify_time = pylon.resources.datapoints.time_stamp_p.time_stamp_p(
        )
        self._register(('current_notify_time', self.__current_notify_time))

        self.__previous_notify_time = pylon.resources.datapoints.time_stamp_p.time_stamp_p(
        )
        self._register(('previous_notify_time', self.__previous_notify_time))
        self._original_name = 'SNVT_log_status'
        self._definition = standard.add(self)


    def __set_status(self, v):
        self.__status._value = v

    status = property(
        lambda self: self.__status._value,
        __set_status,
        None,
        """Log state.  State of the selected data log."""
    )

    def __set_log_number(self, v):
        self.__log_number._value = v

    log_number = property(
        lambda self: self.__log_number._value,
        __set_log_number,
        None,
        """Selected log number.  The log number of the reported data log.
        Logs are numbered from 1 to number_of_logs."""
    )

    def __set_level(self, v):
        self.__level._value = v

    level = property(
        lambda self: self.__level._value,
        __set_level,
        None,
        """Log level.  The percent of maximum records in the selected data
        log.  (Percent)."""
    )

    def __set_record_count(self, v):
        self.__record_count._value = v

    record_count = property(
        lambda self: self.__record_count._value,
        __set_record_count,
        None,
        """Record count.  Number of records in the selected data log.  A
        record is a logged value and any associated data such as a
        timestamp.  (records)."""
    )

    def __set_byte_count(self, v):
        self.__byte_count._value = v

    byte_count = property(
        lambda self: self.__byte_count._value,
        __set_byte_count,
        None,
        """Byte count.  Number of bytes in the selected data log.
        (bytes)."""
    )

    def __set_total_record_count(self, v):
        self.__total_record_count._value = v

    total_record_count = property(
        lambda self: self.__total_record_count._value,
        __set_total_record_count,
        None,
        """Total record count.  Total records collected in the selected data
        log since the data log was created.  Wraps to 0 on overflow.
        (records)."""
    )

    def __set_records_since_notification(self, v):
        self.__records_since_notification._value = v

    records_since_notification = property(
        lambda self: self.__records_since_notification._value,
        __set_records_since_notification,
        None,
        """Records since notification.  The number of log records collected
        since the last notificiation.  (records)."""
    )

    def __set_current_notify_time(self, v):
        self.__current_notify_time._value = v

    current_notify_time = property(
        lambda self: self.__current_notify_time._value,
        __set_current_notify_time,
        None,
        """Current notify time.  Timestamp of the most recently collected
        data point."""
    )

    def __set_previous_notify_time(self, v):
        self.__previous_notify_time._value = v

    previous_notify_time = property(
        lambda self: self.__previous_notify_time._value,
        __set_previous_notify_time,
        None,
        """Previous notify time.  Timestamp of the most recently collected
        data point in the previous update to the log status.  (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_status(v.__status)
        self.__set_log_number(v.__log_number)
        self.__set_level(v.__level)
        self.__set_record_count(v.__record_count)
        self.__set_byte_count(v.__byte_count)
        self.__set_total_record_count(v.__total_record_count)
        self.__set_records_since_notification(v.__records_since_notification)
        self.__set_current_notify_time(v.__current_notify_time)
        self.__set_previous_notify_time(v.__previous_notify_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 30


if __name__ == '__main__':
    # unit test code.
    item = log_status()
    pass
