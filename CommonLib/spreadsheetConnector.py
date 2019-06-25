import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# import openpyxl
# from robot.libraries.BuiltIn import BuiltIn
# JSON_KEY_FILE_NAME= BuiltIn().get_variable_value("${SEND_EMAIL}")
# GOOGLE_URL = BuiltIn().get_variable_value("${GOOGLE_URL}")

JSON_KEY_FILE_NAME= "./Config/FacebookLogin-json.json"
# JSON_KEY_FILE_NAME= "spreadSheetConnector.json"
GOOGLE_URL = "https://www.googleapis.com/auth/drive"

# curWorkPath = os.getcwd()
# print(curWorkPath)
# JSON_KEY_FILE_NAME= "spreadSheetConnector.json"
# JSON_KEY_FILE_NAME = curWorkPath+"\\spreadSheetConnector.json"
# print(JSON_KEY_FILE_NAME)



def get_data_gDrive(fileName, targetRange):

    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(0)

    return dataSheet.acell(targetRange).value


def get_data_googleDrive(fileName, col1 ,col2):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(1)

    return  dataSheet.acell(col1).value , dataSheet.acell(col2).value


def get_data_googleDrive_atSheet(fileName,sheetIndex, col1 ,col2):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)

    return  dataSheet.acell(col1).value , dataSheet.acell(col2).value


def set_data_googleDrive_atSheet(fileName,sheetIndex):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)

    row = ["I'm", "inserting", "a", "new", "row", "into", "a,", "Spreadsheet", "using", "Python"]
    index = 1
    dataSheet.insert_row(row, index)



def update_data_googleDrive_atSheet(fileName, sheetIndex , str):
        scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
        creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(fileName)
        dataSheet = sheet.get_worksheet(sheetIndex)

        dataSheet.update_cell(1, 1, str)


def write_data_googleDrive(fileName):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    # client = gspread.authorize(creds)



def getGoogleSheetBySheetIndex(fileName,sheetIndex):

    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)
    dataValue = dataSheet.get_all_values()

    return  dataValue


###TEST
# fileN = 'https://docs.google.com/spreadsheets/d/1PwfrGYropY-UuwsneiD2UR5SUKqkNEthWkLVkWbJA_I/edit'
# a , b = get_data_googleDrive(fileN , 'A1', 'B1')
# print(a)
# print(b)

# fileN = 'https://drive.google.com/drive/folders/1iYF4t6y-4-mmf7oG_VgGFT5NP71OQQpJ'
# write_data_googleDrive(fileN)




