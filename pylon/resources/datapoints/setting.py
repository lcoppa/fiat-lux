"""setting standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  """


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
import pylon.resources.enumerations.setting_t


class setting(pylon.resources.base.Structure):
    """setting standard datapoint type.  Setting control.  (function,
    setting, rotation.)."""

    def __init__(self):
        super().__init__(
            key=117,
            scope=0
        )

        self.__function = pylon.resources.enumerations.setting_t.setting_t(
        )
        self._register(('function', self.__function))

        self.__setting = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            scaling=(0.5, 0),
            invalid=127.5,
            minimum=0,
            maximum=100
        )
        self._register(('setting', self.__setting))

        self.__rotation = pylon.resources.base.Scaled(
            size=2,
            signed=True,
            scaling=(0.02, 0),
            invalid=655.34,
            minimum=-359.98,
            maximum=360
        )
        self._register(('rotation', self.__rotation))
        self._original_name = 'SNVT_setting'
        self._definition = standard.add(self)


    def __set_function(self, v):
        self.__function._value = v

    function = property(
        lambda self: self.__function._value,
        __set_function,
        None,
        """Setting control function.  (setting control function names.)."""
    )

    def __set_setting(self, v):
        self.__setting._value = v

    # member renamed to 'setting_' to avoid shadowing of the class name.
    setting_ = property(
        lambda self: self.__setting._value,
        __set_setting,
        None,
        """Scene setting level.  (% of full level.)."""
    )

    def __set_rotation(self, v):
        self.__rotation._value = v

    rotation = property(
        lambda self: self.__rotation._value,
        __set_rotation,
        None,
        """Rotation angle.  (degrees)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_function(v.__function)
        self.__set_setting(v.__setting)
        self.__set_rotation(v.__rotation)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = setting()
    pass
