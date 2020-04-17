#!/usr/bin/env python3


class Sheet:

    def __init__(self, sheet, spreadsheet,):

        self._sheet = sheet
        self._spreadsheet = spreadsheet

    @property
    def sheetId(self):
        return self._sheet["sheetId"]
