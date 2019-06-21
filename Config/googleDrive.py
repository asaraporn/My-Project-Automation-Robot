from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os

# # Login to Google Drive and create drive object
# g_login = GoogleAuth()
# g_login.LocalWebserverAuth()
# drive = GoogleDrive(g_login)


def upload_to_gDrive(file):

    print("upload_to_gDrive >>> "+file)

    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)

    os.chdir(os.getcwd())
    print("Drive ===> "+ os.getcwd())

    # for file in glob.glob("*.txt"):
    # print("file >>>>>> "+file)
    with open(file, "r") as f:
        fn = os.path.basename(f.name)
        file_drive = drive.CreateFile({'title': fn})

        file_drive.SetContentString(f.read())
        file_drive.Upload()

        print("The file: " + fn + " has been uploaded")
        print("All files have been uploaded")


# TESTING
# fileName = 'facebook_register_config.txt'
# upload_to_gDrive(fileName)