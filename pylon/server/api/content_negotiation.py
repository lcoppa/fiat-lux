#
# Copyright (c) 2013 Echelon Corporation.  All rights reserved.
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

"""
Pilon IP-C Server REST API content type negotiation.


Overrides 'DefaultContentNegotiation' to fully negotiate
the content type with respect to q-factor and precedence.
"""

__version__ = "$Revision: #5 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/content_negotiation.py $


import logging
import re

from rest_framework                  import exceptions
from rest_framework.negotiation      import DefaultContentNegotiation
from rest_framework.utils.mediatypes import media_type_matches
from rest_framework.utils.mediatypes import _MediaType

from shared                          import NAMESPACE


# our logger
logger = logging.getLogger(NAMESPACE('api.content_negotiation'))


# (compiled) regular expression to match all 'accept-params'
# and capture the q-factor, if present
RE_ACCEPT_PARAMS = re.compile(r'\s*;\s*q\s*=\s*(?P<q>\d*(\.\d*)?)(;.*)?')


def remove_accept_params(media_type):
    """
    Removes 'accept-params' (especially 'q' params) from the 'media_type'.
    See <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.
    """
    return re.sub(RE_ACCEPT_PARAMS, '', media_type)


def q_factor(media_type):
    match = re.search(RE_ACCEPT_PARAMS, media_type)
    if not match:
        return 1.0
    return float(match.group('q'))


def order_by_q_and_precedence(media_type_lst):
    """
    Returns an ordered list of lists of media type strings,
    ordered by q-factor and then by precedence.  Input order
    is preserved for media types with the same q-factor and precedence.
    Precedence is determined by how specific a media type is:

    3. 'type/subtype; param=val'
    2. 'type/subtype'
    1. 'type/*'
    0. '*/*'
    """
    ret = {}
    for media_type in media_type_lst:
        q = q_factor(media_type)
        media_type = remove_accept_params(media_type)
        precedence = _MediaType(media_type).precedence
        
        if not q in ret:
            # create a new list of lists for this new q-factor
            ret[q] = [[], [], [], []]
        ret[q][3 - precedence].append(media_type)
        
    return [media_types for q in sorted(ret, reverse=True) for media_types in ret[q] if media_types]


class ContentNegotiation(DefaultContentNegotiation):
    """
    Overrides 'DefaultContentNegotiation' to fully negotiate the content type
    with respect to q-factor and precedence.
    """
    def select_renderer(self, request, renderers, format_suffix=None):
        """
        Given a request and a list of renderers, return a two-tuple of:
        (renderer, media type).
        """
        # trace the accepted/overridden formats
        logger.debug('HTTP_ACCEPT: "%s", URL_ACCEPT_OVERRIDE: "%s", URL_FORMAT_OVERRIDE: "%s"',
                     request.META.get('HTTP_ACCEPT'),
                     request.QUERY_PARAMS.get(self.settings.URL_ACCEPT_OVERRIDE),
                     request.QUERY_PARAMS.get(self.settings.URL_FORMAT_OVERRIDE))
        
        # Allow URL style format override.  eg. "?format=json
        format_query_param = self.settings.URL_FORMAT_OVERRIDE
        fmt = format_suffix or request.QUERY_PARAMS.get(format_query_param)

        if fmt:
            renderers = self.filter_renderers(renderers, fmt)

        accepts = self.get_accept_list(request)

        # Check the acceptable media types against each renderer,
        # attempting more desirable media types first.
        for media_type_set in order_by_q_and_precedence(accepts):
            for media_type in media_type_set:
                for renderer in renderers:
                    if media_type_matches(renderer.media_type, media_type):
                        # Return the most specific media type as accepted.
                        if (_MediaType(renderer.media_type).precedence >
                            _MediaType(media_type).precedence):
                            # Eg client requests '*/*'
                            # Accepted media type is 'application/json'
                            return renderer, renderer.media_type
                        else:
                            # Eg client requests 'application/json; indent=8'
                            # Accepted media type is 'application/json; indent=8'
                            return renderer, media_type

        raise exceptions.NotAcceptable(available_renderers=renderers)
