import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# import pandas as pd
# from gspread_dataframe import get_as_dataframe

# import openpyxl
# from robot.libraries.BuiltIn import BuiltIn
# JSON_KEY_FILE_NAME= BuiltIn().get_variable_value("${SEND_EMAIL}")
# GOOGLE_URL = BuiltIn().get_variable_value("${GOOGLE_URL}")

JSON_KEY_FILE_NAME= "./Config/FacebookLogin-json.json"
# JSON_KEY_FILE_NAME =  os.getcwd() + "\\spreadSheetConnector.json"
GOOGLE_URL = "https://www.googleapis.com/auth/drive"

# curWorkPath = os.getcwd()
# print(curWorkPath)
# JSON_KEY_FILE_NAME= "spreadSheetConnector.json"
# JSON_KEY_FILE_NAME = curWorkPath+"\\spreadSheetConnector.json"
# print(JSON_KEY_FILE_NAME)

#Function : getGoogleSheetBySheetIndex
def getGoogleSheetBySheetIndex(fileName,sheetIndex):

    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)
    dataValue = dataSheet.get_all_values()

    return  dataValue



# ======================================================================================================= #


def writeDataSheet(fileName):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    # client = gspread.authorize(creds)


def getDataSheet(fileName, targetRange):

    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(0)

    return dataSheet.acell(targetRange).value


def getDataSheetByCell(fileName, col1 ,col2):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(1)

    return  dataSheet.acell(col1).value , dataSheet.acell(col2).value


def getDataSheetBySheetIndex(fileName,sheetIndex, col1 ,col2):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)

    return  dataSheet.acell(col1).value , dataSheet.acell(col2).value


def updateCell(fileName, sheetIndex , str):
        scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
        creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(fileName)
        dataSheet = sheet.get_worksheet(sheetIndex)

        dataSheet.update_cell(1, 1, str)


def insertRow(fileName,sheetIndex):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)

    row = ["I'm", "inserting", "a", "new", "row", "into", "a,", "Spreadsheet", "using", "Python"]

    index = 1
    dataSheet.insert_row(row, index)



def insertImage(fileName,sheetIndex):
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)

    row = ["=IMAGE(\"http://themisadventuresofjenn.com/wp-content/gallery-bank/gallery-uploads/o_1a5j5e6er1jph1g741eb51gn513r79c.jpg\""]
    index = 1

    dataSheet.insert_row(row, index)



import openpyxl
def getGoogleSheetBySheetIndex2(fileName,sheetIndex):

    JSON_KEY_FILE_NAME = os.getcwd() + "\\spreadSheetConnector.json"
    scope = ['https://spreadsheets.google.com/feeds', GOOGLE_URL]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE_NAME, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(fileName)
    dataSheet = sheet.get_worksheet(sheetIndex)
    dataValue = dataSheet.get_all_values()

    #Set Value keyword
    col_index = 2
    list_of_lists_keyword = dataSheet.col_values(col_index)
    lenCols = len(list_of_lists_keyword)
    for i in range(lenCols):
        keyword = list_of_lists_keyword[i]
        newKeyword = "[KW]"+keyword
        #set new keyword
        print(i,newKeyword)
        dataSheet.update_cell( 2 , 5 , newKeyword)


    print(dataSheet.get_all_values())
    return  dataValue


# ===================== TEST =========================== #
# fileN = 'https://docs.google.com/spreadsheets/d/1PwfrGYropY-UuwsneiD2UR5SUKqkNEthWkLVkWbJA_I/edit'
# a = getGoogleSheetBySheetIndex2(fileN , 7)







