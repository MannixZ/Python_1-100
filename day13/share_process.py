#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:48
# @Author  : Mannix
# @File    : share_process.py
# @Software: PyCharm

from multiprocessing import Process, Queue
from time import sleep


def sub_task(q, string):
    number = q.get()
    while number:
        print('%d: %s' % (number, string))
        sleep(0.01)
        number = q.get()

def main():
    q = Queue(10)
    for number in range(1, 11):
        q.put(number)
    Process(target=sub_task, args=(q, 'Ping')).start()
    Process(target=sub_task, args=(q, 'Pong')).start()


if __name__ == '__main__':
    main()