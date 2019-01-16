#coding:utf-8
"""
退出系统
"""


import sys
from run.common_test_set import UrineWebInterfaceTestCase

class LogoutSystem(UrineWebInterfaceTestCase):
    def test_web_urine_v2_adminInfo_loginOut(self):
        """
        退出登录
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)
