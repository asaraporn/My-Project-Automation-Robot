*** Settings ***
Library    Selenium2Library
Library    BuiltIn
Library    String
Library    DateTime
###TODO : Line-Lib
Library    ../CommonLib/lineNotification.py
###TODO : GoogleSheet Connector
Library    ../CommonLib/spreadsheetConnector.py
Resource  ../Config/facebook_config.txt
Documentation     A test suite with a single test for valid login.

*** Test Cases ***
Scenario From GoogleSheet
  ${row}    Set Variable    row
  ${info_para} =  get_data_googleDrive_atSheet2       ${google_doc}       ${3}
  ${cnt} =  Get Length  ${info_para}
    : FOR    ${INDEX}    IN RANGE    1    ${cnt}
        \  Run Keyword If	    '1' == '1'      ${info_para}[${INDEX}][${1}]   ${info_para}[${INDEX}][${2}]


*** Keywords ***
[KW]MyKeyWord
    [Arguments]        ${arg}
    log to console     ${arg}

[KW]Open Browser To Open web
    [Arguments]        ${arg}
    Open Browser  ${arg}    chrome
    Maximize Browser Window
    Set Selenium Speed      0.3

[KW]Click Target Link
     [Arguments]        ${arg}
     log to console     ${arg}
     Click Element      ${arg}


[KW]Screenshot
     [Arguments]        ${arg}
     Capture Page Screenshot        ${arg}


[KW]Send Line Notification
     [Arguments]        ${arg}
     notifyImageFile    ${arg}


[KW]Verify web page
     [Arguments]        ${arg}
     Title Should Be    ${arg}


[KW]Close your browser
    [Arguments]        ${arg}
    Close Browser

Get Scenario From GoogleSheet
  ${row}    Set Variable    row
  ${info_para} =  get_data_googleDrive_atSheet2       ${google_doc}       ${3}
  ${cnt} =  Get Length  ${info_para}
    : FOR    ${INDEX}    IN RANGE    1    ${cnt}
        \  Run Keyword If	    '1' == '1'      ${info_para}[${INDEX}][${1}]   ${info_para}[${INDEX}][${2}]