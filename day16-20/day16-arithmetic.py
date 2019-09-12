#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 19:14
# @Author  : Mannix
# @File    : day16-arithmetic.py
# @Software: PyCharm

def select_sort(origin_items, comp=lambda x, y: x < y):
    '''简单选择排序'''
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], i[min_index] = items[min_index], items[i]
    return items

if __name__ == '__main__':
    select_sort([1,3,5,11,2,4,21,5123,512,32,121])