# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.kunst


class MedialogKunstLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=medialog.kunst)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.kunst:default')


MEDIALOG_KUNST_FIXTURE = MedialogKunstLayer()


MEDIALOG_KUNST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_KUNST_FIXTURE,),
    name='MedialogKunstLayer:IntegrationTesting'
)


MEDIALOG_KUNST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_KUNST_FIXTURE,),
    name='MedialogKunstLayer:FunctionalTesting'
)


MEDIALOG_KUNST_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_KUNST_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MedialogKunstLayer:AcceptanceTesting'
)
