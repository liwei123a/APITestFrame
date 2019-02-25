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
        query_orderlist = self.get_request_data(func_name)
        orderlist_copy = query_orderlist.copy()
        for k in orderlist_copy.keys():
            orderlist_copy[k] = None
        for data in ['pageNum', 'pageSize', 'totalCount']:
            orderlist_copy[data] = query_orderlist[data]
        query = orderlist_copy
        expect_result = self.get_expect_result(func_name)
        """根据手机号查询"""
        query['phone'] = query_orderlist['phone']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        query['pageSize'] = totalCount
        res = self.get_result(func_name, var_params=query)
        order_list = res[0].json()['data']['list']
        for order in order_list:
            self.assertEqual(query['phone'], order['phone'])
        """根据手机号、商品名称查询"""
        query['checkType'] = query_orderlist['checkType']
        res = self.get_result(func_name, var_params=query)
        order_list = res[0].json()['data']['list']
        for order in order_list:
            self.assertEqual(query['phone'], order['phone'])
            self.assertEqual(query['checkType'], order['checkType'])
        """根据手机号、商品名称、城市查询"""
        query['cityId'] = query_orderlist['cityId']
        city_list = self.web_urine_v2_cityAreaSettingInfo_getAllCitys()
        city_name = None
        for city in city_list:
            if city['keyID'] == query['cityId']:
                city_name = city['cityName']
        res = self.get_result(func_name, var_params=query)
        order_list = res[0].json()['data']['list']
        for order in order_list:
            self.assertEqual(query['phone'], order['phone'])
            self.assertEqual(query['checkType'], order['checkType'])
            self.assertEqual(city_name, order['cityName'])
        """根据手机号、商品名称、城市、楼宇查询"""
        query['buildingId'] = query_orderlist['buildingId']
        res = self.get_result(func_name, var_params=query)
        order_list = res[0].json()['data']['list']
        for order in order_list:
            self.assertEqual(query['phone'], order['phone'])
            self.assertEqual(query['checkType'], order['checkType'])
            self.assertEqual(city_name, order['cityName'])
            self.assertEqual(query['buildingId'], order[''])
        """根据手机号、商品名称、城市、楼宇、订单状态查询"""
        query['payStatus'] = query_orderlist['payStatus']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result5 = eval(expect_result)
        self.assertTrue(result5)
        """根据手机号、商品名称、城市、楼宇、订单状态、购买机器查询"""
        query['machineID'] = query_orderlist['machineID']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result6 = eval(expect_result)
        self.assertTrue(result6)
        """根据手机号、商品名称、城市、楼宇、订单状态、购买机器、订单号查询"""
        query['outOrderID'] = query_orderlist['outOrderID']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        result7 = eval(expect_result)
        self.assertTrue(result7)
        """默认查询所有订单"""
        res = self.get_result(func_name, var_params=orderlist_copy)
        totalCount = res[0].json()['data']['totalCount']
        default_result = eval(expect_result)
        self.assertTrue(default_result)

    def test_web_urine_v2_cityAreaSettingInfo_getAreaByCityID(self):
        """
        查询商圈
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_buildingInfo_queryAllBuildingInfo(self):
        """
        查询楼宇
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)