"""SCPTbuttonColor standard property type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTbuttonColor(base.Structure):
    """SCPTbuttonColor standard property type.  Button color.  Button color
    configuration for on and off states of a button.  May be used to create
    an array that is used with a SCPTbuttonAction array to specify keypad
    button behavior."""

    class on_colorType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__red = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('red', self.__red))

            self.__green = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('green', self.__green))

            self.__blue = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('blue', self.__blue))

        def __set_red(self, v):
            self.__red._value = v

        red = property(
            lambda self: self.__red._value,
            __set_red,
            None,
            """Red.  Red level component of the on state color."""
        )

        def __set_green(self, v):
            self.__green._value = v

        green = property(
            lambda self: self.__green._value,
            __set_green,
            None,
            """Green.  Green level component of the on state color."""
        )

        def __set_blue(self, v):
            self.__blue._value = v

        blue = property(
            lambda self: self.__blue._value,
            __set_blue,
            None,
            """Blue.  Blue level component of the on state color."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_red(v.__red)
            self.__set_green(v.__green)
            self.__set_blue(v.__blue)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 3

    class off_colorType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__red = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('red', self.__red))

            self.__green = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('green', self.__green))

            self.__blue = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('blue', self.__blue))

        def __set_red(self, v):
            self.__red._value = v

        red = property(
            lambda self: self.__red._value,
            __set_red,
            None,
            """Red.  Red level component of the off state color."""
        )

        def __set_green(self, v):
            self.__green._value = v

        green = property(
            lambda self: self.__green._value,
            __set_green,
            None,
            """Green.  Green level component of the off state color."""
        )

        def __set_blue(self, v):
            self.__blue._value = v

        blue = property(
            lambda self: self.__blue._value,
            __set_blue,
            None,
            """Blue.  Blue level component of the off state color."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_red(v.__red)
            self.__set_green(v.__green)
            self.__set_blue(v.__blue)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 3

    def __init__(self):
        super().__init__(
            key=312,
            scope=0
        )

        self.__on_color = SCPTbuttonColor.on_colorType(
        )
        self._register(('on_color', self.__on_color))

        self.__off_color = SCPTbuttonColor.off_colorType(
        )
        self._register(('off_color', self.__off_color))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 312
        self._definition = standard.add(self)

    def __set_on_color(self, v):
        self.__on_color._value = v

    on_color = property(
        lambda self: self.__on_color._value,
        __set_on_color,
        None,
        """On color.  RGB color for the on state."""
    )

    def __set_off_color(self, v):
        self.__off_color._value = v

    off_color = property(
        lambda self: self.__off_color._value,
        __set_off_color,
        None,
        """Off color.  RGB color for the off state."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_on_color(v.__on_color)
        self.__set_off_color(v.__off_color)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SCPTbuttonColor()
    pass
