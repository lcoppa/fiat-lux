"""SNVT_log_fx_request standard datapoint type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0.  """


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


class SNVT_log_fx_request(base.Structure):
    """SNVT_log_fx_request standard datapoint type.  Log file transfer
    request.  Requests a data log to be transferred via FTP.  Must be
    followed by a stanard FTP request to get the data log file.  Required on
    devices implementing the Data Logger functional profile that support data
    log transfer via FTP."""

    def __init__(self):
        super().__init__(
            key=193,
            scope=0
        )

        self.__requested_log = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('requested_log', self.__requested_log))

        self.__record_count = base.Scaled(
            size=4,
            signed=False,
            minimum=0,
            maximum=-1
        )
        self._register(('record_count', self.__record_count))

        self.__start_time = SNVT_time_stamp_p(
        )
        self._register(('start_time', self.__start_time))

        self.__end_time = SNVT_time_stamp_p(
        )
        self._register(('end_time', self.__end_time))
        self._definition = standard.add(self)


    def __set_requested_log(self, v):
        self.__requested_log._value = v

    requested_log = property(
        lambda self: self.__requested_log._value,
        __set_requested_log,
        None,
        """Requested log number.  The log number of the data log to be
        transferred.  Logs are numbered from 1 to number_of_logs."""
    )

    def __set_record_count(self, v):
        self.__record_count._value = v

    record_count = property(
        lambda self: self.__record_count._value,
        __set_record_count,
        None,
        """Record count.  The maximum number of log records to be
        transferred."""
    )

    def __set_start_time(self, v):
        self.__start_time._value = v

    start_time = property(
        lambda self: self.__start_time._value,
        __set_start_time,
        None,
        """Start time.  Timestamp of first record to be transferred.  If no
        records exist with this timestamp, the first record with a timestamp
        after this timestamp is the starting record.  (seconds)."""
    )

    def __set_end_time(self, v):
        self.__end_time._value = v

    end_time = property(
        lambda self: self.__end_time._value,
        __set_end_time,
        None,
        """End time.  Timestamp of last record to be transferred.  If no
        records exist with this timestamp, the last record with a timestamp
        before this timestamp is the ending record.  (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_requested_log(v.__requested_log)
        self.__set_record_count(v.__record_count)
        self.__set_start_time(v.__start_time)
        self.__set_end_time(v.__end_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 16


if __name__ == '__main__':
    # unit test code.
    item = SNVT_log_fx_request()
    pass
