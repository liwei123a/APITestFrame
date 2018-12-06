#coding:utf-8

import json
from custom.case_info import CaseInfo
from lib.request_method import ReqMethod

class RunCase(object):
    def __init__(self, datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec):
        self.case_info = CaseInfo(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)
        self.case_rows = self.case_info.excel.get_table_rows()

    def execution_request(self, url, request_method, header, request_field, fileparams, row, cookies):
        url = self.case_info.get_url(url, row)
        # is_run = self.case_info.get_is_run(is_run, row)
        request_method = self.case_info.get_request_method(request_method, row)
        header = self.case_info.get_header(header, row)
        params = self.case_info.get_request_data(request_field, row)
        # if is_run:
        if header != None:
            header = json.loads(header)
            if 'multipart/form-data' in header['content-type']:
                self.req = ReqMethod(url=url, cookies=cookies, header=header, params=fileparams)
            else:
                self.req = ReqMethod(url=url, cookies=cookies, header=header, params=params)
        else:
            self.req = ReqMethod(url=url, cookies=cookies, params=params)
        res = self.req.req_send(request_method)
        self.cookies = self.req.get_cookies()
        return [res, self.cookies]
        # else:
        #     return None

