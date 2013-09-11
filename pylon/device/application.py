"""The pilon application module, providing the Application class.

This module defines the Pylon Application class, which provides the core
of the Python for Pylon runtime kit. To create a Pylon application,
instantiate this class, set properties as necessary and create
interoperable data items such as datapoints from the appropriate
factory classes, then start() the application.
You will then need to service() the application object frequently and
periodically.
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
import logging
import logging.handlers
import math
import random
import threading
import _thread      # used in runtime < Python 3.3

from pylon.device import event
from pylon.device import toolkit
from pylon.device import interface

import pylon.device.stack
import pylon.device.system
import pylon.device.isi
from pylon.resources import base

from pylon.resources.SNVT_xxx import SNVT_xxx
from pylon.resources.SFPTnodeObject import SFPTnodeObject
from pylon.resources.object_request_t import object_request_t
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
from pylon.resources.config_source_t import config_source_t

logger = logging.getLogger('pylon-rtk')


class Application:
    """Application represents the interoperable application and device.

    Application is a singleton class, providing the principal element of the
    Pylon package for Python. Create an instance of the Application object,
    set the unique and program identifiers, then create interoperable objects
    with the corresponding factories (e.g. using the Datapoint() method).
    Also consider setting other properties of the application object, such
    as sd_string, domains, addresses, etc.
    When all interoperable items are created, call the start() function.
    Remember to call the stop() function before the application object goes
    out of scope.

    Note the application class can't be instantiated without a valid Pilon
    stack present in a suitable location along the LD_LIBRARY search path.
    """

    class State:
        """Represents the state of the Application object.

        The State class of enumerated values defines mnemonics for the state
        the application object is in. These states start with Pylon-specific
        states IDLE, INIT and CREATED, reflecting the current stage of the
        initialization process, followed by ISO/IEC 14908-3 states OFFLINE
        and ONLINE, reflecting the state of the running application.
        Note the values in this enumeration are ordered.
        """

        IDLE = 0
        INIT = 1            # Application.__init__ completed
        CREATED = 2         # LonLidCreate completed
        OFFLINE = 3         # LonLidStartStack completed and offline
        ONLINE = 4            # online

    class OnResetEventArgs(event.EventArgs):
        """Argument type for the OnReset event.

        This event carries no event data.
        """

        def __init__(self):
            super().__init__('OnResetEventArgs')

    class OnWinkEventArgs(event.EventArgs):
        """Argument type for the OnWink event.

        This event carries no event data.
        """

        def __init__(self):
            super().__init__('OnWinkEventArgs')

    class OnOfflineEventArgs(event.EventArgs):
        """Argument type for the OnOffline event.

        This event carries no event data.
        """

        def __init__(self):
            super().__init__('OnOfflineEventArgs')

    class OnOnlineEventArgs(event.EventArgs):
        """Argument type for the OnOnline event.

        This event carries no event data.
        """

        def __init__(self):
            super().__init__('OnOnlineEventArgs')

    class OnServiceLedEventArgs(event.EventArgs):
        """Argument type for the OnServiceLed event.

        This argument type carries the new service LED state, off (0), on (1)
        or flashing at 0.5Hz (2). Each interoperable device must implement the
        service LED functionality with these patterns, but it is not required
        that an implementation uses a physical LED.
        Implementations can use any suitable GUI representation, or any other
        suitable implementation, provided the 'service LED' status is easily
        obtained by the device user, integrator or administrator.
        """

        def __init__(self, state):
            super().__init__('OnServiceLedEventArgs')
            self.state = state

    __instances = 0     # Application instance counter

    def _validate_thread(self):
        """Raise PylonContextError in case of a thread violation."""
        if self.__threadid != self.__get_ident():
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.WRONG_THREAD,
                'Not the main pilon thread'
            )

    def _validate_prestart(self):
        """Raise PylonContextError if the stack is already started."""
        if self.__state > Application.State.INIT:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.ALREADY_STARTED,
                'Stack is already started'
            )

    def _validate_prestart_context(self):
        """Combine thread and pre-start validations."""
        self._validate_thread()
        self._validate_prestart()

    def _apply_bytes(self, dpi, minimum, maximum, invalid, default):
        """Apply the minimum, maximum, invalid and default bytes objects,
        if any. In case a default bytes object is provided, this is applied
        last so that the item starts out with these default values. If no
        default bytes object is provided, a temporary default bytes object
        is created using the present values, and re-applied as the default
        at the end of the sequence."""

        if minimum or maximum or invalid or default:
            # Only do anything if anything is to do at all, but if anything is
            # to do here, and a default bytes object isn't given, make one by
            # packing the current value. This is required because we must
            # restore the current (default) value after applying any of the
            # minimum, maximum or invalid bytes objects, because this process
            # modifies the current value.
            if not default:
                default = dpi._pack()

            if minimum:
                dpi._unpack(minimum)
                dpi._accept_as_minimum()
            if maximum:
                dpi._unpack(maximum)
                dpi._accept_as_maximum()
            if invalid:
                dpi._unpack(invalid)
                dpi._accept_as_invalid()
            dpi._unpack(default)
            dpi._accept_as_default()

    def __datapoint(self, object_type, data, flags, name=None, sd=None):
        """Produce a Datapoint or PropertyDatapoint object.

        __datapoint is an internal factory, producing Datapoint and
        PropertyDatapoint objects. See datapoint() for a public interface.
        """
        self._validate_prestart_context()

        if len(self.__datapoints) >= pylon.device.stack.MAX_DATAPOINTS:
            raise toolkit.PylonLimitError(
                toolkit.PylonLimitError.TOO_MANY_DPS,
                'More than {0} datapoints'.format(
                    pylon.device.stack.MAX_DATAPOINTS
                )
            )
        if name and len(name) > pylon.device.stack.MAX_EXT_DP_NAME:
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.NAME_TOO_LONG,
                "A datapoint's external name can't exceed {0} bytes".format(
                    pylon.device.stack.MAX_EXT_DP_NAME
                )
            )

        dpd = pylon.device.stack.DpDefinition()

        dpd.Version = 0
        dpd.Flags = flags
        dpd.ArrayCount = 0

        if name:
            dpd.Name = name.encode(
                encoding='ascii',
                errors='ignore'
            )
        else:
            dpd.Name = None

        dpd.MaxRate = 0
        dpd.MeanRate = 0

        index = len(self.__datapoints)

        dp = object_type(self, index, dpd, data, sd)
        self.__datapoints.append(dp)

        if dp.is_property:
            self.__no_dpp += 1
        elif dp.is_output:
            self.__no_dpo += 1
        else:
            self.__no_dpi += 1

        if self.__auto_aliases:
            self.__aliases = int(
                max(
                    3,
                    min(
                        pylon.device.stack.MAX_ALIASES,
                        self.__no_dpo/3 + self.__no_dpi/4 + self.__no_dpp/10
                    )
                )
            )
        if self.__auto_addresses:
            self.__addresses = int(
                max(
                    15,
                    min(
                        pylon.device.stack.MAX_ADDRESSES,
                        self.__bindable_mt +
                            self.__no_dpi/4 + self.__no_dpi/5 + self.__no_dpp/8
                    )
                )
            )

        dpi = dp.get_data_item()
        self._apply_bytes(
            dpi,
            dpi._minimum_bytes,
            dpi._maximum_bytes,
            dpi._invalid_bytes,
            dpi._default_bytes
        )

        logger.info('{0} {1}: {2}, "{3}"'.format(
            str(object_type),
            index,
            str(data),
            name
        ))
        return dp

    def datapoint(self, data, flags, name=None, sd=None):
        """Create and return a Datapoint object.

        datapoint(...) is the Datapoint factory method. While it
        is possible to create Datapoint objects without the use of this
        factory, *only* those created with the factory are linked with the
        application object and will be able to interact with the network.
        The input_datapoint() and output_datapoint() factories can be used
        as a shorthand whenever 'flags' contains nothing standard flags and
        the direction indicator.

        Parameters:

        data:       an implementation of the datapoint type
        flags:      a combination of flags defined in interface.Datapoint
        name:       the external datapoint name (stack.MAX_EXT_DP_NAME)
        sd:         self-documentation string (comment portion)

        Example:

        from pylon.resources.SNVT_count import SNVT_count

        my_value_input = my_app.input_datapoint(
           data=SNVT_count(),
           name='nviValue'
        )

        Note the distinction between local and external names: a local name is
        the name you give to a variable, such as my_value_input in this
        example. This is the name of the Python variable, and the name you use
        in your script. The datapoint factory, however, also accepts a 'name'
        argument. This refers to datapoint's the external name, the name
        exposed to the network and the network tool through the device's
        self-identification data.
        The external name is optional but recommended.

        When external names are used, they should meet the established naming
        conventions and use an nvi prefix for input datapoints, nvo for
        outputs, and nci (or cp) for datapoints implementing properties.
        The internal names, on the other hand, should meet Python coding
        standards and guidelines.

        External names help managing the device without printed documentation.
        However, these names consume storage space and, because they must be
        discovered by the network tool, may prolong discovery and some
        management processes. While the affected task are typically executed
        infrequently, the extra time required can add up when using large
        numbers of devices on low-bandwidth media.
        """
        return self.__datapoint(
            object_type=interface.Datapoint,
            data=data,
            flags=flags,
            name=name,
            sd=sd
        )

    def input_datapoint(self, data, name=None, sd=None):
        """Create and return a typical input datapoint object.

        input_datapoint is a sub-factory of the datapoint() factory method,
        producing typical input datapoints only. Use the datapoint factory
        for control over advanced flags, maximum or mean rate estimates.

        Parameters:

        data:       an implementation of the datapoint type
        name:       the external datapoint name (stack.MAX_EXT_DP_NAME)
        sd:         self-documentation string (comment portion)
        """
        return self.datapoint(
            data,
            interface.Datapoint.STANDARD | interface.Datapoint.INPUT,
            name,
            sd
        )

    def output_datapoint(self, data, name=None, sd=None):
        """Create and return a typical output datapoint object.

        output_datapoint is a sub-factory of the datapoint() factory method,
        producing typical output datapoints only. Use the datapoint() factory
        for control over advanced flags, maximum or mean rate estimates.

        Parameters:

        data:       an implementation of the datapoint type
        name:       the external datapoint name (stack.MAX_EXT_DP_NAME)
        sd:         self-documentation string (comment portion)
        """
        return self.datapoint(
            data,
            interface.Datapoint.STANDARD | interface.Datapoint.OUTPUT,
            name,
            sd
        )

    def __init(self):
        """Prepare the runtime kit for re-starting."""
        self.__state = Application.State.IDLE

        # The Application object maintains a list of all registered datapoint
        # objects, in index order, and maintains two separate index numbers
        # for the next priority or non-priority datapoint to be processed.
        # Output datapoints are processed by propagation, input datapoints are
        # processed by polling.
        # Note that datapoints include pure Datapoint objects and
        # PropertyDatapoint objects.
        self.__datapoints = []

        # Properties applying to the application as a whole are referenced
        # through this list.
        self.__properties = []

        # The list of implemented blocks and a reference to the node object
        self.__blocks = []
        self.__node_object = None
        self.__node_object_profile = SFPTnodeObject

        # When implementing a block, the factory method may need to create
        # external names for implementations of profile members. It does so
        # whenever the block itself has been given an external name (by the
        # factory caller). When a member name is created, the factory can only
        # derive this from the member name, but must make sure the name is
        # unique, and not exceeding 16 characters. The same applies to external
        # block names: while these aren't strictly required to be unique,
        # duplicate names tend to confuse.
        # The private __ext_name_mangle() tool handles this, based on the
        # __??_names dictionaries.
        self.__dp_names = {}
        self.__fb_names = {}

        # datapoint housekeeper state variables:
        self.__next_dp = 0

        self.__todo = collections.deque()
        self.__todo_lock = threading.Lock()

        #
        #    Stack interface data defaults
        #
        self.__is_program_id_set = False
        self.__is_unique_id_set = False

        self.__dynamic_dps = 0
        # Track numbers of input and output datapoints through separate
        # counters, as these are used to determine the size of address and
        # alias tables. Properties implemented as datapoints weigh less in the
        # address and alias allocation (because they are not typically
        # connected to other items), so they are counted separately.
        self.__no_dpo = 0   # output data points
        self.__no_dpi = 0   # input data points
        self.__no_dpp = 0   # (input) data points implementing properties

        # Automatic allocation of address and alias table records can be
        # overwritten by the script through an explicit assignment to the
        # aliases and addresses properties. This is monitored with the auto_*
        # attributes:
        self.__auto_aliases = True
        self.__auto_addresses = True

        self.__domains = 2
        self.__addresses = 15
        self.__aliases = 0
        self.__bindable_mt = 0
        self.__sd_string = ''
        self.__avg_dyn_dp_sd_size = 18

    def __init__(self,
                 library='libpylon-stack.so',
                 use_isi=True,
                 log_file='pylon-rtk.log',
                 log_level=logging.WARNING):
        """Create the Application object.

        The application class implements the Application class. Each Pilon
        script contains exactly one application class at any given time.

        Parameters:

        library:    the shared library containing the stack
        use_isi:    whether to link with the ISI engine. Note that the decision
                    to start the engine is in the start() method.
        log_file:   the name of the pilon run-time log file
        log_level:  log level, e.g. logging.WARNING
        """

        # Check some essentials first
        if toolkit.language_version(3, 3):
            self.__get_ident = threading.get_ident
        else:
            self.__get_ident = _thread.get_ident

        self.__threadid = self.__get_ident()

        if Application.__instances:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.SINGLETON,
                'Application is a singleton.'
            )

        self.__log_level = log_level
        logger.setLevel(log_level)
        fileHandler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=100000,
            backupCount=3
        )
        fileHandler.setLevel(log_level)
        formatter = logging.Formatter(
            '%(asctime)-15s %(name)-20s %(levelname)-8s  %(message)s'
        )
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.info('\n\t######### application object initializing\n')
        logging.captureWarnings(True)

        random.seed()

        self.__service_signal = threading.Event()
        self.__service_timeout = 0.005
        self.__housekeeping_timeout = 0.005

        self.__init()

        self.communication_parameters = pylon.device.stack.CommParameters()
        # TODO REMINDER consider supporting non-default xcvr
        self.communication_parameters.TransceiverType = 0

        self.buffers = pylon.device.stack.Buffers()
        self.buffers.ApplicationBuffers.PriorityMsgOutCount = 1
        self.buffers.ApplicationBuffers.NonPriorityMsgOutCount = 3
        self.buffers.ApplicationBuffers.MsgInCount = 3

        self.buffers.LinkLayerBuffers.LinkLayerBufferCount = 5

        self.buffers.TransceiverBuffers.NetworkBufferInputSize = 114
        self.buffers.TransceiverBuffers.NetworkBufferOutputSize = 114
        self.buffers.TransceiverBuffers.PriorityNetworkOutCount = 2
        self.buffers.TransceiverBuffers.NonPriorityNetworkOutCount = 2
        self.buffers.TransceiverBuffers.NetworkInCount = 5

        # TODO REMINDER review the following defaults

        self.__receive_transactions = 16
        self.__transmit_transactions = 4
        self.__transmit_ttl = 24576

        self.__device_uri = 'uc://0.0.0.0:1628'
        self.__persistence_path = '.pylon-nvd'

        self.OnReset = event.SimpleEvent(
            limit=None,
            doc="""
            Signal a logical reset.

            OnReset() fires when the stack processed a reset command.

            Note that this does not necessarily require that the entire Pilon
            device resets physically. Most Pilon devices will reset themselves
            logically with OnReset."""
        )

        self.OnWink = event.SimpleEvent(
            limit=None,
            doc="""
            Signal receipt of a simple wink command.

            OnWink() fires when the device receives a simple wink command.
            Wink commands are typically used to help identifying individual
            physical devices in a network of many. Interoperable devices are
            required to respond to a wink command with a benign, human-
            recognizable visual or audible response. Many devices will flash a
            dedicated LED for a certain duration in response to a Wink request.

            Arguments:

            sender:     the application class
            arguments:  an Application.OnWinkEventArgs object"""
        )

        self.OnOffline = event.SimpleEvent(
            limit=None,
            doc="""
            Signal a mode change to Offline.

            OnOffline() fires when the device changes its state to offline.
            The interpretation of this state is application-specific, but it is
            generally assumed that an application in this state refrains from
            potentially dangerous and automated action.

            For example, a script might freeze its current physical output
            lines in their current state, or drive physical outputs into a
            safe position when entering the offline state. While in this state,
            scripts will often ignore input datapoint updates.

            The OnOnline event indicates the reversal of this state.

            Arguments:

            sender:     the application class
            arguments:  an Application.OnOfflineEventArgs object"""
        )

        self.OnOnline = event.SimpleEvent(
            limit=None,
            doc="""
            Signal a mode change to Online.

            OnOnline() fires when the device changes its state to online,
            or when the device received a logical reset (which implies a
            change to the online state).

            Some scripts may need to request an update to certain input
            datapoints (using the poll() method) at this time, but since this
            can result in severe peak network traffic, it is generally
            preferred to resume operation based on the last known values,
            relying on remote data sources to update these values in time.

            Arguments:

            sender:     the application class
            arguments:  an Application.OnOfflineEventArgs object"""
        )

        self.OnServiceLed = event.SimpleEvent(
            limit=None,
            doc="""
            Signal a change of the service LED status.

            OnServiceLed() fires when the service LED status changes.
            The 'service LED' is a visual indicator for the network state of
            the device. Interoperable devices are required to support at least
            the following two states:

            unconfigured:   service LED flashes at 0.5 Hz
            configured:     service LED is off

            Service LED on indicates the 'applicationless' state. For a Pilon
            device, this state can only occur when the script is not running;
            therefore, the script cannot control this service LED behavior.

            However, devices supporting a physical LED should take advantage of
            suitable hardware to accomplish this effect.

            The service LED may be implemented using a physical LED, but
            logical service LED implementations, such as a suitable indicator
            on a graphical user interface, are permitted.

            Many scripts indicate additional state information through the
            service LED, using multi-color LED or advanced flashing patterns.

            Arguments:

            sender:     the application class
            arguments:  an Application.OnServiceLedEventArgs object"""
        )

        Application.__instances += 1
        self._stack = pylon.device.stack.Stack(library)
        self.__state = Application.State.INIT

        if use_isi:
            # Support ISI in principle. Whether ISI will be started is decided
            # later, based on the value of the SCPTnwrkConfig property.
            self.__isi = pylon.device.isi.ISI(self._stack, self)
            self.__scpt_nwrk_cnfg = None
        else:
            self.__isi = None

        self.__stack_tracefile = None

    def __signature(self, ctd, ifd):
        """Return a 32-bit signature for this item.

        The signature reflects all attributes relevant to the interoperable
        interface. Note the signature is not a hash, and note that the Python
        hash() function cannot generally be used to compute a signature or
        parts of it due to its random seed.
        The signature must remain the same every time the application executes
        on a given physical device (hardware), unless an aspect affecting the
        interoperable interface changes. The signature's numeric value is
        irrelevant, but starting the script twice must yield the same signature
        value if no relevant change occurred, and must yield a different value
        if such a change occurred.

        However, an automatically calculated 32-bit signature value cannot
        reflect all possible relevant changes to the interoperable interface.
        It is assumed that this implementation yields a different signature
        with 'reasonable likelihood' when aspects of the interoperable
        interface change.

        You may also assign an explicit signature value to the start() method,
        and take responsibility for its management."""
        signature = ctd._signature() ^ ifd._signature()

        for dp in self.__datapoints:
            signature ^= dp.index
            signature ^= dp._signature() << (dp.index % 4)

        for block in self.__blocks:
            signature ^= block._signature()

        if self.__isi:
            signature ^= self.__isi._signature()

        return signature & 0x0FFFFFFFF

    def start(self, signature=None):
        """Create, configure and start the stack.

        The method expects an unique unsigned integer signature, which
        uniquely identifies this application - applications with a different
        set of datapoints, properties, etc, expose a
        different interface to the network and must use a different signature
        value, but the application should re-use the previous signature value
        so long as the interoperable network interface remains unchanged.
        The stack implies no interpretation on the value of the signature.

        Parameters:

        signature:      unique numeric identifier for this application (opt.)

        The Application computes a signature value automatically, unless an
        explicit value is provided. Most scripts should use the automatically
        computed signature value. See __signature() for more information."""
        self._validate_prestart_context()

        if self.__isi and not self.__node_object:
            #
            #   This configuration requires a SCPTnwrkCnfg device property.
            #   Make it so:
            #
            for p in self.__properties:
                if isinstance(p, SCPTnwrkCnfg):
                    self.__scpt_nwrk_cnfg = p
                    break
            if not self.__scpt_nwrk_cnfg:
                self.__scpt_nwrk_cnfg = self.implement(
                    name='nciNetConfig',
                    property_type=SCPTnwrkCnfg,
                    flags=base.PropertyFlags.RESET,
                    expose_name=True
                )
                self.__scpt_nwrk_cnfg.data = config_source_t.CFG_LOCAL
                self.__scpt_nwrk_cnfg.get_data_item()._accept_as_default()
                logger.info(
                    'Implemented device property {0} (for ISI)'.format(
                        self.__scpt_nwrk_cnfg
                    )
                )

        if not self.__is_program_id_set:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.PID_MUST_BE_SPECIFIED,
                'A program ID must be specified with Application.programId'
            )

        #
        # Compile all self-documentation
        #
        self.__compile_sd()

        #
        # Gather stack configuration details:
        #
        ifd = pylon.device.stack.InterfaceData()
        ctd = pylon.device.stack.ControlData()

        ctd.Version = 0
        ctd.ServicePinInterval = 0
        ctd.NvdFlushGuardTimeout = 5
        ctd.CommParameters = self.communication_parameters
        ctd.Buffers = self.buffers
        ctd.ReceiveTransCount = self.__receive_transactions
        ctd.TransmitTransCount = self.__transmit_transactions
        ctd.TransmitTransIdLifetime = self.__transmit_ttl

        ifd.Version = 0
        ifd.ProgramId = self.__pid
        ifd.StaticNvCount = len(self.__datapoints)
        ifd.NvTblSize = len(self.__datapoints) + self.__dynamic_dps
        ifd.DomainTblSize = self.__domains
        ifd.AddrTblSize = self.__addresses
        ifd.AliasTblSize = self.__aliases
        ifd.BindableMsgTagCount = self.__bindable_mt
        ifd.NodeSdString = toolkit.ebcdic(self.__sd_string)
        ifd.AvgDynNvSdLength = self.__avg_dyn_dp_sd_size

        if not signature:
            # Compute a signature. Make sure this is pretty much the last step
            # before creating the stack, as all profiles, datapoints,
            # properties and their SD must be finalized for this.
            signature = self.__signature(ctd, ifd)

        logger.info('Application signature: 0x{0:X}'.format(signature))
        ifd.Signature = signature

        if self.__persistence_path:
            self._stack.set_persistence_path(self.__persistence_path)

        if self.__device_uri:
            self._stack.set_device_uri(self.__device_uri)

        if self.__is_unique_id_set:
            self._stack.register_unique_id(self.__unique_id)

        #
        #    Create the stack:
        #
        self._stack.create_stack(
            ifd,
            ctd
        )
        self.__state = Application.State.CREATED

        #
        #    Register event handlers
        #
        self._stack.register_dp_update(self.__onDpUpdateHandler)
        self._stack.register_dp_complete(self.__onDpCompleteHandler)
        self._stack.register_reset(self.__onResetHandler)
        self._stack.register_wink(self.__onWinkHandler)
        self._stack.register_offline(self.__onOfflineHandler)
        self._stack.register_online(self.__onOnlineHandler)
        self._stack.register_service_led(self.__onServiceLedStatusHandler)

        if pylon.device.stack.sync_evnt:
            self._stack.register_event_ready(self.__onEventReadyHandler)

        #
        # Register Network Variables, in index order
        #
        for dp in self.__datapoints:
            logger.info('Registering {0}'.format(dp))
            self._stack.register_datapoint(dp._dpd)

        self._stack.start_stack()

        self.__unique_id = self._stack.get_unique_id()

        if self.__isi and \
                self.__scpt_nwrk_cnfg and \
                self.__scpt_nwrk_cnfg.data == config_source_t.CFG_LOCAL:
            self.__isi.start()

        self.signal()
        self.__state = Application.State.OFFLINE

    def stop(self):
        """Stop and destroy the stack.

        stop() reverts start() by stopping and destroying the stack.
        stop() stops the stack, de-registers all events registered with the
        stack, removes all subscriptions to events fired by the application
        object, and removes its list of registered datapoints.

        The caller is responsible for disposing of the previously created
        interoperable objects such as datapoints, properties and blocks.
        You (the caller) are responsible for discarding any remaining
        references to any of these, as these objects will no longer be served
        by the application."""
        self._validate_thread()

        if self.__isi:
            self.__isi.stop()

        if self.__state >= Application.State.CREATED:
            self._stack.destroy_stack()

        logger.debug('Stack is destroyed and control is back with us.')

        # Always re-init, even when we stopped a not started stack.
        self.OnReset.reset()
        self.OnWink.reset()
        self.OnOffline.reset()
        self.OnOnline.reset()

        self.__init()
        self.__state = Application.State.INIT

    def enqueue(self, dp, always=False):
        """Enqueue a datapoint object for processing.

        Enqueue a datapoint object for processing: input datapoint objects will
        be polled, output datapoint objects will be propagated. With 'always'
        set to False (the default), each item is added to the queue only once.
        Set 'always' to True to enforce adding the datapoint 'dp' even if it is
        already enlisted.

        Arguments:

        dp      - the datapoint to enlist in the processing queue
        always  - a flag to enforce duplicate registration

        This API is generally used by the Datapoint object's with statement
        context management routines, and by similar API provided by the
        Datapoint class. """

        if self.__log_level <= logging.DEBUG:
            # this should not occur in release code, so skip the test for speed
            if not isinstance(dp, interface.Datapoint):
                raise TypeError('Expect Datapoint, got {0}'.format(type(dp)))
        with self.__todo_lock:
            if always or not (dp in self.__todo):
                if self.__log_level <= logging.DEBUG:
                    logger.debug('Enqueueing datapoint {0}'.format(dp))
                if dp.is_priority:
                    self.__todo.appendleft(dp)
                else:
                    self.__todo.append(dp)
                self.signal()

    def service(self, timeout=None):
        """Service the stack and other components of the runtime kit.

        The service routine performs these tasks:

        1. service() processes any incoming events by processing the
        stack's event pump. This yields events such as OnUpdate or OnComplete
        events.

        2. service() processes any pending datapoints. These are datapoints
        enqueued for processing earlier, either through explicit API such as
        Datapoint.poll() or .propagate(), or implicitly by updating the
        datapoint's data. Enqueued input datapoints are polled, output
        datapoints are updated and, unless they are flagged as polled outputs,
        propagated.

        3. service() services the ISI object if ISI is enabled and running.

        4. service() performs lower priority housekeeping tasks.

        You must call the service routine frequently and periodically, and
        it must be called from the same and single thread which owns the
        application class and engages its API.

        You should review the service_timeout and housekeeping_timeout
        properties to adjust the timing of this method.

        You can use the optional timeout argument to specify a service timeout
        value or to temporarily override the configured service timeout. Note
        that specifying a value through the timeout argument does not affect
        the service_timeout property."""
        self._validate_thread()
        try:
            #
            # Service the event pump
            #
            if not timeout:
                timeout = self.__service_timeout

            if self.__service_signal.wait(timeout):
                self.__service_signal.clear()
                self._stack.event_pump()
            elif not pylon.device.stack.sync_evnt:
                self._stack.event_pump()

            #
            # Process pending items
            #
            with self.__todo_lock:
                # Examine all items in the queue of pending items _once_.
                # When the queue contains a currently locked item, this is
                # re-added (at the end of the queue), while currently unlocked
                # items are being processed. Because items may be re-added to
                # the queue, this look must iterate only over the initial size
                # of the queue, not until it is empty.
                todo = len(self.__todo)
                while todo:
                    dp = self.__todo.popleft()
                    todo -= 1
                    if dp._lock(blocking=False):
                        # OK, we have a lock on the datapoint object. Let's
                        # process it.
                        if self.__log_level <= logging.DEBUG:
                            logger.debug(
                                'Dequeueing datapoint {0}'.format(
                                    dp
                                )
                            )
                        if not dp.is_disabled:
                            if dp.is_output:
                                # Propagate or update output
                                try:
                                    self._stack._set_dp_value(
                                        dp.index,
                                        dp.get_data_item()._pack()
                                    )
                                    if not dp.is_polled:
                                        self._stack.propagate_dp(dp.index)
                                        if self.__log_level <= logging.INFO:
                                            logger.info(
                                                'Propagated datapoint '
                                                '{0} ({1})'.format(
                                                    dp.index, dp.name
                                                )
                                            )
                                except Exception as e:
                                    logger.error(
                                        'Propagating datapoint '
                                        '{0} ({1}): {2}'.format(
                                            dp.index,
                                            dp.name,
                                            e
                                        )
                                    )
                            else:
                                # Poll input
                                try:
                                    self._stack.poll_dp(dp.index)
                                    if self.__log_level <= logging.INFO:
                                        logger.info(
                                            'Polling datapoint '
                                            '{0} ({1})'.format(
                                                dp.index,
                                                dp.name
                                            )
                                        )
                                except Exception as e:
                                    logger.error(
                                        'Polling datapoint '
                                        '{0} ({1}): {2}'.format(
                                            dp.index,
                                            dp.name,
                                            e
                                        )
                                    )
                        dp._unlock()
                    else:
                        # This datapoint is currently locked. This may be OK;
                        # for example, a script may have called propagate()
                        # within a with-block. We push the datapoint back to
                        # the end of the pending queue (regardless of its
                        # priority), and hope to deal with it the next time.
                        # Note that we are not re-triggering the service
                        # signal to allow the script time to unlock the item.
                        self.__todo.push(dp)

            if self.__state >= Application.State.CREATED:
                #
                #   service ISI
                #
                if self.__isi:
                    self.__isi.service()

                #
                #    Housekeeping:
                #
                total = len(self.__datapoints)
                timeout = toolkit.Timer(self, self.__housekeeping_timeout)
                visited = 0

                while visited < total and not timeout.is_expired:
                    dp = self.__datapoints[self.__next_dp]
                    # Refresh each datapoint's is_bound info. Many applications
                    # monitor this state. Obtaining this information from the
                    # pilon stack is a fairly low-cost operation, so we cache
                    # this detail here as part of the lower priority
                    # housekeeping service, thus avoiding thread
                    # synchronization issues which could arise in an on-demand
                    # is_bound query with the stack.

                    bound = bool(self._stack.is_dp_bound(dp.index))
                    if bound != bool(dp.is_bound):
                        if self.__log_level <= logging.INFO:
                            logger.info(
                                'Datapoint {0} ({1}) is {2}'.format(
                                    dp.index,
                                    dp.name,
                                    'bound' if bound else 'not bound'
                                )
                            )
                        dp._is_bound = bound
                    self.__next_dp = (self.__next_dp + 1) % total
                    visited += 1

        except Exception as e:
            logger.error(
                'Application.service() caught an exception: {0}'.format(
                    e
                )
            )

    def signal(self):
        """Raise the service signal.

        Signal() may be used to raise the service signal. Complex applications
        may raise the service timeout to a very large value (or disable the
        timeout). When such an application needs servicing the stack, it can
        raise the service signal with this API."""
        self.__service_signal.set()

    def send_service_message(self, drum=True):
        """Send a service message to the network.

        Arguments:

        drum : Boolean  whether to also send an ISI DRUM message (if ISI)

        sendServiceMessage() broadcasts the device's service message, also
        known as its 'service pin message,' which reports the device's program
        Id and unique Id values.
        This is often used for light network debugging, and is commonly used
        to register the device with a network management tool.
        Interoperable devices must provide a user-accessible method of sending
        the service pin message.

        When ISI is in use and running, the method also issues an ISI DRUM
        message unless suppressed with a False drum argument."""
        self._validate_thread()
        self._stack.send_service_message()
        if self.__isi and self.__isi.is_running() and drum:
            self.__isi.send_drum()

    #
    #    Attributes:
    #
    def __setv(self, v, minimum, maximum, label, max_state=State.INIT):
        """Private setter for numeric properties."""
        if self.__state > max_state:
            raise toolkit.PylonContextError(
                toolkit.PylonContextError.ALREADY_STARTED,
                'Stack is already started'
            )

        if minimum <= v <= maximum:
            return v
        else:
            raise ValueError(
                '{0} must be in the {1}..{2} range'.format(
                    label,
                    minimum,
                    maximum
                )
            )

    def __set_unique_id(self, v):
        self._validate_prestart_context()
        self.__unique_id = v
        self.__is_unique_id_set = True

    def __get_unique_id(self):
        if self.__state <= Application.State.INIT and \
                not self.__is_unique_id_set:
            raise AttributeError(
                'Automatically allocated unique ID values are only available '
                'once the stack is started'
            )
        return self.__unique_id

    def __set_pid(self, v):
        self._validate_prestart_context()
        words = v.split(':')
        if not isinstance(v, str) or \
                len(words) != pylon.device.stack.PROGRAM_ID_LENGTH:
            raise AttributeError(
                'Expected 8 ASCII encoded, colon-separated, hex bytes'
            )
        # PyCharm flags the following as "trying to call non-callable object",
        # but this is a false alarm. The following instruction correctly
        # constructs a stack.PROGRAM_ID_TYPE object.
        # noinspection PyCallingNonCallable
        self.__pid = pylon.device.stack.PROGRAM_ID_TYPE(
            int(words[0], 16), int(words[1], 16),
            int(words[2], 16), int(words[3], 16),
            int(words[4], 16), int(words[5], 16),
            int(words[6], 16), int(words[7], 16)
        )
        self.__is_program_id_set = True

    def __get_pid(self):
        result = ''
        for i in range(pylon.device.stack.PROGRAM_ID_LENGTH):
            result += '{0:02X}:'.format(self.__pid[i])
        return result.rstrip(':')

    def __set_domains(self, v):
        self._validate_prestart_context()
        self.__domains = self.__setv(
            v,
            1,
            pylon.device.stack.MAX_DOMAINS, 'domains'
        )

    def __set_addresses(self, v):
        self._validate_prestart_context()
        self.__addresses = self.__setv(
            v,
            0,
            pylon.device.stack.MAX_ADDRESSES, 'addresses'
        )
        self.__auto_addresses = False

    def __set_aliases(self, v):
        self._validate_prestart_context()
        self.__aliases = self.__setv(
            v,
            0,
            pylon.device.stack.MAX_ALIASES, 'aliases'
        )
        self.__auto_aliases = False

    def __set_bindable_mt(self, v):
        self._validate_prestart_context()
        self.__bindable_mt = self.__setv(
            v,
            0,
            min(15, self.__addresses - 1),
            'bindable message tags'
        )

    def __set_sd_string(self, v):
        self._validate_prestart_context()
        self.__sd_string = str(v)

    def __set_device_uri(self, v):
        self._validate_prestart_context()
        self.__device_uri = str(v)

    def __set_persistence_path(self, v):
        self._validate_prestart_context()
        self.__persistence_path = str(v)

    def __set_stack_tracefile(self, v):
        if not v:
            self.__stack_tracefile = None
        else:
            self.__stack_tracefile = str(v)
        self._stack.set_stack_tracefile(self.__stack_tracefile, 0)

    def __set_service_timeout(self, v):
        if not (isinstance(v, int) or isinstance(v, float)):
            raise TypeError("Expected 'int' or float'")
        if self.__log_level <= logging.INFO:
            logger.info(
                'Changing service timeout from {0} to {1}'.format(
                    self.__service_timeout,
                    v
                )
            )
        self.__service_timeout = v

    def __set_housekeeping_timeout(self, v):
        if not (isinstance(v, int) or isinstance(v, float)):
            raise TypeError("Expected 'int' or float'")
        if 0 < v <= 1:
            if self.__log_level <= logging.INFO:
                logger.info(
                    'Changing the housekeeping timeout from {0} to {1}'.format(
                        self.__housekeeping_timeout,
                        v
                    )
                )
            self.__housekeeping_timeout = v
        else:
            raise ValueError('Expected a value between 0 and 1')

    def __set_node_object_profile(self, profile):
        if not issubclass(profile, SFPTnodeObject):
            raise TypeError('{0} must derive from SFPTnodeObject'.format(
                profile
            ))
        if self.__node_object:
            raise AttributeError('A node object is already implemented')
        self.__node_object_profile = profile

    uniqueId = property(
        __get_unique_id,
        __set_unique_id,
        None, """Node unique identifier.

        The 48-bit ISO/IEC 14908-3 unique node identifier, formatted as an
        ASCII-encoded sequence of dot-separated hex bytes, for example
        'FE.AA.C5.01.02.03'.

        If you do not define a unique ID, the stack will chose one for you.
        This automatically selected unique ID will be tied to your script's
        persistence_path, see there for more.

        Once the start() method completed, you can read-back the current
        unique ID from this property."""
    )

    programId = property(
        __get_pid,
        __set_pid,
        None, """Program identifier.

        Specifies the 64-bit program identifier in an ASCII-encoded sequence
        of colon-separated hex bytes, e.g. '9F:FF:FF:00:00:00:00:01'. This
        identifier uniquely identifies one particular program, or application,
        which may be loaded onto multiple different physical devices.

        You must specify a program identifier before calling start().

        The programId has a general form of 'FM:MM:MM:CC:CC:UU:TT:NN', where

        F   is 9 for prototypes, or 8 for certified devices,
        M   is the 20-bit manufacturer identifier,
        C   identifies the program's category and device class,
        U   details teh program's usage,
        T   describes the physical media used (channel type), and
        N   contains an 8-bit model number.

        For more details about the program ID fields refer to
        http://www.lonmark.org/technical_resources/resource_files/spid_master_list
    """)

    domains = property(
        lambda self: self.__domains,
        __set_domains,
        None, """The number of domain table entries."""
    )

    addresses = property(
        lambda self: self.__addresses,
        __set_addresses,
        None, """The number of address table entries.

        Address table allocation occurs automatically as datapoint objects are
        created, using an estimation of the required number of address table
        records as a function of the number of applicable resources.

        You can override this process at any time before calling the start()
        method. Note that you should always allocate at least 15 address table
        entries."""
    )

    aliases = property(
        lambda self: self.__aliases,
        __set_aliases,
        None, """The number of alias table entries.

        Alias allocation occurs automatically as datapoint objects are
        created, using an estimation of the required number of aliases as a
        function of the number of applicable resources.

        You can override this process at any time before calling the start()
        method."""
    )

    datapoints = property(
        lambda self: tuple(self.__datapoints),
        None,
        None, """All currently defined datapoints.

        Provides a tuple of implemented (static) datapoints.
        Dynamic datapoints are not supported with this release.

        Note this tuple includes regular Datapoint items as well as those
        implementing a property. Properties implemented as a datapoint are
        instances of the interface.PropertyDatapoint class. You can use the
        isinstance() built-in function to identify those, if necessary."""
    )

    properties = property(
        lambda self: tuple(self.__properties),
        None,
        None, """A tuple of properties applying to the device."""
    )

    blocks = property(
        lambda self: tuple(self.__blocks),
        None,
        None, """A tuple of blocks registered with the device."""
    )

    node_object = property(
        lambda self: self.__node_object,
        None,
        None, """The current node object block, or None if none."""
    )

    node_object_profile = property(
        lambda self: self.__node_object_profile,
        __set_node_object_profile,
        None, """The node object profile.

        Defines the profile to be used for implementing the node object.
        This property can only be set before a node object is implemented.
        The property defaults to SFPTnodeObject."""
    )

    bindable_mt = property(
        lambda self: self.__bindableMt,
        __set_bindable_mt,
        None, """The number of message tags.

        This number counts so-called 'bindable' message tags only, that is,
        message tags which may be used in message tag connections for implicit
        addressing."""
    )

    sd_string = property(
        lambda self: self.__sd_string,
        __set_sd_string,
        None, """The node's self-documentation string.

        Note this property reports and affects the comment portion of the
        self-documentation string, only."""
    )

    device_uri = property(
        lambda self: self.__device_uri,
        __set_device_uri,
        None, """The network interface's URI.

        The device URI is a string which describes how the stack connects to
        the network. The general form of the pilon device URI is

        uc://ipv4-addr:port

        for use with a unicast channel, where

        ipv4-addr   is a valid IPv4 address,
        port        is a valid and free port number,

        For example, "uc://10.0.1.23:1628" is a valid device URI for unicast
        mode.

        For use with multicast mode, you must specify the local IP address to
        listen to, and the broadcast address, using this general form:

        mc://<listen-address>,<broadcast-address>:<port>

        For example, "mc://10.0.1.23,10.0.255.254:1628" is a valid device URI
        for multicast mode.
        """
    )

    persistence_path = property(
        lambda self: self.__persistence_path,
        __set_persistence_path,
        None, """The folder for storing persistent data.

        Specifies the folder where application-specific persistent data is
        kept. Note this folder must be unique for each logical device, as
        it also contains and manages the unique Id. The same folder can be
        used with different applications, so long as these do not co-exist."""
    )

    stack_tracefile = property(
        lambda self: self.__stack_tracefile,
        __set_stack_tracefile,
        None, """Stack tracefile name, or None for no trace logging.

        Specifies the filename for stack trace messages. These are fairly
        low-level trace messages not normally required or particularly
        helpful, but such tracing might be useful when troubleshooting.
        This property accepts a string (containing a file path or name), or
        'None' to disable stack trace logging. The default value is None."""
    )

    state = property(
        lambda self: self.__state,
        None,
        None, """The state of the Pylon application object."""
    )

    service_timeout = property(
        lambda self: self.__service_timeout,
        __set_service_timeout,
        None, """Service timeout, in seconds or fractions of seconds.

        Defines the timeout, in seconds, which the application object's
        service() method allows when waiting for an event from the stack.
        Setting this to zero disables the timeout and results in an indefinite
        wait.
        The property supports fractions of seconds, e.g. 0.010 for 10ms.

        Scripts supporting the interoperable self-installation protocol, ISI,
        must support a service timeout of less than 250ms (0.25), even if the
        script implements a dedicated pilon worker thread.
        When ISI is in use, pilon must stop waiting for events signalled by
        the stack in order to service the ISI engine at least once every 250ms.
    """)

    housekeeping_timeout = property(
        lambda self: self.__housekeeping_timeout,
        __set_housekeeping_timeout,
        None, """The application's housekeeping timeout in seconds.

        The housekeeping timeout determines the maximum duration spent per
        service() call for housekeeping tasks, such as refreshing the
        datapoints' is_bound property.

        The property defaults to 0.005s, and can be set to a value greater than
        0, but not exceeding 1s."""
    )

    #
    # Callbacks:
    # The application registers the following functions as event handlers
    # with the protocol stack
    #
    def __onEventReadyHandler(self):
        """Service the stack's event pump.

        The __onEventReadyHandler handles 'event ready' notifications.
        Note this is a synchronous stack event, which executes in one
        of the stack's threads."""
        self.__service_signal.set()

    def __onResetHandler(self):
        logger.info('OnReset')
        self.OnReset.fire(
            sender=self,
            argument=Application.OnResetEventArgs()
        )
        # Reset implies the online state:
        if self.__state == Application.State.OFFLINE:
            self.__onOnlineHandler()

        if self.node_object:
            #  Reset returns all blocks to normal
            nviRequest = self.node_object.nviRequest
            nviRequest.data.object_id = 0
            nviRequest.data.object_request = object_request_t.RQ_NORMAL
            nviRequest._update(None)

    def __onWinkHandler(self):
        logger.info('OnWink')
        self.OnWink.fire(
            sender=self,
            argument=Application.OnWinkEventArgs()
        )

    def __onOfflineHandler(self):
        logger.info('OnOffline')
        self.__state = Application.State.OFFLINE
        self.OnOffline.fire(
            sender=self,
            argument=Application.OnOfflineEventArgs()
        )

    def __onOnlineHandler(self):
        logger.info('OnOnline')
        self.__state = Application.State.ONLINE
        self.OnOnline.fire(
            sender=self,
            argument=Application.OnOnlineEventArgs()
        )

    def __onServiceLedStatusHandler(self, state):
        logger.info(
            'OnServiceLedStatus(state={0})'.format(
                state
            )
        )
        self.OnServiceLed.fire(
            sender=self,
            argument=Application.OnServiceLedEventArgs(state)
        )

    def __onDpUpdateHandler(self, index, source):
        if self.__log_level <= logging.DEBUG:
            logger.debug(
                '__onDpUpdateHandler({0}, ...)'.format(
                    index
                )
            )

        dp = self.__datapoints[index]
        if dp._lock(timeout=0.05):
            disabled = True
            try:
                if not dp.is_disabled:
                    disabled = False
                    dpi = dp.get_data_item()
                    # update the datapoint with the latest value from the stack
                    remaining = dpi._unpack(
                        self._stack._get_dp_value(
                            index,
                            len(dpi)
                        )
                    )
                    if self.__log_level <= logging.WARN:
                        if len(remaining):
                            logger.warn(
                                'Datapoint {0} has {1} bytes of surplus '
                                'data'.format(
                                    index,
                                    len(remaining)
                                )
                            )
            except Exception as e:
                logger.error(
                    "Can't update datapoint {0} ({1}): {2}".format(
                        dp.index,
                        dp.name,
                        e
                    )
                )
            finally:
                # unlock now, so that the script may lock the datapoint again
                # within an onUpdate handler, for example.
                dp._unlock()

            if not disabled:
                # Now notify the datapoint about the update (which in turn will
                # fire OnUpdate events, if any). Make sure the datapoint is not
                # locked now.
                dp._update(source)

    def __onDpCompleteHandler(self, index, success):
        if self.__log_level <= logging.DEBUG:
            logger.debug(
                '__onDpCompleteHandler({0}, {1})'.format(
                    index,
                    success
                )
            )
        self.__datapoints[index]._complete(success)

    def __ext_name_mangle(self, names, intended):
        """Produce a unique external name for an interface item.

        Return a unique name up to 16 characters long, equal to or derived
        from the name argument. The method can be called with a None name, in
        which case it returns None."""
        if intended:
            name = ''
            for c in intended:
                if c.isalnum() or c in "_":
                    name += c
            if name[0].isdigit():
                name = '_' + name

            name = name[:16]    # no more than 16 characters!

            if name in names:
                # Use the name as far as possible, and make it unique by adding
                # a counter. Clip the name as much as necessary, but no more.
                number = names[name]
                width = 1+int(math.log10(number))

                newname = name[:16-width] + str(number)
                names[name] = 1 + number
                name = newname
            else:
                names[name] = 1

            if name != intended:
                logger.info(
                    'Mangled external name {0} to {1}'.format(
                        intended,
                        name
                    )
                )

            return name
        else:
            return intended

    def _implement_block_datapoint(self, member, block, snvt_xxx=None):
        """Implement a member of a block as a datapoint.

        This utility is used by the block factory (for mandatory members), and
        by the block's implement() method (for optional members).

        Return the new datapoint object."""
        datatype = member.datatype

        if issubclass(datatype, SNVT_xxx):
            if not snvt_xxx:
                raise TypeError(
                    "No SNVT_xxx resolver for {0}".format(
                        member.name
                    )
                )
            else:
                datatype = snvt_xxx

        flags = interface.Datapoint.STANDARD
        if member.is_output:
            flags |= interface.Datapoint.OUTPUT
        if member.is_polled:
            flags |= interface.Datapoint.POLLED
        if member.service_type == \
                base.Profile.DatapointMember.ACKNOWLEDGED:
            flags |= interface.Datapoint.ACKD
        elif member.service_type == \
                base.Profile.DatapointMember.REPEATED:
            flags |= interface.Datapoint.UNACKD_RPT
        elif member.service_type == \
                base.Profile.DatapointMember.UNREPEATED:
            flags |= interface.Datapoint.UNACKD

        # Create the datapoint. Note that the SD string is compiled
        # later, since the block index may need to change.
        dp = self.__datapoint(
            object_type=interface.Datapoint,
            data=datatype(),
            flags=flags,
            name=self.__ext_name_mangle(
                self.__dp_names,
                member.name
            )
        )

        dpi = dp.get_data_item()
        self._apply_bytes(
            dpi,
            member._minimum,
            member._maximum,
            member._invalid,
            None
        )

        # register datapoint, member block with each other:
        member._set_implementer(dp)
        dp._implements(block, member)
        block._implement_dp(member.name, dp)

        #
        # Implement each mandatory property applying to this datapoint
        #
        for property_name in sorted(member.properties):
            property_member = member.properties[property_name]
            if property_member.is_mandatory:
                self._implement_block_property(
                    member=property_member,
                    block=block,
                    applies_to=dp,
                    donor=dp
                )

        return dp

    def _implement_block_property(self, member, block, applies_to, donor):
        """Implement a property defined in a profile.

        The property can apply to one of the block's datapoints, or the block
        as a whole. The method returns nothing.

        Arguments:

        member      The profile member to be implemented
        block       The related block
        applies_to  The item to which the property applies
        donor       Resolves type-inheriting properties, can be None
        """
        declared_type = member.datatype()

        if isinstance(declared_type, base.Inheriting):
            #
            # A type-inheriting property "inherits" its data type from the item
            # it applies to. For properties applying to blocks, the type-
            # inheriting property derives its type from the block's principal
            # datapoint member (which always is a mandatory member).
            #
            if not donor:
                raise TypeError("Type donor can't be None")
            if not isinstance(donor, interface.Datapoint):
                raise TypeError("Type donor must derive from Datapoint")

            datatype_object = donor.get_data_type()()
            datatype_object._property_scope = declared_type._property_scope
            datatype_object._property_key = declared_type._property_key
        else:
            datatype_object = declared_type

        flags = interface.Datapoint.STANDARD | interface.Datapoint.CONFIG_CLASS

        # Create the datapoint. Note that the SD string is compiled
        # later, since the block index may need to change.
        dp = self.__datapoint(
            object_type=interface.PropertyDatapoint,
            data=datatype_object,
            flags=flags,
            name=self.__ext_name_mangle(
                self.__dp_names,
                member.name
            )
        )

        dpi = dp.get_data_item()
        self._apply_bytes(
            dpi,
            member._minimum,
            member._maximum,
            member._invalid,
            member._default
        )

        dp._flags = member._flags | base.PropertyFlags.NONE

        # register datapoint, member block with each other:
        member._set_implementer(dp)
        dp._implements(block, member)
        applies_to._implement_property(member.name, dp)
        return dp

    def implement(self, name, property_type,
                  flags=base.PropertyFlags.NONE,
                  expose_name=True):
        """Implement and apply a property to the application.

        Use implement() to implement and apply a property to the application as
        a whole.

        Arguments:

        name        The new property will be added as an instance variable to
                    the application object under this name. The name must be
                    unique within the application object.

        property_type   The type of the new property.

        flags       Property behavior flags, as a combination of constants
                    defined in base.PropertyFlags

        expose_name Whether the name should be used as the basis for an
                    external name. External names are visible to network tools
                    and integrators, and are generally recommended.

        The method returns the new property object.

        Example:

        my_new_property = my_app.implement('nciNwrkCnfg', SCPTnwrkCnfg)

        Device properties can not implement type-inheriting property types.
        Each property type can only be applied once.
        """
        self._validate_prestart_context()

        if name in self.__dict__:
            raise NameError('Instance member {0} already exists'.format(name))
        for p in self.__properties:
            if isinstance(p.get_data_item(), property_type):
                raise toolkit.PylonInterfaceError(
                    toolkit.PylonInterfaceError.DUPLICATE_PROPERTY_TYPE,
                    'Each property type must be unique within its application '
                    'set. {0} is already implemented by {1}'.format(
                        str(property_type),
                        str(p)
                    )
                )
        declared_type = property_type()
        if isinstance(declared_type, base.Inheriting):
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.TYPE_INHERITING_NOT_ALLOWED,
                'A type-inheriting property cannot be applied to the device'
            )

        dp_flags = interface.Datapoint.STANDARD | \
            interface.Datapoint.CONFIG_CLASS

        if expose_name:
            ext_name = name
        else:
            ext_name = None

        dp = self.__datapoint(
            object_type=interface.PropertyDatapoint,
            data=declared_type,
            flags=dp_flags,
            name=ext_name
        )

        dp._flags = flags | base.PropertyFlags.NONE

        # register:
        self.__properties.append(dp)
        self.__dict__[name] = dp
        return dp

    def block(self, profile, ext_name=None, snvt_xxx=None):
        """Create and return a block.

        Use this method to create a block, an instance of a profile.
        For inheriting profiles, the block honors this profile and the
        inherited profile. The block automatically implements all mandatory
        datapoint members of this profile (and the inherited profile, if any),
        all mandatory properties applying to the block, and all mandatory
        properties applying to any of the mandatory datapoint members.

        Arguments:

        profile     An instance of the profile to implement.
        ext_name    The block's optional external name, or None.
        snvt_xxx    For profiles which include SNVT_xxx members.

        Example:

        openLoopSensor = app.block(
            profile=SFPTopenLoopSensor(),
            ext_name='ols',
            snvt_xxx=SNVT_temp
        )

        The external name, if given and not None, also allows exposure of the
        implemented members' external names. If no external name is give (or
        set to None), the block's external name is not exposed, and neither
        are the members' external names.

        The snvt_xxx argument is optional in the general case, but required if
        the profile specifies any member through the placeholder type SNVT_xxx.
        This block factory supports only one SNVT_xxx replacement type (as
        provided with this factory argument), which is applied to all SNVT_xxx
        references within the profile (and the inherited profile, if any).
        """
        self._validate_prestart_context()

        if not isinstance(profile, base.Profile):
            raise TypeError(
                '{0} is no instance of Profile'.format(
                    profile
                )
            )

        if isinstance(profile, self.__node_object_profile) and \
                self.__node_object:
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.ALREADY_IMPLEMENTED,
                'A node object is already implemented'
            )

        block = interface.Block(
            application=self,
            index=len(self.__blocks),
            profile=profile,
            ext_name=self.__ext_name_mangle(
                self.__fb_names,
                ext_name
            ),
            snvt_xxx=snvt_xxx
        )

        #
        # The profile might be an inheriting profile. The Block's constructor
        # resolves this, but we'd better be careful to use the block's view of
        # the profile from now on: block.profile.
        #

        #
        # Implement mandatory members *in alphabetical order* of the member
        # names. This is important, because the order of item retrieval from
        # a Python dictionary is not deterministic (which, in turn, is caused
        # by the fact that the built-in hash function uses a random seed for
        # strings). However, it is important that the implementation order of
        # block members is deterministic, because a change in the order affects
        # the external interface and storage of persistent data.
        #
        for name in sorted(block.profile.datapoints):
            member = block.profile.datapoints[name]
            if member.is_mandatory:
                self._implement_block_datapoint(
                    member=member,
                    block=block,
                    snvt_xxx=snvt_xxx
                )

        #
        # Now implement all mandatory properties applying to the block,
        # again, in alphabetical order:
        #
        for property_name in sorted(block.profile.properties):
            property_member = block.profile.properties[property_name]
            if property_member.is_mandatory:
                self._implement_block_property(
                    member=property_member,
                    block=block,
                    applies_to=block,
                    donor=block.principal
                )

        if isinstance(block.profile, self.__node_object_profile):
            #
            # We just made a new node object.
            # Make sure the node object has block index 0,
            # make sure it implements the optional nciNetConfig property
            # with a default value of CFG_LOCAL. (In case this application run
            # before, with the same signature, the most recent value will be
            # recovered and may be different from CFG_LOCAL.
            #
            self.__node_object = block
            self.__blocks.insert(0, block)
            # update each block's index:
            for i in range(len(self.__blocks)):
                self.__blocks[i]._set_index(i)

            # If ISI is supported, we need nciNetConfig:
            if self.__isi and not self.__scpt_nwrk_cnfg:
                self.__scpt_nwrk_cnfg = block.implement('nciNetConfig')
                self.__scpt_nwrk_cnfg.data = config_source_t.CFG_LOCAL
                self.__scpt_nwrk_cnfg.get_data_item()._accept_as_default()

                logger.info(
                    'Implemented node object property {0} (for ISI)'.format(
                        self.__scpt_nwrk_cnfg
                    )
                )

            # Register the default node object event handler:
            block.nviRequest.OnUpdate += self.on_nviRequest_update
            # Clear the current status:
            block.nvoStatus.data._flags = 0

        else:
            # regular blocks append to the end:
            self.__blocks.append(block)

            if len(self.__blocks) > 1 and not self.__node_object:
                # node object is now required. Make one:
                self.block(self.__node_object_profile(), 'node')

        return block

    def __compile_sd(self):
        """Compute self-documentation data.

        Computes all self-documentation strings for the device, and all its
        blocks, properties and datapoints.

        See http://www.lonmark.org/technical_resources/guidelines/ for more.
        """

        #
        # node SD:
        #
        if self.__blocks:
            node_sd = '&3.4@'
        else:
            node_sd = ''

        if self.__blocks:
            for block in self.__blocks:
                node_sd += block.get_self_documentation() + ','
            node_sd = node_sd.rstrip(',')

        if self.__sd_string:
            node_sd += ';' + self.__sd_string
        self.__sd_string = node_sd

        if len(node_sd) > 1024:
            raise toolkit.PylonInterfaceError(
                toolkit.PylonInterfaceError.NODE_SD_TOO_BIG,
                "The node's self-documentation string exceeds 1024 characters"
            )

        #
        # datapoint SD:
        #
        if self.__datapoints:
            for datapoint in self.__datapoints:
                datapoint._compile_self_documentation()

    # noinspection PyUnusedLocal
    def on_nviRequest_update(self, sender, arguments):
        """Default Node Object nviRequest processor.

        The default processor for update events to the node object's nviRequest
        input. This default implementation provides basic functionality for the
        node object. It supports the mandatory RQ_NORMAL, RQ_UPDATE_STATUS and
        RQ_REPORT_MASK requests. In addition, it also support the optional
        RQ_DISABLED and RQ_ENABLE requests.

        The block factory automatically registers this handler with this
        datapoint. To supply your own handler, reset the event source and
        attach your own handler:

        my_app.node_object.nviRequest.OnUpdate.reset()
        my_app.node_object.nviRequest.OnUpdate += my_node_request_handler

        Your "my_node_request_handler" can still benefit from the built-in
        default. To do so, simply call my_app.on_nviRequest_update() with the
        same arguments supplied to your handler.
        """
        index = sender.data.object_id
        request = sender.data.object_request

        nvoStatus = self.node_object.nvoStatus
        nvoStatus.data.object_id = index
        nvoStatus.data._flags = 0

        def update_status(block_list):
            """
            Internal utility to update the status with the combined status
            report of all parties involved.
            """
            status = nvoStatus.get_data_item()
            for index in block_list:
                status |= self.__blocks[index].status
            # Never include invalid_id or invalid_request flags though:
            status.invalid_id = False
            status.invalid_request = False

        logger.debug(
            'Node object call for index {0}, request {1}'.format(
                index, request
            )
        )

        if index:
            # Single block affected:
            if index >= len(self.__blocks):
                nvoStatus.data.invalid_id = True
                return
            block_list = range(index, index+1)
        else:
            # All blocks except the node object are affected:
            block_list = range(1, len(self.__blocks))

        if request == object_request_t.RQ_NORMAL:
            # Return to normal, exit 'disabled' or 'overridden' states:
            for index in block_list:
                block = self.__blocks[index]
                block.disabled = False
                block.status._flags = 0
            nvoStatus.data._flags = 0
        elif request == object_request_t.RQ_UPDATE_STATUS:
            # Report status (OR'ed from all affected blocks)
            update_status(block_list)
        elif request == object_request_t.RQ_REPORT_MASK:
            # Report capability:
            # invalid_id, invalid_request, report_mask, disable
            nvoStatus.data._flags = 0xE0001000
        elif request == object_request_t.RQ_DISABLED:
            for index in block_list:
                self.__blocks[index].is_disabled = True
            update_status(block_list)
        elif request == object_request_t.RQ_ENABLE:
            for index in block_list:
                self.__blocks[index].is_disabled = False
            update_status(block_list)
        else:
            nvoStatus.data.invalid_request = True

    system = property(
        lambda self: pylon.device.system.System(self._stack, self),
        None,
        None, """Returns a system object.

        The system object provides access to lower-level tools."""
    )

    isi = property(
        lambda self: self.__isi,
        None,
        None, """Returns the ISI object, or None if ISI is not supported."""
    )

    stack = property(
        lambda self: self._stack,
        None,
        None, """Returns the Stack object.

        The Stack object is generally considered an internal object, but may
        sometimes be useful to implement advanced functionality. Some pylon
        components also access the stack object directly."""
    )
