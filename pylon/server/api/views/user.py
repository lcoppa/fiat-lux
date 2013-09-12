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
Pilon IP-C Server REST API Device view.
"""

__version__ = "$Revision: #7 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/views/user.py $


from django.contrib.auth.models       import User

from rest_framework                   import permissions, viewsets

from api.serializers.user             import UserSerializer

__all__ = ['UserViewSet']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the **users** in the system.
       
    **NOTE:**  You must be logged in to view users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)     # IsAdminUser

#     def get_queryset(self):
#         user = self.request.user
#         if user and user.is_active and user.is_staff:
#             return User.objects.all()
#         return User.objects.filter(username=user.username)
        
#     # CreateModelMixin override(s)
#     def create(self, request, *args, **kwargs):
#         return super().create(self, request, *args, **kwargs)
# 
#     # ListModelMixin override(s)
#     def list(self, request, *args, **kwargs):
#         return super().list(self, request, *args, **kwargs)
# 
#     # RetrieveModelMixin override(s)
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(self, request, *args, **kwargs)
# 
#     # UpdateModelMixin override(s)
#     def update(self, request, *args, **kwargs):
#         return super().update(self, request, *args, **kwargs)
# 
#     # DestroyModelMixin override(s)
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(self, request, *args, **kwargs)
