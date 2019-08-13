#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 21:29
# @Author  : Mannix
# @Site    : 
# @File    : map_json.py
# @Software: PyCharm

import re

re_1 = re.compile(r'[A-Za-z0-9-.*]+')

re_2 = re.compile(r'[0-9.]+')

re_3 = re.compile(r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))')

re_4 = re.compile(r'[0-9a-zA-Z-*]+')


def map_json():
    with open('map.txt', 'r+') as file:
        with open('json.txt', 'w+') as doc:
            for line_content in file:
                str_1 = re_1.findall(line_content)
                for l in range(len(str_1)):
                    if len(re_2.findall(str_1[l])) == 1 and len(re_3.findall(str_1[l])) != 1 and len(
                            re_4.findall(str_1[l])) != 1:
                        pass
                    elif len(str_1[l]) >= 1:
                        try:
                            int_eme = int(str_1[l])
                            pass
                        except:
                            if str_1[l] == 'true' or str_1[l] == 'false':
                                pass
                            else:
                                line_content = line_content.replace(str_1[l], '\"%s\"' % str_1[l])
                                line_content = line_content.replace('=', ':')
                doc.write(line_content)


if __name__ == '__main__':
    map_json()