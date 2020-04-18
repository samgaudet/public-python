#!/usr/bin/env python3


class Sheet:

    def __init__(self, sheet, spreadsheet,):

        self._sheet = sheet
        self._properties = sheet["properties"]
        self._spreadsheet = spreadsheet

    @property
    def sheetId(self):
        return self._properties["sheetId"]

    @property
    def title(self):
        return self._properties["title"]

    @property
    def sheetIndex(self):
        return self._properties["index"]

    @property
    def sheetType(self):
        return self._properties["sheetType"]

    @property
    def rowCount(self):
        return self._properties["rowCount"]

    @property
    def columnCount(self):
        return self._properties["columnCount"]
