# import unittest
# import HtmlTestRunner
# from run.test_interface_set import UrineWebInterfaceTestCase
from utx import *

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


if __name__ == '__main__':
    runner = TestRunner()
    runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run')
    runner.run_test(report_title='接口自动化测试报告')
