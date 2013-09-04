"""A simple event class for pilon.

This module defines a simple event handler mechanism for use with the
pilon module. The principal class defined in this module is SimpleEvent.
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

from pylon.device import toolkit


class EventArgs:
    """EventArgs is the base class of all event arguments.

    EventArgs is the base class for the argument type used with SimpleEvent.
    Most events will use an event type derived from EventArgs.
    """

    def __init__(self, doc=None):
        self.__doc__ = doc


class SimpleEvent:
    """Event class for most pilon events.

    The simple event class is used to manage event handlers at the event
    source (the publisher). Event subscribers can register their event
    handlers using the += notation, and remove event handlers with -=.
    All event handlers used with this class have the same prototype, the
    sender object and an event-specific parameter (which may be None, or
    must be derived from EventArgs.

    While most events support unlimited subscribers, individual events may
    limit the number of registered handlers (typically to 1) using the 'limit'
    argument to this class' constructor.
    """

    def __init__(self, limit, doc=None):
        """Create a SimpleEvent object.

        Arguments:

        limit: specifies the maximum number of supported handlers for this
        event, defaults to 0 (zero) for no explicit limit.

        doc: docstring for this event.
        """

        self.__doc__ = doc
        self.__limit = limit
        self.__handlers = []

    def add(self, handler):
        """Subscribe a handler to this event.

        Subscribe to the event by adding your handler using add(), or use the
        += operator. All SimpleEvent handlers must accept two arguments, a
        sender object which typically provides access to the object which
        triggered the event, and an arguments object which is None, or an
        object derived from EventArgs with additional data.

        Arguments:

        handler: your handler for this event
        """

        if not self.__limit or len(self.__handlers) < self.__limit:
            self.__handlers.append(handler)
        else:
            raise toolkit.PylonLimitError(
                toolkit.PylonLimitError.TOO_MANY_SUBSCRIBERS,
                '{0} supports only {1} subscriber'.format(
                    type(self), self.__limit
                )
            )
        return self

    def remove(self, handler):
        """Remove handler from this event object."""
        self.__handlers.remove(handler)
        return self

    def reset(self):
        """Remove all handlers from this event object."""
        self.__handlers = []

    def fire(self, sender, argument=None):
        """Fire the event by executing all registered handlers."""
        for handler in self.__handlers:
            handler(sender, argument)

    __iadd__ = add      # override for the  += operator
    __isub__ = remove   # override for the -= operator

