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

def bubble_sort(origin_items, comp=lambda x, y : x > y):
    '''高质量冒泡排序(搅拌排序)'''
    items = origin_items[:]
    for i in range(len(items) - 1):
        swappend = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swappend = True
        if swappend:
            swappend = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swappend = True
        if not swappend:
            break
    return items


def metge_sort(items, comp=lambda x, y: x <= y):
    '''归并排序(分治法)'''
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = metge_sort(items[:mid], comp)
    right = metge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    '''合并(将两个有序的列表合并成一个有序的列表)'''
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def seq_search(items, key):
    '''顺序查找'''
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    '''折半查找'''
    start, end = 0, len(items) - 1
    while start <= end:
        mid =(start + end) // 2
        if key > items[mid]:
            start = mid +1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


'''
使用生成式（推导式）语法
说明：生成式（推导式）可以用来生成列表、集合和字典
'''
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices)

'''嵌套的列表'''
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考 http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses) * len(names)]
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

def heapq_test():
    '''
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    '''
    import heapq

    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda  x: x['shares']))


def itertools_test():
    '''
    迭代工具 - 排列 / 组合 / 笛卡尔积
    :return:
    '''
    import itertools
    print(len(list(itertools.permutations('ABCD'))))
    print(len(list(itertools.combinations('ABCDE', 3))))
    print(len(list(itertools.product('ABCD', '123'))))


def collections_test():
    '''
    找出序列中出现次数最多元素
    :return:
    '''
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))


if __name__ == '__main__':
    collections_test()
    select_sort([1,3,5,11,2,4,21,5123,512,32,121])