"""SNVT_ctrl_resp standard datapoint type, originally defined in resource
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
from pylon.resources.control_resp_t import control_resp_t


class SNVT_ctrl_resp(base.Structure):
    """SNVT_ctrl_resp standard datapoint type.  Control response.  (status,
    sender, controller ID.)."""

    class senderType(base.Union):

        class range_Type(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__lower = base.Scaled(
                    size=2,
                    signed=False,
                    invalid=65535,
                    minimum=1,
                    maximum=65535
                )
                self._register(('lower', self.__lower))

                self.__upper = base.Scaled(
                    size=2,
                    signed=False,
                    invalid=65535,
                    minimum=1,
                    maximum=65535
                )
                self._register(('upper', self.__upper))

            def __set_lower(self, v):
                self.__lower._value = v

            lower = property(
                lambda self: self.__lower._value,
                __set_lower,
                None,
                """Sender range lower ID.  (ID number.)."""
            )

            def __set_upper(self, v):
                self.__upper._value = v

            upper = property(
                lambda self: self.__upper._value,
                __set_upper,
                None,
                """Sender range upper ID.  (ID number.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_lower(v.__lower)
                self.__set_upper(v.__upper)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 4

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__id_ = base.Scaled(
                size=2,
                signed=False,
                invalid=65535,
                minimum=1,
                maximum=65535
            )
            self._register(('id_', self.__id_))

            self.__range_ = SNVT_ctrl_resp.senderType.range_Type(
            )
            self._register(('range_', self.__range_))

        def __set_id_(self, v):
            self.__id_._value = v

        id_ = property(
            lambda self: self.__id_._value,
            __set_id_,
            None,
            """Sender ID.  (ID number.)."""
        )

        def __set_range_(self, v):
            self.__range_._value = v

        range_ = property(
            lambda self: self.__range_._value,
            __set_range_,
            None,
            """Sender ID range.  (lower, upper.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_id_(v.__id_)
            self.__set_range_(v.__range_)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=149,
            scope=0
        )

        self.__status = control_resp_t(
        )
        self._register(('status', self.__status))

        self.__sender = SNVT_ctrl_resp.senderType(
        )
        self._register(('sender', self.__sender))

        self.__controller_id = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=1,
            maximum=65535
        )
        self._register(('controller_id', self.__controller_id))
        self._definition = standard.add(self)


    def __set_status(self, v):
        self.__status._value = v

    status = property(
        lambda self: self.__status._value,
        __set_status,
        None,
        """Control response type.  (control response type names.)."""
    )

    def __set_sender(self, v):
        self.__sender._value = v

    sender = property(
        lambda self: self.__sender._value,
        __set_sender,
        None,
        """Sender ID."""
    )

    def __set_controller_id(self, v):
        self.__controller_id._value = v

    controller_id = property(
        lambda self: self.__controller_id._value,
        __set_controller_id,
        None,
        """Controller ID.  (ID number.)."""
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
        self.__set_sender(v.__sender)
        self.__set_controller_id(v.__controller_id)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 7


if __name__ == '__main__':
    # unit test code.
    item = SNVT_ctrl_resp()
    pass
