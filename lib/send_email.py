# -*- coding:utf-8 -*-

"""
封装发送邮件库
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail(object):
    def __init__(self, smtpserver, sender, password):
        """
        定义发送邮件需要的参数
        :param smtpserver: smtp服务器
        :param sender: 发送者的邮箱
        :param password: 登录smtp服务器的密码
        """
        self.smtpserver = smtpserver
        self.sender = sender
        self.password = password

    def generate_msg(self, subject, content, username, receiver, filename):
        """
        生成邮件正文
        :param subject: 邮件标题
        :param content: 邮件内容
        :return:
        """
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = username + "<" + self.sender + ">"
        msg['To'] = ",".join(receiver)
        # 构造附件
        att1 = MIMEApplication(open(filename, 'rb').read())
        att1.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att1)
        return msg

    def send(self, username, receiver, subject, content, filename):
        """
        发送邮件
        :param receiver: 接收人的邮箱
        :return:
        """
        smtp = smtplib.SMTP()
        smtp.connect(host=self.smtpserver)
        smtp.login(user=self.sender, password=self.password)
        smtp.sendmail(from_addr=self.sender, to_addrs=receiver, msg=self.generate_msg(subject, content, username, receiver, filename).as_string())
        smtp.quit()

# if __name__ == '__main__':
#     send_email = SendEmail(smtpserver='smtp.163.com', sender='18508233582@163.com', password='KSQPCQPXFSVZSBWQ')
#     send_email.send(username="测试组",receiver=['1101125016@qq.com'], subject='自动化测试', content='测试完成')