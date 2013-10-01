"""safe_8 standard datapoint type, originally defined in resource file set
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


class safe_8(pylon.resources.base.Structure):
    """safe_8 standard datapoint type.  Safe protocol for 8 bytes data
    length."""

    def __init__(self):
        super().__init__(
            key=208,
            scope=0
        )

        self.___bf00 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__address_a_1 = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('address_a_1', self.__address_a_1))

        self.___bf01 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf01', self.___bf01))

        self.__address_a_3 = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('address_a_3', self.__address_a_3))

        self.__time_stamp_msword = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('time_stamp_msword', self.__time_stamp_msword))

        self.__data_a = pylon.resources.base.Array(
            [
                pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(8)
            ]
        )
        self._register(('data_a', self.__data_a))

        self.__crc_a = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('crc_a', self.__crc_a))

        self.___bf02 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf02', self.___bf02))

        self.__address_b_1 = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('address_b_1', self.__address_b_1))

        self.___bf03 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf03', self.___bf03))

        self.__address_b_3 = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('address_b_3', self.__address_b_3))

        self.__time_stamp_lsword = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('time_stamp_lsword', self.__time_stamp_lsword))

        self.__data_b = pylon.resources.base.Array(
            [
                pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(8)
            ]
        )
        self._register(('data_b', self.__data_b))

        self.__crc_b = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('crc_b', self.__crc_b))
        self._original_name = 'SNVT_safe_8'
        self._definition = standard.add(self)

    def __set_id_a_header(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_id_a_header(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    id_a_header = property(
        __get_id_a_header,
        __set_id_a_header,
        None,
        """Header Header is always 0."""
    )

    def __set_id_a_format(self, v):
        if 0 <= v <= 3:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_id_a_format(self):
        return self.___bf00._getbits(
            size=2,
            offset=1,
            signed=False
        )

    id_a_format = property(
        __get_id_a_format,
        __set_id_a_format,
        None,
        """Format Information.  00:  Data 01:  CMD 10:  SEG 11:  reserved for
        future use."""
    )

    def __set_id_a_version(self, v):
        if 0 <= v <= 3:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=3
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_id_a_version(self):
        return self.___bf00._getbits(
            size=2,
            offset=3,
            signed=False
        )

    id_a_version = property(
        __get_id_a_version,
        __set_id_a_version,
        None,
        """Version Number.  00:  valid version 01:  reserved for future use
        10:  reserved for future use 11:  reserved for future use."""
    )

    def __set_id_a_length(self, v):
        if 0 <= v <= 7:
            self.___bf00._setbits(
                value=v,
                size=3,
                offset=5
            )
        else:
            raise ValueError('Not in range 0..7')

    def __get_id_a_length(self):
        return self.___bf00._getbits(
            size=3,
            offset=5,
            signed=False
        )

    id_a_length = property(
        __get_id_a_length,
        __set_id_a_length,
        None,
        """Data Length.  000:  1 Byte data length 001:  2 Byte data length
        010:  4 Byte data length 011:  8 Byte data length."""
    )


    def __set_address_a_1(self, v):
        self.__address_a_1._value = v

    address_a_1 = property(
        lambda self: self.__address_a_1._value,
        __set_address_a_1,
        None,
        """Safe Address Information SADR [1]."""
    )
    def __set_address_a_timedate(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_address_a_timedate(self):
        return self.___bf01._getbits(
            size=1,
            offset=0,
            signed=False
        )

    address_a_timedate = property(
        __get_address_a_timedate,
        __set_address_a_timedate,
        None,
        """Time / Data Service Type.  0:  Data service type 1:  Time service
        type."""
    )

    def __set_address_a_2(self, v):
        if 0 <= v <= 127:
            self.___bf01._setbits(
                value=v,
                size=7,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..127')

    def __get_address_a_2(self):
        return self.___bf01._getbits(
            size=7,
            offset=1,
            signed=False
        )

    address_a_2 = property(
        __get_address_a_2,
        __set_address_a_2,
        None,
        """Bitfield address_a_2"""
    )


    def __set_address_a_3(self, v):
        self.__address_a_3._value = v

    address_a_3 = property(
        lambda self: self.__address_a_3._value,
        __set_address_a_3,
        None,
        """Safe Address Information SADR [3]."""
    )

    def __set_time_stamp_msword(self, v):
        self.__time_stamp_msword._value = v

    time_stamp_msword = property(
        lambda self: self.__time_stamp_msword._value,
        __set_time_stamp_msword,
        None,
        """Time Stamp.  Holds the most significant word of the Time Stamp."""
    )

    def __set_data_a(self, v):
        self.__data_a._value = v

    data_a = property(
        lambda self: self.__data_a._value,
        __set_data_a,
        None,
        """."""
    )

    def __set_crc_a(self, v):
        self.__crc_a._value = v

    crc_a = property(
        lambda self: self.__crc_a._value,
        __set_crc_a,
        None,
        """CRC CRC over the frame part fields:  id_a_header, id_a_format,
        id_a_version, id_a_length, address_a_1, address_a_timedate,
        address_a_2, address_a_3.  time-stamp_msword, data_a."""
    )
    def __set_id_b_header(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_id_b_header(self):
        return self.___bf02._getbits(
            size=1,
            offset=0,
            signed=False
        )

    id_b_header = property(
        __get_id_b_header,
        __set_id_b_header,
        None,
        """Header Header is always 0."""
    )

    def __set_id_b_format(self, v):
        if 0 <= v <= 3:
            self.___bf02._setbits(
                value=v,
                size=2,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_id_b_format(self):
        return self.___bf02._getbits(
            size=2,
            offset=1,
            signed=False
        )

    id_b_format = property(
        __get_id_b_format,
        __set_id_b_format,
        None,
        """Format Information.  00:  Data 01:  CMD 10:  SEG 11:  reserved for
        future use."""
    )

    def __set_id_b_version(self, v):
        if 0 <= v <= 3:
            self.___bf02._setbits(
                value=v,
                size=2,
                offset=3
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_id_b_version(self):
        return self.___bf02._getbits(
            size=2,
            offset=3,
            signed=False
        )

    id_b_version = property(
        __get_id_b_version,
        __set_id_b_version,
        None,
        """Version Number.  00:  valid version 01:  reserved for future use
        10:  reserved for future use 11:  reserved for future use."""
    )

    def __set_id_b_length(self, v):
        if 0 <= v <= 7:
            self.___bf02._setbits(
                value=v,
                size=3,
                offset=5
            )
        else:
            raise ValueError('Not in range 0..7')

    def __get_id_b_length(self):
        return self.___bf02._getbits(
            size=3,
            offset=5,
            signed=False
        )

    id_b_length = property(
        __get_id_b_length,
        __set_id_b_length,
        None,
        """Data Length.  000:  1 Byte data length 001:  2 Byte data length
        010:  4 Byte data length 011:  8 Byte data length."""
    )


    def __set_address_b_1(self, v):
        self.__address_b_1._value = v

    address_b_1 = property(
        lambda self: self.__address_b_1._value,
        __set_address_b_1,
        None,
        """Safe Address Information SADR [1]."""
    )
    def __set_address_b_timedate(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_address_b_timedate(self):
        return self.___bf03._getbits(
            size=1,
            offset=0,
            signed=False
        )

    address_b_timedate = property(
        __get_address_b_timedate,
        __set_address_b_timedate,
        None,
        """Time / Data Service Type.  0:  Data service type 1:  Time service
        type."""
    )

    def __set_address_b_2(self, v):
        if 0 <= v <= 127:
            self.___bf03._setbits(
                value=v,
                size=7,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..127')

    def __get_address_b_2(self):
        return self.___bf03._getbits(
            size=7,
            offset=1,
            signed=False
        )

    address_b_2 = property(
        __get_address_b_2,
        __set_address_b_2,
        None,
        """Bitfield address_b_2"""
    )


    def __set_address_b_3(self, v):
        self.__address_b_3._value = v

    address_b_3 = property(
        lambda self: self.__address_b_3._value,
        __set_address_b_3,
        None,
        """Safe Address Information SADR [3]."""
    )

    def __set_time_stamp_lsword(self, v):
        self.__time_stamp_lsword._value = v

    time_stamp_lsword = property(
        lambda self: self.__time_stamp_lsword._value,
        __set_time_stamp_lsword,
        None,
        """Time Stamp.  Holds the least significant word of the Time
        Stamp."""
    )

    def __set_data_b(self, v):
        self.__data_b._value = v

    data_b = property(
        lambda self: self.__data_b._value,
        __set_data_b,
        None,
        """."""
    )

    def __set_crc_b(self, v):
        self.__crc_b._value = v

    crc_b = property(
        lambda self: self.__crc_b._value,
        __set_crc_b,
        None,
        """CRC CRC over the frame part fields:  id_b_header, id_b_format,
        id_b_version, id_b_length, address_b_1, address_b_timedate,
        address_b_2, address_b_3.  time-stamp_lsword, data_b."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_address_a_1(v.__address_a_1)
        self.__set_address_a_3(v.__address_a_3)
        self.__set_time_stamp_msword(v.__time_stamp_msword)
        self.__set_data_a(v.__data_a)
        self.__set_crc_a(v.__crc_a)
        self.__set_address_b_1(v.__address_b_1)
        self.__set_address_b_3(v.__address_b_3)
        self.__set_time_stamp_lsword(v.__time_stamp_lsword)
        self.__set_data_b(v.__data_b)
        self.__set_crc_b(v.__crc_b)
        self.___bf03._value = v.___bf03._value
        self.___bf02._value = v.___bf02._value
        self.___bf01._value = v.___bf01._value
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 30


if __name__ == '__main__':
    # unit test code.
    item = safe_8()
    pass
