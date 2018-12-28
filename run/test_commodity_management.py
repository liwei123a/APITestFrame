#coding:utf-8

import random
import sys
from lib.read_config import ConfReader
from run.common_test_set import UrineWebInterfaceTestCase

class CommodityManagement(UrineWebInterfaceTestCase):
    def test_web_urine_v2_qiniu_getToken(self):
        """
        获取七牛token
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        return res[0].json()

    def test_upload(self):
        """
        上传文件
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        token = self.get_depend_params(func_name)
        conf_read = ConfReader(self.datadir, self.dirsec, self.dir3, self.namesec, self.file3)
        file_path = conf_read.get_file_path()
        file_name = conf_read.get_file_name()
        fileparams = {
            'token': (None, token),
            'file': (file_name, open(file_path, 'rb'), 'image/jpeg')
        }
        expect_result, res, row = self.get_result(func_name, fileparams=fileparams)
        return res[0].json()

    def test_web_urine_v2_goodsInfo_saveGoodsInfo(self):
        """
        添加商品
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        hash = self.get_depend_params(func_name)
        row = self.get_case_row_index(func_name)
        request_data = self.run_case.case_info.get_request_data(self.request_field, row)
        for imgs in ['imgs', 'detailImgs', 'bigProductImgs', 'bigImgs']:
            request_data[imgs] += hash
        randomId = random.random()
        randomId_en = random.random()
        request_data['goodsScenes'][0]['randomId'] = randomId
        request_data['goodsScenesEn'][0]['randomId'] = randomId_en
        expect_result, res, row = self.get_result(func_name, var_params=request_data)
        actual_result = res[0].json()['data']
        self.update_result(row, actual_result, expect_result)

    def test_web_urine_v2_goodsInfo_queryGoodsInfos(self):
        """
        查询商品信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        expect_result, res, row = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        self.update_result(row, actual_result, expect_result)
        return res[0].json()

    def test_web_urine_v2_goodsInfo_removeGoodsInfo(self):
        """
        删除商品
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        goods_info = self.run_case.case_info.get_request_data(self.request_field, row)
        goods_name = goods_info['goodsName']
        goods_id = goods_info['keyID']
        goods_list = self.get_depend_params(func_name)
        for goods in goods_list:
            if goods['goodsName'] == goods_name:
                goods_id = goods['keyID']
        request_data = {}
        request_data['keyID'] = goods_id
        expect_result, res, row = self.get_result(func_name, var_params=request_data)
        actual_result = res[0].json()['data']
        self.update_result(row, actual_result, expect_result)