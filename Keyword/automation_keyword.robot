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

[KW]Select List by value
    [Arguments]     @{arg}
#    Click Element   ${combo_box_day}
#    Select From List by Value    ${combo_box_day}    ${arg[0]}
    log to console      \n@{arg}
    log to console      \n${arg[0]}

