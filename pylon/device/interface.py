"""The interface module

    The interface module provides classes used to implement datapoints,
    properties and functional blocks, which are all used to implement
    the interface of an interoperable pilon application.

    To implement an object based on one of these classes, you will generally
    use a corresponding factory method provided by the Application class.

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
import threading

from pylon.device import event
from pylon.device import toolkit
from pylon.resources import base


class Interface(toolkit.PilonObject):
    """The superclass for all datapoints, properties and functional blocks."""
    def __init__(self):
        super().__init__()


class Datapoint(Interface):
    """The principal class for exchanging data with the network.

    The Datapoint class implements datapoints, used to implement input or
    output datapoints. Each datapoint supports a set of methods, properties
    and events. Each datapoint also implements a value based on a datapoint
    type.

    For an input datapoint, this value is typically modified with an
    update message received from the network. Your script will typically look
    out for such an updated value with the OnUpdate event, evaluate the current
    value through the data property, and respond as appropriate.
    For example, one script could evaluate the value of an input datapoint,
    determine the new speed setpoint for a ceiling fan, and drive that fan
    using appropriate I/O circuitry at the desired speed.

    Output datapoints are typically updated by the application. For example,
    your script could sense a significant change in a temperature reading
    (maybe using suitable physical I/O circuitry). Your script might then
    subject the temperature reading to further processing (such as data
    filtering or range-limiting) and update a suitable output datapoint with
    the new value, using the datapoint's data property.

    """

    #
    # Datapoint flags, used with the Application.datapoint() factory
    #
    NONE = 0
    INPUT = 0
    CONFIG_CLASS = 0x0001       # this datapoint implements a property
    AUTH_CONFIG = 0x0002        # authentication is run-time configurable
    PRIORITY_CONFIG = 0x0004    # priority is run-time configurable
    SERVICE_CONFIG = 0x0008     # service is run-time configurable
    OFFLINE = 0x0010            # prefer value changes when offline
    POLLED = 0x0020             # the datapoint is being polled
    SYNC = 0x0040               # A synchronous datapoint
    CHANGEABLE = 0x0080         # Pilon: n/a
    PRIORITY = 0x0100           # use priority service (for outputs)
    AUTHENTICATED = 0x0200      # use authenticated service
    ACKD = 0x0400               # use acknowledged service
    UNACKD_RPT = 0x0800         # use unacknowledged, repeated service
    UNACKD = 0x1000             # use unacknowledged, unrepeated service
    OUTPUT = 0x8000             # datapoint is an output

    STANDARD = AUTH_CONFIG | PRIORITY_CONFIG | SERVICE_CONFIG

    class OnUpdateEventArgs(event.EventArgs):
        """Argument type for the OnUpdate event.

        This argument type supplies the source address of the update.
        """
        def __init__(self, source):
            super().__init__('OnUpdateEventArgs')
            self.__source = source

        source = property(
            lambda self: self.__source,
            None,
            None, """The source address for this update.

            This will be None, or a ReceiveAddress object. The ReceiveAddress
            object indicates the source (the sender) or this datapoint update,
            and indicates how the update was received on this device."""
        )

    class OnCompletionEventArgs(event.EventArgs):
        """Argument type for the OnComplete event.

        This argument type supplies a Boolean "result" property, which
        reports success or failure of a previously initiated update (the
        propagation of an output) or poll request (the request that an input
        may be updated from remote sources).
        """
        def __init__(self, result):
            super().__init__('OnCompletionEventArgs')
            self.__result = result

        result = property(
            lambda self: self.__result,
            None,
            None, """Success or failure of the related transaction."""
        )

    def __init__(self, application, index, dpDefinition, data, user_sd=None):
        """Create a Datapoint object.

        You must use the factory methods provided by the Application class to
        create any object derived from the Interface class.
        """
        super().__init__()
        self.__lock = threading.Lock()

        self.__application = application
        self.__dpd = dpDefinition
        self.__data = data		    # the value, implementing the type
        self.__data._set_onAssign(self.__on_assign)
        self.__index = index		# index, in creation order
        self.__disabled = False

        # When the application object's service routine processes an enqueued
        # output datapoint object, it submits the datapoint's value to the
        # protocol stack, and requests propagation of this datapoint. However,
        # when the service routine finds an input datapoint object in the
        # to-do queue, it needs to take one of the following actions, or both:
        # If the script has called the poll() method, it needs to request a
        # polling transaction with the protocol stack.
        # If the script has updated the value, it needs to submit the updated
        # value to the protocol stack.
        # These two possible actions are managed with the following two
        # boolean attributes and their corresponding properties.
        self.__do_poll = False
        self.__do_sync = False

        self.__array_size = 0
        self.__array_index = 0

        self._is_bound = False		# see is_bound property for details
        self.__user_sd = user_sd

        self.__dpd.DeclaredSize = len(self.__data)

        if self.__data._scope == 0:
            self.__dpd.SnvtId = self.__data._key

        # __block and __implements reference a block, if this datapoint
        # implements a block member. In this case, __implements refers to
        # the corresponding profile member object. These are set through
        # the _implement() method, used by the Application.block() factory.

        self.__block = None
        self.__member = None

        self.__properties = []

        self.OnUpdate = event.SimpleEvent(limit=None, doc="""
            Signal a new or updated value.

            This event fires when an input datapoint received a value update
            from the network. At the time of the event, the updated value is
            readily available from the corresponding datapoint object.

            Note that the event occurs with every value update; subsequent
            updates with the same value are only suppressed as part of the
            protocol's duplicate detection process.

            Arguments:

            sender:     the datapoint object to which the update occurred
            arguments:  a Datapoint.OnUpdateEventArgs object
        """)

        self.OnComplete = event.SimpleEvent(limit=None, doc="""
            Signals the completion of a transaction.

            This event fires when the propagation of an output datapoint or
            the polling of an input datapoint completes with either success
            or failure, as indicated with the OnCompletionEventArgs argument.

            Note that the fact whether a datapoint is bound, or connected, to
            another datapoint is transparent to the script. An unbound output
            datapoint, for example, will always successfully propagate (in the
            sense that no propagation failure occurs, and all intended targets
            have received the update).

            For bound datapoints, successful completion reflects the completion
            state of the corresponding network transaction. This may include
            receipt of an acknowledgement and successful authentication, or
            simply indicate successful transmission, subject to the current
            service type and other transport properties.

            Binding of datapoints as well as selecting service type and data
            properties typically is performed by ISI (or, for larger networks,
            an external network management tool), but your script can define
            some of these attributes' defaults when creating datapoint objects
            through the Application.datapoint() factory method.
        """)

    # noinspection PyUnusedLocal
    def __on_assign(self, sender):
        """Handle onAssign event."""
        if self._lock(blocking=False):
            # Add this item to the queue of pending things only if it is not
            # currently locked. Also set the do_sync flag for inputs.
            # It is assumed that a locked item is currently within a
            # with-block, which queues the item upon exit. Scripts which make
            # explicit calls to lock must explicitly unlock and propagate as
            # necessary.
            try:
                if not self.is_output:
                    self.__do_sync = True
                self.__application.enqueue(self)
            finally:
                self._unlock()

    #
    #	Properties:
    #
    properties = property(
        lambda self: tuple(self.__properties),
        None,
        None, """A tuple with property objects applying to this datapoint."""
    )

    def __set_data(self, v):
        self.__data._value = v

    data = property(
        lambda self: self.__data._value,
        __set_data,
        None, """The data implemented and supported by this datapoint.

        Gets or sets the value of the datapoint's network data.
        Writing flags the datapoint for propagation at the subsequent service()
        call.

        Writing to this property is only supported for output datapoints. Use
        the reset() method to return any datapoint, including input datapoints,
        to its initial (or 'default') value.

        Writing to this property modifies the value with a deep copy of the
        value which you assign. Reading from this property, however, yields a
        value for scalar types, and an object reference for complex types,
        according to standard Python behavior.

        Also see the get_data_object() method.
    """)

    def get_data_item(self):
        """The object implementing the datapoint type.

        Provides a reference to the object implementing the datapoint type.

        This can be useful if additional properties of this object, such as
        value range limitations, are of interest.
        """
        return self.__data

    def get_data_type(self):
        """The type of the object implementing the datapoint type."""
        return self.__data.__class__

    index = property(
        lambda self: self.__index,
        None,
        None, """The datapoint's zero-based index within the application.

        Reports the 0-based index of the datapoint within the interoperable
        application. The property is read-only. Its value is determined by
        the order in which Datapoint objects are created.
    """)

    def __set_is_disabled(self, v):
        """Internal setter, used by the disabled property."""
        self.__disabled = v

    is_disabled = property(
        lambda self: self.__disabled,
        __set_is_disabled,
        None, """Indicates and changes the datapoint's disabled state.

        A block, and each of its implemented datapoint members, can be disabled
        and enabled through the Node Object block, in response to RQ_DISABLE
        and RQ_ENABLE requests received through the Node Object block's
        nviRequest datapoint. When disabled, a block does not propagate changes
        to output datapoints, and does not process updates of input datapoints.

        In this framework, this is automatically managed by the default node
        object block, supported by the Application.on_nviRequest_update
        handler.
        """
    )

    _dpd = property(
        lambda self: self.__dpd,
        None,
        None, """Read-only. Provides the dpDefinition structure."""
    )

    name = property(
        lambda self: self.__dpd.Name,
        None,
        None, """External name, or None.

        Read-only. Provides the external name as specified when creating.
        Note the external name may be None."""
    )

    is_property = property(
        lambda self: self.__dpd.Flags & Datapoint.CONFIG_CLASS,
        None,
        None, """Indicates whether the datapoint implements a property.

        The is_property property is read-only. Its value is determined by the
        flags argument passed into the datapoint factory."""
    )

    is_authentication_configurable = property(
        lambda self: self.__dpd.Flags & Datapoint.AUTH_CONFIG,
        None,
        None, """Indicates whether authentication may be disabled or enabled.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        Scripts relying on authentication methods for datapoints should
        generally define the affected datapoints in a way that prevents a
        network tool from disabling authentication. However, scripts that
        implement applications not specifically requiring, but tolerant of,
        the use of authentication will typically implement their datapoints
        such that a network tool can enable authentication when necessary."""
    )

    is_priority_configurable = property(
        lambda self: self.__dpd.Flags & Datapoint.PRIORITY_CONFIG,
        None,
        None, """Indicates whether the priority may be changed.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        Use of priority services may lead to a higher probability of speedy
        delivery in congested network. Vital services such as fire detectors
        may prefer using priority services, but most scripts allow a network
        tool to change the priority preferences as necessary."""
    )

    is_service_configurable = property(
        lambda self: self.__dpd.Flags & Datapoint.SERVICE_CONFIG,
        None,
        None, """Indicates whether the default service type may change.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        Most scripts allow the service type to be changed by the network tool,
        and thus allow for versatile use of the device."""
    )

    is_offline_requested = property(
        lambda self: self.__dpd.Flags & Datapoint.OFFLINE,
        None,
        None, """Requests that value updates occur only when offline.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        This property expresses a preference for updating this datapoint's
        value only when the device is in the offline state. Note this property
        expresses a recommendation and preference, not a requirement."""
    )

    is_polled = property(
        lambda self: self.__dpd.Flags & Datapoint.POLLED,
        None,
        None, """Indicates a polling input or polled output.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        The property affects resource allocation when the network tool connects
        this datapoint to others. You should raise this flag for input
        datapoints with which you plan on using the poll() method, and you
        should raise this flag for output datapoints which you do not expect
        to propagate (but which may be polled by some other device or tool).
    """)

    is_sync = property(
        lambda self: self.__dpd.Flags & Datapoint.SYNC,
        None,
        None, """Indicates a synchronous datapoint.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        The sync attribute has no effect in this release."""
    )

    is_changeable_type = property(
        lambda self: self.__dpd.Flags & Datapoint.CHANGEABLE,
        None,
        None, """Indicates a changeable-type datapoint.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        Changeable-type datapoints can change the datapoint type which they
        support at runtime. Changeable-type datapoints are not supported in
        this release."""
    )

    is_priority = property(
        lambda self: self.__dpd.Flags & Datapoint.PRIORITY,
        None,
        None, """Indicates a priority datapoint.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        Indicates a priority datapoint.
        The designation has no effect for input datapoints, but priority
        output datapoints are processed before non-priority ones. Subject to
        the physical channel, priority datapoints may get priority transport
        on the media.
        A network tool may change this preference if allowed with
        is_priority_configurable. The is_priority property reflects the
        default preference, not the current actual setting."""
    )

    is_authenticated = property(
        lambda self: self.__dpd.Flags & Datapoint.AUTHENTICATED,
        None,
        None, """Indicates an authenticated datapoint.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        A network tool may change this preference if allowed with
        is_authentication_configurable. The is_authenticated property reflects
        the default preference, not the current actual setting."""
    )

    is_acknowledged_service = property(
        lambda self: self.__dpd.Flags & Datapoint.ACKD,
        None,
        None, """Prefer the acknowledged service type.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        A network tool may change this preference if allowed with
        is_service_configurable. This property reflects the default preference,
        not the current actual setting."""
    )

    is_unacknowledged_repeated_service = property(
        lambda self: self.__dpd.Flags & Datapoint.UNACKD_RPT,
        None,
        None, """Prefer the unacknowledged, repeated, service type.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        A network tool may change this preference if allowed with
        is_service_configurable. This property reflects the default preference,
        not the current actual setting."""
    )

    is_unacknowledged_service = property(
        lambda self: self.__dpd.Flags & Datapoint.UNACKD,
        None,
        None, """Prefer the unacknowledged (unrepeated) service type.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory.

        A network tool may change this preference if allowed with
        is_service_configurable. This property reflects the default preference,
        not the current actual setting."""
    )

    is_output = property(
        lambda self: self.__dpd.Flags & Datapoint.OUTPUT,
        None,
        None, """Indicates an output datapoint.

        The property is read-only. Its value is determined by the flags
        argument passed into the datapoint factory."""
    )

    is_bound = property(
        lambda self: self._is_bound,
        None,
        None, """Indicates a bound datapoint.

        This property is read-only. The application object automatically
        updates this property with the current setting in each service cycle,
        subject to the housekeeping_timeout setting."""
    )

    array_size = property(
        lambda self: self.__array_size,
        None,
        None, """Datapoint array size or zero.

        This property is read-only. The array size reports zero for a regular
        single Datapoint object, and reports N, N > 1, for a Datapoint object
        which is an element in an Datapoint array. The array_index property
        provides the zero-based index of this Datapoint object within that
        array."""
    )

    array_index = property(
        lambda self: self.__array_index,
        None,
        None, """Zero-based index within a Datapoint array.

        This property is read-only. The array_size reports zero for a regular
        single Datapoint object, and reports N, N > 1, for a Datapoint object
        which is an element in an Datapoint array. The array_index property
        provides the zero-based index of this Datapoint object within that
        array."""
    )

    def __set_block(self, v):
        if not v:
            self.__block = None
        elif isinstance(v, Block):
            self.__block = v
        else:
            raise TypeError(
                'Expected an instance of Block, got {0}'.format(
                    type(v)
                )
            )

    block = property(
        lambda self: self.__block,
        __set_block,
        None, """The block of which this object is a member, or None."""
    )

    def __set_member(self, v):
        if not v:
            self.__member = None
        elif isinstance(v, base.Profile.Member):
            self.__member = v
        else:
            raise TypeError(
                'Expected an instance of Profile.Member, got {0}'.format(
                    type(v)
                )
            )

    member = property(
        lambda self: self.__member,
        __set_member,
        None, """The profile member implemented by this object, or None."""
    )

    def __get_do_poll(self):
        result = self.__do_poll
        self.__do_poll = False
        return result

    def __get_do_sync(self):
        result = self.__do_sync
        self.__do_sync = False
        return result

    _do_poll = property(
        __get_do_poll,
        None, None, """Return and clear the do_poll flag."""
    )

    _do_sync = property(
        __get_do_sync,
        None, None, """Return and clear the do_sync flag."""
    )

    #
    #	Methods:
    #
    def __safe_name(self):
        """Internal utility, returns the external name or <Anonymous>."""
        return self.__dpd.Name if self.__dpd.Name else '<Anonymous>'

    def __safe_sd(self):
        """Internal utility, returns SD or an empty string."""
        return self.__dpd.SdString if self.__dpd.SdString else ''

    def _str(self):
        """Implement the core for __str__ overrides for both Datapoint and
        PropertyDatapoint objects.
        """
        return '{0}, {1}{2}'.format(
            self.__safe_name(),
            str(self.__data),
            ', disabled' if self.__disabled else ''
        )

    def __str__(self):
        return 'Datapoint ' + self._str()

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
        signature = self.__data._signature()
        signature += (self.__index ^ 5) << 3
        signature += self.__dpd.Flags
        signature += (toolkit.simple_checksum(self.__safe_name()) ^ 7) << 1
        signature += (toolkit.simple_checksum(self.__safe_sd()) ^ 13) << 5
        signature += (self.__array_index ^ 23) << 9
        signature += (self.__array_size ^ 17) << 13

        return signature

    #m
    #   locks, and 'with' statement context management
    #
    def _lock(self, blocking=True, timeout=None):
        """Acquire the datapoint's lock.

        Acquire the datapoint's lock, using blocking and timeout parameters
        as documented with the standard Python threading.Lock.acquire API,
        except that None may be used to specify no timeout (potentially
        infinite wait).

        This tool is typically used with the 'with' statement, e.g.

        with myDatapoint:
           # statements within the with statement are locked
           myDatapoint.data.x = 2
           myDatapoint.data.y = 3

        """
        # http://docs.python.org/3.3/library/threading.html states that it is
        # forbidden to specify a timeout if blocking is False, so we make sure
        # to comply:
        if blocking:
            return self.__lock.acquire(
                timeout=timeout if timeout else -1
            )
        else:
            return self.__lock.acquire(
                blocking=False
            )

    def _unlock(self):
        """Unlock a previously locked datapoint.

        It is an error to unlock an already unlocked datapoint. This method
        redirects to the standard Python threading.Lock.release() API."""
        self.__lock.release()

    def __enter__(self):
        self._lock()
        return self

    # noinspection PyUnusedLocal
    def __exit__(self, exc_type, exc_value, traceback):
        # Unlock all and enqueue output datapoints, unless an exception
        # occurred. We unlock the datapoint first, since enqueuing doesn't
        # modify the datapoint but could set off a potentially higher-priority
        # thread to process pending outputs, which would want to find the
        # object unlocked. (It copes with enqueued but locked objects, but
        # for optimum performance, enqueued objects should be unlocked.)
        self._unlock()
        if self.is_output and not exc_type:
            self.__application.enqueue(self)
        return False

    def _set_array_aspect(self, size, index):
        """Set the array size and array index attributes.

        This is an internal utility used when property arrays are implemented
        as datapoints."""
        self.__array_size, self.__array_index = size, index

    def poll(self):
        """Request that an input datapoint be refreshed.

        Use the poll method with an input datapoint to request that all
        output datapoints bound to this input re-send their latest
        value. Note the method succeeds even if the input datapoint
        is unbound.

        Use poll with caution and in moderation, as it can lead to peak
        network traffic demand, for example following a site-wide power
        cycle. A more defensive alternative is to operate on reasonable
        defaults or last known values, and rely on the data sources to
        update their data periodically (commonly implemented with a
        configurable heartbeat).

        """
        if self.is_output:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.MUST_BE_INPUT,
                'Can only poll inputs'
            )
        self.__application.enqueue(self)
        self.__do_poll = True

    def propagate(self):
        """Trigger propagation of an output datapoint.

        Use the propagate method to initiate propagation of this output
        datapoint without new value assignment. This is often used when
        implementing a heartbeat, the repeated re-transmission of output
        values at slow and configurable 'heartbeat intervals.'
        """

        if not self.is_output:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.MUST_BE_OUTPUT,
                'Can only propagate outputs'
            )
        self.__application.enqueue(self)

    def _implement_property(self, name, prop):
        """Register the implementation of a property member with the block.

        The method creates an instance variable within the block object, which
        grants access to the implemented member as a first-class attribute of
        the block, using the member name as defined in the profile.

        This function is used by the Application.block() and datapoint()
        factories.
        """
        self.__properties.append(prop)
        if isinstance(prop, collections.Iterable):
            for element in prop:
                element._apply_to(self)
        else:
            prop._apply_to(self)
        self.__dict__[name] = prop

    def _implements(self, block, member):
        """Maintain a link to block and member implementation.

        This method is used by the Application.block() factory method. The
        factory calls this and provides the block to which this datapoint
        applies, and the profile member which it implements.
        """
        self.__block = block
        self.__member = member

    def _complete_self_documentation(self, sd):
        """Complete generation of the self-documentation.

        This internal helper completes the supplied self-documentation string,
        adds the user-defined comment string (if any), and converts the result
        into the appropriate structures and format suitable for registration
        with the stack.
        This method is used by Datapoint and PropertyDatapoint objects.
        """
        if not self.__array_index:
            # Only Datapoint objects with array index zero have SD (that is,
            # those datapoints which are not member of a datapoint array, or
            # those implementing the first element of a datapoint array.
            # Subsequent datapoint array elements have no SD and are implicitly
            # registered with the stack.
            if self.__user_sd:
                if not sd:
                    sd = ''     # make sure we have a string to append to
                sd += ';' + self.__user_sd.strip(',; ')
            if sd:
                self._dpd.SdString = toolkit.ebcdic(sd)
        else:
            self._dpd.SdString = None

    def _compile_self_documentation(self):
        """Compute the datapoint's own self-documentation.

        This method is used by Application.__compile_sd().
        """
        if self.__block and self.__member and not self.__array_index:
            sd = '@{0}{1}{2}'.format(
                self.__block.index,
                self.__member.selector,
                self.__member.number
            )
            if self.is_changeable_type:
                sd += '?'
        else:
            sd = ''

        self._complete_self_documentation(sd)

    def implement(self, name, array_size=0):
        """Implement an optional property by name.

        Arguments:

        name        The property name as defined in the profile
        array_size  The size of the property array, if any.

        The method returns the new item.

        For property members which support an implementation as a property
        array, where the implementation is free to chose the size of the
        property array, the array_size argument determines the size of that
        array. array_size=0, the default value, yields the implementation of
        the smallest possible construct: no array if permitted, or the smallest
        permitted array.

        When array_size applies, it must be within the range of minimum to
        maximum permitted array size, as defined in the profile.

        """
        if not self.__block or not self.__member:
            raise AttributeError(
                'Can only apply properties to datapoint profile members'
            )

        self.__application._validate_prestart()

        if name in self.__member.properties:
            member = self.__member.properties[name]
        else:
            raise LookupError(
                'Not found: property {0}'. format(
                    name
                )
            )

        if member.implementer:
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.ALREADY_IMPLEMENTED,
                'Member {0} is already implemented'.format(
                    name
                )
            )

        if isinstance(member, base.Profile.PropertyMember):
            dp = self.__application._implement_block_property(
                member=member,
                block=self.__block,
                applies_to=self,
                donor=self,
                array_desc=array_size
            )
        else:
            raise TypeError(
                'Member {0} is of type {1}, expected '
                'Profile.DatapointMember or PropertyMember'.format(
                    name,
                    type(member)
                )
            )
        return dp

    #
    #	Events:
    #
    def _update(self, source):
        """Internal update re-director.

        The application object calls this when the input datapoint
        has been updated. This re-director subsequently notifies any
        subscribers to this datapoint's OnUpdate event.
        """
        self.OnUpdate.fire(
            sender=self,
            argument=Datapoint.OnUpdateEventArgs(source)
        )

    def _complete(self, success):
        """Internal completion re-director.

        The application object calls this when the datapoint receives a
        completion event. This re-director subsequently notifies any
        subscribers to this datapoint's OnComplete event.
        """
        self.OnComplete.fire(
            sender=self,
            argument=Datapoint.OnCompletionEventArgs(success)
        )


class PropertyDatapoint(Datapoint):
    """
    This class is used to implement properties as datapoints. An alternative
    method, the implementation of properties as value file elements, is not
    supported in this release.

    The PropertyDatapoint class acts like the Datapoint class, but supplies
    a different self-documentation string generator, and a few other aspects
    specific to properties.
    """

    def __init__(self, application, index, dpDefinition, data, user_sd=None):
        """Create a PropertyDatapoint object.

        This is created by factory methods. Do not create such an item
        directly.
        """
        super().__init__(
            application=application,
            index=index,
            dpDefinition=dpDefinition,
            data=data,
            user_sd=user_sd
        )

        self.__applies_to = []

    applies_to = property(
        lambda self: tuple(self.__applies_to),
        None,
        None, """A tuple of items to which this property datapoint applies."""
    )

    def _apply_to(self, item):
        self.__applies_to.append(item)

    def _enumerate_applies_to(self):
        result = ''
        for item in self.__applies_to:
            result += str(item.index) + '.'
        return result.rstrip('.')

    def _compile_self_documentation(self):
        """Compute the datapoint's own self-documentation.

        This method is used by Application.__compile_sd().
        """
        #   For a property implemented as a Datapoint:
        #
        #   SD ::= &header,select,flags,index,[array_size],[rangemod],[?][;rem]

        sd = '&'    # &

        #   &header,select
        if not self.__applies_to:
            # device property
            sd += '0,'
        elif isinstance(self.__applies_to[0], Datapoint):
            # datapoint property
            sd += '2,' + self._enumerate_applies_to()
        else:
            # block property
            sd += '1,' + self._enumerate_applies_to()

        data_item = self.get_data_item()

        # We compose the SD string with an embedded \x escape code, which we
        # transcode later. This detour is required because the 'ascii'
        # encoding is limited to a value range(128) only.
        #
        #   ,flags,index
        sd += ',{0}{1},{2}'.format(
            data_item._property_scope,
            chr(self._flags),
            data_item._property_key
        )

        # Notice that the 'dim' field is _not generated_, even if this property
        # implements a property array. The LonMark Application Layer Guidelines
        # version 3.4 are wrong in this respect; the 'dim' field for property
        # arrays is only required (and, indeed, acceptable) for properties
        # implemented in property value files.

        # ### TODO REMINDER: consider adding range-mod support
        # ### TODO REMINDER: add changeable-type support

        self._complete_self_documentation(sd)

    def __str__(self):
        return 'PropertyDatapoint ' + self._str()


class Block(Interface):
    """Block implements a profile.

    Do not instantiate Block directly. To implement a block, you must obtain it
    from the Application.block() factory method.
    """

    def __init__(self, application, index, profile, ext_name=None,
                 xxx=None):
        super().__init__()
        self.__application = application
        self.__index = index
        self.__profile = profile
        self.__ext_name = ext_name
        self.__datapoint_xxx = xxx

        self.__datapoints = []          # all datapoint members implemented
        self.__properties = []          # all properties applying to this block
        self.__principal = None

        self.status = base.obj_status(object_id=index)

        self.__array_index = 0
        self.__array_size = 0

    datapoints = property(
        lambda self: tuple(self.__datapoints),
        None,
        None, """A tuple with the currently implemented datapoint members.
        Read-only.
    """)

    properties = property(
        lambda self: tuple(self.__properties),
        None,
        None, """A tuple with property objects applying to this block.
    """)

    def _set_index(self, v):
        v = int(v)
        if v < 0:
            raise TypeError('block index must be an integer >= 0')
        self.__index = v

    index = property(
        lambda self: self.__index,
        None,
        None, """The block's zero-based index within the application.

        Reports the zero-based index of the block within this application's
        interoperable interface. The index number is used to correlated
        implementations of member datapoints and properties to the block.
        Index 0 (zero) is reserved for implementations of SFPTnodeObject, or
        profiles derived thereof, if such a profile is implemented.

        The index property is read-only, but a protected "_set_index()"
        method may be used by the Application class to re-index a previously
        created block if necessary.

        Note that a block's index may change with the implementation of the
        node object. It is recommended to refrain from inspecting a block's
        index property until the application's start() method completed.
    """)

    profile = property(
        lambda self: self.__profile,
        None,
        None, """The profile implemented by this block."""
    )

    def __set_array_index(self, v):
        self.__array_index = int(v)

    array_index = property(
        lambda self: self.__array_index,
        __set_array_index,
        None, """The index within an array of blocks.

        This property is provided to assist scripts which group block objects
        into a container (a tuple, a list, a set, etc) and share code, such as
        update event handler for member input datapoints, among those blocks.

        Such a script could create a tuple of four block object using the block
        factory in a generator expression, then assign array_index and
        array_size values to each of the elements of this block container.

        When the shared update event handler processes an input datapoint value
        update, it can determine the associated datapoint from the event
        handler's 'sender' argument. This datapoint object reports the block it
        applies to, if any, through its 'block' property, and the block might
        then reveal its index within the script-specific tuple through this
        property.

        Grouping similar blocks in this manner is optional."""
    )

    def __set_array_size(self, v):
        self.__array_size = int(v)

    array_size = property(
        lambda self: self.__array_size,
        __set_array_size,
        None, """The size of an array of blocks.

        This property is provided to assist scripts which group block objects
        into a container (a tuple, a list, a set, etc) and share code, such as
        update event handler for member input datapoints, among those blocks.

        Such a script could create a tuple of four block object using the block
        factory in a generator expression, then assign array_index and
        array_size values to each of the elements of this block container.

        When the shared update event handler processes an input datapoint value
        update, it can determine the associated datapoint from the event
        handler's 'sender' argument. This datapoint object reports the block it
        applies to, if any, through its 'block' property, and the block might
        then reveal its index within the script-specific tuple through this
        property.

        The array_size property can be useful in similar use-cases.

        Grouping similar blocks in this manner is optional."""
    )

    def __set_is_disabled(self, v):
        """Internal setter, used by the is_disabled property."""
        self.status.disabled = v
        for datapoint in self.__datapoints:
            datapoint.is_disabled = v

    is_disabled = property(
        lambda self: self.status.disabled,
        __set_is_disabled,
        None, """Indicates and changes the block's disabled state.

        A block can be disabled and enabled through the Node Object block, in
        response to RQ_DISABLE and RQ_ENABLE requests received through the
        Node Object block's nviRequest datapoint. When disabled, a block does
        not propagate changes to output datapoints, and does not process
        updates of input datapoints.
    """)

    def _implement_dp(self, name, datapoint):
        """Register the implementation of a datapoint member with the block.

        The method creates an instance variable within the block object, which
        grants access to the implemented member as a first-class attribute of
        the block, using the member name as defined in the profile.

        This function is used by the Application.block() factory.
        """
        self.__datapoints.append(datapoint)
        self.__dict__[name] = datapoint

        if name == self.__profile.principal:
            self.__principal = datapoint

    def _implement_property(self, name, property_):
        """Register the implementation of a property member with the block.

        The method creates an instance variable within the block object, which
        grants access to the implemented member as a first-class attribute of
        the block, using the member name as defined in the profile.

        This function is used by the Application.block() and datapoint()
        factories.
        """
        self.__properties.append(property_)

        if isinstance(property_, collections.Iterable):
            for element in property_:
                element._apply_to(self)
        else:   # single property
            property_._apply_to(self)

        self.__dict__[name] = property_

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
        signature = self.__profile._signature()
        signature ^= toolkit.simple_checksum(self.__ext_name) ^ self.__index

        # datapoint and property member implementations are captured with the
        # datapoint and property signatures, no need to count twice.
        return signature

    def get_self_documentation(self):
        """Return the block's self-documentation string for use with Node SD
        """
        sd = str(self.__profile._key)
        if self.__ext_name:
            sd += self.__ext_name
        return sd

    def implement(self, name, array_desc=0):
        """Implement an optional datapoint or property member by name.

        Arguments:

        name        the member name as defined in the profile
        array_desc  the array descriptor object or array size. See below.

        The method returns the new item. The method searches the desired member
        in this order:
        1. datapoint members defined in this profile
        2. datapoint members defined in the inherited profile (if any)
        3. property members defined in this profile
        4. property members defined in the inherited profile (if any)

        The array descriptor, if provided, must meet the rules described with
        the Application.block() factory method.
        """
        self.__application._validate_prestart()

        if name in self.__profile.datapoints:
            member = self.__profile.datapoints[name]
        elif name in self.__profile.properties:
            member = self.__profile.properties[name]
        else:
            raise LookupError(
                '{0} does not support member {1}'. format(
                    type(self.__profile),
                    name
                )
            )

        if member.implementer:
            return member.implementer

        array_guide = self.__application._normalize_array_desc(array_desc)

        if isinstance(member, base.Profile.DatapointMember):
            dp = self.__application._implement_block_datapoint(
                member=member,
                block=self,
                array_desc=array_guide,
                xxx=self.__datapoint_xxx
            )
        elif isinstance(member, base.Profile.PropertyMember):
            dp = self.__application._implement_block_property(
                member=member,
                block=self,
                applies_to=self,
                array_desc=array_guide,
                donor=self.__principal
            )
        else:
            raise TypeError(
                'Member {0} is of type {1}, expected '
                'Profile.DatapointMember or PropertyMember'.format(
                    name,
                    type(member)
                )
            )
        return dp

    def __str__(self):
        return 'Block {0}{1}'.format(
            self.__ext_name,
            ', disabled' if self.status.disabled else ''
        )

    principal = property(
        lambda self: self.__principal,
        None,
        None, """The principal datapoint member or None if none."""
    )
