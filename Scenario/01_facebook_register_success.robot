*** Settings ***
###TODO : FaceBook Keyword
Resource  ../Keyword/facebook_login_keyword.robot
Resource  ../Keyword/facebook_register_keyword.robot


Documentation     A test suite with a single test for valid login.
*** Test Cases ***
Test Case success
    log_on_thread   on thread [Register]- open facebook

1.Open browser
    my_logger     [Register]- open browser
    Open chrom set option

2. Open facebook
    my_logger     [Register]- open facebook
    Go To           ${url_facebook}


3. Filling out Birthday
#    ${combo_box_day}  ${combo_box_day_value} =  get_data_googleDrive_atSheet   ${google_doc}     ${1}      A1      B1
#    Log  \nDay= ${combo_box_day_value}
#    Log   [Register-START TEST]- input info data-Day=${combo_box_day_value}
#    Log   [Register-START TEST]- input info data-Month=${combo_box_month_value}
#    Log   [Register-START TEST]- input info data-Yesr=${combo_box_year_value}


    Click Element   ${combo_box_day}
    Select From List by Value    ${combo_box_day}    ${combo_box_day_value}



    Click Element    ${combo_box_month}
    Select From List by Index      ${combo_box_month}    ${combo_box_month_value}

    Click Element    ${combo_box_year}
    Select From List by Value    ${combo_box_year}   ${combo_box_year_value}

4. Filling out of sex
    Select Radio Button     ${radio_box_sex}     ${radio_box_sex_value}

5. Input first name
     Input Text       ${text_box_firstName}        ${text_box_firstName_value}

6. Input surname
     Input Text       ${text_box_lastName}       ${text_box_lastName_value}

7. Input password
     Input Text       ${text_box_email}        ${text_box_email_value}
     Input Text       ${text_box_reEmail}         ${text_box_reEmail_value}


8. Input confirm-password
      Input Text       ${text_box_password}       ${text_box_password_value}


9. Verify Login Success and LineNotify
    Capture Page Screenshot  ${filename}Register.${TYPE OF FILE}
    notifyImageFile  ${filename}Register.${TYPE OF FILE}

9. Register Facebook
     Click Element     ${register_button}


10. Close facebook
    Sleep    3s
    Close Browser


    Finish All


#11. Generator log file
#    ${result_grep} =      grep file       ${CURDIR}/TestResult/myLog.log      START TEST
#    append to file        ${CURDIR}/TestResult/myLog-grep-test.log       ${result_grep}
