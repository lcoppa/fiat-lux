"""SNVT_sec_status standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  Note this resource is marked as
obsolete.  It should not be used for new development, but continued use in
existing designs is permitted."""


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
from pylon.resources.sec_status_t import sec_status_t


class SNVT_sec_status(base.Structure):
    """SNVT_sec_status standard datapoint type.  Security Status.  Status
    information from a security device."""

    def __init__(self):
        super().__init__(
            key=179,
            scope=0
        )

        self.__status = sec_status_t(
        )
        self._register(('status', self.__status))

        self.__identity = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('identity', self.__identity))
        self._mark_obsolete()
        self._definition = standard.add(self)


    def __set_status(self, v):
        self.__status._value = v

    status = property(
        lambda self: self.__status._value,
        __set_status,
        None,
        """."""
    )

    def __set_identity(self, v):
        self.__identity._value = v

    identity = property(
        lambda self: self.__identity._value,
        __set_identity,
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
        self.__set_status(v.__status)
        self.__set_identity(v.__identity)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SNVT_sec_status()
    pass
