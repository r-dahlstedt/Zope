##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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

import unittest
import transaction


class DoomedTransactionInManagerTest(unittest.TestCase):

    def testDoomedFails(self):
        transaction.begin()
        trans = transaction.get()
        trans.doom()
        from transaction.interfaces import DoomedTransaction
        self.assertRaises(DoomedTransaction, trans.commit)

    def testDoomedSilentInTM(self):
        from Zope2.App.startup import TransactionsManager
        tm = TransactionsManager()
        transaction.begin()
        trans = transaction.get()
        trans.doom()
        tm.commit()
