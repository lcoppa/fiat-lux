"""The pilon system module, providing the System class and related classes.

This module defines the System class. You do not normally create an instance
of the system object, but obtain one from the read-only Application.system
property.
The System object provides access to low-level data structures and utilities.

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

import pylon.device.stack
from pylon.device import toolkit

logger = logging.getLogger('pylon-rtk.system')


class ResetCause:
    """Describes the most recent reset cause."""

    CLEARED = 0x00
    POWER_UP = 0x01
    EXTERNAL = 0x02
    WATCHDOG = 0x0C
    SOFTWARE = 0x14


class NodeState:
    """Describes the current node state."""

    INVALID = 0x00              # invalid or Echelon use only
    INVALID_1 = 0x01            # see INVALID
    UNCONFIGURED = 0x02         # has application, node unconfigured
    APPLICATIONLESS = 0x03      # has no application, node unconfigured
    CONFIGURED_ONLINE = 0x04    # node is configured, application is online
    INVALID_5 = 0x05            # see INVALID
    HARD_OFFLINE = 0x06         # node is configured, application offline
    INVALID_7 = 0x07            # see INVALID
    SOFT_OFFLINE = 0x12         # node is configured, application offline
    BYPASS = 0x8C               # node is configured, application in bypass


class NodeMode:
    """Describes the node's mode."""

    OFFLINE = 0
    ONLINE = 1
    RESET = 2
    CHANGESTATE = 3


class StackError:
    """System error codes."""

    NO_ERROR = 0
    BAD_EVENT = 129
    DATAPOINT_LENGTH_MISMATCH = 130
    DATAPOINT_MSG_TOO_SHORT = 131
    EEPROM_WRITE_FAIL = 132
    BAD_ADDRESS_TYPE = 133
    PREEMPTION_MODE_TIMEOUT = 134
    ALREADY_PREEMPTED = 135
    SYNCNV_UPDATE_LOST = 136
    INVALID_RESP_ALLOC = 137
    INVALID_DOMAIN = 138
    READ_PAST_END_OF_MSG = 139
    WRITE_PAST_END_OF_MSG = 140
    INVALID_ADDR_TABLE_INDEX = 141
    INCOMPLETE_MSG = 142
    DATAPOINT_UPDATE_ON_OUTPUT = 143
    NO_MSG_AVAILABLE = 144
    ILLEGAL_SEND = 145
    UNKNOWN_PDU = 146
    INVALID_DATAPOINT_INDEX = 147
    DIVIDE_BY_ZERO = 148
    INVALID_APPL_ERROR = 149
    MEMORY_ALLOC_FAILURE = 150
    WRITE_PAST_END_OF_NET_BUFFER = 151
    APPL_CHECKSUM_ERROR = 152
    CNFG_CHECKSUM_ERROR = 153
    INVALID_XCVR_REG_ADDR = 154
    XCVR_REG_TIMEOUT = 155
    WRITE_PAST_END_OF_APPL_BUFFER = 156
    IO_READY = 157
    SELFTEST_FAILED = 158
    SUBNET_ROUTER = 159
    AUTHENTICATION_MISMATCH = 160
    SELFINST_SEMAPHORE_SET = 161
    READ_WRITE_SEMAPHORE_SET = 162
    APPL_SIGNATURE_BAD = 163
    ROUTER_FIRMWARE_VERSION_MISMATCH = 164


class NeuronModel:
    NEURON_3150 = 0         # 3150, FT 3150
    NEURON_PL3150 = 1       # PL 3150
    NEURON_3150L = 2        # CY7C53150L
    NEURON_3120 = 8         # Legacy 3120
    NEURON_3120E1 = 9       # 3120E1, TMPN3120FE1M
    NEURON_3120E2 = 10      # 3120E2
    NEURON_3120E3 = 11      # 3120E3, TMPN3120FE3M
    NEURON_3120A20 = 12     # 3120A20
    NEURON_3120E5 = 13      # 3120E5, TMPN3120FE5M
    NEURON_3120E4 = 14      # CY7C53120E4, FT 3120-E4
    NEURON_PL3120E4 = 15    # PL 3120-E4
    NEURON_3120L8 = 16      # CY7C53120L8
    NEURON_PL3170 = 17      # PL 3170
    NEURON_FT5000 = 32      # FT 5000
    NEURON_5000 = 33        # Neuron 5000
    OTHER = 128             # Not a Neuron Chip or Smart Transceiver


class RepeatTimer:
    RPT16 = 0    # 16 ms
    RPT24 = 1    # 24 ms
    RPT32 = 2    # 32 ms
    RPT48 = 3    # 48 ms
    RPT64 = 4    # 64 ms
    RPT96 = 5    # 96 ms
    RPT128 = 6    # 128 ms
    RPT192 = 7    # 192 ms
    RPT256 = 8    # 256 ms
    RPT384 = 9    # 384 ms
    RPT512 = 10    # 512 ms
    RPT768 = 11    # 768 ms
    RPT1024 = 12    # 1024 ms
    RPT1536 = 13    # 1536 ms
    RPT2048 = 14    # 2048 ms
    RPT3072 = 15    # 3072 ms


class ReceiveTimer:
    RCV128 = 0    # 128 ms
    RCV192 = 1    # 192 ms
    RCV256 = 2    # 256 ms
    RCV384 = 3    # 384 ms
    RCV512 = 4    # 512 ms
    RCV768 = 5    # 768 ms
    RCV1024 = 6    # 1024 ms
    RCV1536 = 7    # 1536 ms
    RCV2048 = 8    # 2048 ms
    RCV3072 = 9    # 3072 ms
    RCV4096 = 10    # 4096 ms
    RCV6144 = 11    # 6144 ms
    RCV8192 = 12    # 8192 ms
    RCV12288 = 13    # 12288 ms
    RCV16384 = 14    # 16384 ms
    RCV24576 = 15    # 24576 ms


class TransmitTimer:
    TX16 = 0    # 16 ms
    TX24 = 1    # 24 ms
    TX32 = 2    # 32 ms
    TX48 = 3    # 48 ms
    TX64 = 4    # 64 ms
    TX96 = 5    # 96 ms
    TX128 = 6    # 128 ms
    TX192 = 7    # 192 ms
    TX256 = 8    # 256 ms
    TX384 = 9    # 384 ms
    TX512 = 10    # 512 ms
    TX768 = 11    # 768 ms
    TX1024 = 12    # 1024 ms
    TX1536 = 13    # 1536 ms
    TX2048 = 14    # 2048 ms
    TX3072 = 15    # 3072 ms


class AddressType:
    UNBOUND = 0
    SUBNETNODE = 1
    UNIQUEID = 2
    BROADCAST = 3
    LOCAL = 127


class Status(toolkit.PilonObject):
    """Provide read-only access to node status and statistics."""

    def __init__(self, raw):
        self.__raw = raw

    transmit_errors = property(
        lambda self: self.__raw.TransmitErrors,
        None,
        None, """Transmit error counter.

        The number of CRC errors detected during packet reception."""
    )

    transaction_timeouts = property(
        lambda self: self.__raw.TransactionTimeouts,
        None,
        None, """Transaction timeout counter.

        The number of times the node failed to receive expected responses or
        acknowledgements after all configured retries were exhausted."""
    )

    receive_transactions_full = property(
        lambda self: self.__raw.ReceiveTransactionsFull,
        None,
        None, """Receive transaction full counter.

        The number of times an incoming packet was discarded because there was
        no room in the transaction database."""
    )

    lost_messages = property(
        lambda self: self.__raw.LostMessages,
        None,
        None, """Lost messages counter.

        The number of times an incoming packet was discarded because no input
        application buffer was available."""
    )

    missed_messages = property(
        lambda self: self.__raw.MissedMessages,
        None,
        None, """Missed messages counter.

        The number of times an incoming packet was discarded because no input
        network buffer was available."""
    )

    reset_cause = property(
        lambda self: self.__raw.ResetCause,
        None,
        None, """Cause of most recent reset.

        Reports the cause of the most recent reset, using a value from
        ResetCause. With the pilon stack, this refers to a logical reset."""
    )

    node_state = property(
        lambda self: self.__raw.NodeState,
        None,
        None, """The node state, using a value from NodeState."""
    )

    version_number = property(
        lambda self: self.__raw.VersionNumber,
        None,
        None, """The stack firmware version number."""
    )

    error_log = property(
        lambda self: self.__raw.ErrorLog,
        None,
        None, """The most recent system error, using StackError."""
    )

    model_number = property(
        lambda self: self.__raw.ModelNumber,
        None,
        None, """Chip model number.

        Reports the model number of the hosting chip (for Neuron Chip and
        Smart Transceiver based devices only). Uses values from NeuronModel.
    """)


class Domain(toolkit.PilonObject):
    """A domain table record.

    You can create a Domain object and use it with the System object's
    update_domain() method, however, it is generally recommended to obtain
    one of the current domain records from the System object's query_domain()
    method, modify it as necessary, and assign the modified object with
    update_domain().
    """

    def __init__(self, raw=None):
        if raw:     # init from a stack.Domain object
            self.__id = bytearray(raw.Id)
            self.__subnet = raw.Subnet
            self.__clone_domain = not (raw.NodeClone & 0x80)
            self.__node = raw.NodeClone & 0x7F
            self.__is_valid = raw.InvalidIdLength & 0x80
            self.__id_length = raw.InvalidIdLength & 0x07
            self.__key = bytearray(raw.Key)
        else:
            self.__id = bytearray(pylon.device.stack.DOMAIN_ID_MAX_LENGTH)
            self.__subnet = 0
            self.__clone_domain = False
            self.__node = 0
            self.__is_valid = False
            self.__id_length = 0
            self.__key = bytearray(pylon.device.stack.AUTHENTICATION_KEY_LENGTH)

    def __set_id(self, v):
        if isinstance(v, bytes):
            v = bytearray(v)
        if isinstance(v, bytearray):
            length = self._in_selection(
                'Domain Id length', len(v), (0, 1, 3, 6)
            )
            self.__id = v
            self.__id_length = length
            self.__is_valid = True
        elif isinstance(v, str):
            words = v.split(':')
            length = self._in_selection(
                'Domain Id length', len(words), (0, 1, 3, 6)
            )
            self.__id = bytearray(length)
            self.__id_length = length
            self.__is_valid = True
            for i in range(length):
                self.__id[i] = int(words[i], 16)
        else:
            raise AttributeError(
                'Expected bytes, bytearray or string'
            )

    domain_id = property(
        lambda self: self.__id[:self.__id_length],
        __set_id,
        None, """The domain identifier.

        Reports the domain id as a bytearray object, and accepts bytes,
        bytearray and string objects when set. When using string assignment,
        use a colon-separated hex-encoded ASCII form, e.g. '0A:BC:02'.

        To obtain the length of the domain Id, use len().

        To set the length of the domain Id, assign a domain Id of the desired
        length.
    """)

    def __set_is_valid(self, v):
        self.__is_valid = bool(v)

    is_valid = property(
        lambda self: self.__is_valid,
        __set_is_valid,
        None, """Domain record validity.

        Reports and controls whether this domain record contains a valid
        configuration.
    """)

    def __set_subnet(self, v):
        self.__subnet = self._in_range('Subnet Id', v, 1, 255)

    subnet_id = property(
        lambda self: self.__subnet,
        __set_subnet,
        None, """Subnet Id, 1..255. """
    )

    def __set_is_cloned(self, v):
        self.__clone_domain = bool(v)

    is_cloned = property(
        lambda self: self.__clone_domain,
        __set_is_cloned,
        None, """Clone domain flag."""
    )

    def __set_node(self, v):
        self.__node = self._in_range("Node Id", v, 1, 127)

    node_id = property(
        lambda self: self.__node,
        __set_node,
        None, """Node Id, 1..127"""
    )

    def __set_key(self, v):
        if isinstance(v, bytes):
            v = bytearray(v)
        if isinstance(v, bytearray):
            self._in_selection('Key length', len(v), 6)
            self.__key = v
        elif isinstance(v, str):
            words = v.split(':')
            length = self._in_selection('Key length', len(words), 6)
            self.__key = bytearray(length)
            for i in range(length):
                self.__key[i] = int(words[i], 16)
        else:
            raise AttributeError(
                'Expected bytes, bytearray or string'
            )

    key = property(
        lambda self: self.__key,
        __set_key,
        None, """Authentication key.

        Reports the authentication key as a bytearray object, and accepts
        bytes, bytearray and string objects when set.
        When using string assignment, use a colon-separated hex-encoded ASCII
        form, e.g. 'F0:F1:F2:F3:F4:F5' """
    )

    def _get_raw(self):
        result = pylon.device.stack.Domain()
        result.Id = tuple(self.__id)
        result.Subnet = self.__subnet
        if self.__clone_domain:
            result.NodeClone = self.__node
        else:
            result.NodeClone = self.__node | 0x80
        if self.__is_valid:
            result.InvalidIdLength = self.__id_length
        else:
            result.InvalidIdLength = 0x80
        result.Key = tuple(self.__key)
        return result

    def __str__(self):
        if self.__is_valid:
            return 'D S/N (K): {0} {1}/{2}{3} ({4})'.format(
                bytes(self.domain_id),
                self.subnet_id,
                self.node_id,
                '*' if self.is_cloned else '',
                bytes(self.key)
            )
        else:
            return 'Not in use'


class Address(toolkit.PilonObject):
    """The root for all classes representing an address table entry."""

    def __init__(self, raw):
        if raw:
            self.__repeat_timer = raw[2] >> 4 & 0x0F
            self.__retry = raw[2] & 0x0F
            self.__receive_timer = raw[3] >> 4 & 0x0F
            self.__transmit_timer = raw[3] & 0x0F
        else:
            self.__repeat_timer = 0
            self.__retry = 0
            self.__receive_timer = 0
            self.__transmit_timer = 0

    def _get_raw(self):
        raw = bytearray(5)
        raw[2] = (self.__repeat_timer << 4 | self.__retry) & 0x0FF
        raw[3] = (self.__receive_timer << 4 | self.__transmit_timer) & 0x0FF
        return raw

    def __str__(self):
        return 'RPT {0} RTY {1} RCV {2} TX {3}'.format(
            self.__repeat_timer,
            self.__retry,
            self.__receive_timer,
            self.__transmit_timer
        )

    def __set_repeat_timer(self, v):
        self.__repeat_timer = self._in_range('Repeat timer', v, 0, 15)

    repeat_timer = property(
        lambda self: self.__repeat_timer,
        __set_repeat_timer,
        None, """Repeat timer (encoded, use RepeatTimer constants).

        Provides address to the repeat timer.
        Use constants declared with RepeatTimer.
    """)

    def __set_retries(self, v):
        self.__retry = self._in_range('Retries', v, 0, 15)

    retries = property(
        lambda self: self.__retry,
        __set_retries,
        None, """Number of retries."""
    )

    def __set_receive_timer(self, v):
        self.__receive_timer = self._in_range('Receive timer', v, 0, 15)

    receive_timer = property(
        lambda self: self.__receive_timer,
        __set_receive_timer,
        None, """Receive timer (encoded, use ReceiveTimer constants).

        Provides address to the receive timer. This should be set to zero for
        broadcast and turnaround addresses.
        Use constants declared with ReceiveTimer.
    """)

    def __set_transmit_timer(self, v):
        self.__transmit_timer = self._in_range('Transmit timer', v, 0, 15)

    transmit_timer = property(
        lambda self: self.transmit_timer,
        __set_transmit_timer,
        None, """Transmit timer (encoded, use TransmitTimer constants).

        Provides address to the transmit timer.
        Use constants declared with TransmitTimer.
    """)


class GroupAddress(Address):
    """An address table record for group addressing."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytesarray object of from scratch.
        """
        super().__init__(raw)

        if raw:
            self.__size = raw[0] & 0x7F
            self.__domain = raw[1] & 0x80
            self.__member = raw[1] & 0x7F
            self.__group = raw[4]
        else:
            self.__size = 0
            self.__domain = 0
            self.__member = 0
            self.__group = 0

    def _get_raw(self):
        raw = super()._get_raw()
        raw[0] = 0x80 | self.__size
        raw[1] = self.__domain | self.__member
        raw[4] = self.__group
        return raw

    def __str__(self):
        return 'Group {0} Member {1} Size {2} Domain {3} {4}'.format(
            self.__group,
            self.__member,
            self.__size,
            self.domain,
            super().__str__()
        )

    def __set_size(self, v):
        self.__size = self._in_range('Group size', v, 0, 63)

    size = property(
        lambda self: self.__size,
        __set_size,
        None, """Group size (number of members)."""
    )

    def __set_domain(self, v):
        self.__domain = 0x80 if self._in_range('Domain index', v, 0, 1) else 0

    domain = property(
        lambda self: 1 if self.__domain else 0,
        __set_domain,
        None, """Domain index. """
    )

    def __set_member(self, v):
        self.__member = self._in_range('Member number', v, 0, 63)

    member = property(
        lambda self: self.__member,
        __set_member,
        None, """Member number."""
    )

    def __set_group(self, v):
        self.__group = self._in_range('Group ', v, 0, 255)

    group_id = property(
        lambda self: self.__group,
        __set_group,
        None, """Group Id."""
    )


class SubnetNodeAddress(Address):
    """An address table record for subnet/node addressing."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytesarray object or from scratch.
        """
        super().__init__(raw)

        if raw:
            self.__domain = raw[1] & 0x80
            self.__node = raw[1] & 0x7F
            self.__subnet = raw[4]
        else:
            self.__domain = 0
            self.__node = 0
            self.__subnet = 0

    def _get_raw(self):
        raw = super()._get_raw()
        raw[0] = AddressType.SUBNETNODE
        raw[1] = self.__domain | self.__node
        raw[4] = self.__subnet
        return raw

    def __str__(self):
        return 'S/N {0}/{1} Domain {2} {3}'.format(
            self.__subnet,
            self.__node,
            self.domain,
            super().__str__()
        )

    def __set_domain(self, v):
        self.__domain = 0x80 if self._in_range('Domain index', v, 0, 1) else 0

    domain = property(
        lambda self: 1 if self.__domain else 0,
        __set_domain,
        None, """Domain index."""
    )

    def __set_node(self, v):
        self.__node = self._in_range('Node id', v, 1, 127)

    node_id = property(
        lambda self: self.__node,
        __set_node,
        None, """Node Id, 1..127."""
    )

    def __set_subnet(self, v):
        self.__subnet = self._in_range('Subnet id', v, 1, 255)

    subnet_id = property(
        lambda self: self.__subnet,
        __set_subnet,
        None, """Subnet Id, 1..255."""
    )


class BroadcastAddress(Address):
    """An address table record for broadcast addressing."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytesarray object or from scratch.
        """
        super().__init__(raw)

        if raw:
            self.__domain = raw[1] & 0x80
            self.__backlog = raw[1] & 0x3F
            self.__subnet = raw[4]
        else:
            self.__domain = 0
            self.__backlog = 0
            self.__subnet = 0

    def _get_raw(self):
        raw = super()._get_raw()
        raw[0] = AddressType.BROADCAST
        raw[1] = self.__domain | self.__backlog
        raw[4] = self.__subnet
        return raw

    def __str__(self):
        return 'Broadcast S {0} Domain {1} {2}'.format(
            self.__subnet,
            self.domain,
            super().__str__()
        )

    def __set_domain(self, v):
        self.__domain = 0x80 if self._in_range('Domain index', v, 0, 1) else 0

    domain = property(
        lambda self: 1 if self.__domain else 0,
        __set_domain,
        None, """Domain index."""
    )

    def __set_backlog(self, v):
        self.__backlog = self._in_range('Backlog', v, 0, 63)

    backlog = property(
        lambda self: self.__backlog,
        __set_backlog,
        None, """Backlog estimate, or zero if unknown."""
    )

    def __set_subnet(self, v):
        self.__subnet = self._in_range('Subnet id', v, 0, 255)

    subnet_id = property(
        lambda self: self.__subnet,
        __set_subnet,
        None, """Subnet Id, 1..255 or 0 for domain-wide broadcasts."""
    )


class TurnaroundAddress(Address):
    """An address table record for a turnaround address."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytesarray object or from scratch.
        """
        super().__init__(raw)

    def _get_raw(self):
        raw = super()._get_raw()
        raw[0] = AddressType.UNBOUND
        raw[1] = 1
        return raw

    def __str__(self):
        return 'Turnaround {0}'.format(
            super().__str__()
        )


class UnusedAddress(Address):
    """An unused address table record."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytesarray object or from scratch.
        """
        super().__init__(raw)

    def _get_raw(self):
        raw = super()._get_raw()
        raw[0] = AddressType.UNBOUND
        raw[1] = 0
        return raw

    def __str__(self):
        return 'Not in use'


class SelectionType:
    SELECTOR_ONLY = 0          # normal: select with selector match
    SELECTOR_AND_SOURCE = 1    # select w/ selector and source match
    NO_SELECTION = 2           # no selection; reserved for poll-only inputs


class ServiceType:
    ACKNOWLEDGED = 0
    REPEATED = 1
    UNACKNOWLEDGED = 2
    REQUEST = 3


class DatapointConfig(toolkit.PilonObject):
    """A datapoint's system configuration data."""

    ADDRESS_UNUSED = 0x0FFFF        # use for invalid address index

    def __init__(self, raw=None):
        """Create the object from a bytes or bytearray object, of from scratch.
        """
        super().__init__()

        if raw:
            self.__priority = raw[0] & 0x80
            self.__output = raw[0] & 0x40
            self.__selector = (raw[0] & 0x3F) << 8 | raw[1]
            self.__turnaround = raw[2] & 0x80
            self.__authentication = raw[2] & 0x40
            self.__write_by_index = raw[2] & 0x20
            self.__remote_nm_auth = raw[2] & 0x10
            self.__response_selection = (raw[2] & 0x0C) >> 2
            self.__read_by_index = raw[3] & 0x80
            self.__service = (raw[3] & 0x60) >> 5
            self.__request_selection = (raw[3] & 0x18) >> 3
            self.__update_selection = (raw[3] & 0x06) >> 1
            self.__source_selection = raw[3] & 0x01
            self.__address_index = raw[4] << 8 | raw[5]
            self.__remote_datapoint_index = raw[6] << 8 | raw[7]
        else:
            self.__priority = 0
            self.__output = 0
            self.__selector = 0
            self.__turnaround = 0
            self.__authentication = 0
            self.__write_by_index = 0
            self.__remote_nm_auth = 0
            self.__response_selection = SelectionType.SELECTOR_ONLY
            self.__read_by_index = 0
            self.__service = ServiceType.ACKNOWLEDGED
            self.__request_selection = SelectionType.SELECTOR_ONLY
            self.__update_selection = SelectionType.SELECTOR_ONLY
            self.__source_selection = 0
            self.__address_index = 0
            self.__remote_datapoint_index = 0

    def _get_raw(self, raw=None):
        if not raw:
            raw = bytearray(8)

        raw[0] = self.__priority | self.__output
        raw[0] |= self.__selector >> 8 & 0x03F

        raw[1] = self.__selector & 0x0FF

        raw[2] = self.__turnaround | \
            self.__authentication | \
            self.__write_by_index | \
            self.__remote_nm_auth
        raw[2] |= self.__response_selection << 2

        raw[3] = self.__read_by_index | self.__source_selection
        raw[3] |= self.__service << 5
        raw[3] |= self.__request_selection << 3
        raw[3] |= self.__update_selection << 1

        raw[4] = self.__address_index >> 8
        raw[5] = self.__address_index & 0x0FF

        raw[6] = self.__remote_datapoint_index >> 8
        raw[7] = self.__remote_datapoint_index & 0x0FF

        return raw

    def __str__(self):
        """Report a summary of this object."""
        return 'Selector {0:04X}, {1}, address #({2}), service #{3}'.format(
            self.selector,
            'Output' if self.__output else 'Input',
            self.__address_index if self.__address_index != 65535 else 'None',
            self.__service
        )

    def __set_priority(self, v):
        self.__priority = 0x80 if v else 0

    priority = property(
        lambda self: True if self.__priority else False,
        __set_priority,
        None, """Current priority selection.

        Indicates whether the datapoint is currently configured for priority
        transport.
    """)

    def __set_output(self, v):
        self.__output = 0x40 if v else 0

    output = property(
        lambda self: True if self.__output else False,
        __set_output,
        None, """Direction, True for an output.

        Indicates whether the datapoint is an output. (Otherwise, it is an
        input. Datapoints are never directionless, never bidirectional.)"""
    )

    def __set_selector(self, v):
        self.__selector = self._in_range('Selector', v, 0, 0x3FFF)

    selector = property(
        lambda self: self.__selector,
        __set_selector,
        None, """Current datapoint selector value."""
    )

    def __set_turnaround(self, v):
        self.__turnaround = 0x80 if v else 0

    turnaround = property(
        lambda self: True if self.__turnaround else False,
        __set_turnaround,
        None, """Current turnaround attribute.

        Indicates whether the datapoint is part of a local turnaround."""
    )

    def __set_authentication(self, v):
        self.__authentication = 0x40 if v else 0

    authentication = property(
        lambda self: True if self.__authentication else False,
        __set_authentication,
        None, """Current authentication selection.

        Indicates whether the datapoint uses authentication."""
    )

    def __set_write_by_index(self, v):
        self.__write_by_index = 0x20 if v else 0

    write_by_index = property(
        lambda self: True if self.__write_by_index else False,
        __set_write_by_index,
        None, """
        Indicates whether the datapoint may be written by index."""
    )

    def __set_remote_nm_auth(self, v):
        self.__remote_nm_auth = 0x10 if v else 0

    remote_nm_auth = property(
        lambda self: True if self.__remote_nm_auth else False,
        __set_remote_nm_auth,
        None, """
        Indicates whether network management authentication is enabled on
        devices connected to this datapoint."""
    )

    def __set_response_selection(self, v):
        self.__response_selection = self._in_range(
            'Response selection', v, 0, 3
        )

    response_selection = property(
        lambda self: self.__response_selection,
        __set_response_selection,
        None, """
        Indicates the selection mode for responses. Use one of the constants
        defined with SelectionType."""
    )

    def __set_read_by_index(self, v):
        self.__read_by_index = 0x080 if v else 0

    read_by_index = property(
        lambda self: True if self.__read_by_index else False,
        __set_read_by_index,
        None, """
        Indicates whether the datapoint can be read by index."""
    )

    def __set_service(self, v):
        self.__service = self._in_range('Service type', v, 0, 3)

    service_type = property(
        lambda self: self.__service,
        __set_service,
        None, """Current service type.

        Reports the configured service type. Use one of the constants defined
        by ServiceType."""
    )

    def __set_request_selection(self, v):
        self.__request_selection = self._in_range(
            'Request selection', v, 0, 3
        )

    request_selection = property(
        lambda self: self.__request_selection,
        __set_request_selection,
        None, """
        Reports the selection type for requests. Use one of the constants
        defined with SelectionType."""
    )

    def __set_update_selection(self, v):
        self.__update_selection = self._in_range(
            'Request selection', v, 0, 3
        )

    update_selection = property(
        lambda self: self.__update_selection,
        __set_update_selection,
        None, """
        Reports the selection type for updates. Use one of the constants
        defined with SelectionType.
    """)

    def __set_source_selection(self, v):
        self.__source_selection = 0x01 if v else 0

    source_selection = property(
        lambda self: True if self.__source_selection else False,
        __set_source_selection,
        None, """
        Indicates whether source selection is enabled.
    """)

    def __set_address_index(self, v):
        self.__address_index = self._in_range(
            'Address index',
            v, 0, pylon.device.stack.MAX_ADDRESSES-1,
            DatapointConfig.ADDRESS_UNUSED
        )

    address_index = property(
        lambda self: self.__address_index,
        __set_address_index,
        None, """The address index configured for this datapoint.
    """)

    def __set_remote_datapoint_index(self, v):
        self.__remote_datapoint_index = self._in_range(
            'Remote datapoint index',
            v, 0, pylon.device.stack.MAX_DATAPOINTS-1,
            0x0FFFF
        )

    remote_datapoint_index = property(
        lambda self: self.__remote_datapoint_index,
        __set_remote_datapoint_index,
        None, """The configured remote datapoint index.
    """)


class AliasConfig(DatapointConfig):
    """A datapoint alias's system configuration data."""

    def __init__(self, raw=None):
        """Create the object from a bytes or bytearray object, of from scratch.
        """
        super().__init__(raw)

        if raw:
            self.__primary = raw[8] << 8 | raw[9]
        else:
            self.__primary = 0

    def _get_raw(self, raw=None):
        if not raw:
            raw = bytearray(10)
        raw = super()._get_raw(raw)

        raw[8] = self.__primary >> 8
        raw[9] = self.__primary & 0x0FF
        return raw

    def __str__(self):
        """Report a summary of this object."""
        return 'Alias to {0}: {1}'.format(
            self.__primary if self.__primary != 0xFFFF else 'None',
            super().__str__()
        )

    def __set_primary(self, v):
        if isinstance(v, pylon.device.interface.Datapoint):
            v = v.index

        self.__primary = self._in_range(
            'Primary index', v, 0, pylon.device.stack.MAX_DATAPOINTS-1, 0x0FFFF
        )

    primary = property(
        lambda self: self.__primary,
        __set_primary,
        None, """Primary datapoint index.

        Manages the index of the primary datapoint of this alias. When reading,
        this property returns a datapoint index number. When writing, you can
        write a datapoint index number, or assign the datapoint object.
    """)


class System:

    def __init__(self, stack, application):
        self.__stack = stack
        self.__app = application

    #
    #   Status
    #
    def __set_status(self, v):
        if not v:
            self.__stack.clear_status()
        else:
            raise AttributeError(
                'Only None can be assigned to clear the status'
            )

    status = property(
        lambda self: Status(self.__stack.query_status()),
        __set_status,
        None, """Returns the system status and statistics object.
        Assignment of None or any other False expression to this property
        clears the statistics.
    """)

    #
    #   State and mode changes
    #
    def go_online(self):
        self.__stack.set_node_mode(
            NodeMode.ONLINE,
            NodeState.INVALID
        )

    def go_offline(self):
        self.__stack.set_node_mode(
            NodeMode.OFFLINE,
            NodeState.INVALID
        )

    def go_configured(self):
        self.__stack.set_node_mode(
            NodeMode.CHANGESTATE,
            NodeState.CONFIGURED_ONLINE
        )

    def go_unconfigured(self):
        self.__stack.set_node_mode(
            NodeMode.CHANGESTATE,
            NodeState.UNCONFIGURED
        )

    #
    #   Local domain table access
    #
    def query_domain(self, index):
        """Return a Domain object for the domain with the given index."""
        return Domain(
            self.__stack.query_domain(index)
        )

    def update_domain(self, index, domain):
        """Assign a Domain object to the domain with the given index."""
        if isinstance(domain, Domain):
            self.__stack.update_domain(
                index,
                domain._get_raw()
            )
            logger.info(
                'Updated domain {0} to {1}'.format(
                    index,
                    domain
                )
            )
        else:
            raise TypeError(
                'Expected an instance of Domain'
            )

    #
    #   Local address table access
    #
    def query_address(self, index):
        """Return an address object for the given index.

        Return one of several types of address objects for the given index.
        The tool returns a GroupAddress, SubnetNodeAddress, BroadcastAddress,
        TurnaroundAddress or UnusedAddress object.
        """
        raw = self.__stack.query_address(index)
        if raw[0] & 0x80:
            return GroupAddress(raw)
        elif raw[0] == AddressType.SUBNETNODE:
            return SubnetNodeAddress(raw)
        elif raw[0] == AddressType.BROADCAST:
            return BroadcastAddress(raw)
        elif raw[0] == AddressType.UNBOUND:
            if raw[1]:
                return TurnaroundAddress(raw)
            else:
                return UnusedAddress(raw)
        else:
            raise toolkit.PylonApiError(
                toolkit.PylonApiError.NOT_IMPLEMENTED,
                'Address type {0}'.format(raw[0])
            )

    def update_address(self, index, address):
        """Assign an Address object to the given address table index.

        The address object must be one of the possible result objects of
        the query_address() method.
        """
        if not isinstance(address, Address):
            raise TypeError(
                'Expect instance of Address'
            )
        self.__stack.update_address(
            index,
            address._get_raw()
        )
        logger.info(
            'Updated address {0} to {1}'.format(
                index,
                address
            )
        )

    #
    #   Local datapoint configuration table access
    #
    def query_datapoint_config(self, dp):
        """Return DatapointConfig object given the datapoint or its index."""

        if isinstance(dp, pylon.device.interface.Datapoint):
            dp = dp.index
        return DatapointConfig(
            raw=self.__stack.query_datapoint_config(dp)
        )

    def update_datapoint_config(self, dp, config):
        """Assign a DatapointConfig object.

        Assign a DatapointConfig object to the given datapoint configuration
        table index, given the datapoint object or its index.
        """
        if isinstance(dp, pylon.device.interface.Datapoint):
            dp = dp.index
        if not isinstance(config, DatapointConfig):
            raise TypeError(
                'Expect instance of DatapointConfig'
            )
        self.__stack.update_datapoint_config(
            dp,
            config._get_raw()
        )
        logger.info(
            'Updated datapoint config {0} to {1}'.format(
                dp,
                config
            )
        )

    #
    #   Local alias table access
    #
    def query_alias_config(self, index):
        """Return an AliasConfig object given its index."""
        return AliasConfig(
            raw=self.__stack.query_alias_config(index)
        )

    def update_alias_config(self, index, config):
        """Assign an AliasConfig object to the alias table given its index."""
        if not isinstance(config, DatapointConfig):
            raise TypeError(
                'Expect instance of AliasConfig'
            )
        self.__stack.update_alias_config(
            index,
            config._get_raw()
        )
        logger.info(
            'Updated alias {0} to {1}'.format(
                index,
                config
            )
        )
