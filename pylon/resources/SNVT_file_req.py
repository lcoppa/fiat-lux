"""SNVT_file_req standard datapoint type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.file_request_t import file_request_t


class SNVT_file_req(base.Structure):
    """SNVT_file_req standard datapoint type.  File request."""

    class dest_addressType(base.Union):

        class addrtType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__type_ = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=33,
                    maximum=33
                )
                self._register(('type_', self.__type_))

                self.__index = base.Scaled(
                    size=2,
                    signed=False,
                    minimum=0,
                    maximum=65535
                )
                self._register(('index', self.__index))

            def __set_type_(self, v):
                self.__type_._value = v

            type_ = property(
                lambda self: self.__type_._value,
                __set_type_,
                None,
                """Address type.  The address-table address type is 33
                (0x21).  (8-bit unsigned value.)."""
            )

            def __set_index(self, v):
                self.__index._value = v

            index = property(
                lambda self: self.__index._value,
                __set_index,
                None,
                """Address table index.  (16-bit unsigned value.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_type_(v.__type_)
                self.__set_index(v.__index)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class snType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__type_ = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=1,
                    maximum=1
                )
                self._register(('type_', self.__type_))

                self.___bf00 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf00', self.___bf00))

                self.___bf01 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))

                self.__subnet = base.Scaled(
                    size=1,
                    signed=False,
                    invalid=0,
                    minimum=0,
                    maximum=255
                )
                self._register(('subnet', self.__subnet))

            def __set_type_(self, v):
                self.__type_._value = v

            type_ = property(
                lambda self: self.__type_._value,
                __set_type_,
                None,
                """Address type.  The subnet-node address type is 1.  (8-bit
                unsigned value.)."""
            )
            def __set_domain(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_domain(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            domain = property(
                __get_domain,
                __set_domain,
                None,
                """LonWorks domain index."""
            )

            def __set_node(self, v):
                if 0 <= v <= 127:
                    self.___bf00._setbits(
                        value=v,
                        size=7,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..127')

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
                """Node There can be 127 nodes (1-127) in a subnet.  (node
                number.)"""
            )

            def __set_retry(self, v):
                if 0 <= v <= 15:
                    self.___bf01._setbits(
                        value=v,
                        size=4,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_retry(self):
                return self.___bf01._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            retry = property(
                __get_retry,
                __set_retry,
                None,
                """number of retries."""
            )

            def __set_tx_timer(self, v):
                if 0 <= v <= 15:
                    self.___bf02._setbits(
                        value=v,
                        size=4,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_tx_timer(self):
                return self.___bf02._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            tx_timer = property(
                __get_tx_timer,
                __set_tx_timer,
                None,
                """timer code value."""
            )


            def __set_subnet(self, v):
                self.__subnet._value = v

            subnet = property(
                lambda self: self.__subnet._value,
                __set_subnet,
                None,
                """Subnet There can be 255 subnets (1-255) in a domain.
                (subnet number.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_type_(v.__type_)
                self.__set_domain(v.__domain)
                self.__set_node(v.__node)
                self.__set_retry(v.__retry)
                self.__set_tx_timer(v.__tx_timer)
                self.__set_subnet(v.__subnet)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 5

        class gpType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.___bf00 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf00', self.___bf00))

                self.___bf01 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))

                self.___bf03 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf03', self.___bf03))

                self.__group = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('group', self.__group))
            def __set_type_(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_type_(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            type_ = property(
                __get_type_,
                __set_type_,
                None,
                """Address type.  The group address type is 1.  (boolean)"""
            )

            def __set_size(self, v):
                if 0 <= v <= 65:
                    self.___bf00._setbits(
                        value=v,
                        size=7,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..65')

            def __get_size(self):
                return self.___bf00._getbits(
                    size=7,
                    offset=1,
                    signed=False
                )

            size = property(
                __get_size,
                __set_size,
                None,
                """Size An acknowledged group can have from 0-64 addressees,
                plus the sender.  (LonWorks group size.)"""
            )

            def __set_domain(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_domain(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            domain = property(
                __get_domain,
                __set_domain,
                None,
                """LonWorks domain index."""
            )

            def __set_unused(self, v):
                if 0 <= v <= 0:
                    self.___bf01._setbits(
                        value=v,
                        size=7,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..0')

            def __get_unused(self):
                return self.___bf01._getbits(
                    size=7,
                    offset=1,
                    signed=False
                )

            unused = property(
                __get_unused,
                __set_unused,
                None,
                """Unused field.  This field is reserved."""
            )

            def __set_retry(self, v):
                if 0 <= v <= 15:
                    self.___bf02._setbits(
                        value=v,
                        size=4,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_retry(self):
                return self.___bf02._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            retry = property(
                __get_retry,
                __set_retry,
                None,
                """number of retries."""
            )

            def __set_tx_timer(self, v):
                if 0 <= v <= 15:
                    self.___bf03._setbits(
                        value=v,
                        size=4,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_tx_timer(self):
                return self.___bf03._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            tx_timer = property(
                __get_tx_timer,
                __set_tx_timer,
                None,
                """timer code value."""
            )


            def __set_group(self, v):
                self.__group._value = v

            group = property(
                lambda self: self.__group._value,
                __set_group,
                None,
                """Group There can be 256 groups (0-255) in a domain."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_type_(v.__type_)
                self.__set_size(v.__size)
                self.__set_domain(v.__domain)
                self.__set_unused(v.__unused)
                self.__set_retry(v.__retry)
                self.__set_tx_timer(v.__tx_timer)
                self.__set_group(v.__group)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 5

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__addrt = SNVT_file_req.dest_addressType.addrtType(
            )
            self._register(('addrt', self.__addrt))

            self.__sn = SNVT_file_req.dest_addressType.snType(
            )
            self._register(('sn', self.__sn))

            self.__gp = SNVT_file_req.dest_addressType.gpType(
            )
            self._register(('gp', self.__gp))

        def __set_addrt(self, v):
            self.__addrt._value = v

        addrt = property(
            lambda self: self.__addrt._value,
            __set_addrt,
            None,
            """Address table entry.  ANSI/CEA-709.1 address in device's
            internal address table entry.  (Address table entry.)."""
        )

        def __set_sn(self, v):
            self.__sn._value = v

        sn = property(
            lambda self: self.__sn._value,
            __set_sn,
            None,
            """Subnet-node address.  (LonWorks subnet-node address.)."""
        )

        def __set_gp(self, v):
            self.__gp._value = v

        gp = property(
            lambda self: self.__gp._value,
            __set_gp,
            None,
            """Group address.  (LonWorks group address.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_addrt(v.__addrt)
            self.__set_sn(v.__sn)
            self.__set_gp(v.__gp)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=73,
            scope=0
        )

        self.__request = file_request_t(
        )
        self._register(('request', self.__request))

        self.__index = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('index', self.__index))

        self.__receive_timeout = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('receive_timeout', self.__receive_timeout))

        self.__dest_address = SNVT_file_req.dest_addressType(
        )
        self._register(('dest_address', self.__dest_address))

        self.__auth_on = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=1
        )
        self._register(('auth_on', self.__auth_on))

        self.__prio_on = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=1
        )
        self._register(('prio_on', self.__prio_on))
        self._definition = standard.add(self)


    def __set_request(self, v):
        self.__request._value = v

    request = property(
        lambda self: self.__request._value,
        __set_request,
        None,
        """Request (file request names.)."""
    )

    def __set_index(self, v):
        self.__index._value = v

    index = property(
        lambda self: self.__index._value,
        __set_index,
        None,
        """Index (file index.)."""
    )

    def __set_receive_timeout(self, v):
        self.__receive_timeout._value = v

    receive_timeout = property(
        lambda self: self.__receive_timeout._value,
        __set_receive_timeout,
        None,
        """Receive timeout.  (milliseconds)."""
    )

    def __set_dest_address(self, v):
        self.__dest_address._value = v

    dest_address = property(
        lambda self: self.__dest_address._value,
        __set_dest_address,
        None,
        """Destination address.  (LonWorks address.)."""
    )

    def __set_auth_on(self, v):
        self.__auth_on._value = v

    auth_on = property(
        lambda self: self.__auth_on._value,
        __set_auth_on,
        None,
        """Authentication on.  This field specifies whether the message
        requires authentication.  (boolean)."""
    )

    def __set_prio_on(self, v):
        self.__prio_on._value = v

    prio_on = property(
        lambda self: self.__prio_on._value,
        __set_prio_on,
        None,
        """Priority on.  This field specifies whether the message is to be
        sent with priority.  (boolean)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_request(v.__request)
        self.__set_index(v.__index)
        self.__set_receive_timeout(v.__receive_timeout)
        self.__set_dest_address(v.__dest_address)
        self.__set_auth_on(v.__auth_on)
        self.__set_prio_on(v.__prio_on)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 12


if __name__ == '__main__':
    # unit test code.
    item = SNVT_file_req()
    pass
