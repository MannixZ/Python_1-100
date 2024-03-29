#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: mixin_exp.py
@time: 2019/10/30 21:52
@desc:
'''

class SetOnceMappingMixin():
    '''自定义混入类'''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set ')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    '''自定义字典'''
    pass


my_dict = SetOnceDict()

try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)

