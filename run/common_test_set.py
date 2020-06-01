import re
import sys
from lib.read_config import ConfReader
from run.run_setup import RunCase
import run.globalvar as gl
from lib.send_email import SendEmail


class UrineWebInterfaceTestCase():

    id = 'id'
    url = 'url'
    request_method = 'request_method'
    header = 'header'
    # depend_interface = 'depend_interface'
    # depend_data = 'depend_data'
    # depend_field = 'depend_field'
    request_field = 'request_field'
    expect_result = 'expect_result'
    actual_result = 'actual_result'
    datadir = 'config/data_source.ini'
    dirsec = 'path'
    dir1 = 'case_dir'
    dir2 = 'data_dir'
    dir3 = 'pic_dir'
    namesec = 'file'
    file1 = 'case_file'
    file2 = 'data_file'
    file3 = 'pic_file'
    sheet_id = 'test_case'
    colsec = 'columns'
    dmsec = 'domain'
    domain_name = 'domain_name'
    emailsec = 'email'
    smtpserver = 'smtpserver'
    sender = 'sender'
    password = 'password'
    receiver = 'receiver'
    username = 'username'
    subject = 'subject'
    content = 'content'
    filename = 'filename'

    # @classmethod
    def setup_class(self):
        """
        从excel表格读取测试用例
        :return:
        """
        self.run_case = RunCase(self.datadir, self.dirsec, self.dir1, self.dir2, self.namesec, self.file1,
                               self.file2, self.sheet_id, self.colsec, self.dmsec, self.domain_name)

    def get_case_row_index(self, func_name):
        """
        获取用例行号
        :param func_name:
        :return:
        """
        case_url = None
        if 'test' in func_name:
            case_url = re.findall(r'test(\w+)', func_name)[0].replace('_', '/')
        else:
            case_url = func_name.replace('_', '/')
        col_index = self.run_case.case_info.get_col_index(self.url)
        row = self.run_case.case_info.get_row_index(col_index, case_url)
        return row

    def get_result(self, func_name, fileparams=None, var_params=None, domain=True):
        """
        执行用例，并返回结果
        :param func_name:
        :param fileparams:
        :param var_params:
        :return:
        """
        row = self.get_case_row_index(func_name)
        cookies = gl.get_value('cookies')
        res = self.run_case.execution_request(self.url, self.request_method, self.header,
                                              self.request_field, fileparams, var_params, row, cookies, domain)
        return res

    def get_expect_result(self, func_name):
        """
        获取预期结果
        :param func_name:
        :return:
        """
        row = self.get_case_row_index(func_name)
        expect_result = self.run_case.case_info.get_expect_result(self.expect_result, row)
        return expect_result

    def get_request_data(self, func_name):
        """
        获取请求参数
        :param func_name:
        :return:
        """
        row = self.get_case_row_index(func_name)
        request_data = self.run_case.case_info.get_request_data(self.request_field, row)
        return request_data

    # def get_depend_params(self, func_name):
    #     """
    #     获取依赖数据
    #     :param func_name:
    #     :return:
    #     """
    #     row = self.get_case_row_index(func_name)
    #     depend_interface = self.run_case.case_info.get_depend_interface(self.depend_interface, row)
    #     pre_funcname = depend_interface.replace('/', '_')
    #     for func in dir(self):
    #         if pre_funcname in func:
    #             pre_funcname = func
    #     depend_json_data = eval('self.' + pre_funcname + '()')
    #     print(pre_funcname)
    #     print(depend_json_data)
    #     depend_field = self.run_case.case_info.get_depend_field(self.depend_field, row)
    #     depend_data = self.run_case.case_info.get_depend_field(self.depend_data, row)
    #     depend_params = None
    #     if depend_field:
    #         depend_params = depend_json_data[depend_field][depend_data]
    #     else:
    #         depend_params = depend_json_data[depend_data]
    #     return depend_params

    def update_result(self, row, actual_result, expect_result):
        """
        更新excel表格测试结果并进行断言
        :param row:
        :param actual_result:
        :param expect_result:
        :return:
        """
        if actual_result in expect_result:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'pass')
            gl.get_value('pass_case_list').append(self.run_case.case_info.get_id(self.id, row))
        else:
            self.run_case.case_info.update_actual_result(self.actual_result, row, 'fail')
            gl.get_value('fail_case_list').append(self.run_case.case_info.get_id(self.id, row))
        assert actual_result in expect_result

    def urine_v2_qiniu_getToken(self):
        """
        获取七牛token
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()

    def upload(self):
        """
        上传文件
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        token = self.urine_v2_qiniu_getToken()['data']['token']
        conf_read = ConfReader(self.datadir)
        file_path = conf_read.get_file_path( self.dirsec, self.dir3, self.namesec, self.file3)
        file_name = conf_read.get_field_value(self.namesec, self.file3)
        fileparams = {
            'token': (None, token),
            'file': (file_name, open(file_path, 'rb'), 'image/jpeg')
        }
        res = self.get_result(func_name, fileparams=fileparams, domain=True)
        return res[0].json()

    def urine_v2_cityAreaSettingInfo_getAllCitys(self):
        """
        获取城市列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()['data']

    def urine_v2_buildingInfo_queryAllBuildingInfo(self):
        """
        获取楼宇列表
        :return:
        """
        func_name = sys._getframe().f_code.co_name
        res = self.get_result(func_name)
        return res[0].json()['data']

    def send_email(self):
        """
        发送邮件
        :return:
        """
        cf = ConfReader(self.datadir)
        pass_case_num = len(gl.get_value('pass_case_list'))
        fail_case_num = len(gl.get_value('fail_case_list'))
        total_case_num = pass_case_num + fail_case_num
        print(pass_case_num, fail_case_num)
        pass_rate = "%.2f%%" % (pass_case_num/total_case_num*100)
        fail_rate = "%.2f%%" % (fail_case_num/total_case_num*100)
        smtpserver = cf.get_field_value(self.emailsec, self.smtpserver)
        sender = cf.get_field_value(self.emailsec, self.sender)
        password = cf.get_field_value(self.emailsec, self.password)
        receiver = cf.get_field_value(self.emailsec, self.receiver).split(",")
        username = cf.get_field_value(self.emailsec, self.username)
        subject = cf.get_field_value(self.emailsec, self.subject)
        content = cf.get_field_value(self.emailsec, self.content) % (total_case_num, pass_case_num, fail_case_num, pass_rate, fail_rate)
        filename = cf.get_field_value(self.emailsec, self.filename)
        send_email = SendEmail(smtpserver, sender, password)
        send_email.send(username, receiver, subject, content, filename)