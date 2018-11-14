#coding:utf-8

from custom.case_info import CaseInfo
from lib.request_method import ReqMethod

class RunCase(object):
    def __init__(self, datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec):
        self.case_info = CaseInfo(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)
