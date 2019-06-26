*** Settings ***
Library    String
Library    Collections

*** Variables ***
${count}              5
${COMMA}              ,
@{dbws_datapoints}

${para1}          22        xpath=//select[@id="day"]

@{para2}          22,xpath=//select[@id="day"]
@{para3}          22,xpath=//select[@id="day"]

*** Test Cases ***
1.Test
#     split parameter       22,xpath=//select[@id="day"]
      ${result}     passing parameters      22,xpath=//select[@id="day"]
      log to console      \nStr02=${result}[${0}]


*** Keywords ***
Get Text
    [Arguments]    ${i}
    ${list}    Create List    aaa    bbb    ccc    ddd    eee
    [Return]    ${list[${i}]}

Test case para
   : FOR    ${i}    IN RANGE    0    ${count}
        \  ${j}   Get Text    ${i}
        \  ${listCount}    Get Length    ${dbws_datapoints}
        \
        \  Run Keyword If    (${i}>=0)     Append To List  ${dbws_datapoints}    ${j}
        \  Run Keyword If    (${i}>=0)     Log To Console  ${dbws_datapoints[${listCount}]}


split para
    ${random employee}= Convert To String   ${para1}
    ${replace}= Remove String Using Regexp  ${random employee}  ['\\[\\]\\,]

    ${splitline}=   Fetch From Left ${replace}  ${SPACE}
    log to console  ${splitline}


split parameter
    [Arguments]     ${arg}
    log to console      \narg=${arg}

    ${result} =     split string        ${arg}      ${COMMA}
    log to console      \nStr=${result}

    ${length} =    Get Length    ${result}
    log to console      \nlen=${length}
    log to console      \nStr01=${result}[${0}]
    log to console      \nStr02=${result}[${1}]



passing parameters
     [Arguments]     ${arg}
     ${result} =     split string        ${arg}      ${COMMA}
     [Return]    ${result}










