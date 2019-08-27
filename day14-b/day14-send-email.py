#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 11:37
# @Author  : Mannix
# @File    : day14-send-email.py
# @Software: PyCharm

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'zmjbobo3@163.com'
    receivers = ['zmjbobo1@163.com', 'zmjbobo2@163.com']
    message = MIMEText('明天会更好', 'plain', 'utf-8')
    message['From'] = 'zmjbobo3@163.com'
    message['To'] = 'zmjbobo4@163.com'
    message['Subject'] = Header('黎明之时', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'test12345')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

if __name__ == '__main__':
    main()