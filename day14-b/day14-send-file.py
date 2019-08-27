#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 14:47
# @Author  : Mannix
# @File    : day14-send-file.py
# @Software: PyCharm

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', "utf-8")
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('E:/个人信息/Python_1-100/day14-b/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-type'] = 'txt/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('E:/个人信息/Python_1-100/day14-b/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)

    # 创建SMTP对象
    smtper = SMTP('smtp.163.com')
    # 开启安全连接
    # smtper.starttls()
    sender = 'zmjbobo3@163.com'
    receivers = 'zmjbobo1@163.com, zmjbobo2@163.com'
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    message['To'] = receivers
    smtper.login(sender, 'test12345')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')

if __name__ == '__main__':
    main()