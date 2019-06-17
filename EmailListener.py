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



class EmailListener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):

        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0

        self.total_step_tests = 0
        self.passed_step_tests = 0
        self.failed_step_tests = 0


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
                        font-weight: bold; /* Make sure they're bold */
                        background: #F3F3F3; /* Light grey background */
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



        self.date_now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.start_time = datetime.datetime.now().time().strftime('%H:%M:%S')


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
                self.total_step_tests += 1
                if str(attrs['status']) == 'PASS':
                    self.passed_step_tests += 1
                else:
                    self.failed_step_tests += 1




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

        self.end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        self.total_time = ( datetime.datetime.strptime(self.end_time, '%H:%M:%S')
                                    - datetime.datetime.strptime(self.start_time,'%H:%M:%S'))

        # TODO : G-MAIL(Set Config)
        print("G-MAIL(Set Config)")
        send_mail_logsResult(self.total_tests, self.passed_tests, self.failed_tests
             , self.date_now, self.start_time , self.end_time, self.total_time
             , self.total_step_tests, self.passed_step_tests, self.failed_step_tests
             , self.SMTP , self.COMPANY_NAME , self.SUBJECT
             ,self.FROM, self.PASSWORD ,self.TO ,self.CC)


def send_mail_logsResult(total, passed, failed
                         , exe_date,start_time ,exe_time, total_time
                         , total_step, passes_step,failed_step
                         , smtpConfig, companyName, subjectMail
                         , fromMail, passwordMail, toMail, ccMail):

        # server = smtplib.SMTP(smtpConfig)
        # msg = MIMEMultipart()
        # msg['Subject'] = subjectMail
        #
        # msg['From'] = fromMail
        # msg['To'] = toMail
        # msg['Cc'] = ccMail
        # to_addrs = [toMail] + [ccMail]
        # msg.add_header('Content-Type', 'text/html')


        email_content ="""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <title>Automation Status</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
            <style>
                .rf-box {
                    max-width: 60%%;
                    margin: auto;
                    padding: 30px;
                    border: 3px solid #eee;
                    box-shadow: 0 0 10px rgba(0, 0, 0, .15);
                    font-size: 16px;
                    line-height: 28px;
                    font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
                    color: #555;
                }

                .rf-box table {
                    width: 100%%;
                    line-height: inherit;
                    text-align: center;
                }

                .rf-box table td {
                    padding: 5px;
                    vertical-align: center;
                    width: 50%%;
                    text-align: center;
                }

                .rf-box table tr.heading td {
                    background: #eee;
                    border-bottom: 1px solid #ddd;
                    font-weight: bold;
                    text-align: center;
                }

                .rf-box table tr.item td {
                    border-bottom: 1px solid #eee;
                }
            </style>
        </head>
        <body>

            <div class="rf-box">
                <table cellpadding="0" cellspacing="0">
                    <tr class="top">
                        <td colspan="2">
                            <table>
                                <tr>
                                    <td></td>
                                    <td style="text-align:middle">
                                                   <h1>Addtechhub</h1>
                                       </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>

                <p style="padding-left:20px">
                    Hi Team,<br>
                    Following are the last build execution result. Please refer 
					<a href="LiveLogsResult-Failed.html">DetailReport</a> 
					for more info
                </p>

            <table style="width:70%%;padding-left:20px">
				  <tr class="heading" >
					<td rowspan="2">Executed Date</td>
					<td colspan="2">Test Result</td>
					<td colspan="2">Rate</td>
					<td rowspan="2">Total Test</td>
					<td rowspan="2">Start Test</td>
					<td rowspan="2">End Test</td>
					<td rowspan="2">Duration</td>
				  </tr>
				  <tr class="heading" >
						<td >Pass</td>
						<td >Fail</td>
						<td >Fail</td>
						<td >Exec</td>
				
				  </tr>
				  <tr class="item">
						<td>%s</td>
						<td >%s</td>
						<td >%s</td>
						<td >%s</td>
						<td >%s</td>
						<td >%s</td>
						<td>%s</td>
						<td>%s</td>
						<td>%s</td>
				  </tr>
				</table>
                <br>       

                <table>
                    <tr>
                        <td style="text-align:center;color: #999999; font-size: 11px">
                            <p>Test Report</p>
                        </td>
                    </tr>
                </table>
            </div>
        </body>
        </html>
            """% (  exe_date
                    , passes_step
                    , failed_step
                    , passes_step
                    , failed_step
                    , total_step
                    , start_time
                    , exe_time
                    , total_time)

        print(email_content)

        # msg.attach(MIMEText(email_content, 'html'))
        # server.starttls()
        # server.login(msg['From'], passwordMail)
        # server.sendmail(fromMail, to_addrs, msg.as_string())





