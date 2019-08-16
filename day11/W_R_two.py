#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 18:34
# @Author  : Mannix
# @File    : W_R_two.py
# @Software: PyCharm

def main():
    try:
        with open('file-open-mode.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('666.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束')


if __name__ == '__main__':
    main()