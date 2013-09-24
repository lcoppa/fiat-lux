"""SNVT_log_fx_status standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_log_fx_status(base.Structure):
    """SNVT_log_fx_status standard datapoint type.  Log file transfer
    status.  Reports the status of a data log file transfer using FTP.
    Required on devices implementing the Data Logger functional profile that
    support data log transfer via FTP."""

    def __init__(self):
        super().__init__(
            key=194,
            scope=0
        )

        self.__requestor_subnet = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('requestor_subnet', self.__requestor_subnet))

        self.__requestor_node = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('requestor_node', self.__requestor_node))

        self.__log_number = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('log_number', self.__log_number))

        self.__complete = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.5, 0),
            invalid=127.5,
            minimum=0,
            maximum=100
        )
        self._register(('complete', self.__complete))
        self._definition = standard.add(self)


    def __set_requestor_subnet(self, v):
        self.__requestor_subnet._value = v

    requestor_subnet = property(
        lambda self: self.__requestor_subnet._value,
        __set_requestor_subnet,
        None,
        """Requestor subnet ID.  Subnet ID of the device that requested the
        current log file transfer.  Invalid if a file transfer is not
        active."""
    )

    def __set_requestor_node(self, v):
        self.__requestor_node._value = v

    requestor_node = property(
        lambda self: self.__requestor_node._value,
        __set_requestor_node,
        None,
        """Requestor node ID.  Node ID of the device that requested the
        current log file transfer.  Invalid if a file transfer is not
        active."""
    )

    def __set_log_number(self, v):
        self.__log_number._value = v

    log_number = property(
        lambda self: self.__log_number._value,
        __set_log_number,
        None,
        """Data log number.  Log number for the log file currently being
        transferred via FTP.  Invalid if none."""
    )

    def __set_complete(self, v):
        self.__complete._value = v

    complete = property(
        lambda self: self.__complete._value,
        __set_complete,
        None,
        """Data log file transfer percent complete.  Percent of the current
        data log file transfer that has been completed.  Invalid if none."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_requestor_subnet(v.__requestor_subnet)
        self.__set_requestor_node(v.__requestor_node)
        self.__set_log_number(v.__log_number)
        self.__set_complete(v.__complete)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SNVT_log_fx_status()
    pass
