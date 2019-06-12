*** Settings ***
Library    RequestsLibrary

*** Variables ***
${URL_ALIASE}   google
${URL_GET}      http://www.google.com
${URL_GET_SUB}   /search

${URL_POST}     http://localhost:8080

*** Keywords ***
Get API HADSAI TEST
    Create Session	${URL_ALIASE}	${URL_GET}
     ${resp}=  Get Request          google                 ${URL_GET_SUB}
    log to console        \n1.Rspone-${resp.status_code}
    Should Be Equal As Strings	${resp.status_code}	200
    should contain  ${resp.text}     ${URL_ALIASE}


Post API HADSAI TEST
    Create Session    ${URL_ALIASE}    ${URL_POST}
    &{data}=  Create Dictionary        name=login     text= Hello world
    &{headers}=  Content-Type=application/xml
    ${resp}=    POST Request    TESTING    /login    data=${data}   headers=${headers}


    Log ${resp.text}
    Should Contain ${resp.text} 201
    Should Contain ${resp.text} ok


*** Test Cases ***
Test Get API SAI
   Get API HADSAI TEST

Test Post API SAI
    Post API HADSAI TEST
