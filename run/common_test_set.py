import unittest
import re
from run.run_setup import RunCase
import run.globalvar as gl


class UrineWebInterfaceTestCase(unittest.TestCase):

    url = 'url'
    request_method = 'request_method'
    header = 'header'
    depend_interface = 'depend_interface'
    depend_data = 'depend_data'
    depend_field = 'depend_field'
    request_field = 'request_field'
    expect_result = 'expect_result'
    actual_result = 'actual_result'
    datadir = '../config/data_source.ini'
    dirsec = 'path'
    dir1 = 'case_dir'
    dir2 = 'data_dir'
    dir3 = 'pic_dir'
    namesec = 'file'
    file1 = 'case_file'
    file2 = 'data_file'
    file3 = 'pic_file'
    sheet_id = 0
    colsec = 'columns'

    @classmethod
    def setUpClass(cls):
        cls.run_case = RunCase(cls.datadir, cls.dirsec, cls.dir1, cls.dir2, cls.namesec, cls.file1, cls.file2, cls.sheet_id, cls.colsec)

    def get_case_row_index(self, func_name):
        case_url = re.findall(r'test(\w+)', func_name)[0].replace('_', '/')
        col_index = self.run_case.case_info.get_col_index(self.url)
        row = self.run_case.case_info.get_row_index(col_index, case_url)
        return row

    def get_result(self, func_name, fileparams=None, var_params=None):
        row = self.get_case_row_index(func_name)
        cookies = gl.get_value('cookies')
        res = self.run_case.execution_request(self.url, self.request_method, self.header,
                                              self.request_field, fileparams, var_params, row, cookies)
        expect_result = self.run_case.case_info.get_expect_result(self.expect_result, row)
        return expect_result, res, row

    def get_depend_params(self, func_name):
        row = self.get_case_row_index(func_name)
        depend_interface = self.run_case.case_info.get_depend_interface(self.depend_interface, row)
        pre_funcname = depend_interface.replace('/', '_')
        for func in dir(self):
            if pre_funcname in func:
                pre_funcname = func
        depend_json_data = eval('self.' + pre_funcname + '()')
        depend_field = self.run_case.case_info.get_depend_field(self.depend_field, row)
        depend_data = self.run_case.case_info.get_depend_field(self.depend_data, row)
        depend_params = None
        if depend_field:
            depend_params = depend_json_data[depend_field][depend_data]
        else:
            depend_params = depend_json_data[depend_data]
        return depend_params

    def update_result(self, row, actual_result, expect_result):
        if actual_result in expect_result:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'pass')
        else:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'fail')
        self.assertIn(actual_result, expect_result)
