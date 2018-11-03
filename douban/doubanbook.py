# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
# 自己编写的模块
from Book import Book
import mysql

def get_html(url):
    '''
    返回页面代码
    '''
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    try:
        html = requests.get(url, headers=headers)
    except Exception as e:
        print(e)
    return html

def get_book_list(html):
    '''
    页面处理——得到需要的数据
    '''
    book_url_list = []
    try:
        soup = BeautifulSoup(html.text, 'lxml')
        div_list = soup.find_all('div', class_='detail-frame')
        for div_item in div_list:
            href = div_item.find('a').get('href')
            book_url_list.append(href)
    except Exception as e:
          print(e)
    return book_url_list

def get_book_detail(html):
    '''
    取得子页面书籍的详情
    '''
    # book_detail = []
    soup = BeautifulSoup(html.text, 'lxml')
    # 取得相关数据
    try:
        book_name = soup.find(property="v:itemreviewed").text
        author = soup.find(id="info").find('a').text
        # 使用Book类
        book = Book(book_name, author)
        return book
    except Exception as e:
        print(e)



if __name__ == "__main__":
    print(6 * '=' + '数据正在插入' + 6 * '=')
    url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    book_html = get_html(url)
    book_list = get_book_list(book_html)

    if book_list == None:
        print('element not found')
    else:
        for book_list_item in book_list:
            sub_page_html = get_html(book_list_item)
            book = get_book_detail(sub_page_html)

            try:
                insert_sql = '''INSERT INTO tb_book(tb_book.bookName, tb_book.author) VALUES("{0}", "{1}")'''.format(book.book_name, book.author)
                mysql.sql_to_db(insert_sql)
            except Exception as e:
                print(e)
        print(6 * '=' + '数据插入完成！' + 6 * '=')
    
