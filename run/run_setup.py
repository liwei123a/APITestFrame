#coding:utf-8

from custom.case_info import CaseInfo
from lib.request_method import ReqMethod

class RunCase(object):
    def __init__(self, datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec):
        self.case_info = CaseInfo(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)
        self.case_rows = self.case_info.excel.get_table_rows()

    def configuration_parameter(self, url, is_run, request_method, header, request_field, row):
        url = self.case_info.get_url(url, row)
        is_run = self.case_info.get_is_run(is_run, row)
        request_method = self.case_info.get_request_method(request_method, row)
        header = self.case_info.get_header(header, row)
        params = self.case_info.get_request_data(request_field, row)
        if is_run:
            if header != None:
                self.req = ReqMethod(url=url, header=header, params=params)
            else:
                self.req = ReqMethod(url=url, params=params)
            res = self.req.req_send(request_method)
            return res
        else:
            return None

    def execution_test(self, url, is_run, request_method, header, request_field, expect_result):
        for row in range(1, self.case_rows):
            res = self.configuration_parameter(url, is_run, request_method, header, request_field, row)
            expect_result = self.case_info.get_expect_result(expect_result, row)


if __name__ == '__main__':
    case = RunCase('../config/data_source.ini', 'path', 'case_dir', 'data_dir', 'file', 'case_file', 'data_file', 0, 'columns')

    case.execution_test('url', 'is_run', 'request_method', 'take_header', 'header', 'request_field')