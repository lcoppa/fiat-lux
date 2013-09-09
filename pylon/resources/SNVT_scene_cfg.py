"""SNVT_scene_cfg standard datapoint type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.scene_config_t import scene_config_t


class SNVT_scene_cfg(base.Structure):
    """SNVT_scene_cfg standard datapoint type.  Scene configuration.
    (function, scene number, setting, rotation, fade, delay, priority.)."""

    def __init__(self):
        super().__init__(
            key=116,
            scope=0
        )

        self.__function = scene_config_t(
        )
        self._register(('function', self.__function))

        self.__scene_number = base.Scaled(
            size=1,
            signed=False,
            minimum=1,
            maximum=255
        )
        self._register(('scene_number', self.__scene_number))

        self.__setting = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.5, 0),
            invalid=127.5,
            minimum=0,
            maximum=100
        )
        self._register(('setting', self.__setting))

        self.__rotation = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.02, 0),
            invalid=655.34,
            minimum=-359.98,
            maximum=360
        )
        self._register(('rotation', self.__rotation))

        self.__fade_time = base.Scaled(
            size=2,
            signed=False,
            scaling=(0.1, 0),
            invalid=6553.5,
            minimum=0,
            maximum=6553.5
        )
        self._register(('fade_time', self.__fade_time))

        self.__delay_time = base.Scaled(
            size=2,
            signed=False,
            scaling=(0.1, 0),
            invalid=6553.5,
            minimum=0,
            maximum=6553.5
        )
        self._register(('delay_time', self.__delay_time))

        self.__scene_priority = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('scene_priority', self.__scene_priority))
        self._definition = standard.add(self)


    def __set_function(self, v):
        self.__function._value = v

    function = property(
        lambda self: self.__function._value,
        __set_function,
        None,
        """Scene configuration function.  (scene configuration function
        names.)."""
    )

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number."""
    )

    def __set_setting(self, v):
        self.__setting._value = v

    setting = property(
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
        """Scene rotation angle.  (degrees)."""
    )

    def __set_fade_time(self, v):
        self.__fade_time._value = v

    fade_time = property(
        lambda self: self.__fade_time._value,
        __set_fade_time,
        None,
        """Scene fade time.  (seconds)."""
    )

    def __set_delay_time(self, v):
        self.__delay_time._value = v

    delay_time = property(
        lambda self: self.__delay_time._value,
        __set_delay_time,
        None,
        """Scene delay time.  (seconds)."""
    )

    def __set_scene_priority(self, v):
        self.__scene_priority._value = v

    scene_priority = property(
        lambda self: self.__scene_priority._value,
        __set_scene_priority,
        None,
        """Scene priority.  (priority value.)."""
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
        self.__set_scene_number(v.__scene_number)
        self.__set_setting(v.__setting)
        self.__set_rotation(v.__rotation)
        self.__set_fade_time(v.__fade_time)
        self.__set_delay_time(v.__delay_time)
        self.__set_scene_priority(v.__scene_priority)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 10


if __name__ == '__main__':
    # unit test code.
    item = SNVT_scene_cfg()
    pass
