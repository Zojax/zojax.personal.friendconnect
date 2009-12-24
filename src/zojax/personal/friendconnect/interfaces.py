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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory

from zojax.content.friendconnect.interfaces import IContentTaggable, IContentTags
from zojax.content.space.interfaces import IWorkspace, IWorkspaceFactory

from field import PersonalFriendConnectField

_ = MessageFactory('zojax.personal.friendconnect')


class IPersonalFriendConnect(interface.Interface):
    """ personal friend connect """


class IPersonalFriendConnectConfiglet(interface.Interface):
    """Personal friend connect configlet """


class IPersonalFriendConnectWorkspace(IWorkspace):
    """ friend connect workspace """


class IPersonalFriendConnectWorkspaceFactory(IWorkspaceFactory):
    """ friend connect workspace factory """
