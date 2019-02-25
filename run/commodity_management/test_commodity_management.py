#coding:utf-8
"""
商品管理
"""


import random
import sys
from lib.read_config import ConfReader
from run.common_test_set import UrineWebInterfaceTestCase
import run.globalvar as gl

class CommodityManagement(UrineWebInterfaceTestCase):

    def test_web_urine_v2_goodsInfo_saveGoodsInfo(self):
        """
        添加商品
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        hash = gl.get_value('hash')
        row = self.get_case_row_index(func_name)
        request_data = self.get_request_data(func_name)
        for imgs in ['imgs', 'detailImgs', 'bigProductImgs', 'bigImgs']:
            request_data[imgs] += hash
        randomId = random.random()
        randomId_en = random.random()
        request_data['goodsScenes'][0]['randomId'] = randomId
        request_data['goodsScenesEn'][0]['randomId'] = randomId_en
        res = self.get_result(func_name, var_params=request_data)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_goodsInfo_queryGoodsInfos(self):
        """
        查询商品信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
        gl.set_value('goods_list', res[0].json()['data']['list'])
        # return res[0].json()

    def test_web_urine_v2_goodsInfo_updateGoodsInfo(self):
        """
        更新商品信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        update_goods_info = self.get_request_data(func_name)
        goods_name = update_goods_info['goodsName']
        # goods_list = self.get_depend_params(func_name)
        goods_list = gl.get_value('goods_list')
        for goods in goods_list:
            if goods['goodsName'] == goods_name:
                gl.set_value('goods_info', goods)
        for data in update_goods_info:
            gl.get_value('goods_info')[data] = update_goods_info[data]
        res = self.get_result(func_name, var_params=gl.get_value('goods_info'))
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_goodsInfo_removeGoodsInfo(self):
        """
        删除商品
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        goods_info = self.get_request_data(func_name)
        for data in goods_info:
            goods_info[data] = gl.get_value('goods_info')[data]
        res = self.get_result(func_name, var_params=goods_info)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)