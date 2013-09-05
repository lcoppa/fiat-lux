"""
    SNVT_obj_request
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

from pylon.resources.object_request_t import object_request_t


class SNVT_obj_request(base.Structure):
    """SNVT_obj_request standard datapoint type.

    Object request  (ID, request).

    Allows a functional block to be placed in one of several functional modes.
    For more details, see the definition of the Node Object (SFPTnodeObject)
    functional profile.

    Additions found in version 3.3 and later:

    The RQ_CLEAR_RESET request clears the reset_complete flag in
    SNVT_obj_status (nvoStatus in the Node Object) of the corresponding Object
    (object_id). Further requests have no effect, until the next Reset sequence
    has again been executed.

    The RQ_RESET request initiates the Reset sequence in SNVT_obj_status
    (nvoStatus in the Node Object) of the corresponding object (object_id)
    every time that it is sent. The reset_complete flag (SNVT_obj_status) is
    set when the Reset sequence is complete, and the flag must be cleared by
    RQ_CLEAR_RESET (SNVT_obj_request).

    The existing RQ_CLEAR_STATUS and RQ_CLEAR_ALARM functions
    (SNVT_obj_request) remain unchanged.
    """

    def __init__(self, object_id=0, object_request=object_request_t.RQ_NUL):
        super().__init__(
            key=92,
            scope=0
        )
        self._definition = standard.add(self)

        self.__object_id = base.Scaled(
            size=2,
            signed=False,
            default=object_id
        )
        self._register(('object_id', self.__object_id))

        self.__object_request = object_request_t(
            default=object_request
        )
        self._register(('object_request', self.__object_request))

    def __set_object_id(self, v):
        self.__object_id._value = v

    object_id = property(
        lambda self: self.__object_id._value,
        __set_object_id,
        None, """
        Object ID (object index).
        """
    )

    def __set_object_request(self, v):
        self.__object_request._value = v

    object_request = property(
        lambda self: self.__object_request._value,
        __set_object_request,
        None, """
        Object request (object request names).
        """
    )

    def __set(self, v):
        if not isinstance(v, SNVT_obj_request):
            raise TypeError('Expected instance of SNVT_obj_request, '
                            'got {0}'.format(
                                type(v)
                            ))
        self.__set_object_id(v.__object_id)
        self.__set_object_request(v.__object_request)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Returns the length of the data type, in bytes."""
        # No need to compute at runtime, as the size is fixed.
        return 3
