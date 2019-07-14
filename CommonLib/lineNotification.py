import requests
import urllib3
import base64

LINE_ACCESS_TOKEN_ME = "YEs9zKBY27OLxf4OwtNwSoSysMxTlWzK1MtpP5iD33r"
LINE_URL = "https://notify-api.line.me/api/notify"


def _lineNotify(payload,file=None):
    url = LINE_URL
    token = LINE_ACCESS_TOKEN_ME
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers, data=payload, files=file)


def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)


def notifyImageFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': " "}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)


def getLineMsg():
    print('Hello')


def line_noti_ori():
   # https://notify-bot.line.me/my/

    url = LINE_URL
    data = "### Test Result ###"
    message = urllib3.urlencode({"message":data})
    #message = urllib.parse.urlencode({"message": data})

    headers = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN_ME}
    r = requests.post(url, headers=headers, data=message)
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')



###TODO : send report testing via Line
def notifyFile(filename):
    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    payload = {'message': " "}
    return _lineNotify(payload, encodedcontent)





#TEST!!!!
# lineNotify('ทดสอบภาษาไทย hello')
# notifySticker(40,2)
# notifyPicture("https://cdn-images-1.medium.com/max/1200/1*mONNI1lG9VuiqovpnYqicA.jpeg")
# notifyImageFile('pic.png')

# notifyFile('CommonLib/ResultLiveLogs.txt')

