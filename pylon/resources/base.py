"""Defines base classes to implement interoperable types.

This module defines base classes which are used to create pilon representations
of standard and user-defined interoperable types, such as datapoint types,
property types and functional profiles. These types are then used to implement
corresponding interoperable objects (datapoints, properties or functional
blocks) through the pilon Application class and its factory methods.
"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import logging
import struct

from pylon.device import toolkit
#from pylon.resources import standard

logger = logging.getLogger('pylon-rtk.drf')


class Type(toolkit.PilonObject):
    """The root of all interoperable Types.

    You should consider this class abstract, and only to be used with one of
    the classes derived from it.

    As a rule, attributes and methods in this class, and in all classes derived
    from it, use a single underscore prefix to isolate the class namespace from
    that of the member definitions within the resource files.
    """

    def __init__(self, key=-1, scope=-1):
        """Create a Type from a key/scope value pair.

        Arguments:

        key:    the numeric key or type index within the corresponding resource
                file
        scope:  the scope selector value of the corresponding resource file
        """
        super().__init__()
        self.__key = int(key)
        self.__scope = int(scope)
        self.__obsolete = False
        self.__original_name = None

    _key = property(
        lambda self: self.__key,
        None,
        None, """Return the key value or -1 if not applicable.

        This property provides the key, or type index, matching the definition
        of this interoperable item. -1 may be returned for nested Type objects,
        which may not have a valid key.
    """)

    _scope = property(
        lambda self: self.__scope,
        None,
        None, """Return the scope value or -1 if not applicable.

        This property provides the scope value under which this interoperable
        item was defined. Scope values are 0 for types defined with the
        standard, values 3 to 6 are used for user-defined types. See the
        LonMark International website at www.lonmark.org for more details.

        The property may return -1 for nested Type objects, which may not have
        a value scope value.
    """)

    _is_obsolete = property(
        lambda self: self.__obsolete,
        None,
        None, """Indicates an obsolete profile, datapoint or property type.

        Indicates whether the type is marked as obsolete.
        Obsolete definitions may be used with existing design, but their use in
        new development is not recommended."""
    )

    def __set_original_name(self, v):
        if isinstance(v, str):
            self.__original_name = v
        else:
            raise TypeError(
                'Expected string, got {0}'.format(
                    type(v)
                )
            )

    _original_name = property(
        lambda self: self.__original_name,
        __set_original_name,
        None, """Gives the resource's original name, if available.

        Many of the pylon resources (datapoint types, property types, profiles
        and enumerations) originate from definitions in device resource files,
        where the resources carry a slightly different name. While the names of
        the pylon resources are derived from their original definition,
        resource names have been mangled to avoid conflicts with Python
        reserved words and built-ins, and have been stripped of name prefixes
        not necessary when used with Python.
        This property supplies the original resource name, or None if none is
        known."""
    )

    def _mark_obsolete(self):
        """Mark the current type as obsolete.
        This utility is used during the instantiation of resources. Use the
        _is_obsolete property to query this flag. A resource is generally
        flagged obsolete in its definition (typically within a device resource
        file); the 'obsolete' flag should be considered read-only from the
        script."""
        self.__obsolete = True

    def _override_key(self, k):
        """Override the key set with the constructor.

        This method is used internally when one type directly derives from
        another. In such a case, the derived type (parent type, super type)
        defines a key/scope pair, which the deriving (child type) overrides.
        """
        self.__key = k

    def _override_scope(self, s):
        """Override the scope value set with the constructor.

        This method is used internally when one type directly derives from
        another. In such a case, the derived type (parent type, super type)
        defines a key/scope pair, which the deriving (child type) overrides.
        """
        self.__scope = s

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        seed = 0x400000 if self.__obsolete else 0
        return seed | ((self.__key << 3) + self.__scope)


class Definition(toolkit.PilonObject):
    """This class provides information about the definition of a resource.

    Consider this class abstract. Implementations use a class derived from
    Definition, e.g. Drf, to report resource definition details through a
    shared and re-used object. See pylon.resources.standard.standard for an
    example.
    """

    definitions = set()

    def __init__(self):
        super().__init__()
        Definition.definitions.add(self)


class Drf(Definition):
    """This class provides information about DRF-derived resources.

    Pilon resource definitions may be constructed in different ways, but the
    majority of pilon resources are derived from standard and selected user-
    defined device resource files (DRF).

    DRF are extensively documented and supported by LonMark International, see
    http://www.lonmark.org/technical_resources/resource_files/ for more.
    """

    def __init__(self, program_id, scope, name, version, doc):
        """Create a Drf object.

        Arguments:

        program_id  The colon-separated, ASCII-encoded string-format program
                    id of the defining set, e.g. '80:00:00:00:00:00:00:00'.

        scope       The scope selector number, 0 for standard, or 3..6 for
                    user-defined, non-standard, resources.

        name        The name of the defining resource file set.

        version     The major, minor version number tuple for the defining set.

        doc         Suitable documentation, such as the set creator's contact
                    details, etc.
        """
        super().__init__()
        self.program_id = program_id
        self.scope = scope
        self.name = name
        self.version = version
        self.__doc__ = doc
        self.resources = set()

    def add(self, resource):
        """Register a resource with this object, return the definition.

        Resources use the add() method to register themselves with this
        definition object. The method returns a reference to the definition
        object itself.
        """
        for existing in self.resources:
            if isinstance(resource, existing.__class__):
                # Type is already registered. Be done:
                return self
        self.resources.add(resource)
        return self

    def __str__(self):
        """Report the DRF object."""
        return '{0}: {1}-{2} version {3}'.format(
            self.name,
            self.program_id,
            self.scope,
            self.version
        )


class Inheriting(Type):
    """This class provides a root class for type-inheriting types.

    This type is used in the definition of type-inheriting property types,
    allowing the runtime kit to detect whether a given property type is
    type-inheriting.
    Note that type-inheriting property types use a process different from
    the common object-oriented inheritance model for type inheritance. Type-
    inheriting property types derive their data type from the item the
    property applies to. This is neither an "is-a" nor a "has-a" relationship,
    but one might think of it as "implements-a" or "derives-from".
    """

    def __init__(self):
        super().__init__()


class DataType(Type):
    """DataType is the root of all data carrying interoperable types.

    This class is the root of all interoperable data types which carry data,
    such as Datapoint types and property types. By contrast, profiles are
    meta-types, in that the profile combines other interoperable items, but
    does not carry data by itself.

    Use key=-1, scope=-1 for aggregate members, where the aggregate as a whole,
    but not the member, has valid key and scope values.
    """
    def __init__(self, key=-1, scope=-1):
        """Create a DataType object with a key/scope value pair.

        Use -1 for key and scope when not applicable, as might be the case for
        nested DataType objects.
        """
        super().__init__(key, scope)
        self.__unpack_format = self.__pack_format = '?'
        self.__onAssign = None

        # Objects derived from DataType may specify optional minimum, maximum,
        # invalid and default bytes objects, if such data is available. If
        # provided, these are applied when the DataType is instantiated as part
        # of an interface object (a Datapoint, a Property, or a Block).
        self._minimum_bytes = None
        self._maximum_bytes = None
        self._invalid_bytes = None
        self._default_bytes = None

    def _set_onAssign(self, handler):
        """Register an onAssign handler.

        The DataType calls this handler every time an assignment is made,
        regardless whether the value changed or not.
        The onAssign handler is typically used internally only, in order to
        register an updated datapoint with the application object's processing
        queue.
        The handler returns nothing, and takes one argument, the sender. The
        sender is a reference to the DataType object which was updated."""
        self.__onAssign = handler

    def _assigned(self, sender):
        """Fire the onAssign event."""
        if self.__onAssign:
            self.__onAssign(sender)

    def __set_pack_format(self, v):
        self.__pack_format = v

    def __set_unpack_format(self, v):
        self.__unpack_format = v

    _pack_format = property(
        lambda self: self.__pack_format,
        __set_pack_format,
        None, """Provide format instructions for the serializer."""
    )

    _unpack_format = property(
        lambda self: self.__unpack_format,
        __set_unpack_format,
        None, """Provide format instructions for the deserializer."""
    )

    def __pack_binary(self, fmt, value):
        """Serialize the value into a binary packed big-endian byte array.

        The method packs into a binary bytearray in big endian (network) byte
        order. The bytearray is returned. Use this through _packme.
        """
        return struct.pack(fmt, value)

    def __unpack_binary(self, fmt, binary, size):
        """Revert __pack_binary().

        __unpack_binary() reverts __pack_binary(), extracting the current
        value from the given byte array. The method returns a tuple containing
        the unpacked value and the remaining slice of the binary byte array,
        according to the given size (in bytes).

        Call this through _unpackme.
        """
        value = struct.unpack(fmt, binary[:size])
        return value[0], binary[size:]

    # _packme and _unpackme are function pointers, referencing the chosen
    # packing and unpacking methods. This allows, to the extent possible,
    # to switch serialization methods, for example from a compact big-endian
    # binary serializer to JSON or XML or whatever.
    # The function pair returns a pointer to the compact data - for the
    # ISO/IEC 14908 protocol stack, this is a series of bytes. This data may
    # take other forms with other serializers.
    _packme, _unpackme = __pack_binary, __unpack_binary

    def _accept_as_minimum(self):
        """Accept the current value as the minimum value.

        This base class method does nothing. Classes deriving from this class
        override this method if a minimum value is supported.
        """
        pass

    def _accept_as_maximum(self):
        """Accept the current value as the maximum value.

        This base class method does nothing. Classes deriving from this class
        override this method if a maximum value is supported.
        """
        pass

    def _accept_as_default(self):
        """Accept the current value as the default value.

        This base class method does nothing. Classes deriving from this class
        override this method if a default value is supported.
        """
        pass

    def _accept_as_invalid(self):
        """Accept the current value as the dedicated invalid value.

        This base class method does nothing. Classes deriving from this class
        override this method if an invalid value is supported.
        """
        pass


class Scaled(DataType):
    """Base type for all interoperable integer data.

    Scaled implements a base for all signed and unsigned integers, with
    support for scaling factors to emulate fixed-point arithmetic.
    All script-facing values (current value, default value, minimum, maximum
    or designated invalid value) use scaled values.
    The class handles transcoding of scaled values into 'raw' network-facing
    values, and vice versa, transparently.
    """

    __format = {1: 'B', 2: 'H', 4: 'I', 8: 'Q'}
    __limits = {1: 127, 2: 32767, 4: 2147483647, 8: 9223372036854775807}
    __masks = (0x80, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF)
    __pow2 = (1, 2, 4, 8, 16, 32, 64, 128)

    def __init__(self, size, signed, key=-1, scope=-1, default=None,
                 scaling=(1, 0),
                 minimum=None, maximum=None, invalid=None):
        """Construct a Scaled object."""
        super().__init__(key, scope)
        if not size in Scaled.__format:
            raise TypeError(
                'Scaled type of {0} bytes is not supported'.format(size)
            )

        self.__scalingFactor, self.__scalingOffset = scaling

        #	Compute native range limits as scaled values if no explicit limits
        #	are provided. Note this depends on the scaling factor and offset.
        if not minimum:
            if signed:
                minimum = self.__scale(-Scaled.__limits[size] - 1)
            else:
                minimum = self.__scale(0)

        if not maximum:
            if signed:
                maximum = self.__scale(Scaled.__limits[size])
            else:
                maximum = self.__scale(2 * Scaled.__limits[size] + 1)

        if not default:
            default = self.__scale(0)

        self.__minimum = minimum
        self.__maximum = maximum
        self.__default = default
        self.__invalid = invalid

        self.__size = size
        self.__value = self.__default if self.__default else 0
        self.__signed = signed

        if signed:
            self._pack_format = Scaled.__format[size].lower()
        else:
            self._pack_format = Scaled.__format[size]
        self._unpack_format = self._pack_format

    def __scale(self, raw):
        """Convert raw to scaled data.

        The method computes and returns a scaled value as a function of a raw
        input value and scaling offset and factors. The raw input value must
        be in the correct host byte order already.
        """
        return self.__scalingFactor * (raw + self.__scalingOffset)

    def __raw(self, scaled):
        """Convert scaled to raw data.

        The method computes and returns a raw value as a function of a scaled
        input value and scaling offset and factors.
        The function always returns an 'int' in host byte order.
        """
        return int(scaled / self.__scalingFactor - self.__scalingOffset)

    def __set_value(self, v):
        if isinstance(v, Scaled):
            v = v.__value
        elif not isinstance(v, int) and not isinstance(v, float):
            raise TypeError(
                'Expected instance of Scaled, int or float, got {0}'.format(
                    type(v)
                )
            )

        if self.__invalid and v == self.__invalid:
            # the 'invalid' value can be outside the min/max range
            self.__value = v
        else:
            # Otherwise, accept v but limit to the valid range, and make
            # a round trip through raw data to ensure that we aren't
            # pretending a higher than possible resolution:
            v = max(self.__minimum, min(v, self.__maximum))
            self.__value = self.__scale(self.__raw(v))

        # notify of the assignment
        self._assigned(self)

    _value = property(
        lambda self: self.__value,
        __set_value,
        None, """The current value."""
    )

    _minimum = property(
        lambda self: self.__minimum,
        None,
        None, """The (scaled) minimum value."""
    )

    _maximum = property(
        lambda self: self.__maximum,
        None,
        None, """The (scaled) maximum value."""
    )

    _default = property(
        lambda self: self.__default,
        None,
        None, """The (scaled) default value."""
    )

    _invalid = property(
        lambda self: self.__invalid,
        None,
        None, """The designated (scaled) invalid value, or None if none.

        Note that this property may return 'None' when a designated invalid
        value hasn't been specified.
    """)

    def _reset(self, flags=0):
        """Return the item to defaults.

        The reset() method always returns the value to the default specified in
        the constructor. Future implementations may support additional flags to
        reset other aspects of the object. In this release, no other aspects
        are supported.
        """
        self.__value = self.__default

        if flags:
            # A not recognized flags value. Warn, ignore and proceed.
            logger.warn(
                '{0}._reset() does not support flag {1}'.format(
                    type(self), flags
                )
            )

        self._assigned(self)

    def _pack(self):
        result = self._packme(
            '>' + self._pack_format, self.__raw(self.__value)
        )
        return result

    def _unpack(self, binary):
        raw, remainder = self._unpackme(
            '>' + self._unpack_format, binary, self.__size
        )
        self.__value = self.__scale(raw)
        return remainder

    def __bytes__(self):
        return self._pack()

    def __bool__(self):        # returns True or False
        return bool(self.__value)

    def __len__(self):        # returns size in bytes
        return self.__size

    def __str__(self):        # return human-readable form of self
        return '{0}'.format(self.__value)

    def __repr__(self):
        return '<{0}: {1} ({2}..{3}, {4})>'.format(
            self.__class__.__name__,
            self.__str__(),
            self.__minimum,
            self.__maximum,
            self.__default
        )

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        return super()._signature() + (self.__size ^ 5) << 7

    def _accept_as_minimum(self):
        """Accept the current value as the minimum value.

        Call this method to accept the current value as the minimum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__minimum = self.__value

    def _accept_as_maximum(self):
        """Accept the current value as the maximum value.

        Call this method to accept the current value as the maximum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__maximum = self.__value

    def _accept_as_default(self):
        """Accept the current value as the default value.

        Call this method to accept the current value as the default value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__default = self.__value

    def _accept_as_invalid(self):
        """Accept the current value as the dedicated invalid value.

        Call this method to accept the current value as the invalid value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__invalid = self.__value

    def _setbits(self, value, size, offset):
        """This utility is used by bitfields setters.
        This utility supports single-byte containers only."""
        if self.__size == 1 and 1 <= size <= 8 and 0 <= offset <= 7:
            mask = Scaled.__masks[size-1] >> offset

            self.__value &= ~mask
            if value:
                self.__value |= value << 8-offset-size & mask
        else:
            raise AttributeError('bad parameters')

    def _getbits(self, size, offset, signed):
        """This utility is used by bitfield getters.
        This utility supports single-byte containers only."""
        if self.__size == 1 and 1 <= size <= 8 and 0 <= offset <= 7:
            mask = Scaled.__masks[size-1] >> offset
            value = (self.__value & mask) >> 8 - size - offset
            umax = Scaled.__pow2[size-1]

            if signed and value > umax - 1:
                value -= 2*umax
            return value

        else:
            raise AttributeError('bad parameters')


class Enumeration(DataType):
    """Base type for all interoperable enumerations.

    The Enumeration type, and all enumerations derived from it, support the
    following behavior:

    i.  The enumeration has a physical value range -128..+127 (an 8-bit signed
        integer)
    ii. Members can be defined using an alphanumeric 'mnemonic' name for the
        enumerated member, the member's numeric value, and an optional doc
        string. The member name must be a valid Python variable name, and
        should comply with the PEP 8 coding standard and name standard for
        constants, using all capital letters with underscores separating words.
        Within a given enumeration, all such member names *must* share the
        same name prefix.
    iii.When a value is assigned to an enumeration, a warning is raised if the
        assigned value does not match one of the defined members. In this case,
        the numeric value is accepted so long as it fits the -128..+127 value
        range.
    iv. When a value is read from an enumeration, the enumeration returns its
        current numeric value.
    v.  The __str__() method is overridden and provides the alphanumeric
        presentation, if an exact match to the current numeric value exists.

    Example:

    class Trecolori(Enumeration):
       TC_NIENTE = 0
       TC_AZZURRO = 1
       TC_VERDE = 2
       TC_PORPORA = 3

       def __init__(default=Trecolori.TC_NIENTE):
          super().__init__(key=2, scope=4, prefix='TC_', default)
    """

    def __init__(self, prefix, key=-1, scope=-1, default=None):
        """Create an Enumeration object."""
        super().__init__(key, scope)
        self.__default = default
        self.__value = default if default else 0
        self.__prefix = prefix

    def __set_value(self, v):
        if isinstance(v, Enumeration):
            v = v.__value
        elif not isinstance(v, int) and not isinstance(v, float):
            raise TypeError(
                'Expected instance of Scaled, int or float, got {0}'.format(
                    type(v)
                )
            )

        v = int(v)

        if -128 <= v <= +127:
            self.__value = v
        else:
            raise ValueError(
                'Expected value -128..+127, got {0}'.format(
                    v
                )
            )
        self._assigned(self)

    _value = property(
        lambda self: self.__value,
        __set_value,
        None, """
        Provides access to the current value
    """)

    def _reset(self, flags=0):
        """Return the item to defaults.

        The reset() method always returns the value to the default specified in
        the constructor. Future implementations may support additional flags to
        reset other aspects of the object. In this release, no other aspects
        are supported.

        """
        self.__value = self.__default

        if flags:
            # A not recognized flags value. Warn, ignore and proceed.
            logger.warn(
                '{0}._reset() does not support flag {1}'.format(
                    type(self),
                    flags
                )
            )
        self._assigned(self)

    def _pack(self):
        result = self._packme('>b', self.__value)
        return result

    def _unpack(self, binary):
        self.__value, remainder = self._unpackme('>b', binary, 1)
        return remainder

    def __bytes__(self):
        return self._pack()

    def __bool__(self):        # returns True or False
        return bool(self.__value)

    def __len__(self):        # returns size in bytes
        return 1

    def __str__(self):        # return human-readable form of self
        dictionary = self.__class__.__dict__
        result = str(self.__value)

        for name in dictionary:
            if name.startswith(self.__prefix):
                try:
                    if dictionary[name] == self.__value:
                        result = name
                except Exception:
                    pass

        return result

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        signature = super()._signature()
        dictionary = self.__class__.__dict__

        for classMember in dictionary.keys():
            if classMember.startswith(self.__prefix):
                signature ^= toolkit.simple_checksum(classMember)
                signature ^= dictionary[classMember]
        return signature

    def _accept_as_default(self):
        """Accept the current value as the default value.

        Call this method to accept the current value as the default value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__default = self.__value


class Float(DataType):
    """Base type for interoperable floating-point data.

    Float implements a base for IEEE 754 single- and double-precision floating
    point types, with support for additional value range limits.
    Use NAN for an explicit invalid value.
    """

    def __init__(self, single, key=-1, scope=-1,
                 minimum=None, maximum=None,
                 default=0):
        super().__init__(key, scope)

        if default:
            self.__value = self.__default = float(default)
        else:
            self.__value = self.__default = 0.0

        if single:
            self.__maximum = 3.4028234e38
            self.__single = True
            self._pack_format = 'f'
            self.__size = int(4)
        else:
            self.__maximum = 1.7976931348623157e308
            self.__single = False
            self._pack_format = 'd'
            self.__size = int(8)

        self.__minimum = -self.__maximum

        if minimum:
            self.__minimum = minimum
        if maximum:
            self.__maximum = maximum

        self._unpack_format = self._pack_format

    def __set_value(self, v):
        if isinstance(v, Float):
            v = v.__value
        else:
            v = float(v)

        self.__value = max(self.__minimum, min(v, self.__maximum))
        self._assigned(self)

    _value = property(
        lambda self: self.__value,
        __set_value,
        None, """The current value."""
    )

    _minimum = property(
        lambda self: self.__minimum,
        None,
        None, """The minimum value."""
    )

    _maximum = property(
        lambda self: self.__maximum,
        None,
        None, """The maximum value."""
    )

    _default = property(
        lambda self: self.__default,
        None,
        None, """The default value."""
    )

    def _reset(self, flags=0):
        """Return the item to defaults.

        The reset() method always returns the value to the default specified in
        the constructor. Future implementations may support additional flags to
        reset other aspects of the object. In this release, no other aspects
        are supported.
        """
        self.__value = self.__default

        if flags:
            # A not recognized flags value. Warn, ignore and proceed.
            logger.warn(
                '{0}._reset() does not support flag {1}'.format(
                    type(self),
                    flags
                )
            )
        self._assigned(self)

    def _pack(self):
        result = self._packme('>' + self._pack_format, self.__value)
        return result

    def _unpack(self, binary):
        self.__value, remainder = self._unpackme(
            '>' + self._unpack_format, binary, self.__size
        )
        return remainder

    def __bytes__(self):
        return self._pack()

    def __bool__(self):        # returns True or False
        return bool(self.__value)

    def __len__(self):        # returns size in bytes
        return self.__size

    def __str__(self):        # return human-readable form of self
        return str(self.__value)

    def __repr__(self):
        return '<{0} {1} ({2}..{3}, {4})>'.format(
            self.__class__.__name__,
            self.__str__(),
            self.__minimum,
            self.__maximum,
            self.__default
        )

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        return super()._signature() ^ self.__single

    def _accept_as_minimum(self):
        """Accept the current value as the minimum value.

        Call this method to accept the current value as the minimum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__minimum = self.__value

    def _accept_as_maximum(self):
        """Accept the current value as the maximum value.

        Call this method to accept the current value as the maximum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__maximum = self.__value

    def _accept_as_default(self):
        """Accept the current value as the default value.

        Call this method to accept the current value as the default value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.
        """
        self.__default = self.__value


class Aggregate(DataType):
    """Aggregate is the superclass shared by Structure and Union.

    This class maintains a list of members, arranged in declaration order.
    Each element of the list contains a name / value pair, were the name
    matches the field name and the value is a reference to its implementation.

    This class provides services common to Structure and Union.
    """

    def __init__(self, key=-1, scope=-1):
        super().__init__(key, scope)
        self._members = []

    def _reset(self, flags=0):
        """Return the all members to defaults.

        The reset() method always returns the value of all members to their
        default value as specified in the constructor.
        Future implementations may support additional flags to reset other
        aspects of the object. In this release, no other aspects are supported.
        """
        for member in self._members:
            member[1]._reset(flags)

        if flags:
            # A not recognized flags value. Warn, ignore and proceed.
            logger.warn(
                '{0}._reset() does not support flag {1}'.format(
                    type(self),
                    flags
                )
            )

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        signature = super()._signature()

        for member in self._members:
            signature ^= member[1]._signature()
        return signature

    def _accept_as_minimum(self):
        """Accept the current value as the minimum value.

        Call this method to accept the current value as the minimum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        Aggregate applies this call to all members.
        """
        for member in self._members:
            member[1]._accept_as_minimum()

    def _accept_as_maximum(self):
        """Accept the current value as the maximum value.

        Call this method to accept the current value as the maximum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        Aggregate applies this call to all members.
        """
        for member in self._members:
            member[1]._accept_as_maximum()

    def _accept_as_default(self):
        """Accept the current value as the default value.

        Call this method to accept the current value as the default value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        Aggregate applies this call to all members.
        """
        for member in self._members:
            member[1]._accept_as_default()

    def _accept_as_invalid(self):
        """Accept the current value as the dedicated invalid value.

        Call this method to accept the current value as the invalid value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        Aggregate applies this call to all members.
        """
        for member in self._members:
            member[1]._accept_as_invalid()


class Structure(Aggregate):
    """Structure is the root of all structure-type aggregates."""

    def __init__(self, key=-1, scope=-1):
        super().__init__(key, scope)

    def __on_member_assign(self, sender):
        """Forward a member's assignment event."""
        self._assigned(self)

    def _register(self, member_description):
        """Register an Aggregate member.

        Types based on Aggregate must register their members, in the order in
        which they appear within the type definition, with this API. Only
        objects derived from DataType can be registered. """
        if not isinstance(member_description, tuple) or \
                not isinstance(member_description[0], str) or \
                not isinstance(member_description[1], DataType):
            raise TypeError(
                'Expected tuple of (string, DataType)'
            )
        member_description[1]._set_onAssign(self.__on_member_assign)
        self._members.append(member_description)

    def _pack(self):
        result = bytes()
        for member in self._members:
            result += member[1]._pack()
        return result

    def _unpack(self, binary):
        for member in self._members:
            binary = member[1]._unpack(binary)
        return binary

    def __str__(self):
        """Provide a human-readable representation of the current value.

        The structure's default alphanumeric representation lists the structure
        fields as name=value pairs, but lists no more than three elements in
        order to keep the display readable. Override the __str__ method in the
        class deriving from Structure to implement a different display if
        necessary.
        """
        result = '{'
        fields = min(3, len(self._members))
        for i in range(fields):
            if len(result) > 1:
                result += ', '
            result += '{0}={1}'.format(
                self._members[i][0],
                str(self._members[i][1])
            )
        if fields < len(self._members):
            result += ', ...'
        return result + '}'


class Union(Aggregate):
    """Union is the root of all union-type aggregates.

    This class maintains a list of members, arranged in declaration order.
    Each element of the list contains a name / value pair, were the name
    matches the field name and the value is a reference to its implementation.

    It is perhaps important to note that a pilon Union resembles, but does not
    implement the exact same behavior as, a C language union. A pilon Union
    behaves as follows:

    The network-facing interface of the Union is a series of bytes, determined
    by the largest member of the union. When the union is propagated onto the
    network, the most recently updated member is sent, with added bytes (each
    of value zero) to fill up the network data to match the union's largest
    member in size.

    When an update is received from the network, this value is applied to all
    members of the union (possibly ignoring any surplus bytes). The update
    received from the network must match the largest union member in size.

    The script-facing interface of the Union is that of a structure, however:
    Modifying union member A has no effect on union member B, a pilon union
    cannot be used for local type translation in the way a C language union is
    sometimes used.
    """

    def __init__(self, key=-1, scope=-1):
        super().__init__(key, scope)
        self.__largest = None   # largest member
        self.__mru = None       # most recently updated member (from script)

    def __on_member_assign(self, sender):
        """Forward a member's assignment event."""

        for member in self._members:
            if sender is member[1]:
                self.__mru = member
                break

        self._assigned(self)

    def _register(self, member_description):
        """Register an Aggregate member.

        Types based on Aggregate must register their members, in the order in
        which they appear within the type definition, with this API. Only
        objects derived from DataType can be registered. """
        if not isinstance(member_description, tuple) or \
                not isinstance(member_description[0], str) or \
                not isinstance(member_description[1], DataType):
            raise TypeError(
                'Expected tuple of (string, DataType)'
            )
        member_description[1]._set_onAssign(self.__on_member_assign)
        self._members.append(member_description)

    def _finalize(self):
        """Finalize the union.

        Classes deriving from Union must call this method once all members are
        added. The method completes the initialization: it defaults the most
        recently updated member to the first member, and identify the largest
        member.

        The class methods call the finalize method later when necessary,
        however, you should consider calling this method during type creation
        and script initialization for best runtime performance.
        """
        if not self._members:
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.EMPTY_UNION,
                '{0} must have at least one member'.format(
                    type(self)
                )
            )
        self.__largest = self.__mru = self._members[0]

        for member in self._members:
            if len(self.__largest[1]) < len(member[1]):
                self.__largest = member

    def _pack(self):
        if not self.__largest:
            self._finalize()
        padding = len(self.__largest[1]) - len(self.__mru[1])

        result = self.__mru[1]._pack()
        if padding:
            result += bytes(padding * b'\x00')
        return result

    def _unpack(self, binary):
        if not self.__largest:
            self._finalize()

        for member in self._members:
            member[1]._unpack(binary)
        return binary[len(self.__largest[1]):]

    def __len__(self):
        """Return the length of the data type, in bytes."""
        if not self.__largest:
            self._finalize()
        return len(self.__largest[1])

    def __str__(self):
        """Provide a human-readable representation of the current value.

        The union's alphanumeric representation is based on the most recently
        updated field, or the first field in declaration order if the script
        has not updated any fields.
        """
        if not self.__largest:
            self._finalize()

        return '{{{0}={1}}}'.format(self.__mru[0], str(self.__mru[1]))


class Array(DataType):
    """Array implements simple single-dimensional immutable arrays.

    The class implements a simple single-dimensional immutable array. Each
    member of the array implements the same type, and this type must be
    derived from one of the classes derived from pylon.resources.base (with
    the exception of Array itself).
    """

    def __init__(self, elements, key=-1, scope=-1):
        super().__init__(key, scope)
        if not isinstance(elements, tuple) and not isinstance(elements, list):
            raise TypeError(
                'Expected tuple or list, got {0}'.format(
                    type(elements)
                )
            )
        if not elements:
            raise TypeError('Expected at least one element')

        self._element_type = type(elements[0])
        self._elements = elements

        for element in elements:
            element._set_onAssign(self.__on_member_assign)

    def __on_member_assign(self, sender):
        """Forward a member's assignment event."""
        self._assigned(self)

    def __getitem__(self, item):
        return self._elements.__getitem__(item)

    def __setitem__(self, item, value):
        self._elements.__setitem__(item, value)

    def __iter__(self):
        return self._elements.__iter__()

    def __len__(self):
        return self._elements.__len__()

    def _reset(self, flags=0):
        """Return the all members to defaults.

        The reset() method always returns the value of all members to their
        default value as specified in the constructor.
        Future implementations may support additional flags to reset other
        aspects of the object. In this release, no other aspects are supported.
        """
        for member in self._elements:
            member._reset(flags)

        if flags:
            # A not recognized flags value. Warn, ignore and proceed.
            logger.warn(
                '{0}._reset() does not support flag {1}'.format(
                    type(self),
                    flags
                )
            )

    def _pack(self):
        result = bytes()
        for member in self._elements:
            result += member._pack()
        return result

    def _unpack(self, binary):
        for member in self._elements:
            binary = member._unpack(binary)
        return binary

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError('Expected instance of {0}, got {1}'.format(
                type(self),
                type(v)
            ))
        for i in range(min(len(self._elements), len(v._elements))):
            self._elements[i]._value = v._elements[i]._value

    _value = property(
        lambda self: self,
        __set,
        None, """
        The current value.
    """)

    def __str__(self):
        """Provide a human-readable representation of the current value.

        The structure's default alphanumeric representation lists the structure
        fields as name=value pairs, but lists no more than five elements in
        order to keep the display readable. Override the __str__ method in the
        class deriving from Structure to implement a different display if
        necessary.
        """
        result = '['
        fields = min(5, len(self._elements))
        for i in range(fields):
            if len(result) > 1:
                result += ', '
            result += str(self._elements[i])
        if fields < len(self._elements):
            result += ', ...'
        return result + ']'

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        signature = super()._signature()
        signature ^= (len(self._elements) << 5) + \
                        self._elements[0]._signature()

        return signature

    def _accept_as_minimum(self):
        """Accept the current value as the minimum value.

        Call this method to accept the current value as the minimum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        The Array applies this call to all members.
        """
        for member in self._elements:
            member._accept_as_minimum()

    def _accept_as_maximum(self):
        """Accept the current value as the maximum value.

        Call this method to accept the current value as the maximum value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        The Array applies this call to all members.
        """
        for member in self._elements:
            member._accept_as_maximum()

    def _accept_as_default(self):
        """Accept the current value as the default value.

        Call this method to accept the current value as the default value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        The Array applies this call to all members.
        """
        for member in self._elements:
            member._accept_as_default()

    def _accept_as_invalid(self):
        """Accept the current value as the dedicated invalid value.

        Call this method to accept the current value as the invalid value "no
        questions asked," no validation provided. This method is designed to
        support application of "raw" byte arrays containing override data for
        this attribute, but may have other applications. Note, however, that
        attributes such as minimum, maximum and invalid values are generally
        defined with the type. Modifying these attributes at runtime can
        render a device not interoperable, as the implementation would differ
        from the published type.

        The Array applies this call to all members.
        """
        for member in self._elements:
            member._accept_as_invalid()


class PropertyFlags:
    """Flags describing details of a property.

    These are uses with base.Profile.PropertyMember declarations and
    Application.implement() method calls.
    """

    DEVICE_SPECIFIC = 0x20  # device-specific value, i.e. calibration data
    MFG = 0x10              # adjust during manufacture only
    RESET = 0x08            # at least reset the device after change
    CONST = 0x04            # it's a constant (e.g. a version number)
    OFFLINE = 0x02          # at least put the device offline when changing
    DISABLE = 0x01          # at least disable the block when changing
    NONE = 0x80


class Profile(Type):
    """This class is the root of all functional profile definitions."""

    class Member:
        """An internally-used superclass."""

        MEMBER_SELECTORS = '|#'

        def __init__(self, name, profile, number, datatype, mandatory,
                     minimum=None,
                     maximum=None,
                     invalid=None,
                     default=None,
                     doc=''):
            """Create a Member object.

            Arguments:
            name        the member name, as defined with the profile
            number      the member number, as defined with the profile
            profile     the profile which defines this member
            datatype    The type to use (not an instance of the type!)
            mandatory   True for mandatory profile members

            minimum, maximum, invalid, default:

            These are optional parameters. If specified as not None, a bytes
            object must be supplied with the correct number of bytes, which is
            used to define the minimum (maximum, etc) value of the property or
            datapoint to be implemented. In this release, the bytes array must
            be provided as a compact, raw (un-scaled) big-endian stream of
            bytes.
            When a property member is implemented, minimum (maximum, etc)
            values defined with the property type are applied (if any),
            followed by the application of minimum (maximum, etc) values
            defined with the property member. Minimum (maximum, etc) values
            provided with the property member thus provide a means to override
            the preferences defined with the property type.
            When a datapoint member is implemented, minimum (maximum, invalid)
            values are applied in the exact same manner as with property
            members, except that datapoint members never specify a default
            value.
            """

            super().__init__()

            if not issubclass(datatype, (DataType, Inheriting)):
                raise TypeError(
                    '{0} only supports data types derived from '
                    '{1}, got {2}'.format(
                        type(self),
                        type(DataType),
                        type(datatype)
                    )
                )

            self.__name = name
            self.__number = number
            self.__datatype = datatype
            self.__is_mandatory = mandatory
            self.__doc__ = doc
            self.__implementer = None
            self.__derivation = profile.derivation
            self.__minimum = minimum
            self.__maximum = maximum
            self.__invalid = invalid
            self.__default = default

        name = property(
            lambda self: self.__name,
            None,
            None, """The member name, defined in the profile. Read-only."""
        )

        number = property(
            lambda self: self.__number,
            None,
            None, """The member number, defined in the profile. Read-only."""
        )

        datatype = property(
            lambda self: self.__datatype,
            None,
            None, """The member's data type. Read-only."""
        )

        is_mandatory = property(
            lambda self: self.__is_mandatory,
            None,
            None, """Indicates an optional member. Read-only."""
        )

        selector = property(
            lambda self: Profile.Member.MEMBER_SELECTORS[self.__derivation],
            None, None, """Return the selector character.

            Provides the selector character used to prefix the member number in
            an interoperable self-documentation string. This is used by the
            internal self-documentation compiler.
            The property is read-only."""
        )

        def _set_implementer(self, implementer):
            """Update the implementer for this member.

            This protected method is used by the block factory and the block's
            own implement() method to update the implementer reference for this
            member.
            """
            self.__implementer = implementer

        implementer = property(
            lambda self: self.__implementer,
            None,
            None, """A reference to the item implementing the member, or None.
            """
        )

        _minimum = property(
            lambda self: self.__minimum,
            None,
            None, """Return the 'minimum' bytes object or None."""
        )

        _maximum = property(
            lambda self: self.__maximum,
            None,
            None, """Return the 'maximum' bytes object or None."""
        )

        _invalid = property(
            lambda self: self.__invalid,
            None,
            None, """Return the 'invalid' bytes object or None."""
        )

        _default = property(
            lambda self: self.__default,
            None,
            None, """Return the 'default' bytes object or None."""
        )

        def _signature(self):
            """Return a 32-bit signature for this item.

            The signature reflects all attributes relevant to the interoperable
            interface. Note the signature is not a hash, and note that the
            Python hash() function cannot generally be used to compute a
            signature or parts of it due to its random seed.
            The signature must remain the same every time the application
            executes on a given physical device (hardware), unless an aspect
            affecting the interoperable interface changes.
            """
            # note that we CS repr(datatype) - because this is a type, not
            # an instance, we can't have it compute its own _signature()
            return toolkit.simple_checksum(self.__name) ^ \
                ((self.__number ^ 13) << 12) ^ \
                self.__is_mandatory ^ \
                toolkit.simple_checksum(repr(self.__datatype))

        def __str__(self):
            return '{0} {1} {2}'.format(
                self.__name,
                str(self.__datatype),
                "mandatory" if self.__is_mandatory else "optional"
            )

    class DatapointMember(Member):
        """The class details a profile's datapoint member."""

        #
        # Some useful constants. Values for these constants are chosen to match
        # the equivalent constants used by the LonMark Device Resource Files
        # (DRF) and API, as this simplifies transcoding definitions from DRF
        # to pilon.
        #

        INPUT = 0x80           # member is input (otherwise output)
        OUTPUT = 0x00          # logic inverse of INPUT

        POLLED = 0x40          # member implementation as polled
        ACKNOWLEDGED = 0x20    # recommended service: Acknowledged
        REPEATED = 0x10        # recommended service: Unacknowledged, repeated
        UNREPEATED = 0x08      # recommended service: Unacknowledged, unrept.
        UNSPECIFIED = 0x00     # no specific service type recommended

        def __init__(self, name, profile, number, datatype, mandatory,
                     direction, polled=False, service=UNSPECIFIED, doc='',
                     minimum=None, maximum=None, invalid=None,
                     properties=None):
            """Create a DatapointMember object.

            Arguments:
            name        the member name, as defined with the profile
            profile     the profile which defines this member
            number      the member number, as defined with the profile
            datatype    The type to use (not an instance of the type!)
            mandatory   True for mandatory profile members
            direction   DatapointMember.INPUT or OUTPUT
            polled      Boolean 'polled' requirement
            service     DatapointMember.ACKNOWLEDGED, (UN)REPEATED or UNSPEC.
            minimum     minimum bytes object or None, see Profile.Member
            maximum     maximum bytes object or None, see Profile.Member
            invalid     invalid bytes object or None, see Profile.Member

            When the member is created, apply minimum, maximum or invalid value
            overrides if necessary.

            """
            super().__init__(
                name=name,
                profile=profile,
                number=number,
                datatype=datatype,
                mandatory=mandatory,
                minimum=minimum,
                maximum=maximum,
                invalid=invalid,
                doc=doc
            )
            self.__is_output = direction != Profile.DatapointMember.INPUT
            self.__is_polled = polled
            self.__service = service
            if not properties:
                self.properties = {}
            else:
                self.properties = properties

        is_output = property(
            lambda self: self.__is_output,
            None,
            None, """Indicate the member as an output. Read-only."""
        )

        is_polled = property(
            lambda self: self.__is_polled,
            None,
            None, """Provide the 'polled' attribute.

            Indicates whether the member should be implemented 'polled.'
            Read-only."""
        )

        service_type = property(
            lambda self: self.__service,
            None,
            None, """The recommended service type.

            Reports the recommended service type, using one if the
            DatapointMember.ACKNOWLEDGED, REPEATED, UNREPEATED or UNSPECIFIED
            constants."""
        )

        def _signature(self):
            """Return a 32-bit signature for this item.

            The signature reflects all attributes relevant to the interoperable
            interface. Note the signature is not a hash, and note that the
            Python hash() function cannot generally be used to compute a
            signature or parts of it due to its random seed.
            The signature must remain the same every time the application
            executes on a given physical device (hardware), unless an aspect
            affecting the interoperable interface changes.
            """
            signature = super()._signature() + \
                (self.__is_output << 11) + \
                (self.__is_polled << 13)
            return signature

        def __str__(self):
            return '{0} {1}'.format(
                "Output" if self.__is_output else "Input",
                super().__str__()
            )

    class PropertyMember(Member):
        """The class details the properties of a profile's property member."""

        #
        # Some useful constants. Values for these constants are chosen to match
        # the equivalent constants used by the LonMark Device Resource Files
        # (DRF) and API, as this simplifies transcoding definitions from DRF
        # to pilon.
        #

        def __init__(self, name, profile, number, datatype, mandatory,
                     array_size_min=0, array_size_max=0,
                     flags=PropertyFlags.NONE,
                     minimum=None,
                     maximum=None,
                     invalid=None,
                     default=None,
                     doc=''):
            """Create a PropertyMember object.

            Arguments:
            name        the member name, as defined with the profile
            profile     the profile which defines this member
            number      the member number, as defined with the profile
            datatype    The type to use (not an instance of the type!)
            mandatory   True for mandatory profile members
            array_size_min   Minimum size for array implementation, see below.
            array_size_max   Maximum size for array implementation, see below.
            flags       See base.PropertyFlags.DEVICE_SPECIFIC, MFG, RESET, etc
            minimum     Set to None or provide bytes object. See Profile.Member
            maximum     Set to None or provide bytes object. See Profile.Member
            invalid     Set to None or provide bytes object. See Profile.Member
            default     Set to None or provide bytes object. See Profile.Member

            A property is typically implemented as a single property. For
            example, a thermostat profile might include a property to configure
            the temperature setpoint increment during night mode.

            However, profiles can require that a property be implemented as a
            property array with Z elements. The profile can require Z to be an
            exact number N, or to be in a N..M range. The profile can also
            prevent the array implementation.

            For example, a profile can require that the night mode temperature
            setpoint increment be implemented as a single property, but it can
            support a linearization curve of 5 to 100 linearization points, and
            it could support hourly temperature setpoint. The profile might
            require that the hourly set points are implemented as a property
            array of 24 elements.

            Aspects related to the implementation as a property array are
            governed by the array_size_min and array_size_max values as
            follows:

            array_size_min == 0 and array_size_max == 0:
            Array implementation prohibited

            array_size_min == N, N>0, array_size_max == N
            Array implementation required with size N

            array_size_min == N, N>=0, array_size_max == M, M>N:
            Array implementation permitted, size N..M
            """
            super().__init__(
                name=name,
                profile=profile,
                number=number,
                datatype=datatype,
                mandatory=mandatory,
                minimum=minimum,
                maximum=maximum,
                invalid=invalid,
                default=default,
                doc=doc
            )
            self.__array_size_min = array_size_min
            self.__array_size_max = array_size_max
            self.__flags = flags | PropertyFlags.NONE     # NONE != 0!

        array_size_min = property(
            lambda self: self.__array_size_min,
            None,
            None, """The minimum size of an array implementation..

            Describes the minimum size of an array, if this property is to be
            implemented as a property array. Read-only.

            Array boundary requirements are specified as follows:

            array_size_min == 0 and array_size_max == 0:
            Array implementation prohibited

            array_size_min == N, N>0, array_size_max == N
            Array implementation required with size N

            array_size_min == N, N>=0, array_size_max == M, M>N:
            Array implementation permitted, size N..M"""
        )

        array_size_max = property(
            lambda self: self.__array_size_max,
            None,
            None, """The maximum size of an array implementation.
            Describes the maximum size of an array, if this property is to be
            implemented as a property array. Read-only.

            Array boundary requirements are specified as follows:

            array_size_min == 0 and array_size_max == 0:
            Array implementation prohibited

            array_size_min == N, N>0, array_size_max == N
            Array implementation required with size N

            array_size_min == N, N>=0, array_size_max == M, M>N:
            Array implementation permitted, size N..M"""
        )

        _flags = property(
            lambda self: self.__flags,
            None,
            None, """The property's flags.

            Returns the combined flags for this property.
            Prefer using the is_* properties to query individual flags."""
        )

        is_device_specific = property(
            lambda self: self.__flags & PropertyFlags.DEVICE_SPECIFIC,
            None,
            None, """Indicates a device-specific property.

            Indicates whether this is a device-specific property.
            Properties are flagged as device-specific if they contain device-
            specific data, which may not be applicable to other instances of
            the same application. For example, a minor version number could be
            flagged in this manner. Read-only."""
        )

        is_manufacture_only = property(
            lambda self: self.__flags & PropertyFlags.MFG,
            None,
            None, """Indicates a manufacture-only property.

            Indicates whether this is a manufacture-only property.
            Properties are flagged in this manner if they are adjusted during
            manufacture. For example, serial numbers or calibration data could
            be assigned to such a property. Read-only."""
        )

        is_reset_required = property(
            lambda self: self.__flags & PropertyFlags.RESET,
            None,
            None, """Indicates a reset requirement.

            Indicates whether the device should be reset when the property has
            been modified by a network tool. Read-only."""
        )

        is_offline_required = property(
            lambda self: self.__flags & PropertyFlags.OFFLINE,
            None,
            None, """Indicates an offline requirement.

            Indicates whether the device should be taken offline for the
            modification of this property. Note that a network tool may
            execute a more severe closure, for example by resetting the
            device. This requirement is a minimum requirement. Read-only."""
        )

        is_disable_required = property(
            lambda self: self.__flags & PropertyFlags.DISABLE,
            None,
            None, """Indicates a disable requirement.

            Indicates whether the block associated with this property should
            be disabled for the modification of this property. Note that a
            network tool may execute a more severe closure, for example by
            resetting the device or taking it offline. This requirement is a
            minimum requirement. Read-only."""
        )

        is_const = property(
            lambda self: self.__flags & PropertyFlags.CONST,
            None,
            None, """Indicates a constant property.

            Indicates whether the property is constant.
            Constant properties are used to report constant data such as
            version or model numbers. Read-only."""
        )

        def _signature(self):
            """Return a 32-bit signature for this item.

            The signature reflects all attributes relevant to the interoperable
            interface. Note the signature is not a hash, and note that the
            Python hash() function cannot generally be used to compute a
            signature or parts of it due to its random seed.
            The signature must remain the same every time the application
            executes on a given physical device (hardware), unless an aspect
            affecting the interoperable interface changes.
            """
            signature = super()._signature() + \
                (self.__array_size_min << 11) + \
                (self.__array_size_max << 19) + \
                (self.__flags << 26)
            return signature

        def __str__(self):
            array = ''
            if self.__array_size_min and \
                    self.__array_size_min == self.__array_size_max:
                array = '[{0}]'.format(self.__array_size_min)
            elif self.__array_size_min < self.__array_size_max:
                array = '[{0]..{1}]'.format(
                    self.__array_size_min, self.__array_size_max
                )

            return '{0}{1}'.format(
                super().__str__(),
                array
            )

    def __init__(self, key, scope, principal=None):
        super().__init__(key, scope)
        self.__principal = principal
        self.__derivation = 0
        self.datapoints = {}    # holds DatapointMember objects
        self.properties = {}    # holds PropertyMember objects

    def finalize(self):
        """Complete the creation of the object.

        The method must be called at the end of the constructor of any
        class which derives from Profile.
        """
        if self.__derivation >= len(Profile.Member.MEMBER_SELECTORS):
            raise TypeError(
                'Derivation of {0} from SFPT* is excessive'.format(
                    self.__class__.__name__
                )
            )
        self.__derivation += 1

    derivation = property(
        lambda self: self.__derivation,
        None,
        None, """Return the derivation from Profile.

        Indicates the generation gap, or derivation, from Profile.
        A value of zero indicates that this is a standard scope profile,
        but note that the derivation does not equal the scope selector value.
    """)

    is_inheriting = property(
        lambda self: self.type != Profile,
        None,
        None, """Indicates a profile inheriting from another.

        Indicates whether the profile is inheriting from another profile.
        Profile-inheritance is only supported by inheriting from a standard
        profile, and is subject to further restrictions."""
    )

    def _override_principal(self, v):
        """During the creation of inheriting profiles, _override_principle may
        be used to override the inherited principal datapoint member. """
        self.__principal = v

    principal = property(
        lambda self: self.__principal,
        None,
        None, """The profile's principal datapoint member or None if none.

        Returns the name of the principal datapoint member, or None if a
        principal member has not been explicitly defined. Read-only."""
    )

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """
        signature = super()._signature()

        # Iterate over *sorted* lists of dictionary keys, as the native element
        # order within a dictionary is not deterministic, and could therefore
        # affect the signature calculation.
        for member in sorted(self.datapoints):
            signature ^= self.datapoints[member]._signature()

        for member in sorted(self.properties):
            signature ^= self.properties[member]._signature()

        return signature

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return '<{0}>'.format(self.__str__())


class xxx(DataType):
    """xxx is a placeholder type.

    The xxx class does not implement an actual datapoint type. It is sometimes
    used in profile definitions to indicate that a member may use any
    datapoint type in the implementation, The xxx class is known in
    device resource files as "SNVT_xxx."

    For example, the openLoopSensor profile defines a simple and generic
    sensor, using xxx for the sensor's output. The profile definition is
    thus useful for a variety of sensor data, such as temperature, velocity or
    torque measurements.

    This xxx class provides a valid datapoint type which cannot be
    instantiated."""

    def __init__(self):
        super().__init__()
        raise toolkit.PylonInterfaceError(
            toolkit.PylonInterfaceError.XXX,
            'Datapoint placeholder type xxx cannot be implemented'
        )

    def _signature(self):
        """Return a 32-bit signature for this item.

        xxx reports a constant signature. This contributes to the
        calculation of a profile's signature, but does not affect the
        block's and the overall application signature.
        """
        return 0x78787878

    def __str__(self):
        return 'xxx'


class obj_status(Structure):
    """obj_status standard datapoint type.

    This datapoint type, known in device resource files as SNVT_obj_status,
    plays a special role within the pylon framework, because the Application
    class' implementation of the node object profile depends on this type and
    its implementation. This standard datapoint type is, therefore, given extra
    protection by providing it within the pylon.resources.base module.

    Object status (ID, status flags).

    Used to indicate the status of the various objects within a node. For more
    details, see the definition of the Node Object (nodeObject profile).

    Addition found in version 3.3 and later:

    The reset_complete field, indicates the execution of the Reset sequence of
    any object (object_id) within the device. After a Reset sequence, the
    reset_complete flag goes to TRUE (1) and it remains ‘1’ until it is cleared
    (acknowledged) via obj_request (nviRequest in the Node Object) on in
    the corresponding Object (object_id ).

    Note:The additional reset flag uses reserved1 of the previous obj_status
    structure definition.
    """

    def __init__(self, object_id=0, flags=0):
        """
        Creates obj_status.
        """
        super().__init__(
            key=93,
            scope=0
        )

        # For this type, we set the _definition to None because we'd create a
        # circular dependency otherwise. That's OK, because pylon always treats
        # this datapoint type special.
        self._definition = None

        self.__object_id = Scaled(
            size=2,
            signed=False,
            default=object_id
        )
        self._register(('object_id', self.__object_id))

        self.__flags = Scaled(
            size=4,
            signed=False,
            default=flags
        )
        self._register(('flags', self.__flags))
        self._original_name = 'SNVT_obj_status'

    def __set_object_id(self, v):
        self.__object_id._value = v

    object_id = property(
        lambda self: self.__object_id._value,
        __set_object_id,
        None, """
        Object ID (object index).
        """
    )

    def __set(self, v):
        if not isinstance(v, obj_status):
            raise TypeError('Expected instance of obj_status, '
                            'got {0}'.format(
                                type(v)
                            ))

        self.__object_id._value = v.__set_object_id
        self.__flags._value = v.__flags

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Returns the length of the data type, in bytes."""
        # No need to compute at runtime, as the size is fixed.
        return 6

    def __ior__(self, other):
        """Supports combining multiple obj_status objects into one.
        This is used to report the OR'ed status flags of multiple blocks.
        """
        if not isinstance(other, obj_status):
            raise TypeError('Can only combine obj_status objects')
        self.__object_id_value = 0
        self.__flags._value |= other.__flags._value
        return self

    def __set_flags(self, v):
        self.__flags._value = v
        self._assigned(self)

    _flags = property(
        lambda self: self.__flags,
        __set_flags,
        None, """
        Use the _flags property to access all flags through the 32-bit
        bitvector rather than through the individual flag properties supplied
        with this class.
        You should prefer using the individual flag properties to keep your
        code readable, but you should consider using this property where code
        readability is not a concern, and speed or simplicity is.
        For example, to clear all flags, assign 0 (zero) to this property.
        """
    )

    def __set_invalid_id(self, v):
        if v:
            self.__flags._value |= 0x80000000
        else:
            self.__flags._value &= ~0x80000000

    invalid_id = property(
        lambda self: self.__flags._value & 0x80000000,
        __set_invalid_id,
        None, """
        Invalid-ID flag.
        """
    )

    def __set_invalid_request(self, v):
        if v:
            self.__flags._value |= 0x40000000
        else:
            self.__flags._value &= ~0x40000000

    invalid_request = property(
        lambda self: self.__flags._value & 0x40000000,
        __set_invalid_request,
        None, """
        Invalid-request flag.
        """
    )

    def __set_disabled(self, v):
        if v:
            self.__flags._value |= 0x20000000
        else:
            self.__flags._value &= ~0x20000000

    disabled = property(
        lambda self: self.__flags._value & 0x20000000,
        __set_disabled,
        None, """
        Disabled flag.
        """
    )

    def __set_out_of_limits(self, v):
        if v:
            self.__flags._value |= 0x10000000
        else:
            self.__flags._value &= ~0x10000000

    out_of_limits = property(
        lambda self: self.__flags._value & 0x10000000,
        __set_out_of_limits,
        None, """
        Out-of-limits flag.
        """
    )

    def __set_open_circuit(self, v):
        if v:
            self.__flags._value |= 0x08000000
        else:
            self.__flags._value &= ~0x08000000

    open_circuit = property(
        lambda self: self.__flags._value & 0x08000000,
        __set_open_circuit,
        None, """
        Open-circuit flag.
        """
    )

    def __set_out_of_service(self, v):
        if v:
            self.__flags._value |= 0x04000000
        else:
            self.__flags._value &= ~0x04000000

    out_of_service = property(
        lambda self: self.__flags._value & 0x04000000,
        __set_out_of_service,
        None, """
        Out-of-service flag.
        """
    )

    def __set_mechanical_fault(self, v):
        if v:
            self.__flags._value |= 0x02000000
        else:
            self.__flags._value &= ~0x02000000

    mechanical_fault = property(
        lambda self: self.__flags._value & 0x02000000,
        __set_mechanical_fault,
        None, """
        Mechanical-fault flag.
        """
    )

    def __set_feedback_failure(self, v):
        if v:
            self.__flags._value |= 0x01000000
        else:
            self.__flags._value &= ~0x01000000

    feedback_failure = property(
        lambda self: self.__flags._value & 0x01000000,
        __set_feedback_failure,
        None, """
        """
    )

    def __set_over_range(self, v):
        if v:
            self.__flags._value |= 0x00800000
        else:
            self.__flags._value &= ~0x00800000

    over_range = property(
        lambda self: self.__flags._value & 0x00800000,
        __set_over_range,
        None, """
        Over-range flag.
        """
    )

    def __set_under_range(self, v):
        if v:
            self.__flags._value |= 0x00400000
        else:
            self.__flags._value &= ~0x00400000

    under_range = property(
        lambda self: self.__flags._value & 0x00400000,
        __set_under_range,
        None, """
        Under-range flag.
        """
    )

    def __set_electrical_fault(self, v):
        if v:
            self.__flags._value |= 0x00200000
        else:
            self.__flags._value &= ~0x00200000

    electrical_fault = property(
        lambda self: self.__flags._value & 0x00200000,
        __set_electrical_fault,
        None, """
        Electrical-fault flag.
        """
    )

    def __set_unable_to_measure(self, v):
        if v:
            self.__flags._value |= 0x00100000
        else:
            self.__flags._value &= ~0x00100000

    unable_to_measure = property(
        lambda self: self.__flags._value & 0x00100000,
        __set_unable_to_measure,
        None, """
        Unable-to-measure flag.
        """
    )

    def __set_comm_failure(self, v):
        if v:
            self.__flags._value |= 0x00080000
        else:
            self.__flags._value &= ~0x00080000

    comm_failure = property(
        lambda self: self.__flags._value & 0x00080000,
        __set_comm_failure,
        None, """
        Communications-failure flag.
        """
    )

    def __set_fail_self_test(self, v):
        if v:
            self.__flags._value |= 0x00040000
        else:
            self.__flags._value &= ~0x00040000

    fail_self_test = property(
        lambda self: self.__flags._value & 0x00040000,
        __set_fail_self_test,
        None, """
        Failed-self-test flag.
        """
    )

    def __set_self_test_in_progress(self, v):
        if v:
            self.__flags._value |= 0x00020000
        else:
            self.__flags._value &= ~0x00020000

    self_test_in_progress = property(
        lambda self: self.__flags._value & 0x00020000,
        __set_self_test_in_progress,
        None, """
        Self-test-in-progress flag.
        """
    )

    def __set_locked_out(self, v):
        if v:
            self.__flags._value |= 0x00010000
        else:
            self.__flags._value &= ~0x00010000

    locked_out = property(
        lambda self: self.__flags._value & 0x00010000,
        __set_locked_out,
        None, """
        Locked-out flag.
        """
    )

    def __set_manual_control(self, v):
        if v:
            self.__flags._value |= 0x00008000
        else:
            self.__flags._value &= ~0x00008000

    manual_control = property(
        lambda self: self.__flags._value & 0x00008000,
        __set_manual_control,
        None, """
        Manual-control flag.
        """
    )

    def __set_in_alarm(self, v):
        if v:
            self.__flags._value |= 0x00004000
        else:
            self.__flags._value &= ~0x00004000

    in_alarm = property(
        lambda self: self.__flags._value & 0x00004000,
        __set_in_alarm,
        None, """
        Input-alarm flag.
        """
    )

    def __set_in_override(self, v):
        if v:
            self.__flags._value |= 0x00002000
        else:
            self.__flags._value &= ~0x00002000

    in_override = property(
        lambda self: self.__flags._value & 0x00002000,
        __set_in_override,
        None, """
        Input-override flag.
        """
    )

    def __set_report_mask(self, v):
        if v:
            self.__flags._value |= 0x00001000
        else:
            self.__flags._value &= ~0x00001000

    report_mask = property(
        lambda self: self.__flags._value & 0x00001000,
        __set_report_mask,
        None, """
        Report-mask flag.
        """
    )

    def __set_programming_mode(self, v):
        if v:
            self.__flags._value |= 0x00000800
        else:
            self.__flags._value &= ~0x00000800

    programming_mode = property(
        lambda self: self.__flags._value & 0x00000800,
        __set_programming_mode,
        None, """
        Programming-mode flag.
        """
    )

    def __set_programming_fail(self, v):
        if v:
            self.__flags._value |= 0x00000400
        else:
            self.__flags._value &= ~0x00000400

    programming_fail = property(
        lambda self: self.__flags._value & 0x00000400,
        __set_programming_fail,
        None, """
        Programming-fail flag.
        """
    )

    def __set_alarm_notify_disabled(self, v):
        if v:
            self.__flags._value |= 0x00000200
        else:
            self.__flags._value &= ~0x00000200

    alarm_notify_disabled = property(
        lambda self: self.__flags._value & 0x00000200,
        __set_alarm_notify_disabled,
        None, """
        Alarm-notify-disabled flag.
        """
    )

    def __set_reset_complete(self, v):
        if v:
            self.__flags._value |= 0x00000100
        else:
            self.__flags._value &= ~0x00000100

    reset_complete = property(
        lambda self: self.__flags._value & 0x00000100,
        __set_reset_complete,
        None, """
        Reset flag.
        """
    )
