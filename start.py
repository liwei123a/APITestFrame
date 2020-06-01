#coding:utf-8

"""
运行测试脚本
"""

import pytest
from run.common_test_set import UrineWebInterfaceTestCase
import run.globalvar as gl

if __name__ == '__main__':
    gl._init()
    gl.set_value('pass_case_list', [])
    gl.set_value('fail_case_list', [])
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run')
    pytest.main(['-v', '-s', 'run/geekbang', '--html=report/接口自动化测试报告.html', '--self-contained-html', '--cov=./run/'])
    # pytest.main(['-v', 'algorithm_correlation','--html=report/test2.html', '--self-contained-html', '--cov=./'])
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\a_login_system')
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\algorithm_correlation')
    # runner.run_test(report_title='健康终端管理台接口测试报告')
    UrineWebInterfaceTestCase().send_email()
