#coding:utf-8

import json
import configparser
import os
from lib.read_config import ConfReader

class OperationJson(object):
    def __init__(self, datadir, dirsec, filedir, namesec, filename):
        self.conf = ConfReader(datadir)
        self.file = self.conf.get_file_path(dirsec,filedir,namesec,filename)

    def get_field_value(self, field):
        with open(self.file, 'rb') as f:
            d = json.load(f)
        return d[field]

