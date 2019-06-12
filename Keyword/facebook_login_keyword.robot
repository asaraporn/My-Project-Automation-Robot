*** Settings ***
Library    Selenium2Library
Library    BuiltIn
Library    String
Library    DateTime
###TODO : Line-Lib
Library    ../CommonLib/lineNotification.py
###TODO : GoogleSheet Connector
Library    ../CommonLib/spreadsheetConnector.py
###TODO : Looger
Library    ../CommonLib/logger.py
###TODO : config
Resource  ../Config/facebook_config.txt

*** Keywords ***
User Name config
     [Arguments]     @{arg}

My Logging
    [Arguments]     @{arg}
    log many  @{arg}

Verify facebook page
    [Arguments]               ${title}
    Title Should Be            ${title}


Click Button Login
     [Arguments]       ${btn}
     Element Should Be Visible    ${btn}
     Click Element        ${btn}

Verify Login Fail
   [Arguments]        ${xpath}
   Element Should Be Visible        ${xpath}

Verify Login Success
   [Arguments]        ${xpath}
   Element Should Be Visible        ${xpath}

Open chrom set option
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    Maximize Browser Window


Open google drive
     ${googleSheetName} = ${login_user_doc}

Input Username and Password
     [Arguments]      ${xpath_user}       ${xpath_pass}     ${username}       ${password}
     Element Should Be Visible    ${xpath_user}
     Element Should Be Visible    ${xpath_pass}
     Input Text       ${xpath_user}       ${username}
     Input Text       ${xpath_pass}       ${password}


Go to my page
     [Arguments]      ${xpath_home}     ${xpath_home_page}
    Click Element     ${xpath_home}
    Wait Until Element Is Visible     ${xpath_home_page}    timeout=30


Check Noticication
     Click Element     ${link_noti}


Post message in facebook
        [Arguments]    ${xpath_home_page}        ${xpath_post}      ${txtMyStatus}
	    Input Text     ${xpath_post}    ${txtMyStatus}






