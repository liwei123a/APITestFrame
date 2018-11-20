#coding:utf-8

import json
from custom.case_info import CaseInfo
from lib.request_method import ReqMethod

class RunCase(object):
    def __init__(self, datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec):
        self.case_info = CaseInfo(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)
        self.case_rows = self.case_info.excel.get_table_rows()

    def execution_request(self, url, is_run, request_method, header, request_field, row):
        url = self.case_info.get_url(url, row)
        is_run = self.case_info.get_is_run(is_run, row)
        request_method = self.case_info.get_request_method(request_method, row)
        header = json.loads(self.case_info.get_header(header, row))
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

