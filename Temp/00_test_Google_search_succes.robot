*** Settings ***
Documentation   This is a simple test with Robot Framework
Library    Selenium2Library
Library    BuiltIn
Library    String
Library    Screenshot
Library    OperatingSystem

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://www.google.co.th/
${Browser}  chrome
${TYPE OF FILE}    png
${filename}       C:/Project/Selenium_Project02/testResult/shot01_google

*** Keywords ***

*** Test Cases ***
1. Open web google
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3

2. Search Robot Framework
   Input Text  name=q  Robot Framework

3. Click button
   Click Button  name=btnK

4. click Robot Framework
   Click Element  //h3[@class="LC20lb"]

5. Checking result
   ${result}  Get Text  //h1[@class="main-header"]
   Log To Console  ${result}
   Should Be Equal  ${result}  ${expect}

6. Capture result
   Capture Page Screenshot  ${filename}.${TYPE OF FILE}

7. log out
    Close Browser


