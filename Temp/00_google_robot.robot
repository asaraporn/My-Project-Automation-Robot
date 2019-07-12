*** Settings ***
Library    Selenium2Library

*** Variables ***
${BROWSER}    chrome


*** Keywords ***


*** Test Cases ***
Hello
    Open Browser    http://www.google.com   browser=${BROWSER}