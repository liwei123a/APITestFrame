import unittest
import HtmlTestRunner
import sys
import re
import json
import random
from run.run_setup import RunCase
from lib.read_config import ConfReader

cookies = None

class UrineWebInterfaceTestCase(unittest.TestCase):

    url = 'url'
    # is_run = 'is_run'
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
        res = self.run_case.execution_request(self.url, self.request_method, self.header,
                                              self.request_field, fileparams, var_params, row, cookies)
        expect_result = self.run_case.case_info.get_expect_result(self.expect_result, row)
        return expect_result, res, row

    def get_depend_params(self, func_name):
        row = self.get_case_row_index(func_name)
        depend_interface = self.run_case.case_info.get_depend_interface(self.depend_interface, row)
        pre_funcname = 'test' + depend_interface.replace('/', '_')
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

    def test_web_urine_v2_adminInfo_login(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)
        global cookies
        cookies = res[1]

    def test_app_dw_urinalysis_panel_manager_recheck(self):
        func_name = 'test_app_dw-urinalysis-panel_manager_recheck'
        expect_result, res, row = self.get_result(func_name)
        actual_result = re.findall(r'<title>\s+(.+)\s+</title>', res[0].text)[0]
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_urineResult(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_report(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_getRecheck(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_bannerInfo_list(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    # @unittest.skip('获取七牛token 无需单独执行')
    def test_web_urine_v2_qiniu_getToken(self):
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        return res[0].json()

    def test_upload(self):
        func_name = sys._getframe().f_code.co_name
        token = self.get_depend_params(func_name)
        conf_read = ConfReader(self.datadir, self.dirsec, self.dir3, self.namesec, self.file3)
        file_path = conf_read.get_file_path()
        file_name = conf_read.get_file_name()
        fileparams = {
            'token': (None, token),
            'file': (file_name, open(file_path, 'rb'), 'image/jpeg')
        }
        expect_result, res, row = self.get_result(func_name, fileparams=fileparams)
        return res[0].json()

    def test_web_urine_v2_goodsInfo_saveGoodsInfo(self):
        func_name = sys._getframe().f_code.co_name
        hash = self.get_depend_params(func_name)
        row = self.get_case_row_index(func_name)
        request_data = self.run_case.case_info.get_request_data(self.request_field, row)
        for imgs in ['imgs', 'detailImgs', 'bigProductImgs', 'bigImgs']:
            request_data[imgs] += hash
        randomId = random.random()
        randomId_en = random.random()
        request_data['goodsScenes'][0]['randomId'] = randomId
        request_data['goodsScenesEn'][0]['randomId'] = randomId_en
        expect_result, res, row = self.get_result(func_name, var_params=request_data)
        actual_result = res[0].json()['data']
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
