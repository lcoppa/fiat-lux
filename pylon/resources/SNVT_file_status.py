"""SNVT_file_status standard datapoint type, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.file_status_t import file_status_t


class SNVT_file_status(base.Structure):
    """SNVT_file_status standard datapoint type.  File status."""

    class adrType(base.Union):

        class descriptorType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__file_info = base.Array(
                    [
                        base.Scaled(
                            size=1,
                            signed=True,
                            minimum=-128,
                            maximum=127
                        ) for i in range(16)
                    ]
                )
                self._register(('file_info', self.__file_info))

                self.__size = base.Scaled(
                    size=4,
                    signed=True,
                    minimum=0,
                    maximum=2147483647
                )
                self._register(('size', self.__size))

                self.__type_ = base.Scaled(
                    size=2,
                    signed=False,
                    minimum=0,
                    maximum=65535
                )
                self._register(('type_', self.__type_))

            def __set_file_info(self, v):
                self.__file_info._value = v

            file_info = property(
                lambda self: self.__file_info._value,
                __set_file_info,
                None,
                """File info.  (array of 16 characters.)."""
            )

            def __set_size(self, v):
                self.__size._value = v

            size = property(
                lambda self: self.__size._value,
                __set_size,
                None,
                """Size (bytes)."""
            )

            def __set_type_(self, v):
                self.__type_._value = v

            type_ = property(
                lambda self: self.__type_._value,
                __set_type_,
                None,
                """Type."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_file_info(v.__file_info)
                self.__set_size(v.__size)
                self.__set_type_(v.__type_)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 22

        class addressType(base.Structure):

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
                """Domain ID.  ANSI/CEA-709.1 domain ID.  (array of 6
                bytes.)."""
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
                """Subnet There can be 255 subnets (1-255) in a domain.
                (subnet number.)."""
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
                key=-1,
                scope=-1
            )

            self.__descriptor = SNVT_file_status.adrType.descriptorType(
            )
            self._register(('descriptor', self.__descriptor))

            self.__address = SNVT_file_status.adrType.addressType(
            )
            self._register(('address', self.__address))

        def __set_descriptor(self, v):
            self.__descriptor._value = v

        descriptor = property(
            lambda self: self.__descriptor._value,
            __set_descriptor,
            None,
            """Descriptor."""
        )

        def __set_address(self, v):
            self.__address._value = v

        address = property(
            lambda self: self.__address._value,
            __set_address,
            None,
            """Address."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_descriptor(v.__descriptor)
            self.__set_address(v.__address)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=74,
            scope=0
        )

        self.__status = file_status_t(
        )
        self._register(('status', self.__status))

        self.__number_of_files = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('number_of_files', self.__number_of_files))

        self.__selected_file = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('selected_file', self.__selected_file))

        self.__adr = SNVT_file_status.adrType(
        )
        self._register(('adr', self.__adr))
        self._definition = standard.add(self)


    def __set_status(self, v):
        self.__status._value = v

    status = property(
        lambda self: self.__status._value,
        __set_status,
        None,
        """Status (file status names.)."""
    )

    def __set_number_of_files(self, v):
        self.__number_of_files._value = v

    number_of_files = property(
        lambda self: self.__number_of_files._value,
        __set_number_of_files,
        None,
        """Number of files.  (count)."""
    )

    def __set_selected_file(self, v):
        self.__selected_file._value = v

    selected_file = property(
        lambda self: self.__selected_file._value,
        __set_selected_file,
        None,
        """Selected file.  (file index.)."""
    )

    def __set_adr(self, v):
        self.__adr._value = v

    adr = property(
        lambda self: self.__adr._value,
        __set_adr,
        None,
        """Address."""
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
        self.__set_number_of_files(v.__number_of_files)
        self.__set_selected_file(v.__selected_file)
        self.__set_adr(v.__adr)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 27


if __name__ == '__main__':
    # unit test code.
    item = SNVT_file_status()
    pass
