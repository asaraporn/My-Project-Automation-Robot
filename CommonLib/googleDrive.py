from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os

# # Login to Google Drive and create drive object
# g_login = GoogleAuth()
# g_login.LocalWebserverAuth()
# drive = GoogleDrive(g_login)


def uploadToGoogleDrive(file):
    print("uploadToGoogleDrive >>> "+file)
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



def uploadFileToGoogleDrive(targetFile):
    print("uploadFileToGoogleDrive >>> " + targetFile)
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    # test = "Path to my BA_UploadTest.docx"
    test = targetFile
    with open(test, "r", encoding="Latin-1")as file:
        fn = os.path.basename(file.name)
        file_drive = drive.CreateFile({'File_Title': os.path.basename(file.name)})
    file_drive.SetContentString(file.read())
    file_drive.Upload()
    print('File upload successful!')




def uplaod2GoogleDrive(fileName):
    print('==== uplaod2GoogleDrive ======')
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({'title': 'UploadFile.txt'})
    # Create GoogleDriveFile instance with title 'Hello.txt'
    file1.SetContentString('Hello World!')  # Set content of the file from given string
    file1.Upload()

    # Auto-iterate through all files that matches this query
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    print('File upload successful!')



# # TESTING
# fileName = 'UploadFile.txt'
# uploadToGoogleDrive(fileName)




