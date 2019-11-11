#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: more_thread.py
@time: 2019/11/7 23:04
@desc:
'''

"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""

import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    '''银行账户'''

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance