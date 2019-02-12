#coding:utf-8

from mysql.connector import connect
from mysql.connector import Error

class OperationMysql(object):
    def __init__(self, host, user, password, port, database, charset):
        """
        连接数据库
        :param host: 主机地址
        :param user: 用户名
        :param password: 密码
        :param port: 端口
        :param database: 数据库
        :param charset: 字符集
        """
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'port': port,
            'database': database,
            'charset': charset
        }
        try:
            self.conn = connect(**self.config)
        except Error as e:
            print('connect fails!{}'.format(e))
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql_cmd):
        """
        执行sql语句(delete)
        :param sql_cmd: sql命令
        :return:
        """
        try:
            self.cursor.execute(sql_cmd)
            self.conn.commit()
        except Error as e:
            print('execute fails!{}'.format(e))

    def close_connect(self):
        self.cursor.close()
        self.conn.close()
