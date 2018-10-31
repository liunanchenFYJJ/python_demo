# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Book(object):
    # 1）定义几个变量，实例化时就需要传入几个变量
    # def __init__(self, book_name, book_rate, author, publish_date, book_comment, book_cover):
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        # self.book_rate = book_rate
        # self.publish_date = publish_date
        # self.book_comment = book_comment
        # self.book_cover = book_cover
    # 2）实例化时根据实际传入参数进行，此时的book_class定义怎么写？？todo
    # def __init__(self, *args):
    #     # print(*args)
    #     (self.book_name, self.book_rate) = args


# 1）
# book = Book('dialog', 8, 'me', '2019', 'good', 'img')
# print(book.book_name)
# print(book.book_rate)

# 2）
# book = Book('kk', 8)
