#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 15:29
# @Author  : Mannix
# @File    : work_day7.py
# @Software: PyCharm

def marquee():
    '''跑马灯'''
    import os
    import time
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕的输出
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    import random

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    print(code)
    # return code

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    print(pos)
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def max2(x):
    '''返回列表中最大和第二大的元素的值'''
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2, m1 = m1, x[index]
        elif x[index] > m2:
            m2 = x[index]
    return  m1, m2

def pascal_triangle():
    num = int(input('Num of rows: '))
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
        if len(L) == num + 1:
            break


if __name__ == '__main__':
    # print(get_suffix('adfsadf.dd1'))
    for i in pascal_triangle():
        print(i)