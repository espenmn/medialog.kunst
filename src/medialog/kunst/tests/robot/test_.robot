# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.kunst -t test_.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.kunst.testing.MEDIALOG_KUNST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a 
  Given a logged-in site administrator
    and an add  form
   When I type 'My ' into the title field
    and I submit the form
   Then a  with the title 'My ' has been created

Scenario: As a site administrator I can view a 
  Given a logged-in site administrator
    and a  'My '
   When I go to the  view
   Then I can see the  title 'My '


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add  form
  Go To  ${PLONE_URL}/++add++

a  'My '
  Create content  type=  id=my-  title=My 


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the  view
  Go To  ${PLONE_URL}/my-
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a  with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the  title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
