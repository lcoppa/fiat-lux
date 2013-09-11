"""This module provides a wrapper for the Pilon stack.

The module should be considered for use within the pilon package only.
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

import ctypes
import logging
import warnings

from pylon.device import toolkit

#
# test_mode controls whether the runtime kit actually connects to the stack.
# In test_mode, no connection to the stack is made, providing a limited
# environment where the is not available, but portions of the stack wrappers
# and higher layers within this package may still be useful during development
# or prototyping.
# Note that test_mode not only prevents connecting with the stack, but also
# alters the timing and the script's threading environment. Use with care!
#
# Supported values: True, False
# Default value: False
#
test_mode = False

#
# vxl_trace can enable very low-level trace message output for debugging.
# This output is provided on the console.
#
# Supported values: True, False
# Default value: False
#
vxl_trace = False

#
# sync_evnt controls how the runtime kit is informed of synchronous events.
# In most environments, this uses a cross-thread callback to the onEventReady
# handler, which in turn signals an event to notify the Application class'
# service() method. The alternative, sync_evnt = False, avoids any cross-
# thread notification. Instead, the Application class' service() method
# performs a throttled event polling. This method requires more processing,
# but may be used where cross-thread callbacks are not suitable.
#
# Supported values: True, False
# Default value: True
#
sync_evnt = True

DOMAIN_ID_MAX_LENGTH = 6
AUTHENTICATION_KEY_LENGTH = 6
PROGRAM_ID_LENGTH = 8
LOCATION_ID_LENGTH = 6
UNIQUE_ID_LENGTH = 6
SIZEOF_ADDRESS = 5
SIZEOF_DPCONFIG = 8
SIZEOF_ALIASCONFIG = SIZEOF_DPCONFIG+2

MAX_DATAPOINTS = 4096
MAX_DOMAINS = 2
MAX_ADDRESSES = 4096
MAX_ALIASES = 8192

MAX_EXT_DP_NAME = 16


class StackError(toolkit.Enum):
    """Stack error codes."""

    __errors = {
        0: 'Success',
        # API errors related to network variables:
        1: 'invalid datapoint index',
        2: 'assumed length is not equal to actual length',
        3: 'datapoint data is too long',
        4: 'polling input datapoint requires polled attribute',
        5: 'cannot poll output datapoint',
        6: 'cannot propagate input datapoint',
        7: 'cannot propagate a polled datapoint',
        # API errors related to application messages
        11: 'explicit destination required but missing',
        12: 'invalid message tag provided',
        13: 'message data exceeds limits',
        14: 'message should be sent as a request',
        15: 'invalid message code',
        16: 'Invalid <LonCorrelator>',
        17: 'Invalid address',
        # API errors related to driver (not used in Pilon)
        31: 'no transmit (downlink) buffer available',
        32: 'no message has been received from the Micro Server',
        33: 'the Micro Server is not responding to RTS',
        # General API errors
        41: 'Link-layer protocol version information unavailable',
        42: 'Unique ID (Neuron ID) unavailable',
        43: 'Initialization failed',
        44: 'invalid datapoint index',
        45: 'invalid datapoint index',
        46: 'API is not initialized',
        47: 'Structure version not supported',
        48: 'Operation not allowed',
        49: 'Invalid parameter specified',
        50: 'Operation not allowed while device is offline',
        51: 'Callback not registered',
        # Non-Volatile Data errors
        71: 'Not a supported non-volatile data segment type',
        72: 'Generic non-volatile data failure',
        73: 'Non-volatile data size is not supported',
        74: 'Non-volatile data access error',
        # Direct Memory File (DMF) access errors
        81: 'DMF address + count is out of range for operation',
        82: 'Write to read-only DMF area',
        83: 'No DMF driver defined',
        # Miscellaneous errors
        90: 'No Network Interface defined',
        91: 'No IP address defined',
        92: 'Unknown LTS device type',
        93: 'Invalid LTS device URI'
    }

    def __init__(self, value=0):
        super(StackError, self).__init__(StackError.__errors, value)


PROGRAM_ID_TYPE = ctypes.c_ubyte * PROGRAM_ID_LENGTH


class InterfaceData(ctypes.Structure):
    """Interface data is used to instantiate the protocol stack.

    InterfaceData is an exact match to the protocol stack C APIs
    LonStackInterfaceData structure, which is used when creating the stack.
    Field names are preserved from the C API to ease documentation and
    cross-referencing.
    """

    _pack_ = 1
    _fields_ = [
        ('Version', ctypes.c_uint32),       # interface data structure version
        ('Signature', ctypes.c_uint32),     # application's unique signature
        ('ProgramId', PROGRAM_ID_TYPE),     # application's unique program ID
        ('StaticNvCount', ctypes.c_uint32),     # number of static datapoints
        ('NvTblSize', ctypes.c_uint32),     # total number of datapoints
        ('DomainTblSize', ctypes.c_uint32),     # number of domains
        ('AddrTblSize', ctypes.c_uint32),   # number of addresses
        ('AliasTblSize', ctypes.c_uint32),  # number of aliases
        ('BindableMsgTagCount', ctypes.c_uint32),   # number of bindable msg
        ('NodeSdString', ctypes.c_char_p),  # self-documentation string
        ('AvgDynNvSdLength', ctypes.c_uint32)    # avg SD size for dyn datapt.
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        signature = self.StaticNvCount + \
            self.NvTblSize << 2 + \
            self.DomainTblSize << 3 + \
            self.AddrTblSize << 4 + \
            self.AliasTblSize << 6 + \
            self.BindableMsgTagCount << 8
        signature += toolkit.simple_checksum(self.NodeSdString)
        signature += toolkit.simple_checksum(self.ProgramId)

        return signature


class TransceiverType(toolkit.Enum):
    """TransceiverType identifies a transceiver type.

    Transceiver types are used when connecting to some channel types.
    The TCP/IP-based IP-C channels use TransceiverTypeDefault.
    """

    __types = {
        0: 'TransceiverTypeDefault',
        1: 'TransceiverType5MHz',
        2: 'TransceiverType10MHz',
        3: 'TransceiverType20MHz',
        4: 'TransceiverType40MHz',
        5: 'TransceiverTypeCustom'
    }

    def __init__(self):
        super(TransceiverType, self).__init__(TransceiverType.__types, 0)


COMMUNICATION_PARAMETER_TYPE = ctypes.c_ubyte * 16


class CommParameters(ctypes.Structure):
    """CommParameters detail timing and similar aspects of the channel.

    CommParameters matches the stack's LonControlData.CommParameters
    structure.
    This is used with ControlData when creating an instance of the stack.
    """

    _pack_ = 1
    _fields_ = [
        ('TransceiverType', ctypes.c_int32),    # use TransceiverType
        ('CommParms', COMMUNICATION_PARAMETER_TYPE)
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        return self.TransceiverType + toolkit.simple_checksum(self.CommParms)


class ApplicationBuffers(ctypes.Structure):
    """Control number and size of the application buffers.

    ApplicationBuffers matches the stack's
    LonControlData.Buffers.ApplicationBuffers structure.
    This is used with ControlData when creating an instance of the stack.
    """

    _pack_ = 1
    _fields_ = [
        ('PriorityMsgOutCount', ctypes.c_uint32),
        ('NonPriorityMsgOutCount', ctypes.c_uint32),
        ('MsgInCount', ctypes.c_uint32)
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        return self.PriorityMsgOutCount + \
            self.NonPriorityMsgOutCount << 3 + \
            self.MsgInCount << 5


class LinkLayerBuffers(ctypes.Structure):
    """Control number and size of the link layer buffers.

    LinkLayerBuffers matches the stack's
    LonControlData.Buffers.LinkLayerBuffers structure.
    This is used with ControlData when creating an instance of the stack.
    """

    _pack_ = 1
    _fields_ = [
        ('LinkLayerBufferCount', ctypes.c_uint32)
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        return self.LinkLayerBufferCount


class TransceiverBuffers(ctypes.Structure):
    """Control number and size of the transceiver buffers.

    TransceiverBuffers matches the stack's
    LonControlData.Buffers.TransceiverBuffers structure.
    This is used with ControlData when creating an instance of the stack.
    """

    _pack_ = 1
    _fields_ = [
        ('NetworkBufferInputSize', ctypes.c_uint32),
        ('NetworkBufferOutputSize', ctypes.c_uint32),
        ('PriorityNetworkOutCount', ctypes.c_uint32),
        ('NonPriorityNetworkOutCount', ctypes.c_uint32),
        ('NetworkInCount', ctypes.c_uint32)
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        return self.NetworkBufferInputSize + \
            self.NetworkBufferOutputSize << 2 + \
            self.PriorityNetworkOutCount << 4 + \
            self.NonPriorityNetworkOutCount << 6 + \
            self.NetworkInCount << 7


class Buffers(ctypes.Structure):
    """Control application, link layer and transceiver buffers.

    Buffers matches the stack's LonControlData.Buffers structure.
    This is used with ControlData when creating an instance of the stack.
    """

    _pack_ = 1
    _fields_ = [
        ('ApplicationBuffers', ApplicationBuffers),
        ('LinkLayerBuffers', LinkLayerBuffers),
        ('TransceiverBuffers', TransceiverBuffers)
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        return self.ApplicationBuffers._signature() ^ \
            self.LinkLayerBuffers._signature() ^ \
            self.TransceiverBuffers._signature()


class ControlData(ctypes.Structure):
    """Control aspects of the stack.

    ControlData is an exact match for the stack's LonControlData structure,
    which is used when creating the stack. Field names are preserved from the
    LonTalk C API to ease documentation and cross-referencing.
    """

    _pack_ = 1
    _fields_ = [
        ('Version', ctypes.c_uint32),       # control data structure version
        ('ServicePinInterval', ctypes.c_uint32),    # Pilon: n/a
        ('NvdFlushGuardTimeout', ctypes.c_uint32),  # NVD batch timer, 1..60s
        ('CommParameters', CommParameters),
        ('Buffers', Buffers),
        ('ReceiveTransCount', ctypes.c_uint32),     # rcv transaction count
        ('TransmitTransCount', ctypes.c_uint32),    # tx transaction count
        ('TransmitTransIdLifetime', ctypes.c_uint32)    # tx TTL, in ms
    ]

    def _signature(self):
        """Compute a signature for this item.

        The signature is used to manage the state of the stack and the storage
        of persistent data. The numeric value of the signature is irrelevant,
        but the signature must reflect all attributes relevant for the external
        interface. Attributes only used within the script can be ignored; do
        not confuse _signature with __hash__.
        """
        result = self.Buffers._signature() + self.CommParameters._signature()
        result ^= self.ReceiveTransCount ^ \
            self.TransmitTransCount << 3 ^ \
            self.TransmitTransIdLifetime << 5
        return result

UNIQUE_ID_TYPE = ctypes.c_ubyte * UNIQUE_ID_LENGTH


class UniqueId(ctypes.Structure):
    """Used to exchange a unique ID with the stack."""

    _pack_ = 1
    _fields_ = [
        ('value',   UNIQUE_ID_TYPE)
    ]


class DpDefinition(ctypes.Structure):
    """Used when registering a datapoint with the stack.

    DpDefinition is an exact match for the stack's LonNvDefinition data
    structure, which is used at initialization time to register static
    datapoints with the stack.
    Field names are preserved from the LonTalk C API to ease documentation
    and cross-referencing.
    """

    _pack_ = 1
    _fields_ = [
        ('Version', ctypes.c_ubyte),    # structure format version
        ('PValue', ctypes.POINTER(ctypes.c_void_p)),    # Pilon: None
        ('DeclaredSize', ctypes.c_ubyte),   # initial and max size, 1..254
        ('SnvtId', ctypes.c_uint16),    # (0 for non-standard types)
        ('ArrayCount', ctypes.c_uint16),    # 0, 2...N
        ('Flags', ctypes.c_uint32),
        ('Name', ctypes.c_char_p),      # external name
        ('SdString', ctypes.c_char_p),  # self-documentation string
        ('MaxRate', ctypes.c_ubyte),    # max propagation rate, 0 if unknown
        ('MeanRate', ctypes.c_ubyte)    # mean propagation rate, 0 if unknown
    ]


class CompletionCode(toolkit.Enum):
    """Matches the stack's completion code.

    CompletionCode can be used to interpret the completion code supplied with
    the datapoint and message completion events.
    """

    __codes = {
        0: 'Failed',
        1: 'Succeeded'
    }

    def __init__(self):
        super().__init__(CompletionCode.__codes, 1)


class ReceiveAddress(toolkit.PilonObject):
    """The class provides the source address for a datapoint update.

    The source address can be used to process inputs from a large number of
    devices that "fan-in" to a single input on the monitoring device. When the
    devices being monitored have the same type of output, a single input
    datapoint can be used on the monitoring device. The connection would likely
    include many output devices (the sensors) and a single input device (the
    monitor). However, the monitoring device in this example must be able to
    distinguish between the many sensor devices.
    The ReceiveAddress class, provided with the datapoint update event
    arguments, can be used to accomplish this.
    """

    SIZEOF_RECEIVE_ADDRESS_STRUCT = 10

    class SubnetNodeAddress(toolkit.PilonObject):
        """Report a subnet / node ID value pair."""

        def __init__(self, s, n):
            self.__subnet = s
            self.__node = n & 0x7F

        subnet = property(
            lambda self: self.__subnet,
            None,
            None, """Subnet ID number, 1..255"""
        )

        node = property(
            lambda self: self.__node,
            None,
            None, """Node ID number, 1..127"""
        )

        def __str__(self):
            return 'S/N {0}/{1}'.format(
                self.__subnet,
                self.__node
            )

    class BroadcastAddress(toolkit.PilonObject):
        """Report a broadcast address."""

        def __init__(self, s):
            self.__subnet = s

        is_domain_broadcast = property(
            lambda self: not self.__subnet,
            None,
            None, """Domain broadcast.

            Indicates whether the address represents a domain-wide broadcast.
            If this property is False, the address represents a subnet-wide
            broadcast on the subnet indicated by 'subnet'
        """)

        subnet = property(
            lambda self: self.__subnet,
            None,
            None, """Subnet ID number, 1..255

            Reports the subnet number for a subnet broadcast, or zero for a
            domain-wide broadcast.
        """)

        def __str__(self):
            if self.is_domain_broadcast:
                return 'Domain broadcast'
            else:
                return 'Subnet {0} broadcast'.format(
                    self.__subnet
                )

    class GroupAddress(toolkit.PilonObject):
        """Report a group address."""

        def __init__(self, g):
            self.__group = g

        group = property(
            lambda self: self.__group,
            None,
            None, """Group ID, 0..255.
        """)

        def __str__(self):
            return 'Group {0}'.format(
                self.__group
            )

    class UniqueIdAddress(toolkit.PilonObject):
        """Report an address using a unique Id."""
        def __init__(self, s, u):
            self.__subnet = s
            self.__unique_id = u

        subnet = property(
            lambda self: self.__subnet,
            None,
            None, """Subnet ID number, 1..255.

            Reports the subnet number for a unique-id-addressed message,
            or zero.
        """)

        unique_id = property(
            lambda self: self.__unique_id,
            None,
            None, """The unique ID as bytes."""
        )

        def __str__(self):
            return 'S-UNID = {0}-'.format(self.__subnet) + \
                self._tostring(self.__unique_id, '.')

    class TurnaroundAddress(toolkit.PilonObject):
        """Report a turnaround address.

        A turnaround address has no specific data other than the fact that it
        is a turnaround address, indicating that the message has been received
        through a turnaround within the same logical device.
        """
        def __str__(self):
            return 'Turnaround'

    def __init__(self, raw):
        super().__init__()
        self.__raw = raw
        self.__bytes = ctypes.string_at(
            raw,
            ReceiveAddress.SIZEOF_RECEIVE_ADDRESS_STRUCT
        )

    def __get_destination(self):
        receive_address_type = self.__bytes[0] & 0x3F

        if receive_address_type == 0:
            return ReceiveAddress.BroadcastAddress(
                self.__bytes[3]
            )
        elif receive_address_type == 1:
            return ReceiveAddress.GroupAddress(
                self.__bytes[3]
            )
        elif receive_address_type == 2:
            return ReceiveAddress.SubnetNodeAddress(
                self.__bytes[3],
                self.__bytes[4]
            )
        elif receive_address_type == 3:
            return ReceiveAddress.UniqueIdAddress(
                self.__bytes[3],
                self.__bytes[4:]
            )
        elif receive_address_type == 4:
            return ReceiveAddress.TurnaroundAddress()

    domain_index = property(
        lambda self: 1 if self.__bytes[0] & 0x80 else 0,
        None,
        None, """Domain index

        Provides the index of the domain through which the message was
        received, 0 or 1.
    """)

    is_flex_domain = property(
        lambda self: self.__bytes[0] & 0x40,
        None,
        None, """Flex domain indicator.

        Indicates whether the message was received on the 'flex domain,'
        that is, on an unconfigured node.
    """)

    source = property(
        lambda self: ReceiveAddress.SubnetNodeAddress(
            self.__bytes[1], self.__bytes[2]
        ),
        None,
        None, """Source object.

        A SubnetNodeAddress object which reports the sender's subnet/node ID
        pair.
    """)

    destination = property(
        __get_destination,
        None,
        None, """Destination object.

        A BroadcastAddress, GroupAddress, SubnetNodeAddress, UniqueIdAddress
        or TurnaroundAddress object, reporting the address through which the
        message was received.
        Use str() or repr() for tracing or logging of this address.
        For algorithmic evaluation, obtain the destination from this property
        and determine its type with isinstance().
    """)

    def __str__(self):
        return 'ReceiveAddress: ' \
            'domain {0}, source ({1}), destination ({2})'.format(
                self.domain_index,
                str(self.source),
                str(self.destination)
            )


class Status(ctypes.Structure):
    """Provide read-only access to node status and statistics."""

    _pack_ = 1
    _fields_ = [
        ('TransmitErrors',          ctypes.c_uint16),
        ('TransactionTimeouts',     ctypes.c_uint16),
        ('ReceiveTransactionsFull', ctypes.c_uint16),
        ('LostMessages',            ctypes.c_uint16),
        ('MissedMessages',          ctypes.c_uint16),
        ('ResetCause',              ctypes.c_int8),
        ('NodeState',               ctypes.c_int8),
        ('VersionNumber',           ctypes.c_uint8),
        ('ErrorLog',                ctypes.c_int8),
        ('ModelNumber',             ctypes.c_int8)
    ]


class Domain(ctypes.Structure):
    """Represent a domain table record."""

    _pack_ = 1
    _fields_ = [
        ('Id',                  ctypes.c_uint8 * DOMAIN_ID_MAX_LENGTH),
        ('Subnet',              ctypes.c_uint8),
        ('NodeClone',           ctypes.c_uint8),
        ('InvalidIdLength',     ctypes.c_uint8),
        ('Key',                 ctypes.c_uint8 * AUTHENTICATION_KEY_LENGTH)
    ]


class Address(ctypes.Structure):
    """Represent an address table record in raw format."""

    _pack_ = 1
    _fields_ = [
        ('data',                ctypes.c_uint8 * SIZEOF_ADDRESS)
    ]


class DatapointConfig(ctypes.Structure):
    """Represent a datapoint configuration table record in raw format."""

    _pack_ = 1
    _fields_ = [
        ('data',                ctypes.c_uint8 * SIZEOF_DPCONFIG)
    ]


class AliasConfig(ctypes.Structure):
    """Represent an alias table record in raw format."""

    _pack_ = 1
    _fields_ = [
        ('data',                ctypes.c_uint8 * SIZEOF_ALIASCONFIG)
    ]

global _stack
_stack = None

logger = logging.getLogger('pylon-rtk.stack')


class Stack(toolkit.PilonObject):
    """Wraps the pilon stack.

    The Stack wrapper provides adaptation and simple abstraction to the
    pylon.Application class, but is generally used as a straight-through
    routing agent between the pylon Application class and the stack's C API.
    """

    def __init__(self, stack='libpylon-stack.so'):
        """Create a stack object.

        Accepts an optional name for the shared library containing the stack.
        Note this library must be found through the LD_LIBRARY_PATH, or by
        passing the absolute location into the 'stack' argument.
        """

        global _stack
        _stack = self

        super().__init__()

        self.__event = {}    # see RegisterXXX()

        logger.debug('Enter Stack().__init__()')

        #
        # Vectors for event handlers registered by the Application class
        #
        self.__on_event_ready_handler = None
        self.__on_reset_handler = None
        self.__on_wink_handler = None
        self.__on_offline_handler = None
        self.__on_online_handler = None
        self.__on_dp_update_handler = None
        self.__on_dp_complete_handler = None
        self.__on_service_led_handler = None

        #
        # Event handler prototypes and proxies for registering the first-level
        # event handlers (the event handlers defined in this class) with the
        # stack through ctypes.
        #
        self.__on_event_ready_prototype = ctypes.CFUNCTYPE(
            None
        )
        self.__on_event_ready_proxy = self.__on_event_ready_prototype(
            self.__on_event_ready
        )

        self.__on_reset_prototype = ctypes.CFUNCTYPE(
            None,
            ctypes.c_void_p
        )
        self.__on_reset_proxy = self.__on_reset_prototype(
            self.__on_reset
        )

        self.__on_wink_prototype = ctypes.CFUNCTYPE(
            None
        )
        self.__on_wink_proxy = self.__on_wink_prototype(
            self.__on_wink
        )

        self.__on_offline_prototype = ctypes.CFUNCTYPE(
            None
        )
        self.__on_offline_proxy = self.__on_offline_prototype(
            self.__on_offline
        )

        self.__on_online_prototype = ctypes.CFUNCTYPE(
            None
        )
        self.__on_online_proxy = self.__on_online_prototype(
            self.__on_online
        )

        self.__on_dp_update_prototype = ctypes.CFUNCTYPE(
            None,
            ctypes.c_uint32, ctypes.c_void_p
        )
        self.__on_dp_update_proxy = self.__on_dp_update_prototype(
            self.__on_dp_update
        )

        self.__on_dp_complete_prototype = ctypes.CFUNCTYPE(
            None,
            ctypes.c_uint32, ctypes.c_int32
        )
        self.__on_dp_complete_proxy = self.__on_dp_complete_prototype(
            self.__on_dp_complete
        )

        self.__on_service_led_prototype = ctypes.CFUNCTYPE(
            None,
            ctypes.c_int32
        )
        self.__on_service_led_proxy = self.__on_service_led_prototype(
            self.__on_service_led
        )

        if not test_mode:
            self._so = ctypes.CDLL(stack)

            if vxl_trace:
                self.vxl_traceEnable = self._so.vxl_traceEnable
                self.vxl_traceEnable.restype = ctypes.c_int
                self.vxl_traceEnable.argtypes = [ctypes.c_int]

                self.vxl_traceEnable(1)

                self.vxlSetReportEventLevel = self._so.vxlSetReportEventLevel
                self.vxlSetReportEventLevel.restype = None
                self.vxlSetReportEventLevel.argtypes = [ctypes.c_int]

                self.vxlSetReportEventLevel(2)

            #
            # Event registration
            #

            self.__on_event_ready_registrar = self._so.LonEventReadyRegistrar
            self.__on_event_ready_registrar.argtypes = [
                self.__on_event_ready_prototype
            ]

            self.__on_reset_registrar = self._so.LonResetRegistrar
            self.__on_reset_registrar.argtypes = [
                self.__on_reset_prototype
            ]

            self.__on_wink_registrar = self._so.LonWinkRegistrar
            self.__on_wink_registrar.argtypes = [
                self.__on_wink_prototype
            ]

            self.__on_offline_registrar = self._so.LonOfflineRegistrar
            self.__on_offline_registrar.argtypes = [
                self.__on_offline_prototype
            ]

            self.__on_online_registrar = self._so.LonOnlineRegistrar
            self.__on_online_registrar.argtypes = [
                self.__on_online_prototype
            ]

            self.__on_dp_update_registrar = \
                self._so.LonNvUpdateOccurredRegistrar
            self.__on_dp_update_registrar.argtypes = [
                self.__on_dp_update_prototype
            ]

            self.__on_dp_complete_registrar = \
                self._so.LonNvUpdateCompletedRegistrar
            self.__on_dp_complete_registrar.argtypes = [
                self.__on_dp_complete_prototype
            ]

            self.__on_service_led_registrar = \
                self._so.LonServiceLedStatusRegistrar
            self.__on_service_led_registrar.argtypes = [
                self.__on_service_led_prototype
            ]

            #
            # Stack API functions
            #

            self.__event_pump = self._so.LonEventPump
            self.__event_pump.restype = None

            self.__create_stack = self._so.LonLidCreateStack
            self.__create_stack.argtypes = [
                ctypes.POINTER(InterfaceData),
                ctypes.POINTER(ControlData)
            ]

            self.__start_stack = self._so.LonLidStartStack
            self.__start_stack.restype = ctypes.c_int32
            self.__start_stack.argtypes = None

            self.__destroy_stack = self._so.LonLidDestroyStack
            self.__destroy_stack.restype = None
            self.__destroy_stack.argtypes = None

            self.__register_dp = self._so.LonLidRegisterStaticNv
            self.__register_dp.argtypes = [ctypes.POINTER(DpDefinition)]

            self.__get_unique_id = self._so.LonGetUniqueId
            self.__get_unique_id.argtypes = [
                ctypes.POINTER(UniqueId)
            ]

            self.__register_unique_id = self._so.LonRegisterUniqueId
            self.__register_unique_id.argtypes = [
                ctypes.POINTER(UniqueId)
            ]

            self.__generate_unique_id = self._so.LonGenerateUniqueId
            self.__generate_unique_id.argtypes = [
                ctypes.POINTER(UniqueId)
            ]

            self.__set_device_uri = self._so.LonSetDeviceUri
            self.__set_device_uri.argtypes = [
                ctypes.c_char_p
            ]

            self.__set_persistence_path = self._so.LonSetNvdFsPath
            self.__set_persistence_path.argtypes = [
                ctypes.c_char_p
            ]

            self.__set_stack_tracefile = self._so.LonSetTracefile
            self.__set_stack_tracefile.restype = None
            self.__set_stack_tracefile.argtypes = [
                ctypes.c_char_p, ctypes.c_int
            ]

            self.__get_stack_version = self._so.LonGetVersion
            self.__get_stack_version.argtypes = [
                ctypes.POINTER(ctypes.c_uint32),
                ctypes.POINTER(ctypes.c_uint32),
                ctypes.POINTER(ctypes.c_uint32)
            ]

            self.__get_declared_dp_size = self._so.LonGetDeclaredNvSize
            self.__get_declared_dp_size.argtypes = [ctypes.c_uint32]

            self.__query_dp_type = self._so.LonQueryNvType
            self.__query_dp_type.argtypes = [
                ctypes.c_uint32,
                ctypes.POINTER(DpDefinition)
            ]

            self.__poll_dp = self._so.LonPollNv
            self.__poll_dp.argtypes = [
                ctypes.c_uint32
            ]

            self.__propagate_dp = self._so.LonPropagateNv
            self.__propagate_dp.argtypes = [
                ctypes.c_uint32
            ]

            self.__send_service_message = self._so.LonSendServicePin
            self.__send_service_message.argtypes = None

            self.__clear_status = self._so.LonClearStatus
            self.__clear_status.argtypes = None

            self.__is_dp_bound = self._so.LonNvIsBound
            self.__is_dp_bound.argtypes = [
                ctypes.c_uint32,
                ctypes.POINTER(ctypes.c_int32)
            ]

            self.__is_mt_bound = self._so.LonMtIsBound
            self.__is_mt_bound.argtypes = [
                ctypes.c_uint32,
                ctypes.POINTER(ctypes.c_int32)
            ]

            self.__get_dp_value = self._so.LonGetNvValue
            self.__get_dp_value.restype = ctypes.POINTER(ctypes.c_ubyte)
            self.__get_dp_value.argtypes = [
                ctypes.c_uint32
            ]

            self.__set_dp_value = self._so.LonSetNvValue
            self.__set_dp_value.argtypes = [
                ctypes.c_uint32,
                ctypes.c_void_p
            ]

            self.__appseg_updated = self._so.LonNvdAppSegmentHasBeenUpdated
            self.__appseg_updated.argtypes = None

            self.__flush_nvd = self._so.LonNvdFlushData
            self.__flush_nvd.argtypes = None

            self.__query_status = self._so.LonQueryStatus
            self.__query_status.argtypes = [
                ctypes.POINTER(Status)
            ]

            self.__set_node_mode = self._so.LonSetNodeMode
            self.__set_node_mode.argtypes = [
                ctypes.c_int8,  # NodeMode
                ctypes.c_int8   # NodeState
            ]

            self.__query_domain = self._so.LonQueryDomainConfig
            self.__query_domain.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(Domain)
            ]

            self.__update_domain = self._so.LonUpdateDomainConfig
            self.__update_domain.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(Domain)
            ]

            self.__query_address = self._so.LonQueryAddressConfig
            self.__query_address.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(Address)
            ]

            self.__update_address = self._so.LonUpdateAddressConfig
            self.__update_address.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(Address)
            ]

            self.__query_datapoint_config = self._so.LonQueryNvConfig
            self.__query_datapoint_config.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(DatapointConfig)
            ]

            self.__update_datapoint_config = self._so.LonUpdateNvConfig
            self.__update_datapoint_config.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(DatapointConfig)
            ]

            self.__query_alias_config = self._so.LonQueryAliasConfig
            self.__query_alias_config.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(AliasConfig)
            ]

            self.__update_alias_config = self._so.LonUpdateAliasConfig
            self.__update_alias_config.argtypes = [
                ctypes.c_uint,  # index
                ctypes.POINTER(AliasConfig)
            ]

            #
            # To support a monotonic timer, the stack class uses the stack's
            # OsalGetTickCount and OsalGetTicksPerSecond API. This allows for
            # a simple timer base which works across operating systems and
            # Python language versions. This stack class maintains its own
            # tick counter as an integer, and automatically adjusts for wrap-
            # around of the 32-bit OSAL tick counter.
            #
            self.__get_tick_count = self._so.OsalGetTickCount
            self.__get_tick_count.argtypes = []
            self.__get_tick_count.restype = ctypes.c_ulong

            get_ticks_per_sec = self._so.OsalGetTicksPerSecond
            get_ticks_per_sec.argtypes = []
            get_ticks_per_sec.restype = ctypes.c_ulong

            self.__ticks_per_sec = get_ticks_per_sec()
            self.__last_ticks = self.__get_tick_count()
            self.__ticks = 0
        else:
            warnings.warn('Stack wrapper is in test_mode')
        logger.debug('Exit Stack().__init_()')

    def __on_event_ready(self):
        """First-level onEventReady handler."""
        try:
            if self.__on_event_ready_handler:
                self.__on_event_ready_handler()
        except Exception as e:
            logger.error(
                'First-level __on_event_ready_handler: {0}'.format(
                    e
                )
            )

    def register_event_ready(self, handler):
        """Register a handler for this event.

        Call register_event_ready() to register the handler for this event.
        The handler for this event takes no arguments and returns no
        result value.
        This is normally done by the Application class.
        """
        self.__on_event_ready_handler = handler

    def __on_reset(self, void):
        """First-level onReset handler."""
        try:
            if self.__on_reset_handler:
                self.__on_reset_handler()
        except Exception as e:
            logger.error(
                'First-level __on_reset_handler(): {0}'.format(
                    e
                )
            )

    def register_reset(self, handler):
        """Register a handler for this event.

        Call register_reset() to register the handler for this event.
        The handler for this event takes no arguments and returns no
        result value.
        This is normally done by the Application class.
        """
        self.__on_reset_handler = handler

    def __on_wink(self):
        """First-level onWink handler."""
        try:
            if self.__on_wink_handler:
                self.__on_wink_handler()
        except Exception as e:
            logger.error(
                'First-level __on_wink_handler(): {0}'.format(
                    e
                )
            )

    def register_wink(self, handler):
        """Register a handler for this event.

        Call register_wink() to register the handler for this event.
        The handler for this event takes no arguments and returns no
        result value.
        This is normally done by the Application class.
        """
        self.__on_wink_handler = handler

    def __on_offline(self):
        """First-level onOffline handler."""
        try:
            if self.__on_offline_handler:
                self.__on_offline_handler()
        except Exception as e:
            logger.error(
                'First-level __on_offline_handler(): {0}'.format(
                    e
                )
            )

    def register_offline(self, handler):
        """Register a handler for this event.

        Call register_offline() to register the handler for this event.
        The handler for this event takes no arguments and returns no
        result value.
        This is normally done by the Application class.
        """
        self.__on_offline_handler = handler

    def __on_online(self):
        """First-level onOnline handler."""
        try:
            if self.__on_online_handler:
                self.__on_online_handler()
        except Exception as e:
            logger.error(
                'First-level __on_online_handler(): {0}'.format(
                    e
                )
            )

    def register_online(self, handler):
        """Register a handler for this event.

        Call register_online() to register the handler for this event.
        The handler for this event takes no arguments and returns no
        result value.
        This is normally done by the Application class.
        """
        self.__on_online_handler = handler

    def __on_dp_update(self, index, source):
        """First-level datapoint update handler."""
        try:
            if self.__on_dp_update_handler:
                self.__on_dp_update_handler(
                    index,
                    ReceiveAddress(source)
                )
        except Exception as e:
            logger.error(
                'First-level __on_dp_update_handler(): {0}'.format(
                    e
                )
            )

    def register_dp_update(self, handler):
        """Register a handler for this event.

        Call register_dp_update() to register the handler for this event.
        The handler for this event takes a Datapoint index and returns no
        result.
        This handler is normally assigned by the Application class.
        """
        self.__on_dp_update_handler = handler

    def __on_dp_complete(self, index, success):
        """First-level onDpComplete handler."""
        try:
            if self.__on_dp_complete_handler:
                self.__on_dp_complete_handler(index, success)
        except Exception as e:
            logger.error(
                'First-level __on_dp_complete(): {0}'.format(
                    e
                )
            )

    def register_dp_complete(self, handler):
        """Register a handler for this event.

        Call register_dp_complete() to register the handler for this event.
        The handler for this event takes a Datapoint NV index and returns no
        result.
        This is normally done by the Application class.
        """
        self.__on_dp_complete_handler = handler

    def __on_service_led(self, state):
        """First-level onServiceLed handler."""
        try:
            if self.__on_service_led_handler:
                self.__on_service_led_handler(state)
        except Exception as e:
            logger.error(
                'First-level __on_service_led_handler(): {0}'.format(
                    e
                )
            )

    def register_service_led(self, handler):
        """Register a service LED handler.

        Call register_service_led() to register the handler for this event.
        This is normally done by the Application class.
        """
        self.__on_service_led_handler = handler

    def __api_call(self, code):
        """An internal wrapper to stack API calls.

        This method provides a simple wrapper around stack API functions,
        converting a numeric error result code into a PylonError, if
        necessary.
        """
        try:
            sts = StackError(code)
            if not sts.is_default:
                raise toolkit.PylonError(
                    sts.value,
                    str(sts)
                )
        except Exception as e:
            # Something broke! Probably a code not recognized by StackError():
            raise toolkit.PylonError(
                code,
                'An unknown error occurred, code {0} ({1})'.format(
                    code,
                    e
                )
            )

    def deregister_all_callbacks(self):
        """Deregister all callbacks registers with the stack

        Call this API to deregister all callbacks previously registered with
        the stack at once. Alternatively, deregister individual callbacks by
        registering None.
        """
        if not test_mode:
            api = self._so.LonDeregisterAllCallbacks
            api.restype = None
            api.argtypes = None
            api()

    def register_unique_id(self, value, separator='.'):
        if isinstance(value, str):
            raw = self._binary(value, (UNIQUE_ID_LENGTH, ), separator)
            unique_id = UniqueId(
                (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
            )
        elif isinstance(value, UniqueId):
            unique_id = value
        else:
            raise TypeError(
                'Expected string or UniqueId, got {0}'.format(
                    type(value)
                )
            )

        self.__api_call(
            self.__register_unique_id(
                unique_id
            )
        )

    def __format_unique_id(self, unique_id):
        return self._tostring(bytes(unique_id.value), '.')

    def generate_unique_id(self):
        result = UniqueId()
        if not test_mode:
            self.__api_call(
                self.__generate_unique_id(result)
            )
        return self.__format_unique_id(result)

    def get_unique_id(self):
        result = UniqueId()
        if not test_mode:
            self.__api_call(
                self.__get_unique_id(result)
            )
        return self.__format_unique_id(result)

    def set_device_uri(self, v):
        if not test_mode:
            self.__api_call(
                self.__set_device_uri(
                    v.encode(
                        encoding='ascii',
                        errors='strict'
                    )
                )
            )

    def set_persistence_path(self, v):
        if not test_mode:
            self.__api_call(
                self.__set_persistence_path(
                    v.encode(
                        encoding='ascii',
                        errors='strict'
                    )
                )
            )

    def set_stack_tracefile(self, filename, append):
        if not test_mode:
            self.__set_stack_tracefile(
                filename.encode(
                    encoding='ascii',
                    errors='strict'
                ),
                append
            )

    def _get_dp_value(self, index, size):
        """_get_dp_value is used by the Application class.

        In addition to the Datapoint index, the function requires the expected
        Datapoint value size in bytes.

        The function retrieves the current Datapoint value, in compact big-
        endian network presentation and as 'raw' data from the Datapoint
        value buffer maintained by the stack.
        """
        if not test_mode:
            ptr = self.__get_dp_value(index)
            return bytes(ptr[:size])
        else:
            return bytes([0] * size)

    def _set_dp_value(self, index, data):
        """_set_dp_value() is used by the Application class.

        The function assigns a new Datapoint value, in compact big-endian
        network presentation and as 'raw' data to the Datapoint value buffer
        maintained by the stack.
        """
        if not test_mode:
            self.__api_call(
                self.__set_dp_value(
                    index,
                    data
                )
            )

    def event_pump(self):
        if not test_mode:
            self.__event_pump()

    def create_stack(self, ifcData, ctlData):
        if not test_mode:
            self.__api_call(
                self.__create_stack(
                    ifcData,
                    ctlData
                )
            )

            #
            # asynchronous events
            #

            self.__on_reset_registrar(self.__on_reset_proxy)
            self.__on_wink_registrar(self.__on_wink_proxy)
            self.__on_offline_registrar(self.__on_offline_proxy)
            self.__on_online_registrar(self.__on_online_proxy)
            self.__on_dp_update_registrar(self.__on_dp_update_proxy)
            self.__on_dp_complete_registrar(self.__on_dp_complete_proxy)
            self.__on_service_led_registrar(self.__on_service_led_proxy)

            #
            # synchronous events
            #
            if sync_evnt:
                self.__on_event_ready_registrar(self.__on_event_ready_proxy)
            else:
                logger.info(
                    'on_event_ready first level handler *not* registered, '
                    'using throttled polling')

    def start_stack(self):
        if not test_mode:
            self.__api_call(
                self.__start_stack()
            )
#            self.__ticks = 0
#            self.__last_ticks = self.__get_tick_count()
        logger.info('start_stack()')

    def register_datapoint(self, dpDefinition):
        if not test_mode:
            self.__api_call(
                self.__register_dp(
                    dpDefinition
                )
            )
        logger.info('register_datapoint(...)')

    def destroy_stack(self):
        if not test_mode:
            self.__destroy_stack()
        logger.info('destroy_stack()')

    def get_stack_version(self):
        """Return the stack version number

        Provides the major, minor and build version numbers of the stack as a
        tuple of three integer values.
        """

        major = ctypes.c_uint32(0)
        minor = ctypes.c_uint32(0)
        build = ctypes.c_uint32(0)

        if not test_mode:
            self.__api_call(
                self.__get_stack_version(
                    major,
                    minor,
                    build
                )
            )
        return major.value, minor.value, build.value

    def get_declared_dp_size(self, index):
        if not test_mode:
            return self.__get_declared_dp_size(index)
        else:
            return 0

    def poll_dp(self, index):
        if not test_mode:
            self.__api_call(
                self.__poll_dp(index)
            )

    def propagate_dp(self, index):
        if not test_mode:
            self.__api_call(
                self.__propagate_dp(index)
            )

    def send_service_message(self):
        if not test_mode:
            self.__api_call(
                self.__send_service_message()
            )

    def clear_status(self):
        if not test_mode:
            self.__api_call(
                self.__clear_status()
            )

    def is_dp_bound(self, index):
        bound = ctypes.c_int32()
        if not test_mode:
            self.__api_call(
                self.__is_dp_bound(
                    index,
                    ctypes.pointer(bound)
                )
            )
        return bound.value

    def is_mt_bound(self, index):
        bound = ctypes.c_int32()
        if not test_mode:
            self.__api_call(
                self.__is_mt_bound(
                    index,
                    ctypes.pointer(bound)
                )
            )
        return bound.value

    def nvd_appseg_updated(self):
        if not test_mode:
            self.__api_call(
                self.__appseg_updated()
            )

    def flush_nvd(self):
        if not test_mode:
            self.__api_call(
                self.__flush_nvd()
            )

    def query_status(self):
        status = Status()
        if not test_mode:
            self.__api_call(
                self.__query_status(
                    status
                )
            )
        return status

    def set_node_mode(self, mode, state):
        if not test_mode:
            self.__api_call(
                self.__set_node_mode(
                    mode,
                    state
                )
            )

    def query_domain(self, index):
        """Return a stack.Domain object"""
        domain = Domain()
        if not test_mode:
            self.__api_call(
                self.__query_domain(
                    index,
                    domain
                )
            )
        return domain

    def update_domain(self, index, domain):
        """Accept a stack.Domain object."""
        if not test_mode:
            self.__api_call(
                self.__update_domain(
                    index,
                    domain
                )
            )

    def query_address(self, index):
        """Return a bytearray of raw address table data."""
        address = Address()
        if not test_mode:
            self.__api_call(
                self.__query_address(
                    index,
                    address
                )
            )
        return bytearray(address.data)

    def update_address(self, index, raw):
        """Update an address table record from a bytearray."""
        address = Address()
        if not test_mode:
            for i in range(len(raw)):
                address.data[i] = raw[i]
            self.__api_call(
                self.__update_address(
                    index,
                    address
                )
            )

    def query_datapoint_config(self, index):
        """Return a bytearray of raw datapoint config table data."""
        config = DatapointConfig()
        if not test_mode:
            self.__api_call(
                self.__query_datapoint_config(
                    index,
                    config
                )
            )
        return bytearray(config.data)

    def update_datapoint_config(self, index, raw):
        """Update an datapoint config table record from a bytearray."""
        config = DatapointConfig()
        if not test_mode:
            for i in range(len(raw)):
                config.data[i] = raw[i]
            self.__api_call(
                self.__update_datapoint_config(
                    index,
                    config
                )
            )

    def query_alias_config(self, index):
        """Return a bytearray of raw alias table data."""
        config = AliasConfig()
        if not test_mode:
            self.__api_call(
                self.__query_alias_config(
                    index,
                    config
                )
            )
        return bytearray(config.data)

    def update_alias_config(self, index, raw):
        """Update an alias record from a bytearray."""
        config = AliasConfig()
        if not test_mode:
            for i in range(len(raw)):
                config.data[i] = raw[i]
            self.__api_call(
                self.__update_alias_config(
                    index,
                    config
                )
            )

    #
    # Monotonic timer support:
    # To supply a simple monotonic time base to the toolkit.Timer class, the
    # stack provides the 'ticks' property. This works across different
    # operating systems and does not require a specific Python version (unlike
    # Python's time.monotonic(), which requires Python 3.3 or better).
    #
    def __get_ticks(self):
        current = self.__get_tick_count()
        delta = current - self.__last_ticks

        if delta < 0:
            # Wrap-around. The pilon stack provides a 32-bit unsigned tick
            # count, so the number of ticks elapsed must be corrected by
            # compensating for the wrap-around:
            self.__ticks += current + 0x100000000 - self.__last_ticks
        else:
            self.__ticks += delta
        self.__last_ticks = current
        return self.__ticks

    ticks_per_sec = property(
        lambda self: self.__ticks_per_sec,
        None,
        None, """The number of ticks per second. See 'ticks'. """
    )

    ticks = property(
        __get_ticks,
        None,
        None, """The current ticks count.

        Ticks provides a simple monotonic timer API, portable across operating
        systems and Python versions. ticks returns an integer value, which
        increments with 'ticks_per_sec' every second."""
    )
