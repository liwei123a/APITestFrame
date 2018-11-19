import unittest
import HtmlTestRunner
from run.run_setup import RunCase

class UrineWebInterfaceTestCase(unittest.TestCase):

    url = 'url'
    is_run = 'is_run'
    request_method = 'request_method'
    header = 'header'
    request_field = 'request_field'
    row = 'row'
    expect_result = 'expect_result'

    # @classmethod
    # def setUpClass(cls):
        # datadir = '../config/data_source.ini'
        # dirsec = 'path'
        # dir1 = 'case_dir'
        # dir2 = 'data_dir'
        # namesec = 'file'
        # file1 = 'case_file'
        # file2 = 'data_file'
        # sheet_id = 0
        # colsec = 'columns'
        # cls.run_case = RunCase(datadir, dirsec, dir1, dir2, namesec, file1, file2, sheet_id, colsec)
        # print(1231231)

    # def test_UrineWeb_001(self):
        # res = self.run_case.configuration_parameter(self.url, self.is_run, self.request_method, self.header, self.request_field, self.row)
        # expect_result = self.run_case.case_info.get_expect_result(self.expect_result, self.row)
        # actual_result = res.json()['errmsg']
        # self.assertIn(actual_result, expect_result)
        # print('dasdas')
        # self.assertTrue(True, False)
    @classmethod
    def setUpClass(cls):
        print("这是执行前的方法\n")

    @classmethod
    def tearDownClass(cls):
        print("这是执行后的方法")

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\interface'))
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(UrineWebInterfaceTestCase('test1'))
    suite.addTest(UrineWebInterfaceTestCase('test2'))
    filepath = "D:\\interface"
    runner = HtmlTestRunner.HTMLTestRunner(output=filepath)
    runner.run(suite)

