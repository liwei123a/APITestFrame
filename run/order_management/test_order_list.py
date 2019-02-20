#coding:utf-8
"""订单列表"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase


class OrderList(UrineWebInterfaceTestCase):

    def test_web_urine_v2_order_getUrineOrderList(self):
        """
        查询订单
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        query_orderlist = self.run_case.case_info.get_request_data(self.request_field, row)
        orderlist_copy = query_orderlist.copy()
        for k in orderlist_copy.keys():
            orderlist_copy[k] = None
        for data in ['pageNum', 'pageSize', 'totalCount']:
            orderlist_copy[data] = query_orderlist[data]
        query = orderlist_copy
        """根据手机号查询"""
        query['phone'] = query_orderlist['phone']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result1 = eval(expect_result)
        self.assertTrue(result1)
        """根据手机号、商品名称查询"""
        query['checkType'] = query_orderlist['checkType']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result2 = eval(expect_result)
        self.assertTrue(result2)
        """根据手机号、商品名称、城市查询"""
        query['cityId'] = query_orderlist['cityId']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result3 = eval(expect_result)
        self.assertTrue(result3)
        """根据手机号、商品名称、城市、楼宇查询"""
        query['buildingId'] = query_orderlist['buildingId']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result4 = eval(expect_result)
        self.assertTrue(result4)
        """根据手机号、商品名称、城市、楼宇、订单状态查询"""
        query['payStatus'] = query_orderlist['payStatus']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result5 = eval(expect_result)
        self.assertTrue(result5)
        """根据手机号、商品名称、城市、楼宇、订单状态、购买机器查询"""
        query['machineID'] = query_orderlist['machineID']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result6 = eval(expect_result)
        self.assertTrue(result6)
        """根据手机号、商品名称、城市、楼宇、订单状态、购买机器、订单号查询"""
        query['outOrderID'] = query_orderlist['outOrderID']
        expect_result, res, row = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result7 = eval(expect_result)
        self.assertTrue(result7)
        """默认查询所有订单"""
        expect_result, res, row = self.get_result(func_name, var_params=orderlist_copy)
        totalCount = res[0].json()['data']['totalCount']
        default_result = eval(expect_result)
        self.assertTrue(default_result)

    def test_web_urine_v2_cityAreaSettingInfo_getAreaByCityID(self):
        """
        查询商圈
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_buildingInfo_queryAllBuildingInfo(self):
        """
        查询楼宇
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)