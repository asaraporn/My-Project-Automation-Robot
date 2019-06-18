*** Keywords ***
passing parameters
     [Arguments]     ${arg}
     # split string bt comma
     ${result} =     split string        ${arg}      ,
     [Return]    ${result}

[KW]MyKeyWord
    [Arguments]        ${arg}
    log to console     ${arg}

[KW]Open web
    [Arguments]        ${arg}
    Open Browser  ${arg}    chrome
    Maximize Browser Window
    Set Selenium Speed      0.3

[KW]Click Target Link
     [Arguments]        ${arg}
     log to console     ${arg}
     Click Element      ${arg}

[KW]Capture Screenshot
     [Arguments]        ${arg}
     Capture Page Screenshot        ${arg}

[KW]Send Image via Line
     [Arguments]        ${arg}
     notifyImageFile    ${arg}

[KW]Send text via Line
     [Arguments]        ${arg}
     lineNotify         ${arg}

[KW]Verify web page
     [Arguments]        ${arg}
     Title Should Be    ${arg}

[KW]Close web
    [Arguments]        ${arg}
    Close Browser


[KW]Select List by value
    [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console      \nField=${result}[${0}]
#     log to console      \nValue=${result}[${1}]
     Click Element   ${result}[${0}]
     Select From List by Value    ${result}[${0}]    ${result}[${1}]

[KW]Select List by index
    [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console      \nField=${result}[${0}]
#     log to console      \nValue=${result}[${1}]
     Click Element   ${result}[${0}]
     Select From List by Index   ${result}[${0}]    ${result}[${1}]

[KW]Select Radio Button
     [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console      \nField=${result}[${0}]
#     log to console      \nValue=${result}[${1}]
    Select Radio Button     ${result}[${0}]     ${result}[${1}]


[KW]Input Text
    [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console      \nField=${result}[${0}]
#     log to console      \nValue=${result}[${1}]
     Input Text     ${result}[${0}]       ${result}[${1}]

[KW]Click Button
     [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console    \nField=${result}[${0}]
     Click Element     ${result}[${0}]











