#coding:utf-8
"""
广告图组管理
"""

import sys
import time
import run.globalvar as gl
from run.common_test_set import UrineWebInterfaceTestCase

class AdvertisingMapManagement(UrineWebInterfaceTestCase):

    def test_urine_v2_MacActvImageMainInfo_save(self):
        """
        添加广告图组
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        hash = gl.get_value('hash')
        image_info = self.get_request_data(func_name)
        image_info['macActvImageSubInfoVos'][0]['imagePath'] += hash
        res = self.get_result(func_name, var_params=image_info)
        actual_result = res[0].json()['errmsg']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_MacActvImageMainInfo_queryMacActvImageMainInfos(self):
        """
        广告图组列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
        gl.set_value('imageinfo_list', res[0].json()['data']['list'])

    def test_urine_v2_MacActvImageMainInfo_update(self):
        """
        修改广告图组
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        update_imageinfo = self.get_request_data(func_name)
        imageinfo_list = gl.get_value('imageinfo_list')
        acImageName = update_imageinfo['acImageName']
        acimageinfo = None
        for imageinfo in imageinfo_list:
            if imageinfo['acImageName'] == acImageName:
                acimageinfo = imageinfo
        gl.set_value('acimageinfo', acimageinfo)
        modify_time = int(time.time()*1000)
        external_info = {
            'keyID': acimageinfo['keyID'],
            'addTime': acimageinfo['addTime'],
            'modifyTime': modify_time
        }
        internal_info = {
            'keyID': acimageinfo['macActvImageSubInfoVos'][0]['keyID'],
            'macActvImageId': acimageinfo['macActvImageSubInfoVos'][0]['macActvImageId'],
            'imagePath': acimageinfo['macActvImageSubInfoVos'][0]['imagePath'],
            'addTime': acimageinfo['addTime'],
            'modifyTime': modify_time
        }
        for data in ['keyID', 'addTime', 'modifyTime']:
            update_imageinfo[data] = external_info[data]
        for data in ['keyID', 'macActvImageId', 'imagePath', 'addTime', 'modifyTime']:
            update_imageinfo['macActvImageSubInfoVos'][0][data] = internal_info[data]
        res = self.get_result(func_name, var_params=update_imageinfo)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_MacActvImageMainInfo_remove(self):
        """
        删除广告图组
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        imageinfo_key_id = self.get_request_data(func_name)
        acimage_key_id = gl.get_value('acimageinfo')['keyID']
        imageinfo_key_id['keyID'] = acimage_key_id
        res = self.get_result(func_name, var_params=imageinfo_key_id)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

