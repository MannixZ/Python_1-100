#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 9:23
# @Author  : Mannix
# @File    : thread_work1.py
# @Software: PyCharm

import time
import tkinter
import tkinter.messagebox


def download():
    # 模拟下载任务需花费10秒钟
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('关于', '坐着xxx')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()