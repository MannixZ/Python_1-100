#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: yuanclass.py
@time: 2019/10/30 21:59
@desc:
'''

import threading


class SingletonMeta(type):
    '''自定义元类'''

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            with self.__lock:
                if self.__instance is None:
                    self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class President(metaclass=SingletonMeta):
    '''总统(单例类)'''
    pass

