#coding:utf-8
"""诺禾基因检测列表"""

import sys

from run.common_test_set import UrineWebInterfaceTestCase

class NovoGeneTestinglist(UrineWebInterfaceTestCase):

    def test_web_urine_v2_urineInfoList_getGeneOrderList(self):
        """
        查询基因检测列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        query_geneinfo = self.get_request_data(func_name)
        geneinfo_copy = query_geneinfo.copy()
        for k in geneinfo_copy.keys():
            if k not in ['pageNum', 'pageSize']:
                geneinfo_copy[k] = ""
        query = geneinfo_copy
        """默认查询所有记录"""
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        expect_result = self.get_expect_result(func_name)
        self.assertTrue(eval(expect_result))
        """根据手机号查询"""
        query['phone'] = query_geneinfo['phone']
        res = self.get_result(func_name, var_params=query)
        totalCount = res[0].json()['data']['totalCount']
        query['pageSize'] = totalCount
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
        """根据手机号、检测类型查询"""
        query['productId'] = query_geneinfo['productId']
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
                self.assertEqual(query['productId'], gene['productId'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
                self.assertEqual(query['productId'], gene['productId'])
        """根据手机号、检测类型、检测状态查询"""
        query['flowStatus'] = query_geneinfo['flowStatus']
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
        """根据手机号、检测类型、检测状态、采样袋号查询"""
        query['barcode'] = query_geneinfo['barcode']
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
        """根据手机号、检测类型、检测状态、采样袋号、联系人查询"""
        query['deliveryUserName'] = query_geneinfo['deliveryUserName']
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
                self.assertEqual(query['deliveryUserName'], gene['deliveryUser'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
                self.assertEqual(query['deliveryUserName'], gene['deliveryUser'])
        """根据手机号、检测类型、检测状态、采样袋号、联系人、顺丰单号查询"""
        query['sfWayBillId'] = query_geneinfo['sfWayBillId']
        res = self.get_result(func_name, var_params=query)
        gene_list = res[0].json()['data']['list']
        for gene in gene_list:
            if gene['phone'] != None:
                self.assertEqual(query['phone'], gene['phone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
                self.assertEqual(query['deliveryUserName'], gene['deliveryUser'])
                self.assertEqual(query['sfWayBillId'], gene['sfWayBillId'])
            else:
                self.assertEqual(query['phone'], gene['deliveryUserPhone'])
                self.assertEqual(query['productId'], gene['productId'])
                self.assertEqual(query['flowStatus'], gene['flowStatus'])
                self.assertEqual(query['barcode'], gene['barcode'])
                self.assertEqual(query['deliveryUserName'], gene['deliveryUser'])
                self.assertEqual(query['sfWayBillId'], gene['sfWayBillId'])