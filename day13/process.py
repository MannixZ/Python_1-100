#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:39
# @Author  : Mannix
# @File    : process.py
# @Software: PyCharm

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def dwonload_task(filename):
    print('启动下载进程, 进程号[%d]' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=dwonload_task, args=('python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=dwonload_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main()