import unittest
import HtmlTestRunner
import sys
import re
from run.run_setup import RunCase

cookies = None

class UrineWebInterfaceTestCase(unittest.TestCase):

    url = 'url'
    is_run = 'is_run'
    request_method = 'request_method'
    header = 'header'
    request_field = 'request_field'
    expect_result = 'expect_result'
    actual_result = 'actual_result'

    @classmethod
    def setUpClass(cls):
        datadir = '../config/data_source.ini'
        dirsec = 'path'
        dir1 = 'case_dir'
        dir2 = 'data_dir'
        namesec = 'file'
        file1 = 'case_file'
        file2 = 'data_file'
        sheet_id = 0
        colsec = 'columns'
        cls.run_case = RunCase(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)

    def get_result(self, func_name):
        case_id = re.findall(r'test_(\w+)', func_name)[0].replace('_', '-')
        row = self.run_case.case_info.get_row(0, case_id)
        res = self.run_case.execution_request(self.url, self.is_run, self.request_method, self.header,
                                              self.request_field, row, cookies)
        expect_result = self.run_case.case_info.get_expect_result(self.expect_result, row)
        return expect_result, res, row

    def update_result(self, row, actual_result, expect_result):
        if actual_result in expect_result:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'pass')
        else:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'fail')
        self.assertIn(actual_result, expect_result)

    def test_UrineWeb_001(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)
        global cookies
        cookies = res[1]

    def test_UrineWeb_002(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = re.findall(r'<title>\s+(.+)\s+</title>', res[0].text)[0]
        self.update_result(row, actual_result, expect_result)

    def test_UrineWeb_003(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_UrineWeb_004(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_UrineWeb_005(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_UrineWeb_006(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\interface'))
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(UrineWebInterfaceTestCase('test1'))
    # suite.addTest(UrineWebInterfaceTestCase('test2'))
    # filepath = "D:\\interface"
    # runner = HtmlTestRunner.HTMLTestRunner(output=filepath)
    # runner.run(suite)

