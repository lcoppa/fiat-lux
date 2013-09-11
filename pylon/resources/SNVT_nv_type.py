"""SNVT_nv_type standard datapoint type, originally defined in resource file
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
from pylon.resources.nv_type_category_t import nv_type_category_t


class SNVT_nv_type(base.Structure):
    """SNVT_nv_type standard datapoint type.  Network variable type.  Network
    variable type description for network variables that support changeable
    types."""

    def __init__(self):
        super().__init__(
            key=166,
            scope=0
        )

        self.__type_program_ID = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(8)
            ]
        )
        self._register(('type_program_ID', self.__type_program_ID))

        self.__type_scope = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=6
        )
        self._register(('type_scope', self.__type_scope))

        self.__type_index = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('type_index', self.__type_index))

        self.__type_category = nv_type_category_t(
        )
        self._register(('type_category', self.__type_category))

        self.__type_length = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=31
        )
        self._register(('type_length', self.__type_length))

        self.__scaling_factor_a = base.Scaled(
            size=2,
            signed=True,
            invalid=32767,
            minimum=-32768,
            maximum=32767
        )
        self._register(('scaling_factor_a', self.__scaling_factor_a))

        self.__scaling_factor_b = base.Scaled(
            size=2,
            signed=True,
            invalid=32767,
            minimum=-32768,
            maximum=32767
        )
        self._register(('scaling_factor_b', self.__scaling_factor_b))

        self.__scaling_factor_c = base.Scaled(
            size=2,
            signed=True,
            invalid=32767,
            minimum=-32768,
            maximum=32767
        )
        self._register(('scaling_factor_c', self.__scaling_factor_c))
        self._definition = standard.add(self)


    def __set_type_program_ID(self, v):
        self.__type_program_ID._value = v

    type_program_ID = property(
        lambda self: self.__type_program_ID._value,
        __set_type_program_ID,
        None,
        """Type program ID.  Program ID template of the resource file
        containing the network variable type definition."""
    )

    def __set_type_scope(self, v):
        self.__type_scope._value = v

    type_scope = property(
        lambda self: self.__type_scope._value,
        __set_type_scope,
        None,
        """Type scope.  Scope of the resource file containing the network
        variable type definition.  (file scope.)."""
    )

    def __set_type_index(self, v):
        self.__type_index._value = v

    type_index = property(
        lambda self: self.__type_index._value,
        __set_type_index,
        None,
        """Type index.  Index within the specified resource file of the
        network variable type definition.  (type index.)."""
    )

    def __set_type_category(self, v):
        self.__type_category._value = v

    type_category = property(
        lambda self: self.__type_category._value,
        __set_type_category,
        None,
        """Type category.  Type category of the network variable type.  (type
        category names.)."""
    )

    def __set_type_length(self, v):
        self.__type_length._value = v

    type_length = property(
        lambda self: self.__type_length._value,
        __set_type_length,
        None,
        """Type length.  Length of the network variable type.  (bytes)."""
    )

    def __set_scaling_factor_a(self, v):
        self.__scaling_factor_a._value = v

    scaling_factor_a = property(
        lambda self: self.__scaling_factor_a._value,
        __set_scaling_factor_a,
        None,
        """Scaling factor a.  Scaling multiplier 'a' where ScaledValue =
        a*(10**b)*(RawValue+c)."""
    )

    def __set_scaling_factor_b(self, v):
        self.__scaling_factor_b._value = v

    scaling_factor_b = property(
        lambda self: self.__scaling_factor_b._value,
        __set_scaling_factor_b,
        None,
        """Scaling factor b.  Exponent 'b' where ScaledValue =
        a*(10**b)*(RawValue+c)."""
    )

    def __set_scaling_factor_c(self, v):
        self.__scaling_factor_c._value = v

    scaling_factor_c = property(
        lambda self: self.__scaling_factor_c._value,
        __set_scaling_factor_c,
        None,
        """Scaling Factor c.  Offset 'c' where ScaledValue =
        a*(10**b)*(RawValue+c)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_type_program_ID(v.__type_program_ID)
        self.__set_type_scope(v.__type_scope)
        self.__set_type_index(v.__type_index)
        self.__set_type_category(v.__type_category)
        self.__set_type_length(v.__type_length)
        self.__set_scaling_factor_a(v.__scaling_factor_a)
        self.__set_scaling_factor_b(v.__scaling_factor_b)
        self.__set_scaling_factor_c(v.__scaling_factor_c)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 19


if __name__ == '__main__':
    # unit test code.
    item = SNVT_nv_type()
    pass
