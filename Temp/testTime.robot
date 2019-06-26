*** Settings ***
Library           DateTime

*** Test Cases ***
datatimetest
   ${d}=    get time
   log to console   \nTime=${d}
   ${d}=    Get Current Date    result_format=%Y-%m-%d
   log to console    \nDate=${d}



    ${d}=   get time
    ${d} = 	Convert Date 	${d} 	     result_format=%Y%m%d%H%S
    log to console    \nTarget=${d}