*** Settings ***
Library    Selenium2Library
Library    BuiltIn
Library    String
Library    DateTime
###TODO : Library
Library    ../CommonLib/lineNotification.py
Library    ../CommonLib/spreadsheetConnector.py
Library    ../CommonLib/googleDrive.py
###TODO : Configuration
Resource  ../Config/facebook_config.txt
Resource  ../Keyword/automation_keyword.robot

Documentation       A test suite with a single test for valid login.

*** Test Cases ***
Scenario From GoogleSheet
  ${row}    Set Variable    row
  ${info_para} =  getGoogleSheetBySheetIndex       ${google_doc}       ${2}
  ${cnt} =  Get Length  ${info_para}

    : FOR    ${INDEX}    IN RANGE    1    ${cnt}
#       \  log to console   \nRemark=${kw_Flag},${info_para}[${INDEX}][${3}]
#       \  Run Keyword If	 '${kw_Flag}'=='${info_para}[${INDEX}][${3}]'     ${info_para}[${INDEX}][${4}]   ${info_para}[${INDEX}][${2}]
        \  Run Keyword If	 '${kw_Flag}'=='${info_para}[${INDEX}][${3}]'     Run Keyword And Ignore Error     ${info_para}[${INDEX}][${4}]   ${info_para}[${INDEX}][${2}]   ELSE       log      [KW:exception-case]


