#coding:utf-8
"""推荐商品管理"""

import sys
import run.globalvar as gl
import time

from run.common_test_set import UrineWebInterfaceTestCase

class RecommendedCommodityManagement(UrineWebInterfaceTestCase):

    def test_urine_v2_recommendGoodsInfo_list(self):
        """
        推荐商品列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        query_type = self.get_request_data(func_name)
        expect_result = self.get_expect_result(func_name)
        """默认查询所有推荐商品"""
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        recommend_goodsInfo_list = res[0].json()['data']
        self.assertIn(actual_result, expect_result)
        self.assertIsNotNone(recommend_goodsInfo_list)
        """根据图片类型、使用类型查询"""
        for show_type in range(2):
            for use_type in range(3):
                query_type['useType'] = use_type
                query_type['showType'] = show_type
                res = self.get_result(func_name, var_params=query_type)
                actual_result = res[0].json()['errmsg']
                recommend_goodsInfo_list = res[0].json()['data']
                self.assertIn(actual_result, expect_result)
                self.assertIsNotNone(recommend_goodsInfo_list)

    def test_urine_v2_recommendGoodsInfo_add(self):
        """
        添加推荐商品
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        recommended_commodity_info = self.get_request_data(func_name)
        expect_result = self.get_expect_result(func_name)
        recommended_commodity_info['recommendGoodsPicUrl'] += gl.get_value('hash')
        for date in ['recommendGoodsShowStartDate', 'recommendGoodsShowEndDate', 'recommendGoodsStartDate', 'recommendGoodsEndDate']:
            recommended_commodity_info[date] = int(time.time()*1000)
        for show_type in range(2):
            for use_type in range(3):
                recommended_commodity_info['useType'] = use_type
                recommended_commodity_info['showType'] = show_type
                res = self.get_result(func_name, var_params=recommended_commodity_info)
                actual_result = res[0].json()['data']
                self.assertIn(actual_result, expect_result)