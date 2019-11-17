#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: aiohttp_asyncio.py
@time: 2019/11/16 14:24
# @Software: win10 Tensorflow1.13.1 python3.6.3
'''

import re
import aiohttp
import asyncio

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()