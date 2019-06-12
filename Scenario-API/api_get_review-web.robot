*** Settings ***
Library    RequestsLibrary

*** Variables ***
${URL_ALIASE}   ReviewYourLiving
${URL_GET}      https://www.reviewyourliving.com/
${URL_GET_SUB}   /review-townhome

${RES_STATUS}       200
${RES_TEXT}         <ul class="footer-menu">

*** Keywords ***
Get API WEB TEST
    Create Session	${URL_ALIASE}	${URL_GET}
     ${resp}=  Get Request          ${URL_ALIASE}                 ${URL_GET_SUB}

    Should Be Equal As Strings	${resp.status_code}	${RES_STATUS}
    should contain  ${resp.text}     ${RES_TEXT}

    log to console        \nWith rspone_code-${resp.status_code}
#    log to console        \n.Rspone_Text-${resp.text}


*** Test Cases ***
1. Test web is active
   Get API WEB TEST