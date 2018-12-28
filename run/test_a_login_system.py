#coding:utf-8

import sys
from run.common_test_set import UrineWebInterfaceTestCase
import run.globalvar as gl

class LoginSystem(UrineWebInterfaceTestCase):
    def test_web_urine_v2_adminInfo_login(self):
        """
        登录系统
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        gl._init()
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)
        gl.set_value('cookies', res[1])
        # global cookies
        # cookies = res[1]u