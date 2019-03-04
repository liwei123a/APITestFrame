#coding:utf-8
"""视频版广告策略管理"""

import sys
import run.globalvar as gl
from run.common_test_set import UrineWebInterfaceTestCase

class StrategyManagementOfVideoEditionAdvertising(UrineWebInterfaceTestCase):

    def test_web_urine_v2_adPlanInfo_saveAdPlan(self):
        """
        添加视频广告策略
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        ad_plan_info = self.get_request_data(func_name)
        expect_errmsg = self.get_expect_result(func_name)
        """添加策略(不播放广告)"""
        ad_plan_info['playType'] = 1
        res = self.get_result(func_name, var_params=ad_plan_info)
        actual_errmsg = res[0].json()['errmsg']
        self.assertIn(actual_errmsg, expect_errmsg)
        """添加策略(单张播放)"""
        ad_plan_info['playType'] = 2
        ad_plan_info['adImagePlayDuration'] = 5
        res = self.get_result(func_name, var_params=ad_plan_info)
        actual_errmsg = res[0].json()['errmsg']
        self.assertIn(actual_errmsg, expect_errmsg)
        """添加策略(全部播放)"""
        ad_plan_info['playType'] = 3
        ad_plan_info['adImagePlayDuration'] = 3
        res = self.get_result(func_name, var_params=ad_plan_info)
        actual_errmsg = res[0].json()['errmsg']
        self.assertIn(actual_errmsg, expect_errmsg)

    def test_web_urine_v2_adPlanInfo_adPlanList(self):
        """
        查询策略列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        totalCount = res[0].json()['data']['totalCount']
        ad_plan_list = res[0].json()['data']['list']
        gl.set_value('ad_plan_list', ad_plan_list)
        expect_result = self.get_expect_result(func_name)
        self.assertTrue(eval(expect_result))

    def test_web_urine_v2_adPlanInfo_canBeDelete(self):
        """
        视频广告策略能否被删除
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        ad_plan_name = self.get_request_data(func_name)
        plan_name = ad_plan_name['planName']
        ad_plan_list = gl.get_value('ad_plan_list')
        expect_result = self.get_expect_result(func_name)
        key_id_list = []
        for ad in ad_plan_list:
            if ad['planName'] == plan_name:
                key_id = {}
                key_id['keyId'] = ad['keyID']
                res = self.get_result(func_name, var_params=key_id)
                actual_result = res[0].json()['errmsg']
                self.assertIn(actual_result, expect_result)
                data = res[0].json()['data']
                self.assertEqual(data, 0)
                key_id_list.append(key_id['keyId'])
        gl.set_value('key_id_list', key_id_list)

    def test_web_urine_v2_adPlanInfo_deleteAdPlan(self):
        """
        删除视频广告策略
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        key_id = self.get_request_data(func_name)
        key_id_list = gl.get_value('key_id_list')
        expect_result = self.get_expect_result(func_name)
        for key in key_id_list:
            key_id['keyId'] = key
            res = self.get_result(func_name, var_params=key_id)
            actual_result = res[0].json()['errmsg']
            self.assertIn(actual_result, expect_result)