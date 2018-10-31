# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def sql_to_db(sql):
    '''
    根据sql进行数据库操作
    '''
    conn = pymysql.connect(host="localhost", user="root", password="123456",
                          db="python_demo", port=3306, charset="utf8")
    cursor = conn.cursor()

    # insert_sql = '''INSERT INTO tb_book(tb_book.bookName, tb_book.author) VALUES({0}, {1})'''.format('jj_ll', 'jj')
    # query_sql = '''SELECT * FROM tb_book'''

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

# if __name__ == '__main__':
#     insert_sql = '''INSERT INTO tb_book(tb_book.bookName) VALUES('鲁滨逊漂流记11')'''
#     sql_to_db(insert_sql)
