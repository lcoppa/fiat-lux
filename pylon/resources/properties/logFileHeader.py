"""logFileHeader standard property type, originally defined in resource file
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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.time_stamp_p


class logFileHeader(pylon.resources.base.Structure):
    """logFileHeader standard property type.  Data log header.  Describes
    contents of a data log."""

    def __init__(self):
        super().__init__(
            key=338,
            scope=0
        )

        self.__file_type = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=2049,
            maximum=2049
        )
        self._register(('file_type', self.__file_type))

        self.__major_version_number = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=1,
            maximum=1
        )
        self._register(('major_version_number', self.__major_version_number))

        self.__minor_version_number = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=0
        )
        self._register(('minor_version_number', self.__minor_version_number))

        self.__log_number = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('log_number', self.__log_number))

        self.__record_count = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            invalid=2147483647,
            minimum=0,
            maximum=2147483646
        )
        self._register(('record_count', self.__record_count))

        self.__start_time = pylon.resources.datapoints.time_stamp_p.time_stamp_p(
        )
        self._register(('start_time', self.__start_time))

        self.__end_time = pylon.resources.datapoints.time_stamp_p.time_stamp_p(
        )
        self._register(('end_time', self.__end_time))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._original_name = 'SCPTlogFileHeader'
        self._property_scope, self._property_key = 0, 338
        self._definition = standard.add(self)

    def __set_file_type(self, v):
        self.__file_type._value = v

    file_type = property(
        lambda self: self.__file_type._value,
        __set_file_type,
        None,
        """Data log file type.  Constant identifying a data log."""
    )

    def __set_major_version_number(self, v):
        self.__major_version_number._value = v

    major_version_number = property(
        lambda self: self.__major_version_number._value,
        __set_major_version_number,
        None,
        """Data log file format major version number."""
    )

    def __set_minor_version_number(self, v):
        self.__minor_version_number._value = v

    minor_version_number = property(
        lambda self: self.__minor_version_number._value,
        __set_minor_version_number,
        None,
        """Data log minor version number."""
    )

    def __set_log_number(self, v):
        self.__log_number._value = v

    log_number = property(
        lambda self: self.__log_number._value,
        __set_log_number,
        None,
        """Data log number.  Index of the data log functional block that
        received this update."""
    )

    def __set_record_count(self, v):
        self.__record_count._value = v

    record_count = property(
        lambda self: self.__record_count._value,
        __set_record_count,
        None,
        """Data log record count.  Number of records in data log.
        (seconds)."""
    )

    def __set_start_time(self, v):
        self.__start_time._value = v

    start_time = property(
        lambda self: self.__start_time._value,
        __set_start_time,
        None,
        """Data log start time.  (seconds)."""
    )

    def __set_end_time(self, v):
        self.__end_time._value = v

    end_time = property(
        lambda self: self.__end_time._value,
        __set_end_time,
        None,
        """Data log end time.  (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_file_type(v.__file_type)
        self.__set_major_version_number(v.__major_version_number)
        self.__set_minor_version_number(v.__minor_version_number)
        self.__set_log_number(v.__log_number)
        self.__set_record_count(v.__record_count)
        self.__set_start_time(v.__start_time)
        self.__set_end_time(v.__end_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 20


if __name__ == '__main__':
    # unit test code.
    item = logFileHeader()
    pass
