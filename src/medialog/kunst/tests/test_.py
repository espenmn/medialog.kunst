# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from medialog.kunst.interfaces import I
from medialog.kunst.testing import MEDIALOG_KUNST_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class IntegrationTest(unittest.TestCase):

    layer = MEDIALOG_KUNST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='')
        schema = fti.lookupSchema()
        self.assertEqual(I, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(I.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='',
            id='',
        )
        self.assertTrue(I.providedBy(obj))
