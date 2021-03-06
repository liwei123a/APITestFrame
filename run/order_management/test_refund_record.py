#coding:utf-8
"""退款记录"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase

class RefundRecord(UrineWebInterfaceTestCase):

    def test_urine_v2_order_refundLogList(self):
        """
        查询所有退款记录
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)