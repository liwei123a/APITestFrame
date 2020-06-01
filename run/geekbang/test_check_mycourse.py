# -*- coding:utf-8 -*-

import sys
import time
from run.common_test_set import UrineWebInterfaceTestCase

class TestCheckMyCourse(UrineWebInterfaceTestCase):
    def test_serv_v1_user_auth(self):
        """
        校验用户
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name, var_params=str(int(time.time()*1000)))
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_serv_v1_my_data(self):
        """
        检查我的课程
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_serv_v3_search_hot(self):
        """
        检查我的课程
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_serv_v1_user_check(self):
        """
        检查用户
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_serv_v3_learn_product(self):
        """
        检查我的课程
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)