#!/usr/bin/env python3
from gsuite.spreadsheet import Spreadsheet
from gsuite.service_connection import connect_service

SPREADSHEET_ID = "1Q3n6HDCsCFpChaiHA2s_wFRoIuJ0_hsOurPvfq4eRXI"
RANGE = "test_sheet_1!A1:B11"


def get_data_from_gsheet(service, spreadsheetId, range):

    sheet_data = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=range).execute()

    return sheet_data


service = connect_service()
test_data = get_data_from_gsheet(
    service=service, spreadsheetId=SPREADSHEET_ID, range=RANGE)

test_spreadsheet = Spreadsheet(client=service, spreadsheetId=SPREADSHEET_ID)


for sheet in test_spreadsheet.sheets:
    print(sheet.title)

elements = test_spreadsheet.sheets[0]._sheet.get("pageElements")
print(elements)
