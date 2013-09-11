"""SCPTlogRecord standard property type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_time_stamp_p import SNVT_time_stamp_p
from pylon.resources.log_status_t import log_status_t
from pylon.resources.point_status_t import point_status_t


class SCPTlogRecord(base.Structure):
    """SCPTlogRecord standard property type.  Log record.  Documents the
    format of a data log record.  Not used as a CP.  Data logs have variable
    sized records--unused fields are not present."""

    class timeType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__timestamp = SNVT_time_stamp_p(
            )
            self._register(('timestamp', self.__timestamp))

            self.__offset_stamp = base.Scaled(
                size=2,
                signed=False,
                scaling=(0.01, 0),
                invalid=655.35,
                minimum=0,
                maximum=655.34
            )
            self._register(('offset_stamp', self.__offset_stamp))

        def __set_timestamp(self, v):
            self.__timestamp._value = v

        timestamp = property(
            lambda self: self.__timestamp._value,
            __set_timestamp,
            None,
            """Timestamp Full timestamp.  Only present if timestamp_type is
            TS_FULL.  (seconds)."""
        )

        def __set_offset_stamp(self, v):
            self.__offset_stamp._value = v

        offset_stamp = property(
            lambda self: self.__offset_stamp._value,
            __set_offset_stamp,
            None,
            """Offset timestamp.  Offset since last full timestamp.  Only
            present if timestamp_type is TS_OFFSET.  (seconds)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_timestamp(v.__timestamp)
            self.__set_offset_stamp(v.__offset_stamp)

        _value = property(lambda self: self, __set)

    class dataType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__log_status = log_status_t(
            )
            self._register(('log_status', self.__log_status))

            self.__value = base.Scaled(
                size=4,
                signed=True,
                invalid=0,
                minimum=-2147483648,
                maximum=2147483647
            )
            self._register(('value', self.__value))

            self.__old_time = SNVT_time_stamp_p(
            )
            self._register(('old_time', self.__old_time))

        def __set_log_status(self, v):
            self.__log_status._value = v

        log_status = property(
            lambda self: self.__log_status._value,
            __set_log_status,
            None,
            """Data log status.  Changed value for data log status.  Only
            present if record_type is LR_LOG_STATUS."""
        )

        def __set_value(self, v):
            self.__value._value = v

        value = property(
            lambda self: self.__value._value,
            __set_value,
            None,
            """Data log data value.  Data log value.  Size depends on size
            logged value and is defined by data_length.  Only present if
            record_type is LR_DATA."""
        )

        def __set_old_time(self, v):
            self.__old_time._value = v

        old_time = property(
            lambda self: self.__old_time._value,
            __set_old_time,
            None,
            """Data log old time.  Previous time after a time change.  Only
            present if record_type is LR_TIME_CHANGE.  (seconds)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_log_status(v.__log_status)
            self.__set_value(v.__value)
            self.__set_old_time(v.__old_time)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=337,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__data_length = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('data_length', self.__data_length))

        self.__time = SCPTlogRecord.timeType(
        )
        self._register(('time', self.__time))

        self.__member_index = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('member_index', self.__member_index))

        self.__data_source_index = base.Scaled(
            size=2,
            signed=True,
            invalid=-1,
            minimum=0,
            maximum=32767
        )
        self._register(('data_source_index', self.__data_source_index))

        self.__data = SCPTlogRecord.dataType(
        )
        self._register(('data', self.__data))

        self.__point_status_value = point_status_t(
        )
        self._register(('point_status_value', self.__point_status_value))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 337
        self._definition = standard.add(self)
    def __set_timestamp_type(self, v):
        if 0 <= v <= 3:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_timestamp_type(self):
        return self.___bf00._getbits(
            size=2,
            offset=0,
            signed=False
        )

    timestamp_type = property(
        __get_timestamp_type,
        __set_timestamp_type,
        None,
        """Timestamp type.  Specifies whether or not a timestamp is included,
        and if it is incljuded, specifies the format of the timestamp.
        Contents defined by timestamp_t."""
    )

    def __set_record_type(self, v):
        if 0 <= v <= 3:
            self.___bf00._setbits(
                value=v,
                size=3,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_record_type(self):
        return self.___bf00._getbits(
            size=3,
            offset=2,
            signed=False
        )

    record_type = property(
        __get_record_type,
        __set_record_type,
        None,
        """Log record type.  Specifies the format of a data log record.
        Contents defined by log_record_t."""
    )

    def __set_multiple_input(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_multiple_input(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    multiple_input = property(
        __get_multiple_input,
        __set_multiple_input,
        None,
        """Multiple tnput NV flag.  Set to 1 if the functional block has
        multiple input NVs."""
    )

    def __set_fan_in(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_fan_in(self):
        return self.___bf00._getbits(
            size=1,
            offset=6,
            signed=False
        )

    fan_in = property(
        __get_fan_in,
        __set_fan_in,
        None,
        """Data log fan-in flag.  Set to one if this input NV receives data
        from multiple data sources."""
    )

    def __set_point_status(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_point_status(self):
        return self.___bf00._getbits(
            size=1,
            offset=7,
            signed=False
        )

    point_status = property(
        __get_point_status,
        __set_point_status,
        None,
        """Data log point status flag.  Set to one if this data log record
        includes point status information."""
    )


    def __set_data_length(self, v):
        self.__data_length._value = v

    data_length = property(
        lambda self: self.__data_length._value,
        __set_data_length,
        None,
        """Data log record length.  Number of bytes in the data portion of a
        data log record.  Set to 0 if the record does not contain a data
        value.  (bytes)."""
    )

    def __set_time(self, v):
        self.__time._value = v

    time = property(
        lambda self: self.__time._value,
        __set_time,
        None,
        """Timestamp."""
    )

    def __set_member_index(self, v):
        self.__member_index._value = v

    member_index = property(
        lambda self: self.__member_index._value,
        __set_member_index,
        None,
        """Data log member index.  Functional block member number for the
        network variable input that received this update.  Only present if
        mulitple_input is 1."""
    )

    def __set_data_source_index(self, v):
        self.__data_source_index._value = v

    data_source_index = property(
        lambda self: self.__data_source_index._value,
        __set_data_source_index,
        None,
        """Data log data source index.  Index into the cpSourceAddress
        array.  Only present if fan_in is 1."""
    )

    def __set_data(self, v):
        self.__data._value = v

    data = property(
        lambda self: self.__data._value,
        __set_data,
        None,
        """Data log record data.  Data field for a data log record.  Contents
        depend on record_type value.  Unused bytes are not included."""
    )

    def __set_point_status_value(self, v):
        self.__point_status_value._value = v

    point_status_value = property(
        lambda self: self.__point_status_value._value,
        __set_point_status_value,
        None,
        """Data log point status.  Optional status for a data point value.
        Only present if point_status is 1."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_timestamp_type(v.__timestamp_type)
        self.__set_record_type(v.__record_type)
        self.__set_multiple_input(v.__multiple_input)
        self.__set_fan_in(v.__fan_in)
        self.__set_point_status(v.__point_status)
        self.__set_data_length(v.__data_length)
        self.__set_time(v.__time)
        self.__set_member_index(v.__member_index)
        self.__set_data_source_index(v.__data_source_index)
        self.__set_data(v.__data)
        self.__set_point_status_value(v.__point_status_value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 16


if __name__ == '__main__':
    # unit test code.
    item = SCPTlogRecord()
    pass
