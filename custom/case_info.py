#coding:utf-8

from lib.operation_excel import OperationExcel
from lib.operation_json import OperationJson

class CaseInfo(object):
    def __init__(self, datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec):
        self.excel = OperationExcel(datadir, dirsec, dir1, namesec, file1, sheet_id)
        self.json_data = OperationJson(datadir, dirsec, dir2, namesec, file2)
        self.col_section = colsec

    def get_id(self, id, row):
        col = self.excel.conf.get(self.col_section, id)
        return self.excel.get_cell_value(row, col)

    def get_title(self, title, row):
        col = self.excel.conf.get(self.col_section, title)
        return self.excel.get_cell_value(row, col)

    def get_url(self, url, row):
        col = self.excel.conf.get(self.col_section, url)
        return self.excel.get_cell_value(row, col)

    # def get_is_run(self, is_run, row):
    #     flag = None
    #     col = self.excel.conf.get(self.col_section, is_run)
    #     run = self.excel.get_cell_value(row, col)
    #     if run == "yes":
    #         flag = True
    #     else:
    #         flag = False
    #     return flag

    def get_request_method(self, request_method, row):
        col = self.excel.conf.get(self.col_section, request_method)
        return self.excel.get_cell_value(row, col)

    def get_header(self, take_header, row):
        col = self.excel.conf.get(self.col_section, take_header)
        header = self.excel.get_cell_value(row, col)
        if header == '':
            return None
        else:
            return header

    def get_depend_interface(self, depend_interface, row):
        col = self.excel.conf.get(self.col_section, depend_interface)
        return self.excel.get_cell_value(row, col)

    def get_depend_data(self, depend_data, row):
        col = self.excel.conf.get(self.col_section, depend_data)
        return self.excel.get_cell_value(row, col)

    def get_depend_field(self, depend_field, row):
        col = self.excel.conf.get(self.col_section, depend_field)
        depend_field = self.excel.get_cell_value(row, col)
        if depend_field == '':
            return None
        else:
            return depend_field

    def get_request_field(self, request_field, row):
        col = self.excel.conf.get(self.col_section, request_field)
        return self.excel.get_cell_value(row, col)

    def get_request_data(self, request_field, row):
        field = self.get_request_field(request_field, row)
        if field != '':
            return self.json_data.get_field_value(field)
        else:
            return None

    def get_expect_result(self, expect_result, row):
        col = self.excel.conf.get(self.col_section, expect_result)
        return self.excel.get_cell_value(row, col)

    def update_actual_result(self, actual_result, row, value):
        col = self.excel.conf.get(self.col_section, actual_result)
        return self.excel.write_cell_value(row, col, value)

    def get_row_index(self, col, cell_value):
        col_values = self.excel.get_col_values(col)
        row_index = None
        for x in col_values:
            if cell_value in x:
                row_index = col_values.index(x)
        return row_index

    def get_col_index(self, col_name):
        col_index = int(self.excel.conf.get(self.col_section, col_name))
        return col_index