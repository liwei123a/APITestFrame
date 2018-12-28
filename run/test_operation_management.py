#coding:utf-8

import sys
from run.common_test_set import UrineWebInterfaceTestCase

class OperationManagement(UrineWebInterfaceTestCase):
    def test_web_urine_v2_bannerInfo_list(self):
        """
        小程序banner列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)