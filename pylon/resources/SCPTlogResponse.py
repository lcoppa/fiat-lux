"""SCPTlogResponse standard property type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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


class SCPTlogResponse(base.Structure):
    """SCPTlogResponse standard property type.  Data log access response.
    Data log access response message format.  Not used as a CP.  This
    response has a variable size--unused fields are not included."""

    class responseType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__log_record = base.Array(
                [
                    base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=255
                    ) for i in range(16)
                ]
            )
            self._register(('log_record', self.__log_record))

            self.__closest_version = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('closest_version', self.__closest_version))

            self.__number_of_logs = base.Scaled(
                size=2,
                signed=False,
                invalid=0,
                minimum=1,
                maximum=65535
            )
            self._register(('number_of_logs', self.__number_of_logs))

        def __set_log_record(self, v):
            self.__log_record._value = v

        log_record = property(
            lambda self: self.__log_record._value,
            __set_log_record,
            None,
            """."""
        )

        def __set_closest_version(self, v):
            self.__closest_version._value = v

        closest_version = property(
            lambda self: self.__closest_version._value,
            __set_closest_version,
            None,
            """Closest data log access protocol version.  Closest data log
            access protocol version number supported by this device.
            Returned for LRC_VER_MISMATCH responses."""
        )

        def __set_number_of_logs(self, v):
            self.__number_of_logs._value = v

        number_of_logs = property(
            lambda self: self.__number_of_logs._value,
            __set_number_of_logs,
            None,
            """Number of logs.  Number of data logs in the device.  Returned
            for LRC_BAD_LOG_INDEX responses."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_log_record(v.__log_record)
            self.__set_closest_version(v.__closest_version)
            self.__set_number_of_logs(v.__number_of_logs)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=341,
            scope=0
        )

        self.__response = SCPTlogResponse.responseType(
        )
        self._register(('response', self.__response))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 341
        self._definition = standard.add(self)

    def __set_response(self, v):
        self.__response._value = v

    response = property(
        lambda self: self.__response._value,
        __set_response,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_response(v.__response)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 16


if __name__ == '__main__':
    # unit test code.
    item = SCPTlogResponse()
    pass
