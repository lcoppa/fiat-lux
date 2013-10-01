"""Utilities used with the pilon package."""

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

import collections
import logging
import sys

import pylon

logger = logging.getLogger('pylon-rtk.kit')


class PylonError(Exception):
    """Root error class for pilon-specific errors.

    The pilon package uses standard Python errors such as TypeError or
    AttributeError where applicable. For cases where no standard error class
    applies, exception classes derived from PylonError are used.
    PylonError provides both a number error identifier as well as its alpha-
    numeric message. When formatted, the error identifier is included with the
    message using a [PYLON#zzz] postfix, where zzz is the decimal error
    identifier.
    Note that error identifiers are non-contiguous.

    Classes derived from PylonError are

    PylonContextError for errors caused by a bad context (too late, bad thread)
    PylonLimitError for those caused by exceeding an intrinsic limit
    PylonInterfaceError for those related to the interoperable interface
    IsiError for those related to interoperable self-installation
    """

    def __init__(self, code, msg):
        super().__init__()
        self.__msg = msg
        self.__id = code
        logger.error(self.__str__())

    def __str__(self):
        return '{0} [PYLON#{1}]'.format(self.__msg, self.__id)

    def __repr__(self):
        return '{0}(code={1}, msg="{2}")'.format(
            type(self),
            self.__id,
            self.__msg
        )

    code = property(
        lambda self: self.__id,
        None,
        None, """
        Provides the numeric error code.
    """)

    message = property(
        lambda self: self.__msg,
        None,
        None, """
        Provides the alphanumeric error message.
    """)


class PylonContextError(PylonError):
    """Indicate an error due to a bad call context."""

    SINGLETON = 2100          # No more than one Application object allowed
    ALREADY_STARTED = 2101    # Start is started, operation has no effect
    WRONG_THREAD = 2102       # Thread violation detected
    PID_MUST_BE_SPECIFIED = 2103    # a program id must be specified
    MUST_BE_INPUT = 2002    # Operation requires an input, not an output
    MUST_BE_OUTPUT = 2003    # Operation requires an output, not an input

    def __init__(self, code, msg):
        super().__init__(code, msg)


class PylonLimitError(PylonError):
    """Indicate an error caused by exceeding a designed limit."""

    TOO_MANY_DPS = 2200     # Too many datapoints
    TOO_MANY_SUBSCRIBERS = 2201    # event subscriber limit exceeded

    def __init__(self, code, msg):
        super().__init__(code, msg)


class PylonInterfaceError(PylonError):
    """Indicate an error related to the interoperable interface."""

    NAME_TOO_LONG = 2008    # The given name exceeds the maximum length
    EMPTY_UNION = 2009      # A union must have at least one member
    XXX = 2011              # xxx placeholder type cannot be implemented
    ALREADY_IMPLEMENTED = 2012    # This item can only be implemented once
    NODE_SD_TOO_BIG = 2013    # node SD exceeds 1024 characters - illegal
    DUPLICATE_PROPERTY_TYPE = 2014      # property type must be unique in scope
    TYPE_INHERITING_NOT_ALLOWED = 2015    # type-inheriting property

    def __init__(self, code, msg):
        super().__init__(code, msg)


class PylonApiError(PylonError):
    """Indicates an API error."""

    API_FACTORYERROR = 2004    # An error occurred in the API factory
    NOT_IMPLEMENTED = 2010  # something valid was attempted but isn't supported

    def __init__(self, code, msg):
        super().__init__(code, msg)


class Timer:
    """A simple timer class.

    The Timer class provides a simple application timer with a resolution
    reported through the resolution property. The timer supports a simple
    polling API: if can be started, stopped, and queried for expiry.
    The timer does nothing unless the is_expired property is queried. This
    returns True if, and only if, the timer has expired since the last query.

    Note this is not a high precision timer; it is intended to support simple
    tasks such as implementing a timeout, a slow LED flashing pattern, or
    similar.
    """

    def __init__(self, application, timeout=0):
        """Construct a Timer object.

        Construct a Timer object with a reference to the application class and
        an optional timeout value. If the timeout is given and set to a non-
        zero value, the timer starts immediately.
        The timeout is defined in seconds, with support for fractions of
        seconds as indicated through the resolution property. For example, a
        timeout value of 0.25 describes a 250ms timer.
        """

        if not isinstance(application, pylon.device.application.Application):
            raise TypeError(
                "'application' must be an instance of the Application class, "
                " got {0} instead".format(
                    type(application)
                )
            )
        self.__app = application

        self.__expiry = 0
        self.start(timeout)

    def start(self, timeout):
        """Start the timer.

        Use start() to start or re-start this timer.
        Starting a timer with a timeout of zero has no effect.
        """

        if timeout < 0:
            raise ValueError('Timeout must be >= 0')
        elif timeout > 0:
            self.__expiry = self.__app.stack.ticks + \
                timeout * self.__app.stack.ticks_per_sec
        else:
            self.stop()

    def stop(self):
        """Stop the timer."""
        self.__expiry = 0

    def __is_expired(self):
        now = self.__app.stack.ticks
        result = self.__expiry < now
        if result:
            self.stop()
        return result

    is_running = property(
        lambda self: self.__expiry,
        None,
        None, """Indicates whether the timer is running.

        A timer is considered running when it has been started and has not yet
        been stopped. An expired timer is considered running until the
        is_expired property has been read, or the stop() method has been
        called explicitly.
    """)

    is_expired = property(
        __is_expired,
        None,
        None, """Indicates whether the timer has expired.

        Indicates whether the timer has expired. This property returns a true
        value only once, as it automatically stops an expired timer.
    """)

    resolution = property(
        lambda self: 1.0 /  self.__app.stack.ticks_per_sec,
        None,
        None, """Indicates the Timer resolution in seconds"""
    )


class Enum:
    """A simple enumeration class.

    Enum provides a simple enumeration class, that is, a mapping of a set of
    alphanumeric mnemonics and their numeric value.
    """

    def __init__(self, members, value=0):
        """Construct an enumeration with a dictionary of value:mnemonic pairs.

        Parameters:

        members: a dictionary of value:mnemonic pairs, e.g.
        { 0:'No', 1:'Maybe', 2:'Yes' }
        value: an optional default value, defaults to zero.
        """

        self.__map = members
        self.__value = self.__default = value

    def __set_value(self, value):
        if value in self.__map:
            self.__value = value
        else:
            raise ValueError(
                'Not a registered member of this enum: ' + value
            )

    value = property(
        lambda self: self.__value,
        __set_value,
        None, """Current value of the enumeration.

        When read, the value property returns the numeric value.
        When written, the property accepts both numeric and alphanumeric
        values.
    """)

    def __set_default(self, value):
        if value in self.__map:
            self.__default = value
        else:
            raise ValueError(
                'Not a registered member of this enum: {0}'.format(value)
            )

    default = property(
        lambda self: self.__default,
        __set_default,
        None, """Current default value."""
    )

    is_default = property(
        lambda self: self.__value == self.__default,
        None,
        None, """Indicates whether the current value equals the default value.

        Indicates whether the current value equals the default value.
        The default value is defined when constructing the object.
    """)

    def __str__(self):
        return self.__map[self.__value]     # report the alphanumeric self


class PilonObject:
    """Root for most objects defined within this package.

    PilonObject provides a root class with utility functions used by
    several classes defined within the pilon package.
    """
    def __repr__(self):
        return '<{0}: {1}>'.format(
            self.__class__.__name__,
            self.__str__()
        )

    def _in_selection(self, label, value, selection, exception=None):
        """Check that value is in selection, and raise an error otherwise.
           Return value on success or raise AttributeError.
           One exceptional value is allowed outside the selection.
        """
        if exception and value == exception:
            return value
        if isinstance(selection, collections.Iterable):
            if not value in selection:
                raise AttributeError(
                    '{0} must be one of {1}'.format(
                        label,
                        selection
                    )
                )
        elif value != selection:
                raise AttributeError(
                    '{0} must be {1}'.format(
                        label,
                        selection
                    )
                )
        return value

    def _in_range(self, label, value, minimum, maximum, exception=None):
        """Check that value is in the minimum...maximum range, or the
           exceptional value. Return value on success, or raise an
           AttributeError.
        """
        if exception and value == exception:
            return value
        if not (minimum <= value <= maximum):
            raise AttributeError(
                '{0} must be in the {1}..{2} range'.format(
                    label,
                    minimum,
                    maximum
                )
            )
        return value

    def _binary(self, value, expected, separator=':'):
        """Return a bytes object from string-encoded input.

        Utility to return a bytearray with the expected number of bytes, filled
        with data from a value string in hex-encoded ASCII form, where encoded
        bytes are separated with the given separator.
        For example, to_binary('65.66.67.68', (4, ), '.') yields b'efgh'

        Note 'expected' takes a tuple of supported sizes.

        The utility raises a TypeError in the event of failure.
        """
        words = value.split(separator)
        length = len(words)

        if not length in expected:
            raise TypeError(
                'Expected one of {0} encoded bytes, got {1}'.format(
                    expected,
                    length
                )
            )

        result = bytearray(length)
        i = 0
        for word in words:
            result[i] = int(word, 16)
            i += 1
        return result

    def _tostring(self, value, separator=':'):
        """Return a string representation of a bytes object.

        The function reverts _binary().
        """
        result = ''
        for b in value:
            result += '{0:02X}{1}'.format(b, separator)
        return result[:-len(separator)]


def simple_checksum(me):
    """Compute a simple 31-bit checksum over 'me', which must be iterable.

    This method computes a simple checksum over the iterable item 'me.' It is
    intended for use with the automatic signature calculation. The signature
    tries to detect changes in the interoperable interface of a device such
    that two subsequent but different versions of the interface yield two
    numerically different signature values, while two or more subsequent
    instantiations of the same interface must yield the same signature.

    Note this method is a utility used when calculating the signature, but does
    not calculate the signature itself. See Application.__signature().
    """
    cs = 0
    i = 0    # tries to reflect order in the signature

    if me:  # could be None, e.g. for optional strings such as external names
        for item in me:
            if isinstance(item, str):
                if len(item) == 1:
                    cs += ord(item) << i % 29
                else:
                    cs += (ord(item[0]) << i % 29) + simple_checksum(item[1:])
            else:
                cs += item << i % 29
            i += 1

    return cs & 0x7FFFFFFF


def ebcdic(me):
    """Transcode the given string to an 8-bit sequence of bytes.

    Note this is not the same as str.encode(encoding='ascii'), because the
    ascii encoding only accepts 7-bit values. This utility accepts an 8 bit
    value range. This transcoding here simply transcodes non-printable
    characters into their binary equivalent.
    For example, ebcdic('1\x81') yields b'1\x81', a bytes object of two bytes.
    """
    result = bytearray(len(me))
    i = 0
    for c in me:
        result[i] = ord(c)
        i += 1
    return bytes(result)


def language_version(a, b):
    """Indicates whether the current Python version is at least a.b"""
    return \
        sys.version_info.major == a and sys.version_info.minor >= b or \
        sys.version_info.major > a
