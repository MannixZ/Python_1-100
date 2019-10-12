#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: feibolaqie.py
@time: 2019/10/10 12:46
@desc: 斐波拉切数列
'''

def fib(num, temp={}):
    '''用递归计算Fibonacci数'''
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]