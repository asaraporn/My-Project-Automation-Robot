*** Keywords ***
passing parameters
     [Arguments]     ${arg}
     # split string bt comma
     ${result} =     split string        ${arg}      ,
     [Return]    ${result}


##############################################################

[KW]MyKeyWord
    [Arguments]        ${arg}
    log to console     ${arg}

[KW]Open web
    [Arguments]        ${arg}
    ${result}   passing parameters      ${arg}
    Open Browser  ${result}[${0}]    ${result}[${1}]
    Maximize Browser Window
    Set Selenium Speed      0.3

[KW]Click Element
     [Arguments]     ${arg}
     Click Element   ${arg}


[KW]Click Button
     [Arguments]     ${arg}
     ${result}   passing parameters      ${arg}
#     log to console    \nField=${result}[${0}]
     Click Element     ${result}[${0}]


[KW]Capture Screenshot
     [Arguments]        ${arg}
	 Sleep    3s
     Capture Page Screenshot        ${arg}

[KW]Save Screenshot
     [Arguments]        ${arg}
    ${d}=   get time
    ${d}= 	Convert Date 	${d} 	     result_format=%Y%m%d%H%S
	Sleep    3s
    Capture Page Screenshot        ${arg}/${d}.png


[KW]Send Image via Line
     [Arguments]        ${arg}
    ${d}=   get time
    ${d}= 	Convert Date 	${d} 	     result_format=%Y%m%d%H%S
	 Sleep    3s
	 Capture Page Screenshot        ${arg}/${d}.png
	 notifyImageFile    ${arg}/${d}.png

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


[KW]View Page Source
    [Arguments]     ${arg}
    [Return]        Get Source      ${arg}



[KW]Upload File To Google Drive
    [Arguments]     ${arg}
    uploadToGoogleDrive     ${arg}



[KW]Select Date Picker
     [Arguments]     ${arg}
#      ${d}=   get time
#      ${d}=   Convert Date      ${d} 	     result_format=%Y/%m/%d
#      ${result}   passing parameters      ${arg}
#      Run Keyword If  ${result}[${1}]==${EMPTY}         ${result}[${1}]=${d}
#                  else      log to console      setCurrentDate=${d}
#
#     log to console      ${result}[${1}]

     ${result}   passing parameters      ${arg}
     Click Element      ${result}[${0}]
     Input Text         ${result}[${0}]       ${result}[${1}]


[KW]Get Request
    [Arguments]     ${arg}  #URL_ALIASE,URL_GET,URL_GET_SUB
#     log to console       \nArg= ${arg}
      ${result}   passing parameters      ${arg}
#      log to console    \nPara1=${result}[${0}]
#      log to console    \nPara2=${result}[${1}]
#      log to console    \nPara3=${result}[${2}]

     Create Session         ${result}[${0}]             ${result}[${1}]
     ${resp}=  Get Request          ${result}[${0}]                 ${result}[${2}]

    log to console        \nRspone_status_Expect===>>>>>>${RES_STATUS}
    log to console        \nRspone_status_Actual===>>>>>>>${resp.status_code}
#   log to console        \nRspone_status_Text===>>>>>>>${resp.text}
    log to console        \nRspone_status_Json===>>>>>>>${resp.json()}

    Should Be Equal As Strings	${resp.status_code}	${RES_STATUS}
#    should contain  ${resp.text}     ${RES_TEXT}
#    lineNotify      Respone=${resp.status_code}
    [Return]        ${resp.status_code}



