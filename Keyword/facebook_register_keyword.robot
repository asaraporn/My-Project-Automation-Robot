*** Settings ***
Library    Selenium2Library
Library    BuiltIn
Library    String

Library    DateTime
Library    OperatingSystem
Library    Collections
Library    os
#Library    openpyxl

###TODO : Line-Lib
Library    ../CommonLib/lineNotification.py
###TODO : GoogleSheet Connector
Library    ../CommonLib/spreadsheetConnector.py
###TODO : Looger
Library    ../CommonLib/logger.py
###TODO : config
Resource  ../Config/facebook_config.txt
Resource  ../Config/facebook_register_config.txt


*** Keywords ***
create file grep log
    create file     ${log_filename}Register.txt
    ${respone} =   grep file    ./TestResult/LOG-registerFacebook-cmd.log      START TEST
        Log To Console  \n respones >>>>>  ${respone}
    append to file  =   ${log_filename}Register.txt         ${respone}



Test Load Data Excel
    ${wb}    Load Workbook   ${CURDIR}//TestData//${excel}
    ${ws}    Set Variable    ${wb.get_sheet_by_name('Login')}
    ${cell}  Set Variable    ${ws.cell(2,2).value}
    ${body}  Fetch From Right    ${cell}    {}
    Log To Console  \n\n${body}\n


Test Write Excel
    ${wb}    Load Workbook   ${CURDIR}/${excel}
    Log To Console   ${wb}
    ${ws}    Set Variable    ${wb['Result']}
    Log To Console   ${ws}
    evaluate    $ws.cell(1,1,'${data}')
    evaluate    $wb.save('${excel}')




