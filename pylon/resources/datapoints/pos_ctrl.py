"""pos_ctrl standard datapoint type, originally defined in resource file set
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
import pylon.resources.enumerations.cam_func_t
import pylon.resources.enumerations.cam_act_t
import pylon.resources.datapoints.angle_deg
import pylon.resources.datapoints.lev_percent


class pos_ctrl(pylon.resources.base.Structure):
    """pos_ctrl standard datapoint type.  Position control.  (receiver,
    controller ID, controller priority, function, action, value.)."""

    class valueType(pylon.resources.base.Union):

        class absposType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__pan = pylon.resources.datapoints.angle_deg.angle_deg(
                )
                self._register(('pan', self.__pan))

                self.__tilt = pylon.resources.datapoints.angle_deg.angle_deg(
                )
                self._register(('tilt', self.__tilt))

                self.__zoom = pylon.resources.datapoints.lev_percent.lev_percent(
                )
                self._register(('zoom', self.__zoom))

            def __set_pan(self, v):
                self.__pan._value = v

            pan = property(
                lambda self: self.__pan._value,
                __set_pan,
                None,
                """Pan position."""
            )

            def __set_tilt(self, v):
                self.__tilt._value = v

            tilt = property(
                lambda self: self.__tilt._value,
                __set_tilt,
                None,
                """Tilt position."""
            )

            def __set_zoom(self, v):
                self.__zoom._value = v

            zoom = property(
                lambda self: self.__zoom._value,
                __set_zoom,
                None,
                """Zoom position."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_pan(v.__pan)
                self.__set_tilt(v.__tilt)
                self.__set_zoom(v.__zoom)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 6

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__number = pylon.resources.base.Scaled(
                size=1,
                signed=False,
                invalid=0,
                minimum=0,
                maximum=255
            )
            self._register(('number', self.__number))

            self.__abspos = pos_ctrl.valueType.absposType(
            )
            self._register(('abspos', self.__abspos))

        def __set_number(self, v):
            self.__number._value = v

        number = property(
            lambda self: self.__number._value,
            __set_number,
            None,
            """Action number.  (action number.)."""
        )

        def __set_abspos(self, v):
            self.__abspos._value = v

        abspos = property(
            lambda self: self.__abspos._value,
            __set_abspos,
            None,
            """Function absolute values.  (pan, tilt, zoom.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_number(v.__number)
            self.__set_abspos(v.__abspos)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=152,
            scope=0
        )

        self.__receiver_id = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=65535
        )
        self._register(('receiver_id', self.__receiver_id))

        self.__controller_id = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=65535
        )
        self._register(('controller_id', self.__controller_id))

        self.__controller_prio = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=100
        )
        self._register(('controller_prio', self.__controller_prio))

        self.__function = pylon.resources.enumerations.cam_func_t.cam_func_t(
        )
        self._register(('function', self.__function))

        self.__action = pylon.resources.enumerations.cam_act_t.cam_act_t(
        )
        self._register(('action', self.__action))

        self.__value = pos_ctrl.valueType(
        )
        self._register(('value', self.__value))
        self._original_name = 'SNVT_pos_ctrl'
        self._definition = standard.add(self)


    def __set_receiver_id(self, v):
        self.__receiver_id._value = v

    receiver_id = property(
        lambda self: self.__receiver_id._value,
        __set_receiver_id,
        None,
        """Receiver ID.  (ID number.)."""
    )

    def __set_controller_id(self, v):
        self.__controller_id._value = v

    controller_id = property(
        lambda self: self.__controller_id._value,
        __set_controller_id,
        None,
        """Controller ID.  (ID number.)."""
    )

    def __set_controller_prio(self, v):
        self.__controller_prio._value = v

    controller_prio = property(
        lambda self: self.__controller_prio._value,
        __set_controller_prio,
        None,
        """Controller priority.  (priority value.)."""
    )

    def __set_function(self, v):
        self.__function._value = v

    function = property(
        lambda self: self.__function._value,
        __set_function,
        None,
        """Camera function.  (camera function names.)."""
    )

    def __set_action(self, v):
        self.__action._value = v

    action = property(
        lambda self: self.__action._value,
        __set_action,
        None,
        """Camera action.  (camera action names.)."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None,
        """Function value."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_receiver_id(v.__receiver_id)
        self.__set_controller_id(v.__controller_id)
        self.__set_controller_prio(v.__controller_prio)
        self.__set_function(v.__function)
        self.__set_action(v.__action)
        self.__set_value(v.__value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 13


if __name__ == '__main__':
    # unit test code.
    item = pos_ctrl()
    pass
