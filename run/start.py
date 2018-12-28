#coding:utf-8

from utx import *


if __name__ == '__main__':
    runner = TestRunner()
    runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run')
    runner.run_test(report_title='接口自动化测试报告')
