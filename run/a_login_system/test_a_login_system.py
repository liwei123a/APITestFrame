#coding:utf-8
"""
登录系统及修改密码
"""

import sys
from run.common_test_set import UrineWebInterfaceTestCase
import run.globalvar as gl

class LoginSystem(UrineWebInterfaceTestCase):
    def test_urine_v2_adminInfo_login(self):
        """
        登录系统
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        gl._init()
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
        hash = self.upload()['hash']
        gl.set_value('cookies', res[1])
        gl.set_value('hash', hash)

    def test_urine_v2_adminInfo_modifyPassword(self):
        """
        修改登录密码
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
