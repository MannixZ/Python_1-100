#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: decorator_exp_01.py
@time: 2019/10/10 12:51
@desc: 装饰器
'''

from functools import wraps
from time import time

def record_time(func):
    '''自定义装饰函数的装饰器'''
    import time
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name}: {time() - start}秒')
        return result

    return wrapper


def record(output):
    '''自定带参数的装饰器'''
    from functools import wraps
    from time import time

    def decorate(func):

        @wraps(func)
        def wrappper(*args, **kwargs):
            start  = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrappper
    return decorate


class Record():
    '''自定义装饰类(通过__call__魔术方法使得对象可以当成函数调用)'''

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


'''例子：用装饰器来实现单例模式。'''
def singleton(cls):
    """装饰类的装饰器"""
    instances = {}

    @wraps(cls)
    def wrappers(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrappers

@singleton
class President():
    '''"""总统(单例类)"""'''
    pass


'''海鲜线程安全的单例装饰器'''
from functools import wraps
from threading import Lock

def singleton(cls):
    '''现成安全的单例装饰器'''
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

