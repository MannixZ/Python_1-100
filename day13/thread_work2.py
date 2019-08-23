#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 15:12
# @Author  : Mannix
# @File    : thread_work2.py
# @Software: PyCharm

from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
