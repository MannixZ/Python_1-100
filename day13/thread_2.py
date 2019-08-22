#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 18:55
# @Author  : Mannix
# @File    : thread_2.py
# @Software: PyCharm

from random import randint
from threading import Thread
from time import time, sleep

class DownloadTas(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTas('python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTas('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
