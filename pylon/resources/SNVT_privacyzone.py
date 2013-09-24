"""SNVT_privacyzone standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


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
from pylon.resources.privacyzone_t import privacyzone_t


class SNVT_privacyzone(base.Structure):
    """SNVT_privacyzone standard datapoint type.  Privacy zone.  (action,
    zone number, camera ID.)."""

    def __init__(self):
        super().__init__(
            key=151,
            scope=0
        )

        self.__action = privacyzone_t(
        )
        self._register(('action', self.__action))

        self.__number = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=255
        )
        self._register(('number', self.__number))

        self.__camera_id = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=65535
        )
        self._register(('camera_id', self.__camera_id))
        self._definition = standard.add(self)


    def __set_action(self, v):
        self.__action._value = v

    action = property(
        lambda self: self.__action._value,
        __set_action,
        None,
        """Privacy zone action type.  (privacy zone action type names.)."""
    )

    def __set_number(self, v):
        self.__number._value = v

    number = property(
        lambda self: self.__number._value,
        __set_number,
        None,
        """Zone number.  (zone number.)."""
    )

    def __set_camera_id(self, v):
        self.__camera_id._value = v

    camera_id = property(
        lambda self: self.__camera_id._value,
        __set_camera_id,
        None,
        """Camera ID.  (ID number.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_action(v.__action)
        self.__set_number(v.__number)
        self.__set_camera_id(v.__camera_id)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SNVT_privacyzone()
    pass
