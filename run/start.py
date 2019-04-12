#coding:utf-8

from utx import *


if __name__ == '__main__':
    runner = TestRunner()
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run')
    runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\a_login_system')
    runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\algorithm_correlation')
    runner.run_test(report_title='健康终端管理台接口自动化测试报告')
