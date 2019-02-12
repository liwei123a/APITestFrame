#coding:utf-8

import configparser
import os

class ConfReader(object):
    def __init__(self, datadir):
        self.datadir = datadir
        self.conf = configparser.ConfigParser()
        self.conf.read(self.datadir)

    def get_file_path(self, dirsec, dir, namesec, file):
        dirpath = self.conf.get(dirsec, dir)
        filepath = self.conf.get(namesec, file)
        path = os.path.join(dirpath, filepath)
        return path

    def get_file_name(self ,namesec, file):
        file_name = self.conf.get(namesec, file)
        return file_name

    def get_dir_name(self, dirsec, dir):
        dir_name = self.conf.get(dirsec, dir)
        return dir_name

    def get_database_logininfo(self, dbsec, host, user, password, port, database, charset):
        """
        获取数据库登录信息
        :param dbsec:
        :param host:
        :param user:
        :param password:
        :param port:
        :param database:
        :param charset:
        :return:
        """
        login_info = dict()
        login_info['host'] = self.conf.get(dbsec, host)
        login_info['user'] = self.conf.get(dbsec, user)
        login_info['password'] = self.conf.get(dbsec, password)
        login_info['port'] = self.conf.get(dbsec, port)
        login_info['database'] = self.conf.get(dbsec, database)
        login_info['charset'] = self.conf.get(dbsec, charset)
        return login_info