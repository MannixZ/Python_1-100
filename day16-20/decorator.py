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


"""自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)"""
class Record():

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper


'''
例子：用装饰器来实现单例模式。
'''
from functools import wraps


def singleton(cls):
    '''装饰类的装饰器'''
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper()


@singleton
class President()
    '''总统(单例类)'''
    pass


'''
实现线程安全的单例
'''
from functools import wraps
from threading import Lock

def singleton(cls):
    '''线程安全的单例装饰器'''
    instance = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with locker:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper()