#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 16:00
# @Author  : Mannix
# @File    : work_day5.py
# @Software: PyCharm

def narcissus_num():
    '''
    找出100~999之间的所有水仙花数
    水仙花数是各位立方和等于这个数本身的数
    如: 153 = 1**3 + 5**3 + 3**3
    '''
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)

def perfect():
    '''
    找出1~9999之间的所有完美数
    完美数是除自身外其他所有因子的和正好等于这个数本身的数
    例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
    '''
    import time
    import math

    start = time.clock()
    for num in range(1, 10000):
        sum = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum += factor
                if factor > 1 and num / factor != factor:
                    sum += num / factor
        if sum == num:
            print(num)
    end = time.clock()
    print('执行时间: ', (end - start), "秒")

def chicken():
    '''
    1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
    问公鸡 母鸡 小鸡各有多少只
    '''
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

def fibonacci():
    '''
    输出斐波那契数列的前20个数
    1 1 2 3 5 8 13 21 ...
    '''

    a = 0
    b = 1
    for _ in range(20):
        (a, b) = (b, a + b)
        print(a, end=' ')

if __name__ == '__main__':
    perfect()