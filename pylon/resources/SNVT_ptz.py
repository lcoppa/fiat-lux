"""SNVT_ptz standard datapoint type, originally defined in resource file set
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.pan_dir_t import pan_dir_t
from pylon.resources.tilt_dir_t import tilt_dir_t
from pylon.resources.zoom_t import zoom_t


class SNVT_ptz(base.Structure):
    """SNVT_ptz standard datapoint type.  Camera PTZ.  (pan, pan speed, tilt,
    tilt speed, zoom, zoom speed.)."""

    def __init__(self):
        super().__init__(
            key=150,
            scope=0
        )

        self.__pan_dir = pan_dir_t(
        )
        self._register(('pan_dir', self.__pan_dir))

        self.__pan_speed = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.4, 0),
            minimum=0,
            maximum=100
        )
        self._register(('pan_speed', self.__pan_speed))

        self.__tilt_dir = tilt_dir_t(
        )
        self._register(('tilt_dir', self.__tilt_dir))

        self.__tilt_speed = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.4, 0),
            minimum=0,
            maximum=100
        )
        self._register(('tilt_speed', self.__tilt_speed))

        self.__zoom = zoom_t(
        )
        self._register(('zoom', self.__zoom))

        self.__zoom_speed = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.4, 0),
            minimum=0,
            maximum=100
        )
        self._register(('zoom_speed', self.__zoom_speed))
        self._definition = standard.add(self)


    def __set_pan_dir(self, v):
        self.__pan_dir._value = v

    pan_dir = property(
        lambda self: self.__pan_dir._value,
        __set_pan_dir,
        None,
        """Pan direction.  (pan direction names.)."""
    )

    def __set_pan_speed(self, v):
        self.__pan_speed._value = v

    pan_speed = property(
        lambda self: self.__pan_speed._value,
        __set_pan_speed,
        None,
        """Pan speed.  (% of full level.)."""
    )

    def __set_tilt_dir(self, v):
        self.__tilt_dir._value = v

    tilt_dir = property(
        lambda self: self.__tilt_dir._value,
        __set_tilt_dir,
        None,
        """Tilt direction.  (tilt direction names.)."""
    )

    def __set_tilt_speed(self, v):
        self.__tilt_speed._value = v

    tilt_speed = property(
        lambda self: self.__tilt_speed._value,
        __set_tilt_speed,
        None,
        """Tilt speed.  (% of full level.)."""
    )

    def __set_zoom(self, v):
        self.__zoom._value = v

    zoom = property(
        lambda self: self.__zoom._value,
        __set_zoom,
        None,
        """Zoom direction.  (zoom direction names.)."""
    )

    def __set_zoom_speed(self, v):
        self.__zoom_speed._value = v

    zoom_speed = property(
        lambda self: self.__zoom_speed._value,
        __set_zoom_speed,
        None,
        """Zoom speed.  (% of full level.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_pan_dir(v.__pan_dir)
        self.__set_pan_speed(v.__pan_speed)
        self.__set_tilt_dir(v.__tilt_dir)
        self.__set_tilt_speed(v.__tilt_speed)
        self.__set_zoom(v.__zoom)
        self.__set_zoom_speed(v.__zoom_speed)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_ptz()
    pass
