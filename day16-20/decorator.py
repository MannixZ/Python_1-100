#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 18:13
# @Author  : Mannix
# @File    : decorator.py
# @Software: PyCharm

'''输出函数执行时间的装饰器'''
def record_time(func):
    '''自定义装饰函数的装饰器'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start} 秒')
        return result

    return wrapper

'''
如果装饰器不希望跟print函数耦合，可以编写带参数的装饰器。
'''
from functools import wraps
from time import time


def record(output):
    '''自定义带参数的装饰器'''

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper()

    return decorate