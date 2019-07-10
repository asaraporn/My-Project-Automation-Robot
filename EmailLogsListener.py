# https://robot-framework.readthedocs.io/en/2.9.2/_modules/robot/run.html

import os
import webbrowser
import datetime
import math
import time

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from email.mime.base import MIMEBase

# TODO: Import [lineNotification]
import CommonLib.lineNotification
from robot.libraries.BuiltIn import BuiltIn


class EmailLogsListener:
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
        self.log_failed = ""

        live_logs_file = open('EmailContentLogs.html', 'w')
        message = """         
                <div class="detailTable" id="detailTable">
                    <table style="width:80%%;padding-left:20px">
                        <tr class="heading">
                            <td>Executed Time</td>
                            <td >KW Name</td>
                            <td>KW Status</td>
                            <td>Message</td>
                        </tr>      
                       """
        live_logs_file.write(message)
        live_logs_file.close()

    def start_suite(self, name, attrs):
        # TODO :: GET CONFIG FROM FILE (LogConfig))
        self.SMPT = BuiltIn().get_variable_value("${SMPT}")
        self.SUBJECT = BuiltIn().get_variable_value("${SUBJECT}")
        self.FROM = BuiltIn().get_variable_value("${FROM}")
        self.PASSWORD = BuiltIn().get_variable_value("${PASSWORD}")
        self.TO = BuiltIn().get_variable_value("${TO}")
        self.CC = BuiltIn().get_variable_value("${CC}")
        self.COMPANY_NAME = BuiltIn().get_variable_value("${COMPANY_NAME}")

        self.date_now = datetime.datetime.now().strftime("%Y/%m/%d")
        self.start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        self.test_count = len(attrs['tests'])

        if self.test_count != 0:
            live_logs_file = open('EmailContentLogs.html', 'a+')
            message = """ <tr class="detail_suite">
                                 <td colspan="4">%s</td>
                          </tr> """ % (str(name))

            live_logs_file.write(message)
            live_logs_file.close()

    def start_test(self, name, attrs):
        if self.test_count != 0:
            print("start_test")

    # def log_message(self, message):
    #     if str(message['level']) == "FAIL":
    #         self.log_failed = str(self.log_failed).join(str(message['message']))




    def end_keyword(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('EmailContentLogs.html', 'a+')
            message = """
                    <tr class="detail" >
                        <td>%s %s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td></td>
                    </tr>
            """ % (self.date_now, datetime.datetime.now().time().strftime('%H:%M:%S')
                                         , str(attrs['kwname']).replace("[KW]", "")
                                         , str(attrs['status'])
                   )

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
        print("end_test")
        ###### Count test-cse #####
        if self.test_count != 0:
            self.total_tests += 1
        if attrs['status'] == 'PASS':
            self.passed_tests += 1
        else:
            self.failed_tests += 1

    def end_suite(self, name, attrs):
        print("end_suite==>" + str(attrs['message']))
        # if self.test_count != 0:
        #     live_logs_file = open('EmailContentLogs.html', 'a+')
        #     message = """ <tr class="detail_suite">
        #                          <td colspan="4">%s</td>
        #                   </tr> """ % str((attrs['message']))
        #
        #     live_logs_file.write(message)
        #     live_logs_file.close()


    def close(self):
        # print("FAILED ::" + self.log_failed)
        self.end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        self.total_time = (datetime.datetime.strptime(self.end_time, '%H:%M:%S')
                           - datetime.datetime.strptime(self.start_time, '%H:%M:%S'))

        live_logs_file = open('EmailContentLogs.html', 'r')
        testCaseStatus = live_logs_file.read()
        live_logs_file.close()

        # TODO : G-MAIL(Set Config)
        send_mail_logsResult(self.total_tests, self.passed_tests, self.failed_tests
                             , self.date_now, self.start_time, self.end_time, self.total_time
                             , self.total_step_tests, self.passed_step_tests, self.failed_step_tests
                             , self.SMPT, self.COMPANY_NAME, self.SUBJECT
                             , self.FROM, self.PASSWORD, self.TO, self.CC, testCaseStatus)


def send_mail_logsResult(total, passed, failed
                         , exe_date, start_time, exe_time, total_time
                         , total_step, passes_step, failed_step
                         , smtpConfig, companyName, subjectMail
                         , fromMail, passwordMail, toMail, ccMail, testCaseStatus):
    print("===send_mail_logsResult===")
    email_content = """
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
                            padding: 20px;
                            border: 1px solid #eee;
                            box-shadow: 0 0 10px rgba(0, 0, 0, .1);
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
                            padding: 2px;
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
                        .rf-box table tr.detail td {
                            border-bottom: 1px solid #eee;
                                                 font-size: 12px;
                                                 text-align: left;
                        }
                        .rf-box table tr.detail_suite td {
                           border-bottom: .5px solid #eee;
                           font-size: 12px;
                           text-align: left;
                           font-weight: bold;
                        }
                        .detailTable {
                          display: none;
                        }
                    </style>

              <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

                <script type="text/javascript">
                // Load google charts
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(drawChart);

                // Draw the chart and set the chart values
                function drawChart() {
                  var data = google.visualization.arrayToDataTable([
                  ['Status', 'Progress'],
                  ['Passed', %s],
                  ['Failed', %s]
                ]);

                  // Optional; add a title and set the width and height of the chart
                  var options = {'title':'Execution Status', 'width':250, 'height':170};

                  // Display the chart inside the <div> element with id="piechart"
                  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                  chart.draw(data, options);
                }

                <!-- Hidden -->
				function myDetail() {
					  var x = document.getElementById("detailTable");
					  //alert(x.style.display ) ;
					  if (x.style.display === "") {
						x.style.display = "block";
					  }else if (x.style.display === "none") {
						x.style.display = "block";
					  }else {
						x.style.display = "none";
					  }
					}
                </script>

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
                            Following are the last build execution result. 
                            Please refer <a href="#" id="reportLink" onclick="myDetail()" > attachment file </a>
                            for more info
                        </p>


            <table>
            <tr>
                <td style="width:80%%;">
                        <table style="width:100%%;padding-left:20px">
                              <tr class="heading" >
                                    <td rowspan="2">Executed Date</td>
                                    <td colspan="2">Test Result</td>
                                    <td colspan="2">Rate(%%)</td>
                                    <td rowspan="2">Total Test</td>
                                    <td rowspan="2">Start Test</td>
                                    <td rowspan="2">End Test</td>
                                    <td rowspan="2">Duration</td>
                                    <!--<td rowspan="3" style="background-color:WHITE"> <div id="piechart"></div></td> -->
                              </tr>
                              <tr class="heading" >
                                            <td >Pass</td>
                                            <td >Fail</td>
                                            <td >Pass</td>
                                            <td >Fail</td>

                              </tr>
                              <tr class="item">
                                            <td>%s</td>
                                            <td >%s</td>
                                            <td >%s</td>
                                            <td >%s </td>
                                            <td >%s</td>
                                            <td >%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                              </tr>
                        </table>
                    </td>
                    <td style="width:20%%;vertical-align:top;horizontal align:right;">
                        <div id="piechart"></div>
                    </td>
                </tr>
            </table>
        <br/>
            %s


         </table></div>   
        <table>
                    <tr>
                        <td style="text-align:center;color: #999999; font-size: 11px">
                            <p>Test Report</p>
                        </td>
                    </tr>
           </table>
        </body>
        </html>
        """ % (passes_step
                                   , failed_step
                                   , exe_date
                                   , passes_step
                                   , failed_step
                                   , math.ceil(passes_step * 100.0 / total_step)
                                   , math.ceil(failed_step * 100.0 / total_step)
                                   , total_step
                                   , start_time
                                   , exe_time
                                   , total_time
                                   , testCaseStatus)

    # print("Summary >>>> \n" + email_content)

    # TODO : G-mail Notify
    # print(smtpConfig)
    server = smtplib.SMTP(smtpConfig)
    msg = MIMEMultipart()

    msg['Subject'] = "[" + companyName + "]" + subjectMail
    msg['From'] = fromMail
    msg['To'] = toMail

    msg['Cc'] = ccMail
    to_addrs = [toMail] + [ccMail]

    # write file
    live_logs_file = open('EmailContentLogsDetail.html', 'w')
    message = email_content
    live_logs_file.write(message)
    live_logs_file.close()

    # Setup the attachment
    filename = os.path.basename('EmailContentLogsDetail.html')
    attachment = open('EmailContentLogsDetail.html', "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)
    # print("===attachment file===")

    # email content
    msg.add_header('Content-Type', 'text/html')
    msg.attach(MIMEText(email_content, 'html'))
    server.starttls()

    # send mail
    server.login(msg['From'], passwordMail)
    server.sendmail('', to_addrs, msg.as_string())

    print("===END===")

