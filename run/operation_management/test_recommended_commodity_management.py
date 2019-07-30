#coding:utf-8
"""推荐商品管理"""

import sys
import run.globalvar as gl
import time

from run.common_test_set import UrineWebInterfaceTestCase

class RecommendedCommodityManagement(UrineWebInterfaceTestCase):

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
        gl.set_value('recommend_goodsInfo_list', recommend_goodsInfo_list)
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

    def test_urine_v2_recommendGoodsInfo_update(self):
        """
        更新推荐商品信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        update_commodity_info = self.get_request_data(func_name)
        recommend_goodsInfo_list = gl.get_value('recommend_goodsInfo_list')
        expect_result = self.get_expect_result(func_name)
        update_goodsInfo_list = []
        for goodsinfo in recommend_goodsInfo_list:
            if goodsinfo['recommendGoodsName'] == update_commodity_info['recommendGoodsName']:
                update_goodsInfo_list.append(goodsinfo)
        for goodsinfo in update_goodsInfo_list:
            goodsinfo['cityID'] = update_commodity_info['cityID']
            goodsinfo['showStartEndTime'] = update_commodity_info['showStartEndTime']
            goodsinfo['startEndTime'] = update_commodity_info['startEndTime']
            res = self.get_result(func_name, var_params=goodsinfo)
            actual_result = res[0].json()['data']
            self.assertIn(actual_result, expect_result)

    def test_urine_v2_recommendGoodsInfo_moveupdown(self):
        """
        交换推荐商品顺序
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        recommend_goodsInfo_list = gl.get_value('recommend_goodsInfo_list')
