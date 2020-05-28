# -*- coding:utf-8 -*-
"""
登录
"""

import sys
from run.common_test_set import UrineWebInterfaceTestCase
import run.globalvar as gl

class TestLogin(UrineWebInterfaceTestCase):
    def test_account_ticket_login(self):
        """
        登录系统
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        gl._init()
        res = self.get_result(func_name)
        actual_result = str(res[0].json()['code'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
        gl.set_value('cookies', res[1])