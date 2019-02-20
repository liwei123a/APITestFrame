#coding:utf-8
"""退款记录"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase

class RefundRecord(UrineWebInterfaceTestCase):

    def test_web_urine_v2_order_refundLogList(self):
        """
        查询所有退款记录
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)