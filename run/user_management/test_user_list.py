#coding:utf-8
"""用户列表"""

import sys
import run.globalvar as gl
import random

from run.common_test_set import UrineWebInterfaceTestCase

class UserList(UrineWebInterfaceTestCase):

    def test_web_urine_v2_couponManager_getAllCouponRules(self):
        """
        查询所有优惠券
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        errmsg = res[0].json()['errmsg']
        couponrule_list = res[0].json()['data']
        gl.set_value('couponrule_list', couponrule_list)
        expect_errmsg = self.get_expect_result(func_name)
        row = self.get_case_row_index(func_name)
        self.update_result(row, errmsg, expect_errmsg)
        self.assertGreaterEqual(couponrule_list.__len__(), 0)

    def test_web_urine_v2_userInfo_getUserList(self):
        """
        查询用户列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        """默认查询所有用户"""
        res = self.get_result(func_name)
        totalCount = res[0].json()['data']['totalCount']
        expect_result = self.get_expect_result(func_name)
        self.assertTrue(eval(expect_result))
        """根据手机号查询"""
        user_phone = self.get_request_data(func_name)
        res = self.get_result(func_name, var_params=user_phone)
        user_info = res[0].json()['data']['list'][0]
        self.assertEqual(user_phone['phone'], user_info['phone'])

    def test_web_urine_v2_userInfo_giftCoupons(self):
        """
        赠送优惠券
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        coupon_info = self.get_request_data(func_name)
        couponrule_list = gl.get_value('couponrule_list')
        coupon_rand = random.sample(couponrule_list, 1)[0]
        coupon_info['couponId'] = coupon_rand['id']
        coupon_info['couponType'] = coupon_rand['couponType']
        coupon_info['couponName'] = coupon_rand['name']
        coupon_info['price'] = coupon_rand['price']
        selectedCoupon = []
        for data in ['couponId', 'couponType', 'couponName', 'discount', 'price']:
            selectedCoupon.append(str(coupon_info[data]))
        coupon_info['selectedCoupon'] = '~'.join(selectedCoupon)
        res = self.get_result(func_name, var_params=coupon_info)
        expect_result = self.get_expect_result(func_name)
        actual_result = res[0].json()['data']
        row = self.get_case_row_index(func_name)
        self.update_result(row, actual_result, expect_result)