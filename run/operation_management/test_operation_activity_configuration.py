#coding:utf-8
"""运营活动配置"""

import sys
import run.globalvar as gl
import datetime
import random
from run.common_test_set import UrineWebInterfaceTestCase

class OperationActivityConfiguration(UrineWebInterfaceTestCase):

    def test_urine_v2_activityInfo_list(self):
        """
        运营活动配置列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        expect_result = self.get_expect_result(func_name)
        activityInfo_list = res[0].json()['data']
        actual_result = res[0].json()['errmsg']
        self.assertIn(actual_result, expect_result)
        self.assertIsNotNone(activityInfo_list)
        gl.set_value('activityInfo_list', activityInfo_list)

    def test_urine_v2_activityInfo_update(self):
        """
        更新运营活动配置信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        activityInfo_list = gl.get_value('activityInfo_list')
        activity_info = random.sample(activityInfo_list, 1)[0]
        activity_info_copy = activity_info.copy()
        activity_info_copy['activityStartDate'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        activity_info_copy['activityEndDate'] = (datetime.datetime.now()+datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        activity_info_copy['isEnable'] = 0
        activity_info_copy['isLableShow'] = 0
        expect_result = self.get_expect_result(func_name)
        res = self.get_result(func_name, var_params=activity_info_copy)
        actual_result = res[0].json()['data']
        self.assertIn(actual_result, expect_result)
        res = self.get_result(func_name, var_params=activity_info)
        actual_result = res[0].json()['data']
        self.assertIn(actual_result, expect_result)
