#coding:utf-8
"""
尿检算法相关
"""


import sys
import re
from run.common_test_set import UrineWebInterfaceTestCase

class AlgorithmCorrelation(UrineWebInterfaceTestCase):
    def test_app_dw_urinalysis_panel_manager_recheck(self):
        """
        尿检复核列表
        :return:
        """
        func_name = 'test_app_dw-urinalysis-panel_manager_recheck'
        expect_result, res, row = self.get_result(func_name)
        actual_result = re.findall(r'<title>\s+(.+)\s+</title>', res[0].text)[0]
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_urineResult(self):
        """
        尿检报告列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_report(self):
        """
        尿检报告统计
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_recheck_getRecheck(self):
        """
        尿检报告详细
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)