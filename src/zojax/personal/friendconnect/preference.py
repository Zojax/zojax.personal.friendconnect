##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from rwproperty import getproperty, setproperty

from zope import interface
from zope.security.interfaces import IPrincipal
from zope.security.proxy import removeSecurityProxy
from zope.component import getUtility, adapts

from interfaces import IPersonalFriendConnect, IPersonalFriendConnectConfiglet


class BasePersonalFriendConnect(object):
    pass


class PersonalFriendConnect(BasePersonalFriendConnect):
    interface.implements(IPersonalFriendConnect)

