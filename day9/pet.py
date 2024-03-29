#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 10:04
# @Author  : Mannix
# @File    : pet.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    '''宠物'''

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass


class Dog(Pet):
    '''狗'''

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    '''猫'''

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯迪')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()