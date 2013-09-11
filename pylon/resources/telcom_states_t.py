"""telcom_states_t standard enumeration type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class telcom_states_t(base.Enumeration):
    """telcom_states_t standard enumeration."""

    # Invalid Value.
    TEL_NUL = -1

    # "Null State (U0)" not in use.
    TEL_NOTINUSE = 0

    # "Call Initiated (U1)".
    TEL_OFFHOOK = 1

    # "Overlap Sending (U2)".
    TEL_DIALING = 2

    # "Outgoing Call Proceeding (U3)".
    TEL_DIALCOMP = 3

    # "Call Delivered (U4)" hearing ringback.
    TEL_RINGBACK = 4

    # "Call Present (U6)" incoming call has not yet started ringing (only on
    # ISDN line).
    TEL_INCOMING = 5

    # "Call Received (U7)" incoming call when the user has indicated alerting
    # but has not yet answered.
    TEL_RINGING = 6

    # "Connect Request (U8)" user has answered the call and is waiting to be
    # awarded the call.
    TEL_ANSWERED = 7

    TEL_CONNECTED = 8

    # "Active (U10)" two parties are exchanging data.
    TEL_TALKING = 9

    # "Disconnect Request (U11)" user has hung up.
    TEL_HANGINGUP = 10

    # "Disconnect Indication (U12)" the other side hung up.
    TEL_HUNGUPX = 11

    # "Suspend Request (U15)" user has requested the network suspend the
    # call.
    TEL_HOLD = 12

    # "Resume Request (U17)" resume a held call (usually go back to
    # TEL_TALKING).
    TEL_UNHOLD = 13

    # "Release Request (U19)" user has requested the network to release.
    TEL_RELEASE = 14

    # "Overlap Receiving (U25)" user has acknowledged the call and is
    # prepared to receive additional.
    TEL_FULLDUP = 15

    # connection with blocking, (call-waiting disabled).
    TEL_BLOCKED = 16

    # call-waiting coming in.
    TEL_CWAIT = 17

    # destination busy.
    TEL_DESTBUSY = 18

    # problem, network.
    TEL_NETBUSY = 19

    # problem, non-network.
    TEL_ERROR = 20

    def __init__(self):
        super().__init__(
            key=3,
            scope=0,
            prefix='TEL_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = telcom_states_t()
    pass
