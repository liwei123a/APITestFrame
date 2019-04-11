#coding:utf-8
"""
标签管理
"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase


class MachineManagement(UrineWebInterfaceTestCase):

    def test_urine_v2_labelInfo_labelList(self):
        """
        查询标签列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)