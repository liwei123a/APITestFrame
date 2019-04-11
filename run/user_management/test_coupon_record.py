#coding:utf-8
"""优惠券记录"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase

class CouponRecord(UrineWebInterfaceTestCase):

    def test_urine_v2_couponGiftLog_couponGiftLogList(self):
        """
        查询优惠券记录
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        totalCount = res[0].json()['data']['totalCount']
        expect_result = self.get_expect_result(func_name)
        self.assertTrue(eval(expect_result))