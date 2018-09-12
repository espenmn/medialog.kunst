# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from medialog.kunst.testing import MEDIALOG_KUNST_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.kunst is properly installed."""

    layer = MEDIALOG_KUNST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.kunst is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.kunst'))

    def test_browserlayer(self):
        """Test that IMedialogKunstLayer is registered."""
        from medialog.kunst.interfaces import (
            IMedialogKunstLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMedialogKunstLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_KUNST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.kunst'])

    def test_product_uninstalled(self):
        """Test if medialog.kunst is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.kunst'))

    def test_browserlayer_removed(self):
        """Test that IMedialogKunstLayer is removed."""
        from medialog.kunst.interfaces import \
            IMedialogKunstLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IMedialogKunstLayer,
           utils.registered_layers())
