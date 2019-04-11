#coding:utf-8
"""
小程序banner管理
"""

import sys
import time
import run.globalvar as gl
import random
from run.common_test_set import UrineWebInterfaceTestCase


class SmallProgramBannerManagement(UrineWebInterfaceTestCase):

    def test_urine_v2_bannerInfo_add(self):
        """
        添加小程序banner
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        hash = gl.get_value('hash')
        banner_info = self.get_request_data(func_name)
        timestamp = int(time.time()*1000)
        for date in ['bannerShowStartDate', 'bannerShowEndDate', 'bannerStartDate', 'bannerEndDate']:
            banner_info[date] = timestamp
        banner_info['imgs'][0]['uid'] = timestamp
        banner_info['imgs'][0]['url'] += hash
        banner_info['bannerPicUrl'] += hash
        res = self.get_result(func_name, var_params=banner_info)
        actual_result = res[0].json()['errmsg']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_bannerInfo_list(self):
        """
        小程序banner列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
        gl.set_value('banner_list', res[0].json()['data'])
        # return res[0].json()

    def test_urine_v2_bannerInfo_update(self):
        """
        修改小程序banner
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        # banner_list = self.get_depend_params(func_name)
        banner_list = gl.get_value('banner_list')
        # gl.set_value('banner_list', banner_list)
        update_banner_info = self.get_request_data(func_name)
        banner_name = update_banner_info['bannerName']
        query_banner_info = None
        for banner in banner_list:
            if banner['bannerName'] == banner_name:
                query_banner_info = banner
        gl.set_value('banner_info', query_banner_info)
        for data in query_banner_info:
            update_banner_info[data] = query_banner_info[data]
        update_banner_info['imgs'][0]['url'] = query_banner_info['bannerPicUrl']
        update_banner_info['imgs'][0]['uid'] = int(time.time()*1000)
        for date in ['bannerShowStartDate', 'bannerShowEndDate', 'bannerStartDate', 'bannerEndDate']:
            banner_time = time.strftime("%Y.%m.%d", time.localtime(query_banner_info[date]/1000))
            start_end_time = 'showStartEndTime' if 'Show' in date else 'startEndTime'
            update_banner_info[start_end_time].append(banner_time)
        res = self.get_result(func_name, var_params=update_banner_info)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_bannerInfo_moveupdown(self):
        """
        交换小程序banner序号
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        BANNER_NUM = 2
        banner_list = gl.get_value('banner_list')
        rand_two_banner = random.sample(banner_list, BANNER_NUM)
        key_id_list = []
        for banner in rand_two_banner:
            key_id_list.append(banner['keyID'])
        exchange_id = {
            'fromId': key_id_list[0],
            'toId': key_id_list[1]
        }
        res = self.get_result(func_name, var_params=exchange_id)
        actual_result = res[0].json()['data']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_bannerInfo_delete(self):
        """
        删除小程序banner
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        banner_info = gl.get_value('banner_info')
        key_id = {'keyID': banner_info['keyID']}
        res = self.get_result(func_name, var_params=key_id)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)
