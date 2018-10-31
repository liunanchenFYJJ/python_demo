# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123456",
                       db="python_demo", port=3306, charset="utf8")
cursor = conn.cursor()

# 中文保存到数据库乱码 todo
# insert_sql = '''INSERT INTO tb_book(tb_book.bookName) VALUES('鲁滨逊漂流记11')'''
# query_sql = '''SELECT * FROM tb_book'''

def sql_to_db(sql):
    try:
        cursor.execute(sql)
        # 获取booklist
        # booklist = cursor.fetchall()
        # print(booklist)

        # 增删改需要commit()
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()
