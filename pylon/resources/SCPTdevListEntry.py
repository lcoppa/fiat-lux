"""SCPTdevListEntry standard property type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.address_type_t import address_type_t


class SCPTdevListEntry(base.Union):
    """SCPTdevListEntry standard property type.  Device list entry.  Device
    list entry containing the address of the device to be monitored."""

    class snType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__subnet = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=255
            )
            self._register(('subnet', self.__subnet))

            self.___bf00 = base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))

        def __set_subnet(self, v):
            self.__subnet._value = v

        subnet = property(
            lambda self: self.__subnet._value,
            __set_subnet,
            None,
            """Destination subnet.  Specifies the destination subnet number
            (1-255)."""
        )
        def __set_unused(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_unused(self):
            return self.___bf00._getbits(
                size=1,
                offset=0,
                signed=False
            )

        unused = property(
            __get_unused,
            __set_unused,
            None,
            """Unused.  Set to 0."""
        )

        def __set_node(self, v):
            if 1 <= v <= 127:
                self.___bf00._setbits(
                    value=v,
                    size=7,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 1..127')

        def __get_node(self):
            return self.___bf00._getbits(
                size=7,
                offset=1,
                signed=False
            )

        node = property(
            __get_node,
            __set_node,
            None,
            """Destination node.  Specifies the destination node number
            (1-127)"""
        )


        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_subnet(v.__subnet)
            self.___bf00(v.___bf00)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 2

    class niType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__subnet = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('subnet', self.__subnet))

            self.__nid = base.Array(
                [
                    base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=255
                    ) for i in range(6)
                ]
            )
            self._register(('nid', self.__nid))

        def __set_subnet(self, v):
            self.__subnet._value = v

        subnet = property(
            lambda self: self.__subnet._value,
            __set_subnet,
            None,
            """Destination subnet.  Specifies the destination subnet number
            (1-255) or 0 if the destination subnet is unknown."""
        )

        def __set_nid(self, v):
            self.__nid._value = v

        nid = property(
            lambda self: self.__nid._value,
            __set_nid,
            None,
            """."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_subnet(v.__subnet)
            self.__set_nid(v.__nid)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 7

    def __init__(self):
        super().__init__(
            key=323,
            scope=0
        )

        self.__address_type = address_type_t(
        )
        self._register(('address_type', self.__address_type))

        self.__sn = SCPTdevListEntry.snType(
        )
        self._register(('sn', self.__sn))

        self.__ni = SCPTdevListEntry.niType(
        )
        self._register(('ni', self.__ni))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 323
        self._definition = standard.add(self)

    def __set_address_type(self, v):
        self.__address_type._value = v

    address_type = property(
        lambda self: self.__address_type._value,
        __set_address_type,
        None,
        """."""
    )

    def __set_sn(self, v):
        self.__sn._value = v

    sn = property(
        lambda self: self.__sn._value,
        __set_sn,
        None,
        """Device address as subnet/node address.  This structure is filled
        out in case the device address is given as subnet/node address."""
    )

    def __set_ni(self, v):
        self.__ni._value = v

    ni = property(
        lambda self: self.__ni._value,
        __set_ni,
        None,
        """Device address as unique node ID address.  This structure is
        filled out in case the device address is given as unique node ID
        address."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_address_type(v.__address_type)
        self.__set_sn(v.__sn)
        self.__set_ni(v.__ni)

    _value = property(lambda self: self, __set)


if __name__ == '__main__':
    # unit test code.
    item = SCPTdevListEntry()
    pass
