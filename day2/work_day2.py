#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 14:56
# @Author  : Mannix
# @File    : work_day2.py
# @Software: PyCharm

def work_1():
    '''
    将华氏温度转换为摄氏温度
    F = 1.8C + 32
    '''
    f = float(input('请输入华氏温度:'))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' %(f, c))

def work_2():
    '''输入半径计算圆的周长和面积'''
    import math

    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius *radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)

def work_3():
    '''输入年份 如果是闰年输出True 否则输出False'''
    year = int(input('请输入年份: '))
    is_leap = (year % 4 == 0 and year % 100 != 0 or
               year % 400 ==0)
    print(is_leap)

if __name__ == '__main__':
    work_1()
    work_2()
    work_3()