"""SNVT_ex_control standard datapoint type, originally defined in resource
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
from pylon.resources.ex_control_t import ex_control_t


class SNVT_ex_control(base.Structure):
    """SNVT_ex_control standard datapoint type.  Exclusive control.  (status,
    address.)."""

    class control_device_addrType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__domain_id = base.Array(
                [
                    base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=255
                    ) for i in range(6)
                ]
            )
            self._register(('domain_id', self.__domain_id))

            self.__domain_length = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=6
            )
            self._register(('domain_length', self.__domain_length))

            self.__subnet = base.Scaled(
                size=1,
                signed=False,
                invalid=0,
                minimum=0,
                maximum=255
            )
            self._register(('subnet', self.__subnet))

            self.__node = base.Scaled(
                size=1,
                signed=False,
                invalid=0,
                minimum=0,
                maximum=127
            )
            self._register(('node', self.__node))

        def __set_domain_id(self, v):
            self.__domain_id._value = v

        domain_id = property(
            lambda self: self.__domain_id._value,
            __set_domain_id,
            None,
            """Domain ID.  ANSI/CEA-709.1 domain ID.  (array of 6 bytes.)."""
        )

        def __set_domain_length(self, v):
            self.__domain_length._value = v

        domain_length = property(
            lambda self: self.__domain_length._value,
            __set_domain_length,
            None,
            """Domain length.  Valid domain lengths are 0, 1, 3, and 6.
            (ANSI/CEA-709.1 domain length.)."""
        )

        def __set_subnet(self, v):
            self.__subnet._value = v

        subnet = property(
            lambda self: self.__subnet._value,
            __set_subnet,
            None,
            """Subnet There can be 255 subnets (1-255) in a domain.  (subnet
            number.)."""
        )

        def __set_node(self, v):
            self.__node._value = v

        node = property(
            lambda self: self.__node._value,
            __set_node,
            None,
            """Node There can be 127 nodes (1-127) in a subnet.  (node
            number.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_domain_id(v.__domain_id)
            self.__set_domain_length(v.__domain_length)
            self.__set_subnet(v.__subnet)
            self.__set_node(v.__node)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 9

    def __init__(self):
        super().__init__(
            key=157,
            scope=0
        )

        self.__control_status = ex_control_t(
        )
        self._register(('control_status', self.__control_status))

        self.__control_device_addr = SNVT_ex_control.control_device_addrType(
        )
        self._register(('control_device_addr', self.__control_device_addr))
        self._definition = standard.add(self)


    def __set_control_status(self, v):
        self.__control_status._value = v

    control_status = property(
        lambda self: self.__control_status._value,
        __set_control_status,
        None,
        """Control type.  (control type names.)."""
    )

    def __set_control_device_addr(self, v):
        self.__control_device_addr._value = v

    control_device_addr = property(
        lambda self: self.__control_device_addr._value,
        __set_control_device_addr,
        None,
        """Control device address.  (LonWorks subnet-node address.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_control_status(v.__control_status)
        self.__set_control_device_addr(v.__control_device_addr)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 10


if __name__ == '__main__':
    # unit test code.
    item = SNVT_ex_control()
    pass
