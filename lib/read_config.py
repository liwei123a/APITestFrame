#coding:utf-8

import configparser
import os

class ConfReader(object):
    def __init__(self, datadir, dirsec, dir, namesec, file):
        self.datadir = datadir
        self.dirsec = dirsec
        self.dir = dir
        self.namesec = namesec
        self.file = file
        self.conf = configparser.ConfigParser()
        self.conf.read(self.datadir)

    def get_file_path(self):
        dirpath = self.conf.get(self.dirsec, self.dir)
        filepath = self.conf.get(self.namesec, self.file)
        path = os.path.join(dirpath, filepath)
        return path

    def get_file_name(self):
        file_name = self.conf.get(self.namesec, self.file)
        return file_name

    def get_dir_name(self):
        dir_name = self.conf.get(self.dirsec, self.dir)
        return dir_name