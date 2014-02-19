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
from zope import interface, component
from zope.component import getUtility

from z3c.form import converter
from z3c.form.browser import text
from z3c.form.widget import FieldWidget
from z3c.form.interfaces import IFormLayer, IFieldWidget

from zojax.personal.friendconnect.interfaces import IPersonalFriendConnect
from interfaces import IPersonalFriendConnectWidget


class PersonalFriendConnectWidget(text.TextWidget):
    interface.implements(IPersonalFriendConnectWidget)

    klass = u'z-widget-personal-tags'

    def popularTags(self):
        engine = IPersonalFriendConnect(self.request.principal).engine

        idx = 1
        tags = []
        for weight, tag in engine.getTagCloud(True):
            tags.append(tag)
            if idx == 10:
                break
            idx += 1

        return tags


class PersonalFriendConnectWidgetConverter(converter.BaseDataConverter):
    component.adapts(PersonalFriendConnectWidget)

    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return u''
        return u', '.join(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        res = []
        for tag in (v for v in (v.strip() for v in value.split(',')) if v):
            if tag not in res:
                res.append(tag)
        return tuple(res)


@interface.implementer(IFieldWidget)
@component.adapter(IFormLayer)
def PersonalFriendConnectFieldWidget(field, request):
    return FieldWidget(field, PersonalFriendConnectWidget(request))
