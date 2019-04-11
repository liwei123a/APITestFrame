#coding:utf-8
"""
机器管理
"""

import sys
import time
import run.globalvar as gl
import random

from lib.operation_mysql import OperationMysql
from lib.read_config import ConfReader
from run.common_test_set import UrineWebInterfaceTestCase

class MachineManagement(UrineWebInterfaceTestCase):

    dbsec = 'database'
    host = 'host'
    user = 'user'
    password = 'password'
    port = 'port'
    database = 'database'
    charset = 'charset'
    tables = ['MacH5VersionInfo', 'MachineBusiness', 'MachineInfo', 'MachineOnline', 'MachineStock',
              'GoodsSellRecordInfo']

    def test_urine_v2_cityAreaSettingInfo_getAllCitys(self):
        """
        获取城市列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_goodsInfo_queryAllGoodsInfo(self):
        """
        获取商品列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_MacActvImageMainInfo_query(self):
        """
        查询广告图组列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        gl.set_value('adImagePackList', res[0].json()['data']['list'])
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_adImageStrategy_listByPage(self):
        """
        查询图片广告策略列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        gl.set_value('adPlanList', res[0].json()['data']['list'])
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_machineInfo_addMachine(self):
        """
        添加机器
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        add_machine_info = self.get_request_data(func_name)
        gl.set_value('machineID', add_machine_info['machineID'])
        add_machine_info['addTime'] = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.localtime())
        res = self.get_result(func_name, var_params=add_machine_info)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_machineInfo_machineInfoList(self):
        """
        查询机器
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        query_machineinfo = self.get_request_data(func_name)
        machineinfo_copy = query_machineinfo.copy()
        for k in machineinfo_copy.keys():
            machineinfo_copy[k] = None
        for data in ['pageNum', 'pageSize', 'totalCount']:
            machineinfo_copy[data] = query_machineinfo[data]
        query = machineinfo_copy
        """默认查询所有机器"""
        res = self.get_result(func_name, var_params=machineinfo_copy)
        totalCount = res[0].json()['data']['totalCount']
        self.assertTrue(totalCount>0)
        """根据机器编号查询"""
        query['machineID'] = query_machineinfo['machineID']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        expect_result = self.get_expect_result(func_name)
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        gl.set_value('activityId', res[0].json()['data']['list'][0]['activityId'])
        gl.set_value('keyID', res[0].json()['data']['list'][0]['keyID'])
        """根据机器编号、网络状态查询"""
        query['isOnline'] = query_machineinfo['isOnline']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        """根据机器编号、网络状态、故障状态查询"""
        query['troubleStatus'] = query_machineinfo['troubleStatus']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        """根据机器编号、网络状态、故障状态、1号库存查询"""
        query['firstStockStatus'] = query_machineinfo['firstStockStatus']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存查询"""
        query['secondStockStatus'] = query_machineinfo['secondStockStatus']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存、启用状态查询"""
        query['isEnable'] = query_machineinfo['isEnable']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        self.assertEqual(query['isEnable'], actual_machineinfo['isEnable'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存、启用状态、城市查询"""
        query['cityID'] = query_machineinfo['cityID']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        self.assertEqual(query['isEnable'], actual_machineinfo['isEnable'])
        self.assertEqual(query['cityID'], actual_machineinfo['cityID'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存、启用状态、城市、商圈查询"""
        query['areaID'] = query_machineinfo['areaID']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        self.assertEqual(query['isEnable'], actual_machineinfo['isEnable'])
        self.assertEqual(query['cityID'], actual_machineinfo['cityID'])
        self.assertEqual(query['areaID'], actual_machineinfo['areaID'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存、启用状态、城市、商圈、楼宇查询"""
        query['buildingID'] = query_machineinfo['buildingID']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        self.assertEqual(query['isEnable'], actual_machineinfo['isEnable'])
        self.assertEqual(query['cityID'], actual_machineinfo['cityID'])
        self.assertEqual(query['areaID'], actual_machineinfo['areaID'])
        self.assertEqual(query['buildingID'], actual_machineinfo['buildingID'])
        """根据机器编号、网络状态、故障状态、1号库存、2号库存、启用状态、城市、商圈、楼宇、卫生间查询"""
        query['sexType'] = query_machineinfo['sexType']
        res = self.get_result(func_name, var_params=query)
        actual_machineinfo = res[0].json()['data']['list'][0]
        self.assertIn(actual_machineinfo['machineID'], expect_result)
        self.assertEqual(query['isOnline'], actual_machineinfo['isOnline'])
        self.assertEqual(query['troubleStatus'], actual_machineinfo['troubleStatus'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstNoGoods'])
        self.assertEqual(query['firstStockStatus'], actual_machineinfo['firstOutOfstock'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondNoGoods'])
        self.assertEqual(query['secondStockStatus'], actual_machineinfo['secondOutOfstock'])
        self.assertEqual(query['isEnable'], actual_machineinfo['isEnable'])
        self.assertEqual(query['cityID'], actual_machineinfo['cityID'])
        self.assertEqual(query['areaID'], actual_machineinfo['areaID'])
        self.assertEqual(query['buildingID'], actual_machineinfo['buildingID'])
        self.assertEqual(query['sexType'], actual_machineinfo['sexType'])

    def test_urine_v2_machineInfo_updateMachine(self):
        """
        更新机器信息
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        update_machine_info = self.get_request_data(func_name)
        update_machine_info['keyID'] = gl.get_value('keyID')
        update_machine_info['activityId'] = gl.get_value('activityId')
        res = self.get_result(func_name, var_params=update_machine_info)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_machineInfo_log(self):
        """
        查询机器日志
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        actual_result = res[0].json()['errmsg']
        row = self.get_case_row_index(func_name)
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_machineInfo_upIsEnable(self):
        """
        启用禁用机器
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        upIsEnable = self.get_request_data(func_name)
        upIsEnable['keyID'] = gl.get_value('keyID')
        res = self.get_result(func_name, var_params=upIsEnable)
        actual_result = res[0].json()['data']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    def test_urine_v2_machineInfo_batchSetMacH5Version(self):
        """
        批量管理首页
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        row = self.get_case_row_index(func_name)
        mac_h5_version = self.get_request_data(func_name)
        mac_h5_version['adPlanId'] = random.sample(gl.get_value('adPlanList'), 1)[0]['keyID']
        mac_h5_version['adImagePackId'] = random.sample(gl.get_value('adImagePackList'), 1)[0]['keyID']
        res = self.get_result(func_name, var_params=mac_h5_version)
        actual_result = res[0].json()['errmsg']
        expect_result = self.get_expect_result(func_name)
        self.update_result(row, actual_result, expect_result)

    @classmethod
    def tearDownClass(cls):
        """
        删除创建的机器
        :return:
        """
        conf_read = ConfReader(cls.datadir)
        login_info = conf_read.get_database_logininfo(cls.dbsec, cls.host, cls.user, cls.password,
                                                      cls.port, cls.database, cls.charset)
        operation_mysql = OperationMysql(login_info['host'], login_info['user'], login_info['password'],
                                         login_info['port'], login_info['database'], login_info['charset'])
        machineID = gl.get_value('machineID')
        for table in cls.tables:
            sql_cmd = 'delete from %s where MachineId = %s' % (table, machineID)
            operation_mysql.execute_sql(sql_cmd)
        operation_mysql.close_connect()
