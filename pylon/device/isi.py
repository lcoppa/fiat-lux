"""The pilon ISI module, providing access to and support for ISI on pilon.

This module provides access to and support for ISI, the interoperable self-
installation protocol. See http://www.echelon.com/isi for more details about
ISI.

To use ISI with the pilon package for Python, create the pilon Application
object first. The Application.isi property provides an instance of the ISI
object, which implements the ISI class defined in this module.
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

import collections
import ctypes
import logging


import pylon
from pylon.device import toolkit
from pylon.device import event
from pylon.device import interface
from pylon.resources import base

global _me
_me = None

logger = logging.getLogger('pylon-rtk.isi')

#
# Some constants used with various ISI API
#
DEFAULT_GROUP = 128
DEFAULT_CONNECTION_TABLE_SIZE = 32
DEFAULT_REPEATS = 3

NO_ASSEMBLY = 255
NO_INDEX = 255
TICKS_PER_SECOND = 4
APPLICATION_ID_LEN = 6

MAX_CONNECTION_TABLE_SIZE = 254
MAX_DATAPOINT_INDEX = 254
MAX_ASSEMBLY_NUMBER = 254


class IsiType:
    S = 0       # type ISI/S for devices in simple ISI networks
    DA = 1      # type ISI/DA for ISI networks with a domain address server
    DAS = 2     # type ISI/DAS for implementing domain address servers

    alpha = {
        S: 'ISI-S',
        DA: 'ISI-DA',
        DAS: 'ISI-DAS'
    }


class IsiFlags:
    NONE = 0x00             # does nothing
    EXTENDED = 0x01         # enables extended DRUM and enrollment messages
    HEARTBEAT = 0x02        # enables ISI heartbeat support
    APP_PERIODIC = 0x04     # enables support for application-spec. periodics
    DIAGNOSTICS = 0x08      # enables OnDiagnostics events

    alpha = {
        NONE: 'None',
        EXTENDED: 'Extended',
        HEARTBEAT: 'Heartbeat',
        APP_PERIODIC: 'App.Periodic',
        DIAGNOSTICS: 'Diagnostics'
    }


class IsiEventCategory:
    ENGINE = 0,
    ENROLLMENT = 1,
    REGISTRATION = 2,
    OTHER = 3

    alpha = {
        ENGINE: 'Engine',
        ENROLLMENT: 'Enrollment',
        REGISTRATION: 'Registration',
        OTHER: 'Other'
    }


class IsiEvent:
    NORMAL = 0
    RUN = 1     # ISI engine is now running
    # following events relate to connection enrollment:
    PENDING = 2
    APPROVED = 3
    IMPLEMENTED = 4
    CANCELLED = 5
    DELETED = 6
    WARM = 7
    PENDING_HOST = 8
    APPROVED_HOST = 9
    # following events are related to domain and device acquisition
    ABORTED = 10
    RETRY = 11
    WINK = 12
    REGISTERED = 13

    alpha = {
        NORMAL: 'Normal',
        RUN: 'Run',
        PENDING: 'Pending',
        APPROVED: 'Approved',
        IMPLEMENTED: 'Implemented',
        CANCELLED: 'Cancelled',
        DELETED: 'Deleted',
        WARM: 'Warm',
        PENDING_HOST: 'Pending (Host)',
        APPROVED_HOST: 'Approved (Host)',
        ABORTED: 'Aborted',
        RETRY: 'Retry',
        WINK: 'Wink',
        REGISTERED: 'Registered'
    }

    category = {
        NORMAL: IsiEventCategory.ENGINE,
        RUN: IsiEventCategory.ENGINE,
        PENDING: IsiEventCategory.ENROLLMENT,
        APPROVED: IsiEventCategory.ENROLLMENT,
        IMPLEMENTED: IsiEventCategory.ENROLLMENT,
        CANCELLED: IsiEventCategory.ENROLLMENT,
        DELETED: IsiEventCategory.ENROLLMENT,
        WARM: IsiEventCategory.ENGINE,
        PENDING_HOST: IsiEventCategory.ENROLLMENT,
        APPROVED_HOST: IsiEventCategory.ENROLLMENT,
        ABORTED: IsiEventCategory.REGISTRATION,
        RETRY: IsiEventCategory.REGISTRATION,
        WINK: IsiEventCategory.REGISTRATION,
        REGISTERED: IsiEventCategory.REGISTRATION
    }


class IsiDiagnostic:
    SUBNET_NODE_ALLOCATION = 1
    SUBNET_NODE_DUPLICATE = 2
    RECEIVE_DRUM = 4
    RECEIVE_TIMG = 5
    SEND_PERIODIC = 6
    SELECTOR_DUPLICATE = 7
    SELECTOR_UPDATE = 8
    REALLOCATE_SLOT = 9

    alpha = {
        SUBNET_NODE_ALLOCATION: 'S/N allocation',
        SUBNET_NODE_DUPLICATE: 'S/N duplicate',
        RECEIVE_DRUM: 'Received DRUM',
        RECEIVE_TIMG: 'Received TIMG',
        SEND_PERIODIC: 'Send periodic',
        SELECTOR_DUPLICATE: 'Selector duplicate',
        SELECTOR_UPDATE: 'Selector update',
        REALLOCATE_SLOT: 'Reallocating slot'
    }


class IsiScope:
    STANDARD = 0
    MANUFACTURER = 0x30

    alpha = {
        STANDARD: 'Standard',
        MANUFACTURER: 'Manufacturer'
    }


class IsiDirection:
    OUTPUT = 0
    INPUT = 0x40
    ANY = 0x80
    VARIOUS = 0xC0

    alpha = {
        OUTPUT: 'Output',
        INPUT: 'Input',
        ANY: 'Any',
        VARIOUS: 'Various'
    }


class IsiControl:
    NOOP = 0
    OPEN = 1
    CREATE = 2
    EXTEND = 3
    CANCEL = 4
    LEAVE = 5
    DELETE = 6
    FACTORY = 7

    alpha = {
        NOOP: 'Noop',
        OPEN: 'Open',
        CREATE: 'Create',
        EXTEND: 'Extend',
        CANCEL: 'Cancel',
        LEAVE: 'Leave',
        DELETE: 'Delete',
        FACTORY: 'Factory'
    }


class IsiError(toolkit.PylonError):
    """Error class for ISI-specific errors.

    The ISI package uses standard Python errors  such as TypeError or
    AttributeError where applicable. For cases where no standard error class
    applies, IsiError is used.
    """

    ALREADY_STARTED = 3000      # duplicate start() - try stop() first
    API_ERROR = 3001            # an ISI API returned an error
    NO_ENROLLMENT_DATA = 3002   # Enrollment data (CSMO data) missing
    NOT_STARTED = 3003          # API unavailable until the engine is started

    def __init__(self, code, msg):
        super().__init__(code, msg)


class Enrollment(toolkit.PilonObject):
    """Describe an ISI enrollment.

    ISI connections are managed through a process called enrollment:
    One device, the connection host, begins a new connection by opening
    enrollment. The new connection is described with Enrollment.
    Receivers must then examine the enrollment data and decide whether to
    join in or not.

    The Enrollment class is used to advertise an enrollment (generated
    by the host) as well as to examine an open enrollment (on receiving
    devices).

    EnrollmentData wraps the IsiCsmoData structure known in other
    implementations of ISI.
    """

    SIZEOF = 14

    def __init__(self,
                 group=DEFAULT_GROUP,
                 direction=IsiDirection.ANY,
                 width=1,
                 profile=0,
                 type_id=0,
                 variant=0,
                 acknowledged=False,
                 poll=False,
                 scope=IsiScope.STANDARD,
                 application=bytes(APPLICATION_ID_LEN),
                 member=0,
                 raw=None):
        """Construct an Enrollment object.

        Constructs the object from raw bytes, or from distinct values.

        Construction from an raw iterable of bytes is typically used
        internally when creating an Enrollment object from an incoming
        enrollment invitation message. When raw data is provided, all
        other arguments are ignored.

        For explicit creation, for example in order to open enrollment as
        a host, create an Enrollment object using the individual constructor
        arguments, or create an object using the default values and refine
        specific aspects later.

        Each of the constructor's arguments except 'raw' corresponds to a
        property with the same name; see there for more documentation.
        """

        if raw:
            self.__created_from_raw = True
            self.__group = raw[0]
            self.__direction = raw[1] & 0x0C0
            self.__width = raw[1] & 0x3F
            self.__profile = raw[2] << 8 | raw[3]
            self.__type_id = raw[4]
            self.__variant = raw[5]

            if len(raw) > 6:    # extended fields:
                self.__acknowledged = raw[6] & 0x80
                self.__poll = raw[6] & 0x40
                self.__scope = raw[6] & 0x30
                self.__application = raw[7:7+APPLICATION_ID_LEN]
                self.__member = raw[7+APPLICATION_ID_LEN]
            else:
                self.__acknowledged = 0
                self.__poll = 0
                self.__scope = 0
                self.__application = bytes(APPLICATION_ID_LEN)
                self.__member = 0

            logger.debug('Received {0}'.format(repr(self)))
        else:
            self.__created_from_raw = False
            self.group = group
            self.direction = direction
            self.width = width
            self.profile = profile
            self.type_id = type_id
            self.variant = variant
            self.acknowledged = acknowledged
            self.poll = poll
            self.scope = scope
            self.application = application
            self.member = member

            logger.debug('Created {0}'.format(repr(self)))

    def _get_raw(self, raw=None):
        """Internal utility, returns a bytearray with the binary form of this
        object.
        """
        if not raw:
            raw = bytearray(Enrollment.SIZEOF)

        raw[0] = self.__group
        raw[1] = self.__direction | self.__width
        raw[2] = self.__profile >> 8 & 0x0FF
        raw[3] = self.__profile & 0x0FF
        raw[4] = self.__type_id
        raw[5] = self.__variant

        if len(raw) >= 14:
            i = 0
            raw[6] = self.__acknowledged | self.__poll | self.__scope
            for b in self.__application:
                raw[7+i] = b
            raw[7+APPLICATION_ID_LEN] = self.__member

        logger.debug('Submitted {0}'.format(repr(self)))

        return raw

    def __str__(self):
        return 'Grp {0} Dir {1} Profile {2} Type {3} Var {4}... '.format(
            self.group,
            IsiDirection.alpha[self.direction],
            self.profile,
            self.type_id,
            self.variant
        )

    def _resolve_application(self, program_id):
        """Internal utility, used to resolve a wildcard application
        specification. Expects a program Id in string format.
        """
        if isinstance(self.__application, str) and \
                self.__application == '*':
            self.__set_application(program_id[:APPLICATION_ID_LEN])

    def __set_group(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__group = self._in_range('Group', v, 0, 255)

    group = property(
        lambda self: self.__group,
        __set_group,
        None, """Group ID used for connecting.

        The group ID specifying a usage category for the offered ISI
        connection. The group ID may be a standard ID (0 – 127) or a
        manufacturer-defined ID (128 – 255).
        The standard group IDs are defined in the ISI Protocol Guide, see
        'ISI Group IDs and Usage Categories' (http://www.echelon.com/isi)
    """)

    def __set_direction(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__direction = self._in_selection(
            'Direction', v,
            selection=(
                IsiDirection.INPUT,
                IsiDirection.OUTPUT,
                IsiDirection.ANY,
                IsiDirection.VARIOUS
            )
        )

    direction = property(
        lambda self: self.__direction,
        __set_direction,
        None, """Datapoint direction or directions in this enrollment.

        Describes the direction or directions of datapoint(s) in the offered
        connection, based on an host-centric view.
        Use values from IsiDirection.
    """)

    def __set_width(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__width = self._in_range('Width', v, 1, 63)

    width = property(
        lambda self: self.__width,
        __set_width,
        None, """Width, or number of datapoint selectors.

        Number of selector values used with this connection, starting with the
        value of the Selector field. Value 0 is reserved for future use.
    """)

    def __set_profile(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__profile = self._in_range('Profile', v, 0, 65535)

    profile = property(
        lambda self: self.__profile,
        __set_profile,
        None, """Profile number or zero for any.

        Key number of the profile containing the primary datapoint, or zero
        if not specified.
    """)

    def __set_type_id(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        if isinstance(v, interface.Datapoint):
            v = v.get_data_item()._key
        elif isinstance(v, base.DataType):
            v = v._key
        self.__type_id = self._in_range('Datapoint type id', v, 0, 255)

    type_id = property(
        lambda self: self.__type_id,
        __set_type_id,
        None, """Primary datapoint type ID or zero for any.

        The primary datapoint's type key, or zero if not specified.
        You may also assign a datapoint object to this property.
    """)

    def __set_variant(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__variant = self._in_range('Variant', v, 0, 254)

    variant = property(
        lambda self: self.__variant,
        __set_variant,
        None, """Variant value, zero for unspecified.

        The variant value, which is an identifier that customizes the
        information specified in the connection invitation. Variants may be
        defined for any device category and/or functional profile/member number
        pair. Set to zero unless otherwise known.
        Values 1 – 127 reserved for standard variant values specified by the
        ISI Protocol Specification and by standard profiles.
        Values 128 – 254 are available for use by manufacturer-specific
        connections. Value 255 is reserved for future use.
    """)

    def __set_acknowledged(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__acknowledged = 0x80 if v else 0

    acknowledged = property(
        lambda self: True if self.__acknowledged else False,
        __set_acknowledged,
        None, """Acknowledged service requested.

        Indicates whether the enrollment uses acknowledged service.

        This is typically cleared to enable a multicast repeated connection.
        Set to True for an acknowledged unicast connection.
    """)

    def __set_poll(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__poll = 0x40 if v else 0

    poll = property(
        lambda self: True if self.__poll else False,
        __set_poll,
        None, """Polled connection requested.

        Indicates whether the enrollment uses a polled service.

        Typically cleared to enable an event-driven connection.
        Set to True for a polled connection where the destination devices
        must poll the source devices for data.
    """)

    def __set_scope(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__scope = self._in_selection(
            'Scope', v,
            selection=(
                IsiScope.STANDARD,
                IsiScope.MANUFACTURER
            )
        )

    scope = property(
        lambda self: self.__scope,
        __set_scope,
        None, """Definition scope identifier.

        Set to IsiScope.STANDARD to indicate that profile and datapoint types
        refer to standard types. Set to IsiScope.MANUFACTURER to indicate that
        profile and datapoint types used with this enrollment refer to
        user-defined types. All other values are reserved.
    """)

    def __set_application(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        if isinstance(v, bytes) or isinstance(v, bytearray):
            if len(v) != APPLICATION_ID_LEN:
                raise AttributeError(
                    'Expected {0} bytes, got {1}'.format(
                        APPLICATION_ID_LEN,
                        len(v)
                    )
                )
            self.__application = v
        elif isinstance(v, str) and v == '*':
            # resolve this later
            self.__application = v
        else:
            self.__application = self._binary(v, (APPLICATION_ID_LEN, ), ':')

    application = property(
        lambda self: self.__application,
        __set_application,
        None, """Application identifier.

        The first 6 bytes of the host’s standard program ID — the last two
        standard program ID bytes (channel type and model number) are not
        included here. All bytes are zero for 'don't care.'

        The property accepts bytes or bytearray objects, or ASCII-encoded
        strings in the '9F:FF:FF:12:34:56' form. Hosting devices may also
        specify "*", which is interpreted as the first 6 bytes of the
        running application's standard program ID.
    """)

    def __set_member(self, v):
        if self.__created_from_raw:
            raise AttributeError(
                'This Enrollment object is read-only'
            )
        self.__member = self._in_range('Member', v, 0, 255)

    member = property(
        lambda self: self.__member,
        __set_member,
        None, """Member number.

        Datapoint member number with the profile, or zero if not specified.
    """)


class Assembly(toolkit.PilonObject):
    """Describes an ISI assembly.

    ISI manages datapoint connections using Assemblies.

    An assembly is a set of assembly members, identified through their zero-
    based offset within the assembly. Each member is a single datapoint, or a
    set of datapoints.
    Multiple datapoints applying to the same assembly member share the same
    datapoint selector value; a concept used with advanced connections.

    A simple assembly contains just one datapoint. More complex assemblies
    can contain all datapoints of a block (a profile implementation), but
    ISI assemblies are unrestricted in relation to profiles and blocks.

    Most assemblies contain one or more datapoints, one for each offset into
    the assembly.

    No datapoint shall be part of an assembly more than once.

    This class allows registering your script's assemblies, and passing that
    information to the ISI object.

    The class also holds the associated Enrollment object, which describes how
    the assembly will advertise its connection in an enrollment message when
    necessary. The enrollment description is required only for those assemblies
    which can act as enrollment hosts (i.e. the open_enrollment() API is used).
    """

    assemblies = {}

    def __init__(self, assembly, enrollment, number=None):
        """Create an assembly object.

        Arguments:

        assembly    an iterable object describing the assembly. Consult the
                    Assembly.assembly property for more details about the
                    construction of this argument.

        enrollment  the enrollment data for assemblies which might open
                    enrollment, can be set to None if the assembly never opens
                    enrollment.

        number      an assembly Id number unique for this script. Consult the
                    Assembly.number property for more details about the choice
                    of assembly numbers and other important considerations.

                    The number argument is optional. If no number is specified,
                    the next available number is allocated in sequence.

        It is recommended to create all supported assembly objects at
        initialization time, and to refer these previously created objects at
        runtime. Dynamic creation of assembly objects at runtime generally
        leads to inefficient code, as assembly objects remain in memory until
        the application shuts down.
        """
        super().__init__()
        self.__set_assembly(assembly)
        self.__set_enrollment(enrollment)
        self.__set_number(number)

        if self.number in Assembly.assemblies:
            raise ValueError(
                'Duplicate assembly number {0}'.format(
                    self.number
                )
            )

        Assembly.assemblies[self.number] = self

        self.__enrollment.width = self.width

    def __set_assembly(self, description):
        """Validate and assign the assembly description.

        The conditions and requirements are documented with Assembly.assembly.
        The method generates an internal assembly object of iterables.

        Note the uniqueness of assembly members is not being validated.
        """
        def check_index(dp):
            if dp.index > MAX_DATAPOINT_INDEX:
                raise AttributeError(
                    'Only datapoints with index less than {0} can be '
                    'supported by this implementation'.format(
                        1+MAX_DATAPOINT_INDEX
                    )
                )
            return dp

        self.__assembly = None

        if isinstance(description, pylon.device.interface.Datapoint):
            # trivial assembly:
            self.__assembly = ((check_index(description), ), )
        else:
            outer = []
            if not outer:
                raise TypeError(
                    'An assembly cannot be empty'
                )
            for member in description:
                if isinstance(member, pylon.device.interface.Datapoint):
                    outer.append((check_index(member), ))
                else:
                    inner = []
                    if not inner:
                        raise TypeError(
                            'An assembly member list cannot be empty'
                        )
                    for item in member:
                        if isinstance(item, pylon.device.interface.Datapoint):
                            inner.append(check_index(item))
                        else:
                            raise TypeError(
                                'Assembly members must be Datapoint objects '
                                'or iterables yielding Datapoint objects.'
                            )
                    outer.append(tuple(inner))
            self.__assembly = tuple(outer)

    # noinspection PyPropertyDefinition
    assembly = property(
        lambda self: self.__assembly,
        __set_assembly,
        None, """The assembly description or 'shape'.

        When written to, accepts an assembly description object in the form
        detailed below. When read, returns the normalized assembly description
        object.

        When writing, the assembly property accepts an iterable object.
        Each item in this container must be an Datapoint, or another iterable
        item containing nothing but Datapoint objects.

        Examples:

        Consider three datapoints a, b and c.

        This creates an assembly with a single datapoint member:

        trivial_assembly = Assembly( a )

        This creates an assembly with three members of one datapoint each:

        simple_assembly = Assembly( (a, b, c) )

        This creates an assembly with two members, the second containing two
        datapoints. Applying multiple datapoints to one assembly member is an
        advanced feature in support of datapoint selector sharing, and is not
        commonly used.

        complex_assembly = Assembly( (a, (b, c)) )

        The assembly object does not require the use of tuple objects, any
        iterable container will be accepted.

        When reading the property, the normalized assembly description is
        returned. A normalized assembly description is one consisting of an
        outer iterable object, which contains inner iterable objects. The
        inner iterable containers, in turn, contains Datapoint objects.

        It helps to imagine the outer iterable as a horizontal structure, with
        inner iterables as vertical structures as stalactites anchored within
        the horizontal plane. Following is a two-dimensional visualization of
        complex assembly (a, (b, c)) introduced above:

        a b
          c

        The ISI API for pilon automatically interprets this assembly
        description object, but for those familiar with the traditional ISI
        API, IsiGetNvIndex() calls iterate over the horizontal base along the
        'offset,' while IsiGetNextNvIndex() calls iterate over the vertical
        lists for a given offset.
    """)

    def __set_enrollment(self, v):
        if not v:
            self.__enrollment = None
        elif isinstance(v, Enrollment):
            self.__enrollment = v
        else:
            raise TypeError(
                'None or an instance of Enrollment expected, got {0}'.format(
                    type(v)
                )
            )

    enrollment = property(
        lambda self: self.__enrollment,
        None, None, """Enrollment data used when hosting.

        The Enrollment data is used to advertise this assembly in an open
        enrollment. It can be set to None for assemblies which never open
        enrollment, and must be set to meaningful data for all other
        assemblies.

        Notice the distinction between this property and the OnEnrollment
        event: this property dictates how a new enrollment will be advertised,
        while the event controls whether a newly received enrollment
        advertisement will be accepted.

        The property is read-only.
    """)

    def __set_number(self, v):
        """Sets the assembly number. v must be None or convertible to int."""
        if v:
            self.__number = self._in_range(
                'ISI assembly number',
                v,
                0,
                MAX_ASSEMBLY_NUMBER
            )
        else:
            if len(Assembly.assemblies) >= MAX_ASSEMBLY_NUMBER:
                raise ValueError(
                    'No more than {0} assemblies can be supported'.format(
                        MAX_ASSEMBLY_NUMBER
                    )
                )
            self.__number = len(Assembly.assemblies)

    number = property(
        lambda self: self.__number,
        None,
        None, """Assembly number.

        Reports the ISI assembly number.

        The ISI assembly number is a unique numeric identifier, an integer
        number in the 0..isi.MAX_ASSEMBLY_NUMBER (254) range.
        Value 255 is reserved and used to indicate "no assembly" in some
        scenarios.

        The number for each assembly is arbitrary in principle (its numeric
        value bears to significance), but once chosen, the number for a given
        assembly must remain the same throughout the lifetime of a device.

        When the device restarts after a power outage, for example, the script
        must assign the same numbers to assemblies as before.

        The recommended procedure is to create all supported assembly objects
        during the script's initialization phase, either assigning explicit
        assembly numbers, or using the build-in number allocator (which assigns
        assembly numbers sequentially, starting with zero).

        This property is read-only. The assembly number is specified with the
        constructor of the Assembly object.
    """)

    width = property(
        lambda self: len(self.__assembly),
        None,
        None, """Assembly width.

        Returns the assembly width. The property is read-only.
    """)

    def __str__(self):
        if self.__assembly:
            result = '('
            for outer in self.assembly:
                result += '('
                for inner in outer:
                    result += str(inner.index) + ', '
                result += '), '
            if self.__enrollment:
                result += '), ' + self.__enrollment.__str__()
            else:
                result += ') <No Enrollment>'
        else:
            result = 'Empty'
        return result


class OnEnrollmentEventArgs(event.EventArgs):
    """Argument type for the OnEnrollment event.

    This argument type supplies the following data to your script:

    assemblies  a dictionary of previously defined isi.Assembly objects, where
                the assembly number is the dictionary key.

    automatic   a Boolean, indicating whether this event relates to automatic
                enrollment.

    enrollment  an isi.Enrollment object, describing the enrollment on offer.

    Your event handler must inspect this object and return the related assembly
    number(s) through the result output parameter:

    result      this is your event handler's output parameter. It indicates
                the assembly or assemblies, if any, who are candidates for
                enrolling in the new enrollment.

                Indicating an assembly merely enlists the assembly as a
                candidate; it will be 'provisionally approved.' To register a
                provisionally approved assembly with the open enrollment, your
                application must call the create_enrollment() or
                extend_enrollment() API.

                To indicate that no assembly is provisionally approved for this
                enrollment, return isi.NO_ASSEMBLY (the default).

                To provisionally approve a single assembly, return its assembly
                number. You can obtain a given Assembly object's assembly
                number from its number property.

                To provisionally approve multiple assemblies, return an
                iterable object (such as a set or tuple), containing all
                applicable assembly numbers.

    Notice the distinction between the Assembly.enrollment property and this
    event: the property dictates how a new enrollment will be advertised,
    while the event controls whether a newly received enrollment
    advertisement will be accepted. Scripts generally accept a variety of
    compatible enrollment advertisements, but can only open enrollment by
    sending one specific open enrollment message and related Enrollment object.
    """

    def __init__(self, enrollment, automatic, result=NO_ASSEMBLY):
        super().__init__('OnEnrollment')

        self.__enrollment = enrollment
        self.__automatic = automatic
        self.__result = result

    assemblies = property(
        lambda self: Assembly.assemblies,
        None,
        None, """Dictionary of assemblies.

        Returns the dictionary of currently defined Assembly objects, where the
        assembly number is used for the dictionary key.

        The property is read-only.
    """)

    automatic = property(
        lambda self: self.__automatic,
        None,
        None, """True for automatic enrollment.

        Returns the 'automatic' attribute of the open enrollment.
        The property is read-only.
    """)

    enrollment = property(
        lambda self: self.__enrollment,
        None,
        None, """Enrollment on offer.

        Returns the Enrollment object which describes the enrollment on offer.
        The property is read-only.
    """)

    def __set_result(self, v):
        """Internal setter for the 'result' output parameter.
        """
        if v == NO_INDEX:
            self.__result = NO_INDEX
        elif isinstance(v, int):
            self.__result = v
        elif isinstance(v, Assembly):
            self.__result = v.number
        elif isinstance(v, collections.Iterable):
            self.__result = []

            for a in v:
                if isinstance(a, int):
                    self.__result.append(a)
                elif isinstance(a, Assembly):
                    self.__result.append(a.number)
                else:
                    self.__result.append(int(a))

        else:
            raise TypeError(
                'Result must be NO_ASSEMBLY, an integer assembly number, an '
                'assembly, or an iterable item containing integer assembly '
                'numbers or assemblies.'
            )

    result = property(
        lambda self: self.__result,
        __set_result,
        None, """Enrollment validation result.

        This is your event handler's output parameter. It indicates the
        assembly or assemblies, if any, who are candidates for enrolling in the
        new enrollment.

        Indicating an assembly merely enlists the assembly as a candidate; it
        will be 'provisionally approved.' To register a provisionally approved
        assembly with the open enrollment, your application must call the
        create_enrollment() or extend_enrollment() API.

        To indicate that no assembly is provisionally approved for this
        enrollment, return isi.NO_ASSEMBLY (the default).

        To provisionally approve a single assembly, return its assembly number.
        You can obtain a given Assembly object's assembly number from its
        number property.

        To provisionally approve multiple assemblies, return an iterable object
        (such as a set or tuple), containing all applicable assembly numbers.
    """)


class OnUserInterfaceEventArgs(event.EventArgs):
    """Argument type for the OnUserInterface event.

    This argument type supplies the following data to your script:

    event       a value from the constants defined in IsiEvent

    parameter   an event-specific parameter
    """

    def __init__(self, event, parameter):
        super().__init__('OnUserInterface')

        self.__event = event
        self.__parameter = parameter

    event_code = property(
        lambda self: self.__event,
        None,
        None, """User interface event code.

        Returns the user interface event code, one of the constants defined
        with IsiEvent.
        The property is read-only.
    """)

    parameter = property(
        lambda self: self.__parameter,
        None,
        None, """User interface event parameter.

        Returns the parameter value to accompany the event.
        The property is read-only.
    """)


class OnDiagnosticsEventArgs(event.EventArgs):
    """Argument type for the OnDiagnostics event.

    This argument type supplies the following data to your script:

    code        a value from the constants defined in IsiDiagnostics

    parameter   an code-specific parameter
    """

    def __init__(self, code, parameter):
        super().__init__('OnDiagnostic')

        self.__code = code
        self.__parameter = parameter

    code = property(
        lambda self: self.__code,
        None,
        None, """Diagnostics code.

        Returns the diagnostics code, one of the constants defined
        with IsiDiagnostics. The property is read-only.
    """)

    parameter = property(
        lambda self: self.__parameter,
        None,
        None, """Diagnostics parameter.

        Returns the parameter value to accompany the event.
        The property is read-only.
    """)


#
#   First-level event handlers, event handler prototypes and callback proxies
#


def __on_update_ui(event, parameter):
    if _me:
        try:
            _me._on_update_ui(event, parameter)
        except Exception as e:
            logger.error(
                'First level __on_update_ui(): {0}'.format(
                    e
                )
            )

_on_update_ui_proto = ctypes.CFUNCTYPE(
    None,
    ctypes.c_int, ctypes.c_uint8
)
_on_update_ui_proxy = _on_update_ui_proto(
    __on_update_ui
)


def __on_update_diag(event, parameter):
    if _me:
        try:
            _me._on_update_diag(event, parameter)
        except Exception as e:
            logger.error(
                'First level __on_update_diag(): {0}'.format(
                    e
                )
            )

_on_update_diag_proto = ctypes.CFUNCTYPE(
    None,
    ctypes.c_int, ctypes.c_uint8
)
_on_update_diag_proxy = _on_update_diag_proto(
    __on_update_diag
)


def __on_get_dp_index(assembly, offset, previous):
    result = NO_INDEX

    if _me:
        try:
            result = _me._on_get_dp_index(assembly, offset, previous)
        except Exception as e:
            logger.error(
                'First level __on_get_dp_index(): {0}'.format(
                    e
                )
            )
    return result

_on_get_dp_index_proto = ctypes.CFUNCTYPE(
    ctypes.c_uint,
    ctypes.c_uint, ctypes.c_uint, ctypes.c_uint
)
_on_get_dp_index_proxy = _on_get_dp_index_proto(
    __on_get_dp_index
)


def __on_get_width(assembly):
    result = 1

    if _me:
        try:
            result = _me._on_get_width(assembly)
        except Exception as e:
            logger.error(
                'First level __on_get_width(): {0}'.format(
                    e
                )
            )
    return result

_on_get_width_proto = ctypes.CFUNCTYPE(
    ctypes.c_uint,
    ctypes.c_uint
)
_on_get_width_proxy = _on_get_width_proto(
    __on_get_width
)


class _rawCsmoData(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('data', ctypes.c_ubyte * Enrollment.SIZEOF)
    ]


def __on_create_csmo(assembly, csmoData):
    if _me:
        try:
            _me._on_create_csmo(assembly, csmoData.contents)
        except Exception as e:
            logger.error(
                'First level __on_create_csmo(): {0}'.format(
                    e
                )
            )

_on_create_csmo_proto = ctypes.CFUNCTYPE(
    None,
    ctypes.c_uint, ctypes.POINTER(_rawCsmoData)
)
_on_create_csmo_proxy = _on_create_csmo_proto(
    __on_create_csmo
)


def __on_get_assembly(csmo, automatic, previous):
    result = NO_ASSEMBLY
    if _me:
        try:
            result = _me._on_get_assembly(
                ctypes.string_at(
                    csmo,
                    Enrollment.SIZEOF
                ),
                automatic,
                previous
            )
        except Exception as e:
            logger.error(
                'First-level __on_get_assembly(): {0}'.format(
                    e
                )
            )
    return result

_on_get_assembly_proto = ctypes.CFUNCTYPE(
    ctypes.c_uint,
    ctypes.c_void_p, ctypes.c_int, ctypes.c_uint
)
_on_get_assembly_proxy = _on_get_assembly_proto(
    __on_get_assembly
)


class ISI(toolkit.PilonObject):
    """
    This class wraps the ISI/pi C language API into pilon for Python.

    The class is used by the application object; an ISI object may be
    obtained from Application.isi.
    """

    def __init__(self, stack, application, library='libpylon-isi.so'):
        """Create an ISI object.

        You do not normally create ISI objects manually. Instead, the
        Application object creates an ISI object as and when necessary,
        which can be obtained from Application.isi.
        """
        self.__stack = stack
        self.__app = application
        self.__library = library
        self.__engine = None

        global _me
        _me = self

        self.__type = IsiType.DA
        self.__flags = IsiFlags.EXTENDED + IsiFlags.DIAGNOSTICS
        self.__connection_table_size = DEFAULT_CONNECTION_TABLE_SIZE
        self.__repeats = DEFAULT_REPEATS
        self.domain_id = '{0:2X}.{1:2X}.{2:2X}'.format(
            ord('I'), ord('S'), ord('I')
        )

        self.__ticker = toolkit.Timer(self.__app)
        self.__engine = ctypes.CDLL(self.__library)

        #
        # Most API entry points are used infrequently, and thus created on
        # demand. The IsiTick API is frequently used, however, so this wrapper
        # creates a permanent entry point.
        #
        self.__tick = self.__engine.IsiTick
        self.__tick.argtypes = []
        self.__tick.restype = ctypes.c_int

        # Instead of a sequence of IsiGetAssembly() and IsiGetNextAssembly,
        # as common in other implementations of ISI, ISI/pi requires just one
        # event handler and one primary event invocation per enrollment. The
        # OnEnrollment event returns one or more applicable assemblies in one
        # call (or none), and this wrapper supplies this data into the ISI
        # engine through a series of callback invocations.
        self.__candidates = None

        self.OnEnrollment = event.SimpleEvent(limit=1, doc="""
        Signal open enrollment, and obtain a selection of applicable
        assemblies. if any, from your script.

        An ISI-enabled script generally implements this event. When the event
        occurs, the event handler inspects the enrollment details (delivered
        with an OnEnrollmentEventArgs object), and reports none, one or more
        applicable assemblies through the OnEnrollmentEventArgs.result output
        parameter.

        See the OnEnrolllmentEventArgs object and its documentation for more
        details.
        """)

        self.OnUserInterface = event.SimpleEvent(limit=None, doc="""
        Signals a change in state with relevance to the user interface.

        This event typically requires a change to the user interface. For
        example, a connect LED may need turning off, or may need to start
        flashing.

        The event supplies an OnUserInterfaceEventArgs argument, which carries
        the event_code and parameter data.
        """)

        self.OnDiagnostics = event.SimpleEvent(limit=None, doc="""
        Signals a diagnostic event.

        This event is rarely used, but it may be monitored to obtain data
        about the general operation of the network, of to monitor the operation
        when debugging.
        """)

    def __str__(self):
        return 'ISI {0}'.format(
            'is running' if self.is_running() else 'is stopped'
        )

    def _signature(self):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface and to storage or non-volatile data managed by the ISI
        engine. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes.
        """

        # Report the connection table size only, but XOR it with a non-zero
        # constant so that a zero-size connection table has effect on the
        # signature.
        signature = self.__connection_table_size ^ 0x180

        return signature

    def __call(self, label, code):
        if code:
            raise IsiError(
                IsiError.API_ERROR,
                '{0} returned API error code {1}'.format(
                    label,
                    code
                )
            )

    def __register(self, label, registrar, prototype, proxy):
        registrar.argtypes = [prototype]
        self.__call(label, registrar(proxy))

    def __set_type(self, v):
        self.__app._validate_prestart_context()
        self.__type = self._in_selection(
            'ISI type',
            v,
            (IsiType.S, IsiType.DA, IsiType.DAS)
        )

    # isi_type is named isi_* to avoid shaddowing the reserved word 'type'
    isi_type = property(
        lambda self: self.__type,
        __set_type,
        None, """The ISI type, one of the IsiType constants."""
    )

    def __set_flags(self, v):
        self.__app._validate_prestart_context()
        self.__flags = self._in_range('ISI flags', v, 0, 255)

    # isi_flags is named isi_* for consistency with isi_type; see there.
    isi_flags = property(
        lambda self: self.__flags,
        __set_flags,
        None, """Flags for the ISI engine, see IsiFlags."""
    )

    def __set_connection_table_size(self, v):
        self.__app._validate_prestart_context()
        self.__connection_table_size = self._in_range(
            'ISI connection table size',
            v, 0, MAX_CONNECTION_TABLE_SIZE
        )

    connection_table_size = property(
        lambda self: self.__connection_table_size,
        __set_connection_table_size,
        None, """Connection table size.

        Specifies the size of the ISI connection table.

        The ISI engine supports up to isi.MAX_CONNECTION_TABLE_SIZE (254)
        table entries. Most datapoint connections require one connection
        table record for each connection and each connection extension, but
        more complex (wider) connections may require multiple connection
        table records per connection and connection extension.
    """)

    def __set_repeats(self, v):
        self.__app._validate_prestart_context()
        self.__repeats = self._in_range('ISI repeat count', v, 1, 3)

    repeats = property(
        lambda self: self.__repeats,
        __set_repeats,
        None, """Number of repeats used with standard datapoint connections.

        Specifies the repeat count used with all datapoint connections, where
        all connections share the same repeat counter. Only repeat counts of 1,
        2 or 3 are supported. To take full advantage of the secondary frequency
        on a media with multiple carriers, only use a repeat count of 1 or 3.
    """)

    def __set_domain_id(self, v):
        self.__domain_id = self._binary(v, (1, 3, 6), '.')

    domain_id = property(
        lambda self: self._tostring(self.__domain_id, '.'),
        __set_domain_id,
        None, """The primary domain identifier used by ISI.

        The property uses a string-encoded format with dot-separated ascii-
        encoded hex bytes, e.g. '49.53.49'.

        The property supports 1, 3 and 6-byte domain identifiers. The length
        of the domain identifier is derived from the number of bytes provided;
        therefore, '21', '00:00:21' and '00:00:00:00:00:21' define three
        different domains.

        A unique 6-byte domain identifier is recommended in most cases, but is
        generally required when used with an open network media. An open media
        is one which might be shared with others, such as a powerline network.
    """)

    def _on_update_ui(self, event, parameter):
        logger.debug(
            'on_update_ui: event {0}, parameter {1}'. format(
                IsiEvent.alpha[event],
                parameter
            )
        )
        self.OnUserInterface.fire(
            sender=self,
            argument=OnUserInterfaceEventArgs(
                event,
                parameter
            )
        )

    def _on_update_diag(self, event, parameter):
        logger.debug(
            'on_update_diag: event {0}, parameter {1}'.format(
                IsiDiagnostic.alpha[event],
                parameter
            )
        )
        self.OnDiagnostics.fire(
            sender=self,
            argument=OnDiagnosticsEventArgs(
                event,
                parameter
            )
        )

    def _on_get_dp_index(self, assembly_number, offset, previous):
        result = NO_INDEX

        if assembly_number in Assembly.assemblies:
            assembly = Assembly.assemblies[assembly_number]

            if offset >= assembly.width:
                logger.warning(
                    'Unexpected NV index query for assembly {0}:{1}: '
                    'No such offset'.format(
                        assembly_number, offset
                    )
                )
            else:
                vertical = assembly.assembly[offset]
                if previous == NO_INDEX:
                    result = vertical[0]
                else:
                    for index in range(len(vertical)):
                        if vertical[index] == previous:
                            try:
                                result = vertical[index+1]
                            finally:
                                break
        else:
            logger.warning(
                'Unexpected NV index query for assembly {0}: '
                'No such assembly'.format(
                    assembly_number
                )
            )

        logger.debug(
            'on_get_dp_index(assembly={0}, offset={1}, prev={2}) yields '
            '{3}'.format(
                assembly_number, offset, previous, result
            )
        )

        if isinstance(result, interface.Datapoint):
            result = result.index

        return result

    def _on_get_width(self, assembly_number):
        result = 1

        if assembly_number in Assembly.assemblies:
            assembly = Assembly.assemblies[assembly_number]
            result = assembly.width
        else:
            logger.warning(
                'Unexpected width query for assembly {0}: '
                'No such assembly'.format(
                    assembly_number
                )
            )

        logger.debug(
            'on_get_width(assembly={0}) yields {1}'.format(
                assembly_number, result
            )
        )

        return result

    def _on_create_csmo(self, assembly, csmoData):
        if assembly in Assembly.assemblies:
            enrollment = Assembly.assemblies[assembly].enrollment

            if not enrollment:
                raise IsiError(
                    IsiError.NO_ENROLLMENT_DATA,
                    'Assembly {0} requires enrollment data, but none is '
                    'available'.format(assembly)
                )

            raw = enrollment._get_raw()
            for i in range(Enrollment.SIZEOF):
                csmoData.data[i] = raw[i]

            logger.debug(
                'on_create_csmo({0}) yields {1}'.format(
                    assembly,
                    str(enrollment)
                )
            )

        else:
            logger.warning(
                'Unexpected CSMO query for assembly {0}: '
                'No such assembly'.format(
                    assembly
                )
            )

    def _on_get_assembly(self, csmoData, automatic, previous):
        result = NO_ASSEMBLY

        print('CSMODATA=0x{0}, automatic={1}, previous={2}'.format(
            self._tostring(csmoData, '.'),
            'Yes' if automatic else 'No',
            previous
        ))

        def assembly(item):
            if isinstance(item, int):
                return item
            elif isinstance(item, Assembly):
                return item.number
            else:
                return NO_ASSEMBLY

        if previous == NO_ASSEMBLY:
            # First call in the get/get next assembly sequence. We must ask
            # the application:
            argument = OnEnrollmentEventArgs(
                enrollment=Enrollment(
                    raw=csmoData
                ),
                automatic=automatic
            )
            self.OnEnrollment.fire(
                sender=self,
                argument=argument
            )

            applicable = argument.result

            if isinstance(applicable, collections.Sequence):
                self.__candidates = applicable[1:]
                result = assembly(applicable[0])
            else:
                self.__candidates = None
                result = assembly(applicable)

            logger.debug(
                'on_get_assembly(enroll={0}, auto={1}, prev={2}) '
                'yields {3}'.format(
                    str(argument.enrollment),
                    automatic,
                    previous,
                    result
                )
            )
        elif self.__candidates:
            result = assembly(self.__candidates[0])
            self.__candidates = self.__candidates[1:]

            logger.debug(
                'on_get_assembly(*, auto={1}, prev={2}) '
                'yields {3}'.format(
                    automatic,
                    previous,
                    result
                )
            )

        return result

    def __validate_assembly(self, assembly):
        if isinstance(assembly, Assembly):
            assembly = assembly.number
        if not assembly in Assembly.assemblies:
            raise ValueError(
                'Assembly {0} has not been registered.'.format(
                    assembly
                )
            )
        return assembly

    def start(self):
        """Start the ISI engine.

        This is normally done by the Application class' start() method.
        """
        logger.debug('Starting ISI engine with type #{0}'.format(
            self.__type
        ))

        self.__register(
            'on_update_ui',
            self.__engine.IsiUpdateUserInterfaceRegistrar,
            _on_update_ui_proto,
            _on_update_ui_proxy
        )
        self.__register(
            '_on_update_diag',
            self.__engine.IsiUpdateDiagnosticsRegistrar,
            _on_update_diag_proto,
            _on_update_diag_proxy
        )
        self.__register(
            '_on_get_dp_index',
            self.__engine.IsiGetNvIndexRegistrar,
            _on_get_dp_index_proto,
            _on_get_dp_index_proxy
        )
        self.__register(
            '_on_get_width',
            self.__engine.IsiGetWidthRegistrar,
            _on_get_width_proto,
            _on_get_width_proxy
        )
        self.__register(
            '_on_create_csmo',
            self.__engine.IsiCreateCsmoRegistrar,
            _on_create_csmo_proto,
            _on_create_csmo_proxy
        )
        self.__register(
            '_on_get_assembly',
            self.__engine.IsiGetAssemblyRegistrar,
            _on_get_assembly_proto,
            _on_get_assembly_proxy
        )

        class _DomainId(ctypes.Structure):
            _pack_ = 1
            _fields_ = [
                ('data', ctypes.c_ubyte*6)
            ]

        did = _DomainId()
        for i in range(len(self.__domain_id)):
            did.data[i] = self.__domain_id[i]

        api = self.__engine.IsiStart
        api.argtypes = [
            ctypes.c_uint,  # size
            ctypes.c_int,   # type
            ctypes.c_int,   # flags
            ctypes.c_uint,  # connection table size
            ctypes.c_uint,  # didLen
            ctypes.POINTER(_DomainId),
            ctypes.c_uint   # repeatcount
        ]
        api.restype = ctypes.c_int
        api(
            0,
            self.__type,
            self.__flags,
            self.__connection_table_size,
            len(self.__domain_id),
            did,
            self.__repeats
        )
        self.__ticker.start(1 / TICKS_PER_SECOND)

        logger.info('Started ISI engine with type #{0}'.format(
            self.__type
        ))

    def stop(self):
        """Stop the ISI engine.

        This is normally done by the Application class' stop() method.
        """
        logger.debug('Stopping ISI')

        api = self.__engine.IsiStop
        api.argtypes = []
        api.restype = ctypes.c_int
        self.__call('IsiStop', api())

        global _me
        _me = None

        self.__engine = None

        logger.info('Stopped ISI')

    def service(self):
        """Service the ISI engine.

        This is normally done by the Application class' service() method.
        """
        if self.__ticker.is_expired:
            self.__call('IsiTick', self.__tick())
            self.__ticker.start(1 / TICKS_PER_SECOND)

    def return_to_factory_defaults(self):
        """Restore the device's self-installation data to factory defaults.

        This function restores the device's self-installation data to factory
        defaults, causing the immediate and unrecoverable loss of all
        connection information.
        This function has the same functionality regardless of whether the ISI
        engine is running or not. The engine is stopped and the device resets
        to complete the process.
        Because of the reset, this function never returns to the caller.
        Any changes related to returning to factory defaults, such as resetting
        of device-specific configuration properties to their initial values,
        must occur prior to calling this function.
        """
        logger.debug('return_to_factory_defaults() starting')

        api = self.__engine.IsiReturnToFactoryDefaults
        api.argtypes = []
        api.restype = ctypes.c_int
        self.__call('IsiReturnToFactoryDefaults', api())

        logger.info('return_to_factory_defaults() done')

    def fetch_domain(self):
        """Start or restart the fetch domain process in a domain address
        server (DAS).

        This function must not be called from a device that is not a domain
        address server. The ISI engine must be running for this function to
        have any effect, and this function only operates on a domain address
        server.
        """
        logger.debug('fetch_domain() starting')

        api = self.__engine.IsiFetchDomain
        api.argtypes = []
        api.restype = ctypes.c_int
        self.__call('IsiFetchDomain', api())

        logger.info('fetch_domain() done')

    def fetch_device(self):
        """Start or restart the fetch device process in a domain address
        server (DAS).

        This function must not be called from a device that is not a domain
        address server. This operation does not require application code on the
        remote device.
        The remote device remains unaware of the change to its primary domain.
        The ISI engine must be running for this function to have any effect,
        and this function only operates on a domain address server.
        """
        logger.debug('fetch_device() starting')

        api = self.__engine.IsiFetchDevice
        api.argtypes = []
        api.restype = ctypes.c_int
        self.__call('IsiFetchDevice', api())

        logger.info('fetch_device() done')

    def open_enrollment(self, assembly):
        """Open manual enrollment for the specified assembly.

        The method accepts an Assembly object or an assembly number.
        This operation turns the device into a connection host for this
        connection, and sends a CSMO manual connection invitation to all
        devices in the network.
        The ISI engine must be running and in the idle state.
        """
        logger.debug('open_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)

        if not Assembly.assemblies[assembly].enrollment:
            raise IsiError(
                IsiError.NO_ENROLLMENT_DATA,
                'Cannot open enrollment without an Enrollment object '
                'defined with the Assembly object'
            )

        api = self.__engine.IsiOpenEnrollment
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        self.__call('IsiOpenEnrollment', api(assembly))

        logger.info('open_enrollment({0}) done'.format(assembly))

    def create_enrollment(self, assembly):
        """Accept a connection invitation for a new connection.

        The method accepts an Assembly object or an assembly number.

        This function is called after the application has received and approved
        a CSMO open enrollment message. The connection is created anew,
        replacing any previously existing enrollment information associated
        with this assembly.
        On a connection host that has received at least one CSME enrollment
        acceptance message, this command completes the enrollment and
        implements the connection as new, replacing any previously existing
        enrollment information associated with this assembly.

        The ISI engine must be running and in the correct state for this
        function to have any effect. For a connection host, the ISI engine must
        be in the approved state. Other devices must be in the pending state.
        """
        logger.debug('create_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiCreateEnrollment
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        self.__call('IsiCreateEnrollment', api(assembly))

        logger.info('create_enrollment({0}) done'.format(assembly))

    def extend_enrollment(self, assembly):
        """Accept a connection invitation for extending an existing connection.

        The method accepts an Assembly object or an assembly number.

        This function is called after the application has received and approved
        a CSMO open enrollment message. The connection is added to any
        previously existing connections. If no previous connection exists for
        assembly, a new connection is created.
        On a connection host that has received at least one CSME enrollment
        acceptance message, this command completes the enrollment and extends
        any existing connections. If no previous connection exists for the
        assembly, a new connection is created.
        The ISI engine must be running and in the correct state for this
        function to have any effect. For a connection host, the ISI engine must
        be in the approved state. Other devices must be in the pending state.
        """
        logger.debug('extend_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiExtendEnrollment
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        self.__call('IsiExtendEnrollment', api(assembly))

        logger.info('extend_enrollment({0}) done'.format(assembly))

    def cancel_enrollment(self):
        """Cancel an open (pending or approved) enrollment.

        When used on a connection host, a CSMX connection cancellation message
        is issued to cancel enrollment on the connection members. When used on
        a device that has accepted, but not yet implemented, an open
        enrollment, this function causes the device to opt out of the
        enrollment locally.
        The function has no effect unless the ISI engine is running and in the
        pending or approved state.
        """
        logger.debug('cancel_enrollment() starting')

        api = self.__engine.IsiCancelEnrollment
        api.argtypes = []
        api.restype = ctypes.c_int
        self.__call('IsiCancelEnrollment', api())

        logger.info('cancel_enrollment() done')

    def leave_enrollment(self, assembly):
        """Remove the specified assembly from all enrolled connections as a
        local operation only.

        The method accepts an Assembly object or an assembly number.

        When used on the connection host, the function is automatically
        interpreted as a call to delete_enrollment.
        This function has no effect if the ISI engine is stopped.
        """
        logger.debug('leave_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiLeaveEnrollment
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        self.__call('IsiLeaveEnrollment', api(assembly))

        logger.info('leave_enrollment({0}) done'.format(assembly))

    def delete_enrollment(self, assembly):
        """Remove the specified assembly from all enrolled connections.

        The method accepts an Assembly object or an assembly number.

        This function removes the specified assembly from all enrolled
        connections, and sends a CSMD connection deletion message to all other
        devices in the connection to remove them from the connection as well.
        This function has no effect if the ISI engine is stopped.
        """
        logger.debug('delete_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiDeleteEnrollment
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        self.__call('IsiDeleteEnrollment', api(assembly))

        logger.info('delete_enrollment ({0}) done'.format(assembly))

    def is_becoming_host(self, assembly):
        """Query whether assembly is about to become a host for a connection.

        The method accepts an Assembly object or an assembly number.

        Returns a true value if open_enrollment has been called for the
        specified assembly, and the enrollment has not yet been timed out,
        cancelled or confirmed.

        You can also track the state of the assembly with the OnUserInterface
        event.
        The function operates in all states of the ISI engine.
        """
        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiIsBecomingHost
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        return api(assembly)

    def is_running(self):
        """Query whether the ISI engine is running.

        Returns a true value if the ISI engine is running.
        The function operates in all states of the ISI engine.
        """
        api = self.__engine.IsiIsRunning
        api.argtypes = []
        api.restype = ctypes.c_int
        return api()

    def send_drum(self):
        """Issue an out-of-schedule ISI DRUM message.

        The ISI engine periodically broadcasts DRUM messages following a built-
        in message scheduler. This API can be used for an out-of-schedule
        transmission of a DRUM message.
        Some applications send the DRUM message when a service message is sent.
        This promotes fast device discovery in some networks.
        """
        api = self.__engine.IsiSendDrum
        api.argtypes = []
        api.restype = None
        api()

    def initiate_auto_enrollment(self, assembly):
        """Start automatic enrollment for the given assembly.

        This function accepts an assembly number or an Assembly object.
        The assembly must be registered and must have a valid Enrollment
        object.

        Use this function to start automatic enrollment. The local device
        becomes the host for the automatic connection. Automatic enrollment can
        replace previous connections, if any.

        This function cannot be called before the IsiEvent.WARM event has been
        signaled through the OnUserInterface event.
        This function does nothing when the ISI engine is stopped.
        """
        logger.debug('initiate_auto_enrollment({0}) starting'.format(assembly))

        assembly = self.__validate_assembly(assembly)
        enrollment = Assembly.assemblies[assembly]

        if not enrollment:
            raise IsiError(
                IsiError.NO_ENROLLMENT_DATA,
                'Cannot initiate automatic enrollment without an Enrollment '
                'object defined with the Assembly object'
            )

        raw = enrollment._get_raw()
        csmo = _rawCsmoData()

        for i in range(Enrollment.SIZEOF):
            csmo.data[i] = raw[i]

        api = self.__engine.IsiInitiateAutoEnrollment
        api.argtypes = [
            ctypes.POINTER(_rawCsmoData),
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int

        self.__call('IsiInitiateAutoEnrollment', api(csmo, assembly))

        logger.info(
            'initiate_auto_enrollment(csmo={0}, assembly={1}'.format(
                enrollment, assembly
            )
        )

    def is_connected(self, assembly):
        """Indicate whether the given assembly is enrolled in a connection.

        This function accepts an assembly number or an Assembly object.
        The function operates in any state of the ISI engine.
        """
        assembly = self.__validate_assembly(assembly)

        api = self.__engine.IsiIsConnected
        api.argtypes = [
            ctypes.c_uint
        ]
        api.restype = ctypes.c_int
        return api(assembly)

    def engine_version(self):
        """Return the version of the ISI engine.
        """
        api = self.__engine.IsiImplementationVersion
        api.argtypes = []
        api.restype = ctypes.c_uint
        return api()

    def protocol_version(self):
        """Return the version of the ISI protocol supported by the ISI engine.
        """
        api = self.__engine.IsiProtocolVersion
        api.argtypes = []
        api.restype = ctypes.c_uint
        return api()

    def tracefile(self, filename, append):
        """Control trace logging for the ISI engine.

        To enable logging or change logging to a different file, specify a
        valid and writeable file with the filename argument. To override an
        existing file, set the append argument to False, otherwise set append
        to True to append to an existing trace file.

        Set the filename to None to stop trace logging.
        """
        api = self.__engine.IsiSetTracefile
        api.argtypes = [
            ctypes.c_char_p,
            ctypes.c_int
        ]
        api.restype = None
        api(
            filename.encode(
                encoding='ascii',
                errors='strict'
            ),
            append
        )
