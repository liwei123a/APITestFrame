import unittest
import re
import sys
from lib.read_config import ConfReader
from run.run_setup import RunCase
import run.globalvar as gl


class UrineWebInterfaceTestCase(unittest.TestCase):

    url = 'url'
    request_method = 'request_method'
    header = 'header'
    # depend_interface = 'depend_interface'
    # depend_data = 'depend_data'
    # depend_field = 'depend_field'
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
        """
        从excel表格读取测试用例
        :return:
        """
        cls.run_case = RunCase(cls.datadir, cls.dirsec, cls.dir1, cls.dir2, cls.namesec, cls.file1, cls.file2, cls.sheet_id, cls.colsec)

    def get_case_row_index(self, func_name):
        """
        获取用例行号
        :param func_name:
        :return:
        """
        case_url = None
        if 'test' in func_name:
            case_url = re.findall(r'test(\w+)', func_name)[0].replace('_', '/')
        else:
            case_url = func_name.replace('_', '/')
        col_index = self.run_case.case_info.get_col_index(self.url)
        row = self.run_case.case_info.get_row_index(col_index, case_url)
        return row

    def get_result(self, func_name, fileparams=None, var_params=None):
        """
        执行用例，并返回结果
        :param func_name:
        :param fileparams:
        :param var_params:
        :return:
        """
        row = self.get_case_row_index(func_name)
        cookies = gl.get_value('cookies')
        res = self.run_case.execution_request(self.url, self.request_method, self.header,
                                              self.request_field, fileparams, var_params, row, cookies)
        return res

    def get_expect_result(self, func_name):
        """
        获取预期结果
        :param func_name:
        :return:
        """
        row = self.get_case_row_index(func_name)
        expect_result = self.run_case.case_info.get_expect_result(self.expect_result, row)
        return expect_result

    def get_request_data(self, func_name):
        """
        获取请求参数
        :param func_name:
        :return:
        """
        row = self.get_case_row_index(func_name)
        request_data = self.run_case.case_info.get_request_data(self.request_field, row)
        return request_data

    # def get_depend_params(self, func_name):
    #     """
    #     获取依赖数据
    #     :param func_name:
    #     :return:
    #     """
    #     row = self.get_case_row_index(func_name)
    #     depend_interface = self.run_case.case_info.get_depend_interface(self.depend_interface, row)
    #     pre_funcname = depend_interface.replace('/', '_')
    #     for func in dir(self):
    #         if pre_funcname in func:
    #             pre_funcname = func
    #     depend_json_data = eval('self.' + pre_funcname + '()')
    #     print(pre_funcname)
    #     print(depend_json_data)
    #     depend_field = self.run_case.case_info.get_depend_field(self.depend_field, row)
    #     depend_data = self.run_case.case_info.get_depend_field(self.depend_data, row)
    #     depend_params = None
    #     if depend_field:
    #         depend_params = depend_json_data[depend_field][depend_data]
    #     else:
    #         depend_params = depend_json_data[depend_data]
    #     return depend_params

    def update_result(self, row, actual_result, expect_result):
        """
        更新excel表格测试结果并进行断言
        :param row:
        :param actual_result:
        :param expect_result:
        :return:
        """
        if actual_result in expect_result:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'pass')
        else:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'fail')
        self.assertIn(actual_result, expect_result)

    def urine_v2_qiniu_getToken(self):
        """
        获取七牛token
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()

    def upload(self):
        """
        上传文件
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        token = self.urine_v2_qiniu_getToken()['data']['token']
        conf_read = ConfReader(self.datadir)
        file_path = conf_read.get_file_path( self.dirsec, self.dir3, self.namesec, self.file3)
        file_name = conf_read.get_file_name( self.namesec, self.file3)
        fileparams = {
            'token': (None, token),
            'file': (file_name, open(file_path, 'rb'), 'image/jpeg')
        }
        res = self.get_result(func_name, fileparams=fileparams)
        return res[0].json()

    def urine_v2_cityAreaSettingInfo_getAllCitys(self):
        """
        获取城市列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()['data']

    def urine_v2_buildingInfo_queryAllBuildingInfo(self):
        """
        获取楼宇列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()['data']