#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 18:43
# @Author  : Mannix
# @File    : req.py
# @Software: PyCharm

import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()