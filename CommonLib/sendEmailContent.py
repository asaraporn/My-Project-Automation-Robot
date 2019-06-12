import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp = "smtp.gmail.com:587"
server = smtplib.SMTP(smtp)
msg = MIMEMultipart()
msg['Subject'] = 'MAIL TEST'
msg['From'] = 'asaraporn@addtechhub.com'
msg['To'] = 'asaraporn@addtechhub.com'
msg['Cc'] = 'asaraporn@addtechhub.com'
to_addrs = ['asaraporn@addtechhub.com'] + ['asaraporn@addtechhub.com']
msg.add_header('Content-Type', 'text/html')

email_content = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
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
                        <th> >>>>> Generating Live Logs - Scroll Down for latest <<<<< </th>
                    </tr>
                </table>
                </br>

        
                <table>
                    <tr>
                        <th style="background-color:LIGHTSTEELBLUE">Suite (Tests)</th>
                        <th style="background-color:LIGHTSTEELBLUE">Test Name</th>
                        <th style="background-color:LIGHTSTEELBLUE">Test Status</th>
                        <th style="background-color:LIGHTSTEELBLUE">Message</th>
                    </tr>
                    <tr>
                        <td style="background-color:LAVENDER">Facebook Register Success ( 12 )</td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:15.333</td>
                        <td style="background-color:LIGHTBLUE">Test Case 1</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:15.345</td>
                        <td style="background-color:LIGHTBLUE">1.[Register]- open browser</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:18.884</td>
                        <td style="background-color:LIGHTBLUE">2. [Register]- open facebook</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:20.378</td>
                        <td style="background-color:LIGHTBLUE">3. Input text</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:21.348</td>
                        <td style="background-color:LIGHTBLUE">4. Check option</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:21.443</td>
                        <td style="background-color:LIGHTBLUE">5. Input first name</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:21.635</td>
                        <td style="background-color:LIGHTBLUE">6. Input sur name</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:21.797</td>
                        <td style="background-color:LIGHTBLUE">7. Input password</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>FAIL</strong></td>
                        <td style="text-align: left;">ElementNotVisibleException: Message: element not interactable
  (Session info: chrome=74.0.3729.169)
  (Driver info: chromedriver=74.0.3729.6 (255758eccf3d244491b8a1317aa76e1ce10d57e9-refs/branch-heads/3729@{#29}),platform=Windows NT 10.0.17763 x86_64)
</td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:22.662</td>
                        <td style="background-color:LIGHTBLUE">8. Input confirm-password</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:22.763</td>
                        <td style="background-color:LIGHTBLUE">9. Verify Login Success</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:23.146</td>
                        <td style="background-color:LIGHTBLUE">9. Register</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:WHITE">20190611 16:05:23.255</td>
                        <td style="background-color:LIGHTBLUE">10. Close facebook</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td ></td>
                        <td></td>
                        <td style="background-color:BEIGE"><strong>PASS</strong></td>
                        <td style="text-align: left;"></td>                        
                    </tr>
                </table>

            
                <table>
                    <tr>
                        <td style="background-color:LAVENDERBLUSH"><strong>Facebook Register Success</strong></td>
                        <td style="background-color:CORNSILK"><strong>FAIL</strong></td>
 
                    </tr>
                </table>
                </br>

            
                <table>
                    <tr>
                        <td style="background-color:LAVENDERBLUSH"><strong>Scenario</strong></td>
                        <td style="background-color:CORNSILK"><strong>FAIL</strong></td>
 
                    </tr>
                </table>
                </br>

            
            <table>
                <tr>
                    <th>Execution completed!</th>
                </tr>
            </table>

        """
msg.attach(MIMEText(email_content, 'html'))
server.starttls()
server.login(msg['From'], 'Hadsai.1')
server.sendmail('', to_addrs, msg.as_string())