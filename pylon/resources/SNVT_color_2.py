"""SNVT_color_2 standard datapoint type, originally defined in resource file
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.color_encoding_t import color_encoding_t


class SNVT_color_2(base.Structure):
    """SNVT_color_2 standard datapoint type.  Color."""

    class color_valueType(base.Union):

        class CIE1931_lumenType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__x = base.Scaled(
                    size=1,
                    signed=False,
                    scaling=(0.005, 0),
                    invalid=1.275,
                    minimum=0,
                    maximum=0.74
                )
                self._register(('x', self.__x))

                self.__y = base.Scaled(
                    size=1,
                    signed=False,
                    scaling=(0.005, 0),
                    invalid=1.275,
                    minimum=0,
                    maximum=0.84
                )
                self._register(('y', self.__y))

                self.__absolute_Y = base.Scaled(
                    size=2,
                    signed=False,
                    scaling=(10, 0),
                    invalid=655350,
                    minimum=0,
                    maximum=655340
                )
                self._register(('absolute_Y', self.__absolute_Y))

            def __set_x(self, v):
                self.__x._value = v

            x = property(
                lambda self: self.__x._value,
                __set_x,
                None,
                """CIE 1931 x value.  CIE 1931 x-axis color value.  (CIE 1931
                color space coordinate.)."""
            )

            def __set_y(self, v):
                self.__y._value = v

            y = property(
                lambda self: self.__y._value,
                __set_y,
                None,
                """CIE 1931 y value.  CIE 1931 y-axis color value.  (CIE 1931
                color space coordinate.)."""
            )

            def __set_absolute_Y(self, v):
                self.__absolute_Y._value = v

            absolute_Y = property(
                lambda self: self.__absolute_Y._value,
                __set_absolute_Y,
                None,
                """Absolute luminance.  Absolute luminance.  (lumen)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_x(v.__x)
                self.__set_y(v.__y)
                self.__set_absolute_Y(v.__absolute_Y)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 4

        class CIE1931_percentType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__x = base.Scaled(
                    size=1,
                    signed=False,
                    scaling=(0.005, 0),
                    invalid=1.275,
                    minimum=0,
                    maximum=0.74
                )
                self._register(('x', self.__x))

                self.__y = base.Scaled(
                    size=1,
                    signed=False,
                    scaling=(0.005, 0),
                    invalid=1.275,
                    minimum=0,
                    maximum=0.84
                )
                self._register(('y', self.__y))

                self.__percent_Y = base.Scaled(
                    size=2,
                    signed=False,
                    scaling=(0.01, 0),
                    invalid=655.35,
                    minimum=0,
                    maximum=100
                )
                self._register(('percent_Y', self.__percent_Y))

            def __set_x(self, v):
                self.__x._value = v

            x = property(
                lambda self: self.__x._value,
                __set_x,
                None,
                """CIE 1931 x value.  CIE 1931 x-axis color value.  (CIE 1931
                color space coordinate.)."""
            )

            def __set_y(self, v):
                self.__y._value = v

            y = property(
                lambda self: self.__y._value,
                __set_y,
                None,
                """CIE 1931 y value.  CIE 1931 y-axis color value.  (CIE 1931
                color space coordinate.)."""
            )

            def __set_percent_Y(self, v):
                self.__percent_Y._value = v

            percent_Y = property(
                lambda self: self.__percent_Y._value,
                __set_percent_Y,
                None,
                """Luminance Y output in percent of maximum lumen output of
                the lamp.  (% of full level.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_x(v.__x)
                self.__set_y(v.__y)
                self.__set_percent_Y(v.__percent_Y)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 4

        class RGBType(base.Structure):

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
                """Red component.  Red component for RGB color."""
            )

            def __set_green(self, v):
                self.__green._value = v

            green = property(
                lambda self: self.__green._value,
                __set_green,
                None,
                """Green component.  Green component for RGB color."""
            )

            def __set_blue(self, v):
                self.__blue._value = v

            blue = property(
                lambda self: self.__blue._value,
                __set_blue,
                None,
                """Blue component.  Blue component for RGB color."""
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
                key=-1,
                scope=-1
            )

            self.__CIE1931_lumen = SNVT_color_2.color_valueType.CIE1931_lumenType(
            )
            self._register(('CIE1931_lumen', self.__CIE1931_lumen))

            self.__CIE1931_percent = SNVT_color_2.color_valueType.CIE1931_percentType(
            )
            self._register(('CIE1931_percent', self.__CIE1931_percent))

            self.__RGB = SNVT_color_2.color_valueType.RGBType(
            )
            self._register(('RGB', self.__RGB))

            self.__color_temperature = base.Scaled(
                size=1,
                signed=False,
                scaling=(50, 0),
                invalid=12750,
                minimum=2800,
                maximum=7500
            )
            self._register(('color_temperature', self.__color_temperature))

        def __set_CIE1931_lumen(self, v):
            self.__CIE1931_lumen._value = v

        CIE1931_lumen = property(
            lambda self: self.__CIE1931_lumen._value,
            __set_CIE1931_lumen,
            None,
            """CIE 1931 color space with lumen.  CIE 1931 color space with Y
            output in lumen."""
        )

        def __set_CIE1931_percent(self, v):
            self.__CIE1931_percent._value = v

        CIE1931_percent = property(
            lambda self: self.__CIE1931_percent._value,
            __set_CIE1931_percent,
            None,
            """CIE 1931 color space with percent.  CIE 1931 color space with
            Y output in percent of maximum lumen output of the lamp."""
        )

        def __set_RGB(self, v):
            self.__RGB._value = v

        RGB = property(
            lambda self: self.__RGB._value,
            __set_RGB,
            None,
            """RGB color value."""
        )

        def __set_color_temperature(self, v):
            self.__color_temperature._value = v

        color_temperature = property(
            lambda self: self.__color_temperature._value,
            __set_color_temperature,
            None,
            """Color temperature.  (degrees Kelvin.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_CIE1931_lumen(v.__CIE1931_lumen)
            self.__set_CIE1931_percent(v.__CIE1931_percent)
            self.__set_RGB(v.__RGB)
            self.__set_color_temperature(v.__color_temperature)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=190,
            scope=0
        )

        self.__encoding = color_encoding_t(
        )
        self._register(('encoding', self.__encoding))

        self.__color_value = SNVT_color_2.color_valueType(
        )
        self._register(('color_value', self.__color_value))
        self._definition = standard.add(self)


    def __set_encoding(self, v):
        self.__encoding._value = v

    encoding = property(
        lambda self: self.__encoding._value,
        __set_encoding,
        None,
        """Color encoding.  Color encoding specified by the color_value
        union;  additional encodings may be added."""
    )

    def __set_color_value(self, v):
        self.__color_value._value = v

    color_value = property(
        lambda self: self.__color_value._value,
        __set_color_value,
        None,
        """Color value.  Color value encoded as specified by the encoding
        field."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_encoding(v.__encoding)
        self.__set_color_value(v.__color_value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SNVT_color_2()
    pass
