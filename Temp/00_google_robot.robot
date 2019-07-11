*** Settings ***
Library    Selenium2Library

*** Variables ***
${BROWSER}    chrome


*** Keywords ***


*** Testcases ***
Hello
    Open Browser    http://www.google.com   browser=${BROWSER}