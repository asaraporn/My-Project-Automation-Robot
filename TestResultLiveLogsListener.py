# https://robot-framework.readthedocs.io/en/2.9.2/_modules/robot/run.html

import os
import webbrowser
import datetime


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#TODO: Import [lineNotification]
import  CommonLib.lineNotification


from robot.libraries.BuiltIn import BuiltIn



class TestResultLiveLogsListener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):

        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0

        self.PRE_RUNNER = 0
        self.start_time = datetime.datetime.now().time().strftime('%H:%M:%S')


        live_logs_file = open('ResultLiveLogs.html', 'w')

        message = """
        <html>
            <head>
                <title>Live Logs</title>
                <meta http-equiv="refresh" content="5" >
                <style>
                    table {  
                        color: #333; /* Lighten up font color */
                        font-family: Consolas, Helvetica, Arial, sans-serif;
                        table-layout: fixed;
                        width: 100%;
                        font-size: 14px;
                    }

                    td, th { border: 1px solid #CCC; height: 30px; } /* Make cells a bit taller */

                    th {  
                        background: #F3F3F3; /* Light grey background */
                        font-weight: bold; /* Make sure they're bold */
                    }

                    td {  
                        background: #FAFAFA; /* Lighter grey background */
                        text-align: center; /* Center our text */
                        width: 100; 
                        /* css-3 */
                        white-space: -o-pre-wrap; 
                        word-wrap: break-word;
                        white-space: pre-wrap; 
                        white-space: -moz-pre-wrap; 
                        white-space: -pre-wrap;
                    }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <th> >>>>> Automation Execution Status <<<<< </th>
                    </tr>
                </table>
                </br>
        </html>
        """

        live_logs_file.write(message)
        live_logs_file.close()

        current_dir = os.getcwd()
        filename = current_dir + '/ResultLiveLogs.html'

        webbrowser.open_new_tab(filename)

    def start_suite(self, name, attrs):

        # TODO :: GET CONFIG FROM FILE (LogConfig))
        self.SMTP = BuiltIn().get_variable_value("${SMTP}")
        self.SUBJECT = BuiltIn().get_variable_value("${SUBJECT}")
        self.FROM = BuiltIn().get_variable_value("${FROM}")
        self.PASSWORD = BuiltIn().get_variable_value("${PASSWORD}")
        self.TO = BuiltIn().get_variable_value("${TO}")
        self.CC = BuiltIn().get_variable_value("${CC}")
        self.COMPANY_NAME = BuiltIn().get_variable_value("${COMPANY_NAME}")
        # print("############### Config ##########")
        # print("SUBJECT = " + self.SUBJECT)
        # print("FROM = " + self.FROM)
        # print("TO = " + self.TO)
        # print("CC = " + self.CC)

        self.date_now = datetime.datetime.now().strftime("%Y-%m-%d")



        self.test_count = len(attrs['tests'])

        if self.test_count != 0:
            live_logs_file = open('ResultLiveLogs.html', 'a+')

            message = """
                <table>
                    <tr>
                        <th style="background-color:LIGHTSTEELBLUE">Suite (Tests)</th>
                        <th style="background-color:LIGHTSTEELBLUE">Test Name</th>
                        <th style="background-color:LIGHTSTEELBLUE">Test Status</th>
                        <th style="background-color:LIGHTSTEELBLUE">Message</th>
                        <th style="background-color:LIGHTSTEELBLUE">KW Name</th>
                        <th style="background-color:LIGHTSTEELBLUE">KW Status</th>
                    </tr>
                    <tr>
                        <td style="background-color:LAVENDER"><strong>%s (%s)</strong></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>

            """ % (str(name), str(self.test_count))

            live_logs_file.write(message)
            live_logs_file.close()

    def start_test(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('ResultLiveLogs.html', 'a+')

            message = """
                <table>
                    <tr>
                        <td></td>
                        <td style="background-color:LIGHTBLUE"><strong>%s</strong></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>

            """ % (str(name))

            live_logs_file.write(message)
            live_logs_file.close()

    def end_keyword(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('ResultLiveLogs.html', 'a+')

            message = """
                <table>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td style="text-align: left;">%s</td>
                        <td>%s</td>
                    </tr>
                </table>
            """ % ( str(attrs['kwname']), str(attrs['status']))
            # live_logs_file.write(message)
            # live_logs_file.close()

            # TODO : Write Log (Keyword)
            if str(attrs['kwname']).startswith('[KW]'):
                live_logs_file.write(message)
                live_logs_file.close()



    def end_test(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('ResultLiveLogs.html', 'a+')

            message = """
                <table>
                    <tr>
                        <td></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>%s</strong></td>
                        <td style="text-align: left;">%s</td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>

            """ % (str(attrs['status']), str(attrs['message']))

            live_logs_file.write(message)
            live_logs_file.close()

            ###### Count test-cse #####
            if self.test_count != 0:
                self.total_tests += 1
            if attrs['status'] == 'PASS':
                self.passed_tests += 1
            else:
                self.failed_tests += 1



    def end_suite(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('ResultLiveLogs.html', 'a+')
            message = """
                <table>
                    <tr>
                        <td style="background-color:LAVENDERBLUSH"><strong>%s</strong></td>
                        <td style="background-color:CORNSILK"><strong>%s</strong></td>
                    </tr>
                </table>
                </br>

            """ % (str(name), str(attrs['status']))

            live_logs_file.write(message)
            live_logs_file.close()

    def close(self):

        live_logs_file = open('ResultLiveLogs.html', 'a+')
        message = """
            <table>
                <tr>
                    <th>Execution completed! </th>
                </tr>
            </table>
        """

        live_logs_file.write(message)
        live_logs_file.close()

        # TODO : [summary_content] Result!!!!
        self.end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        self.total_time = ( datetime.datetime.strptime(self.end_time, '%H:%M:%S')
                                    - datetime.datetime.strptime(self.start_time,'%H:%M:%S'))

        # TODO : LINE
        send_summary_content(self.total_tests, self.passed_tests, self.failed_tests, self.date_now
                        ,self.end_time , self.total_time )


        # TODO : G-MAIL(Set Config)
        # send_mail_logsResult(self.total_tests, self.passed_tests, self.failed_tests
        #      , self.date_now, self.end_time, self.total_time
        #      , self.SMTP , self.COMPANY_NAME , self.SUBJECT
        #      ,self.FROM, self.PASSWORD ,self.TO ,self.CC)


def send_summary_content(total, passed, failed, exe_date, end_time, total_time):
    print(">>>>>>>>>>>>>>> summary_content <<<<<<<<<<<<<<<<<<<<<<<<<")
    summary_content = """ 
       ### Summary Test Result ####
        Test date : [%s]
           - Total = %s
           - Passed = %s
           - Failed = %s 
        End test :  %s 
        Total time : %s 

        For more details please see 
        at your Gmail https://mail.google.com 
         """ \
                      % (exe_date, total, passed, failed, end_time, total_time)

    # print("TODO : Line Notify")
    print(summary_content)
    # # TODO : Line Notify
    # CommonLib.lineNotification.lineNotify(summary_content)


def send_mail_logsResult(total, passed, failed, exe_date, end_time, total_time
                         , smtpConfig, companyName, subjectMail, fromMail, passwordMail, toMail, ccMail):
    # TODO : G-mail Notify
    print(smtpConfig)
    server = smtplib.SMTP(smtpConfig)
    msg = MIMEMultipart()

    msg['Subject'] = "[" + companyName + "]" + subjectMail
    msg['From'] = fromMail
    msg['To'] = toMail

    msg['Cc'] = ccMail
    to_addrs = [toMail] + [ccMail]
    # msg['Cc'] = 'hadsai.y@gmail.com;hadsai.g@gmail.com'
    # to_addrs = ['asaraporn@addtechhub.com'] + [msg['Cc']]

    msg.add_header('Content-Type', 'text/html')

    live_logs_file = open('LiveLogsResult.html', 'r')
    message = live_logs_file.read()
    email_content = message
    # print(email_content)
    # live_logs_file.close()

    msg.attach(MIMEText(email_content, 'html'))
    server.starttls()

    server.login(msg['From'], passwordMail)
    server.sendmail('', to_addrs, msg.as_string())