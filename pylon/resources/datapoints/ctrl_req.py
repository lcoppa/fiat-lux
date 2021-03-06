"""ctrl_req standard datapoint type, originally defined in resource file set
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


class ctrl_req(pylon.resources.base.Structure):
    """ctrl_req standard datapoint type.  Control request.  (receiver ID,
    sender ID, sender priority.)."""

    def __init__(self):
        super().__init__(
            key=148,
            scope=0
        )

        self.__receiver_id = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('receiver_id', self.__receiver_id))

        self.__sender_id = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=1,
            maximum=65535
        )
        self._register(('sender_id', self.__sender_id))

        self.__sender_prio = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=200
        )
        self._register(('sender_prio', self.__sender_prio))
        self._original_name = 'SNVT_ctrl_req'
        self._definition = standard.add(self)


    def __set_receiver_id(self, v):
        self.__receiver_id._value = v

    receiver_id = property(
        lambda self: self.__receiver_id._value,
        __set_receiver_id,
        None,
        """Receiver ID.  (ID number.)."""
    )

    def __set_sender_id(self, v):
        self.__sender_id._value = v

    sender_id = property(
        lambda self: self.__sender_id._value,
        __set_sender_id,
        None,
        """Sender ID.  (ID number.)."""
    )

    def __set_sender_prio(self, v):
        self.__sender_prio._value = v

    sender_prio = property(
        lambda self: self.__sender_prio._value,
        __set_sender_prio,
        None,
        """Sender priority.  (priority value.)."""
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
        self.__set_sender_id(v.__sender_id)
        self.__set_sender_prio(v.__sender_prio)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = ctrl_req()
    pass
