#coding:utf-8

import xlrd
import os
import configparser
from xlutils.copy import copy

class OperationExcel(object):
    def __init__(self, datadir, dirsec, filedir, namesec, filename, sheetID):
        self.conf = configparser.ConfigParser()
        self.conf.read(datadir)
        self.file = os.path.join(self.conf.get(dirsec, filedir), self.conf.get(namesec, filename))
        self.tables = xlrd.open_workbook(self.file)
        self.sheetID = sheetID
        self.table = self.tables.sheets()[self.sheetID]

    def get_table_rows(self):
        return self.table.nrows

    def get_table_cols(self):
        return self.table.ncols

    def get_cell_value(self, row, col):
        return self.table.cell_value(int(row), int(col))

    def write_cell_value(self, row, col, value):
        tablescopy = copy(self.tables)
        tablecopy = tablescopy.get_sheet(self.sheetID)
        tablecopy.write(int(row), int(col), value)
        tablescopy.save(self.file)

# excel = OperationExcel('../config/data_source.ini', 'path', 'case_dir', 'file', 'case_file', 0)
