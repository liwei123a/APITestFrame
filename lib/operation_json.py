#coding:utf-8

import json
import configparser
import os

class OperationJson(object):
    def __init__(self, datadir, dirsec, filedir, namesec, filename):
        self.conf = configparser.ConfigParser()
        self.conf.read(datadir)
        self.file = os.path.join(self.conf.get(dirsec, filedir), self.conf.get(namesec, filename))

    def get_field_value(self, field):
        with open(self.file, 'rb') as f:
            d = json.load(f)
        return d[field]

# oj = OperationJson('../config/data_source.ini', 'path', 'data_dir', 'file', 'data_file')
