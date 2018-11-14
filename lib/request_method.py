#coding:utf-8

import requests

class ReqMethod(object):
    def __init__(self, url, header=None, params=None):
        self.url = url
        self.header = header
        self.params = params

    def get_method(self):
        res = requests.get(url=self.url, params=self.params, headers=self.header, verify=False)
        return res

    def post_method(self):
        if self.header['content-type'] == 'application/json':
            res = requests.post(url=self.url, json=self.params, headers=self.header, verify=False)
        else:
            res = requests.post(url=self.url, data=self.params, headers=self.header, verify=False)
        return res

    def req_send(self, method):
        if method == "GET":
            return self.get_method()
        elif method == "POST":
            return self.post_method()
