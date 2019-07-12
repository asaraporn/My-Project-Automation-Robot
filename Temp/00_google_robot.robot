*** Settings ***
Library      Selenium2Library
Library      XvfbRobot

*** Variables ***

*** Keywords ***

*** Test Cases ***
Create Headless Browser
    Open Browser   http://google.com
    Set Window Size    1920    1080
    ${title}=    Get Title
    Should Be Equal    Google    ${title}
    [Teardown]    Close Browser