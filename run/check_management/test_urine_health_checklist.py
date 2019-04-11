#coding:utf-8
"""尿液健康检测列表"""

import sys
import run.globalvar as gl
import random

from run.common_test_set import UrineWebInterfaceTestCase

class UrineHealthChecklist(UrineWebInterfaceTestCase):

    def test_urine_v2_urineInfoList_getRecords(self):
        """
        查询尿液健康检测记录
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        query_urineinfo = self.get_request_data(func_name)
        urineinfo_copy = query_urineinfo.copy()
        for k in urineinfo_copy.keys():
            urineinfo_copy[k] = None
        for data in ['pageNum', 'pageSize', 'totalCount']:
            urineinfo_copy[data] = query_urineinfo[data]
        query = urineinfo_copy
        """默认查询所有记录"""
        res = self.get_result(func_name, var_params=urineinfo_copy)
        totalCount = res[0].json()['data']['totalCount']
        expect_result = self.get_expect_result(func_name)
        default_result = eval(expect_result)
        self.assertTrue(default_result)
        """根据手机号查询"""
        query['phone'] = query_urineinfo['phone']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        query['pageSize'] = totalCount
        res = self.get_result(func_name, var_params=query)
        check_list = res[0].json()['data']['list']
        for check in check_list:
            self.assertEqual(query['phone'], check['phone'])
        """根据手机号、检测机器查询"""
        query['machineID'] = query_urineinfo['machineID']
        res = self.get_result(func_name, var_params=query)
        check_list = res[0].json()['data']['list']
        for check in check_list:
            self.assertEqual(query['phone'], check['phone'])
            self.assertEqual(query['machineID'], check['machineID'])
        """根据手机号、检测机器、检测状态查询"""
        query['checkStatus'] = query_urineinfo['checkStatus']
        res = self.get_result(func_name, var_params=query)
        check_list = res[0].json()['data']['list']
        for check in check_list:
            self.assertEqual(query['phone'], check['phone'])
            self.assertEqual(query['machineID'], check['machineID'])
            self.assertEqual(query['checkStatus'], check['checkStatus'])
        urineinfolist = res[0].json()['data']['list']
        for urineinfo in urineinfolist:
            if urineinfo['checkStatus'] != 1:
                urineinfolist.remove(urineinfo)
        gl.set_value('urineinfolist', urineinfolist)

    def test_urine_v2_urineInfoList_getResult(self):
        """
        查看尿液检测报告
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        mac_token = self.get_request_data(func_name)
        urineinfolist = gl.get_value('urineinfolist')
        mac_token['macToken'] = random.sample(urineinfolist, 1)[0]['macToken']
        res = self.get_result(func_name, var_params=mac_token)
        actual_result = res[0].json()['errmsg']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)