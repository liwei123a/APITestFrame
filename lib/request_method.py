#coding:utf-8

"""
封装requests库
"""

import requests

class ReqMethod(object):
    def __init__(self, url, cookies, header=None, params=None):
        self.url = url
        self.header = header
        self.params = params
        self.cookies = cookies

    def get_method(self):
        """
        封装get请求
        :return:
        """
        res = requests.get(url=self.url, params=self.params, headers=self.header, cookies=self.cookies,
                           verify=False)
        self.cookies = res.cookies.get_dict()
        return res

    def post_method(self):
        """
        封装post请求
        :return:
        """
        if self.header['content-type'] == 'application/json':
            res = requests.post(url=self.url, json=self.params, headers=self.header, cookies=self.cookies,
                                verify=False)
        elif 'multipart/form-data' in self.header['content-type']:
            res = requests.post(url=self.url, files=self.params, cookies=self.cookies,verify=False)
        else:
            res = requests.post(url=self.url, data=self.params, headers=self.header, cookies=self.cookies,
                                verify=False)
        self.cookies = res.cookies.get_dict()
        return res

    def get_cookies(self):
        """
        获取cookie
        :return:
        """
        return self.cookies

    def req_send(self, method):
        """
        根据请求类型调用对应的请求
        :param method:
        :return:
        """
        method = method.upper()
        if method == "GET":
            return self.get_method()
        elif method == "POST":
            return self.post_method()
