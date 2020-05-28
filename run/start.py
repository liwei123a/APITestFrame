#coding:utf-8

import pytest


if __name__ == '__main__':
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run')
    pytest.main(['-v', '-s', 'geekbang', '--html=report/test.html', '--self-contained-html', '--cov=./'])
    # pytest.main(['-v', 'algorithm_correlation','--html=report/test2.html', '--self-contained-html', '--cov=./'])
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\a_login_system')
    # runner.add_case_dir(r'C:\Users\Doctorwork\PycharmProjects\APITestFrame\run\algorithm_correlation')
    # runner.run_test(report_title='健康终端管理台接口测试报告')
