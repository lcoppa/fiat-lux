"""
    SNVT_obj_status
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

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_obj_status(base.Structure):
    """SNVT_obj_status standard datapoint type.

    Object status (ID, status flags).

    Used to indicate the status of the various objects within a node. For more
    details, see the definition of the Node Object (SFPTnodeObject).

    Addition found in version 3.3 and later:

    The reset_complete field, indicates the execution of the Reset sequence of
    any object (object_id) within the device. After a Reset sequence, the
    reset_complete flag goes to TRUE (1) and it remains ‘1’ until it is cleared
    (acknowledged) via SNVT_obj_request (nviRequest in the Node Object) on in
    the corresponding Object (object_id ).

    Note:The additional reset flag uses reserved1 of the previous
    SNVT_obj_status structure definition.

    This implementation of the SNVT_obj_status type does not support
    initialization of the flags with the constructor. If you need to initialize
    with non-zero flags, instantiate the item and set the individual flags as
    necessary. Alternatively, provide a 32-bit combined bitvector with the
    constructor.
    """

    def __init__(self, object_id=0, flags=0):
        """
        Creates SNVT_obj_status.
        """
        super().__init__(
            key=93,
            scope=0
        )
        self._definition = standard.add(self)

        self.__object_id = base.Scaled(
            size=2,
            signed=False,
            default=object_id
        )
        self._register(('object_id', self.__object_id))

        self.__flags = base.Scaled(
            size=4,
            signed=False,
            default=flags
        )
        self._register(('flags', self.__flags))

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
        if not isinstance(v, SNVT_obj_status):
            raise TypeError('Expected instance of SNVT_obj_status, '
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
        """Supports combining multiple SNVT_obj_status objects into one.
        This is used to report the OR'ed status flags of multiple blocks.
        """
        if not isinstance(other, SNVT_obj_status):
            raise TypeError('Can only combine SNVT_obj_status objects')
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
