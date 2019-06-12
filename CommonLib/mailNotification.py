# https://myaccount.google.com/lesssecureapps

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("asaraporn@addtechhub.com", "Hadsai.1")
text = "Test by Python"

server.sendmail("asaraporn@addtechhub.com", "hadsai.g@gmail.com", text)
server.quit() # ปิดการเชื่อมต่อ





