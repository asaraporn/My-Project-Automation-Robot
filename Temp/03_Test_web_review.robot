*** Settings ***
Documentation   This is a simple test with Robot Framework
Library    Selenium2Library
Library    BuiltIn
Library    String
Library    Screenshot
Library    OperatingSystem
###TODO : Library
Library    ../CommonLib/lineNotification.py
Library    ../CommonLib/spreadsheetConnector.py
Library    ../CommonLib/googleDrive.py

*** Variables ***
${expect}       AddTechHub
${url}          https://www.reviewyourliving.com/
${Browser}      chrome
${TYPE OF FILE}     png
${filename}         Screenshot/shot_

${expect}            Powered by AddTechHub
*** Keywords ***
Close web
   Close Browser

Open Link
    [Arguments]     ${arg}
    ${contents}=  Get File          ${arg}
    @{lines}=   Split to lines      ${contents}
          :FOR  ${line}  IN  @{lines}
               \ log to console   ${line}


*** Test Cases ***
1. Open Browser To Open web
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3


2. Capture Web Page
   Capture Page Screenshot  ${filename}2.${TYPE OF FILE}

3. View Page Source
#    ${result}  Get Text  //h1[@class="header-logXXX"]
    ${text}     Get Text  //h1[@class="header-logo"]
    ${source}   Get source
    Create File     ${CURDIR}/ReviewYourLiving.html         ${source}

4. Generator log file
    log to console       ${CURDIR}
    ${result_grep} =      grep file       ${CURDIR}/ReviewYourLiving.html       src="*
    append to file        ${CURDIR}/target_link.log       ${result_grep}

5. Testing CommonLib
#     lineNotify     HelloWorld
     uploadToGoogleDrive        ${CURDIR}/target_link.txt


6. Log out
     Close web



