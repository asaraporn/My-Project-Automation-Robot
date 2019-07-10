import requests
import urllib
#https://notify-bot.line.me/my/
LINE_ACCESS_TOKEN   = "YEs9zKBY27OLxf4OwtNwSoSysMxTlWzK1MtpP5iD33r"
url                 = "https://notify-api.line.me/api/notify"
data                = "Hello Sai."
message             = urllib.urlencode({"message":data})
# message             = urllib.parse.urlencode({"message":data})


headers = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
r = requests.post(url, headers=headers, data=message)
print(r.status_code, r.reason)
print(r.text[:300] + '...')
