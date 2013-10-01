"""rac_ctrl standard datapoint type, originally defined in resource file set
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
import pylon.resources.enumerations.rail_audio_type_t
import pylon.resources.enumerations.rail_audio_sensor_type_t


class rac_ctrl(pylon.resources.base.Structure):
    """rac_ctrl standard datapoint type.  Rail-Audio Controller Control.
    Invokes audio control for a given source."""

    class addr_initType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.___bf00 = pylon.resources.base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))

            self.___bf01 = pylon.resources.base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf01', self.___bf01))

            self.__audio_sensor_type = pylon.resources.enumerations.rail_audio_sensor_type_t.rail_audio_sensor_type_t(
            )
            self._register(('audio_sensor_type', self.__audio_sensor_type))
        def __set_unit_id(self, v):
            if 0 <= v <= 8:
                self.___bf00._setbits(
                    value=v,
                    size=4,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..8')

        def __get_unit_id(self):
            return self.___bf00._getbits(
                size=4,
                offset=0,
                signed=False
            )

        unit_id = property(
            __get_unit_id,
            __set_unit_id,
            None,
            """Bitfield unit_id"""
        )

        def __set_location(self, v):
            if 0 <= v <= 15:
                self.___bf00._setbits(
                    value=v,
                    size=4,
                    offset=4
                )
            else:
                raise ValueError('Not in range 0..15')

        def __get_location(self):
            return self.___bf00._getbits(
                size=4,
                offset=4,
                signed=False
            )

        location = property(
            __get_location,
            __set_location,
            None,
            """Bitfield location"""
        )

        def __set_car_id(self, v):
            if 0 <= v <= 31:
                self.___bf01._setbits(
                    value=v,
                    size=5,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..31')

        def __get_car_id(self):
            return self.___bf01._getbits(
                size=5,
                offset=0,
                signed=False
            )

        car_id = property(
            __get_car_id,
            __set_car_id,
            None,
            """Bitfield car_id"""
        )

        def __set_reserved(self, v):
            if 0 <= v <= 7:
                self.___bf01._setbits(
                    value=v,
                    size=3,
                    offset=5
                )
            else:
                raise ValueError('Not in range 0..7')

        def __get_reserved(self):
            return self.___bf01._getbits(
                size=3,
                offset=5,
                signed=False
            )

        reserved = property(
            __get_reserved,
            __set_reserved,
            None,
            """Bitfield reserved"""
        )


        def __set_audio_sensor_type(self, v):
            self.__audio_sensor_type._value = v

        audio_sensor_type = property(
            lambda self: self.__audio_sensor_type._value,
            __set_audio_sensor_type,
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
            self.__set_audio_sensor_type(v.__audio_sensor_type)
            self.___bf01._value = v.___bf01._value
            self.___bf00._value = v.___bf00._value

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 3

    class addr_talkType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.___bf00 = pylon.resources.base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))

            self.___bf01 = pylon.resources.base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf01', self.___bf01))

            self.__audio_sensor_type = pylon.resources.enumerations.rail_audio_sensor_type_t.rail_audio_sensor_type_t(
            )
            self._register(('audio_sensor_type', self.__audio_sensor_type))
        def __set_unit_id(self, v):
            if 0 <= v <= 15:
                self.___bf00._setbits(
                    value=v,
                    size=4,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..15')

        def __get_unit_id(self):
            return self.___bf00._getbits(
                size=4,
                offset=0,
                signed=False
            )

        unit_id = property(
            __get_unit_id,
            __set_unit_id,
            None,
            """Bitfield unit_id"""
        )

        def __set_location(self, v):
            if 0 <= v <= 15:
                self.___bf00._setbits(
                    value=v,
                    size=4,
                    offset=4
                )
            else:
                raise ValueError('Not in range 0..15')

        def __get_location(self):
            return self.___bf00._getbits(
                size=4,
                offset=4,
                signed=False
            )

        location = property(
            __get_location,
            __set_location,
            None,
            """Bitfield location"""
        )

        def __set_car_id(self, v):
            if 0 <= v <= 31:
                self.___bf01._setbits(
                    value=v,
                    size=5,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..31')

        def __get_car_id(self):
            return self.___bf01._getbits(
                size=5,
                offset=0,
                signed=False
            )

        car_id = property(
            __get_car_id,
            __set_car_id,
            None,
            """Bitfield car_id"""
        )

        def __set_reserved(self, v):
            if 0 <= v <= 7:
                self.___bf01._setbits(
                    value=v,
                    size=3,
                    offset=5
                )
            else:
                raise ValueError('Not in range 0..7')

        def __get_reserved(self):
            return self.___bf01._getbits(
                size=3,
                offset=5,
                signed=False
            )

        reserved = property(
            __get_reserved,
            __set_reserved,
            None,
            """Bitfield reserved"""
        )


        def __set_audio_sensor_type(self, v):
            self.__audio_sensor_type._value = v

        audio_sensor_type = property(
            lambda self: self.__audio_sensor_type._value,
            __set_audio_sensor_type,
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
            self.__set_audio_sensor_type(v.__audio_sensor_type)
            self.___bf01._value = v.___bf01._value
            self.___bf00._value = v.___bf00._value

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 3

    class addr_destType(pylon.resources.base.Union):

        class p2pType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.___bf00 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf00', self.___bf00))

                self.___bf01 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.__audio_sensor_type = pylon.resources.enumerations.rail_audio_sensor_type_t.rail_audio_sensor_type_t(
                )
                self._register(('audio_sensor_type', self.__audio_sensor_type))
            def __set_unit_id(self, v):
                if 0 <= v <= 15:
                    self.___bf00._setbits(
                        value=v,
                        size=4,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_unit_id(self):
                return self.___bf00._getbits(
                    size=4,
                    offset=0,
                    signed=False
                )

            unit_id = property(
                __get_unit_id,
                __set_unit_id,
                None,
                """Bitfield unit_id"""
            )

            def __set_location(self, v):
                if 0 <= v <= 15:
                    self.___bf00._setbits(
                        value=v,
                        size=4,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_location(self):
                return self.___bf00._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            location = property(
                __get_location,
                __set_location,
                None,
                """Bitfield location"""
            )

            def __set_car_id(self, v):
                if 0 <= v <= 31:
                    self.___bf01._setbits(
                        value=v,
                        size=5,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..31')

            def __get_car_id(self):
                return self.___bf01._getbits(
                    size=5,
                    offset=0,
                    signed=False
                )

            car_id = property(
                __get_car_id,
                __set_car_id,
                None,
                """Bitfield car_id"""
            )

            def __set_reserved(self, v):
                if 0 <= v <= 7:
                    self.___bf01._setbits(
                        value=v,
                        size=3,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..7')

            def __get_reserved(self):
                return self.___bf01._getbits(
                    size=3,
                    offset=5,
                    signed=False
                )

            reserved = property(
                __get_reserved,
                __set_reserved,
                None,
                """Bitfield reserved"""
            )


            def __set_audio_sensor_type(self, v):
                self.__audio_sensor_type._value = v

            audio_sensor_type = property(
                lambda self: self.__audio_sensor_type._value,
                __set_audio_sensor_type,
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
                self.__set_audio_sensor_type(v.__audio_sensor_type)
                self.___bf01._value = v.___bf01._value
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class p2mType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__mask_unit = pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('mask_unit', self.__mask_unit))

                self.__mask_car = pylon.resources.base.Array(
                    [
                        pylon.resources.base.Scaled(
                            size=1,
                            signed=False,
                            minimum=0,
                            maximum=255
                        ) for i in range(4)
                    ]
                )
                self._register(('mask_car', self.__mask_car))

                self.__mask_location = pylon.resources.base.Array(
                    [
                        pylon.resources.base.Scaled(
                            size=1,
                            signed=False,
                            minimum=0,
                            maximum=255
                        ) for i in range(2)
                    ]
                )
                self._register(('mask_location', self.__mask_location))

                self.__mask_audio = pylon.resources.base.Array(
                    [
                        pylon.resources.base.Scaled(
                            size=1,
                            signed=False,
                            minimum=0,
                            maximum=255
                        ) for i in range(3)
                    ]
                )
                self._register(('mask_audio', self.__mask_audio))

            def __set_mask_unit(self, v):
                self.__mask_unit._value = v

            mask_unit = property(
                lambda self: self.__mask_unit._value,
                __set_mask_unit,
                None,
                """."""
            )

            def __set_mask_car(self, v):
                self.__mask_car._value = v

            mask_car = property(
                lambda self: self.__mask_car._value,
                __set_mask_car,
                None,
                """."""
            )

            def __set_mask_location(self, v):
                self.__mask_location._value = v

            mask_location = property(
                lambda self: self.__mask_location._value,
                __set_mask_location,
                None,
                """."""
            )

            def __set_mask_audio(self, v):
                self.__mask_audio._value = v

            mask_audio = property(
                lambda self: self.__mask_audio._value,
                __set_mask_audio,
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
                self.__set_mask_unit(v.__mask_unit)
                self.__set_mask_car(v.__mask_car)
                self.__set_mask_location(v.__mask_location)
                self.__set_mask_audio(v.__mask_audio)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 10

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__p2p = rac_ctrl.addr_destType.p2pType(
            )
            self._register(('p2p', self.__p2p))

            self.__p2m = rac_ctrl.addr_destType.p2mType(
            )
            self._register(('p2m', self.__p2m))

        def __set_p2p(self, v):
            self.__p2p._value = v

        p2p = property(
            lambda self: self.__p2p._value,
            __set_p2p,
            None,
            """."""
        )

        def __set_p2m(self, v):
            self.__p2m._value = v

        p2m = property(
            lambda self: self.__p2m._value,
            __set_p2m,
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
            self.__set_p2p(v.__p2p)
            self.__set_p2m(v.__p2m)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=181,
            scope=0
        )

        self.___bf00 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__audio_type = pylon.resources.enumerations.rail_audio_type_t.rail_audio_type_t(
        )
        self._register(('audio_type', self.__audio_type))

        self.__addr_init = rac_ctrl.addr_initType(
        )
        self._register(('addr_init', self.__addr_init))

        self.__addr_talk = rac_ctrl.addr_talkType(
        )
        self._register(('addr_talk', self.__addr_talk))

        self.__addr_dest = rac_ctrl.addr_destType(
        )
        self._register(('addr_dest', self.__addr_dest))
        self._original_name = 'SNVT_rac_ctrl'
        self._definition = standard.add(self)

    def __set_audio_line(self, v):
        if 0 <= v <= 7:
            self.___bf00._setbits(
                value=v,
                size=3,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..7')

    def __get_audio_line(self):
        return self.___bf00._getbits(
            size=3,
            offset=0,
            signed=False
        )

    audio_line = property(
        __get_audio_line,
        __set_audio_line,
        None,
        """Bitfield audio_line"""
    )

    def __set_duplex_full(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_duplex_full(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    duplex_full = property(
        __get_duplex_full,
        __set_duplex_full,
        None,
        """Bitfield duplex_full"""
    )

    def __set_dest_p2p(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_dest_p2p(self):
        return self.___bf00._getbits(
            size=1,
            offset=4,
            signed=False
        )

    dest_p2p = property(
        __get_dest_p2p,
        __set_dest_p2p,
        None,
        """Bitfield dest_p2p"""
    )

    def __set_reserved(self, v):
        if 0 <= v <= 7:
            self.___bf00._setbits(
                value=v,
                size=3,
                offset=5
            )
        else:
            raise ValueError('Not in range 0..7')

    def __get_reserved(self):
        return self.___bf00._getbits(
            size=3,
            offset=5,
            signed=False
        )

    reserved = property(
        __get_reserved,
        __set_reserved,
        None,
        """Bitfield reserved"""
    )


    def __set_audio_type(self, v):
        self.__audio_type._value = v

    audio_type = property(
        lambda self: self.__audio_type._value,
        __set_audio_type,
        None,
        """."""
    )

    def __set_addr_init(self, v):
        self.__addr_init._value = v

    addr_init = property(
        lambda self: self.__addr_init._value,
        __set_addr_init,
        None,
        """."""
    )

    def __set_addr_talk(self, v):
        self.__addr_talk._value = v

    addr_talk = property(
        lambda self: self.__addr_talk._value,
        __set_addr_talk,
        None,
        """."""
    )

    def __set_addr_dest(self, v):
        self.__addr_dest._value = v

    addr_dest = property(
        lambda self: self.__addr_dest._value,
        __set_addr_dest,
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
        self.__set_audio_type(v.__audio_type)
        self.__set_addr_init(v.__addr_init)
        self.__set_addr_talk(v.__addr_talk)
        self.__set_addr_dest(v.__addr_dest)
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 18


if __name__ == '__main__':
    # unit test code.
    item = rac_ctrl()
    pass
