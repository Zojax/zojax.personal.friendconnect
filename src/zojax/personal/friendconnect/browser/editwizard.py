##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
from zope import component

from zojax.layoutform import Fields, PageletEditSubForm

from zojax.personal.friendconnect.interfaces import IContentPersonalFriendConnect, IPersonalFriendConnectConfiglet


class TagsEditForm(PageletEditSubForm):

    prefix = 'personal.tags'

    fields = Fields(IContentPersonalFriendConnect)

    def getContent(self):
        return component.getMultiAdapter((self.context, self.request.principal), IContentPersonalFriendConnect)

    def isAvailable(self):
        return not component.getUtility(IPersonalFriendConnectConfiglet).useGlobalTags
