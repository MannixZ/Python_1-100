#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:33
# @Author  : Mannix
# @File    : no_proceed.py
# @Software: PyCharm

from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成!耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    download_task('python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main()