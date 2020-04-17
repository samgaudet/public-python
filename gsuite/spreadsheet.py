#!/usr/bin/env python3

from gsuite.sheet import Sheet


class Spreadsheet:

    def __init__(self, client, spreadsheetId,):

        self._client = client
        self._spreadsheetId = spreadsheetId
        self._spreadsheet = self._client.spreadsheets().get(
            spreadsheetId=spreadsheetId).execute()

    @property
    def sheets(self):
        return [sheet for sheet in self._spreadsheet.get("sheets")]

    def create_sheet(self):
        pass

    def update_sheet(self):
        pass
