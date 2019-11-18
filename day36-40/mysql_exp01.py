#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: mysql_exp01.py
@time: 2019/11/18 23:49
# @Software: win10 Tensorflow1.13.1 python3.6.3
'''

import pymysql


class mySQL():


        def connect_mysql(self, emp):
            # 1. 创建数据库连接对象
            self.con = pymysql.connect(host='localhost', port=3306,
                                  database='test_sql', charset='utf8',
                                  user='root', password='root',
                                  autocommit=True)
            try:
                # 2. 通过连接对象获取游标
                with self.con.cursor() as self.cursor:
                    self.all_department(emp)
            finally:
                # 5. 关闭连接释放资源
                self.con.close()


        def add_department(self):
            no = int(input('编号: '))
            name = input('名字: ')
            loc = input('所在地: ')
            result = self.cursor.execute(
                'insert into department values (%s, %s, %s)',
                (no, name, loc)
            )
            if result == 1:
                print('添加成功!')
            # 4. 操作成功提交事务
            self.con.commit()


        def sub_department(self):
            no = int(input('编号: '))
            result = self.cursor.execute(
                'delete from department where no=%s',
                (no, )
            )
            if result == 1:
                print('删除成功!')


        def update_department(self):
            no = int(input('编号: '))
            name = input('名字: ')
            loc = input('所在地: ')
            result = self.cursor.execute(
                'update department set name=%s, loc=%s where no=%s',
                (name, loc, no)
            )
            if result == 1:
                print('更新成功!')


        def all_department(self, emp):
            self.cursor.execute(
                'select no, name, loc from department'
            )
            results = self.cursor.fetchall()
            # print(results)
            # print('编号\t名称\t\t所在地')
            for dept in results:
                # print(dept[0], end='\t')
                # print(dept[1], end='\t')
                # print(dept[2])
                info = emp(*dept)
                print(info)


class Emp():

    def __init__(self, no, name, loc):
        self.no = no
        self.name = name
        self.loc = loc

    def __str__(self):
        return f'\n编号: {self.no}\n姓名: {self.name}\n所在地: {self.loc}\n'


def main():
    emp = Emp
    mysql = mySQL()
    mysql.connect_mysql(emp)



if __name__ == '__main__':
    main()