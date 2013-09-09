"""SCPTlogRequest standard property type, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_time_stamp_p import SNVT_time_stamp_p


class SCPTlogRequest(base.Structure):
    """SCPTlogRequest standard property type.  Data log access request.  Data
    log access request message format.  Not used as a CP.  This request has a
    variable size--the timestamp field is only included with the get next
    record request."""

    def __init__(self):
        super().__init__(
            key=340,
            scope=0
        )

        self.__dlap_version = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('dlap_version', self.__dlap_version))

        self.__requested_log = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('requested_log', self.__requested_log))

        self.__last_time = SNVT_time_stamp_p(
        )
        self._register(('last_time', self.__last_time))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 340
        self._definition = standard.add(self)

    def __set_dlap_version(self, v):
        self.__dlap_version._value = v

    dlap_version = property(
        lambda self: self.__dlap_version._value,
        __set_dlap_version,
        None,
        """Data log access protocol version.  Data log access protocol
        version number.  Currently must be 1."""
    )

    def __set_requested_log(self, v):
        self.__requested_log._value = v

    requested_log = property(
        lambda self: self.__requested_log._value,
        __set_requested_log,
        None,
        """Requested log number.  The log number of the data log to be
        accessed.  Logs are numbered from 1 to number_of_logs."""
    )

    def __set_last_time(self, v):
        self.__last_time._value = v

    last_time = property(
        lambda self: self.__last_time._value,
        __set_last_time,
        None,
        """Timestamp of last record fetched.  The first record with a
        timestamp after this timestamp is returned.  If this field is
        invalid, the first record in the data log is returned.  Timestamp of
        last record fetched.  The first record with a timestamp after this
        timestamp is returned.  If this field is invalid, the first record in
        the data log is returned."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_dlap_version(v.__dlap_version)
        self.__set_requested_log(v.__requested_log)
        self.__set_last_time(v.__last_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SCPTlogRequest()
    pass
