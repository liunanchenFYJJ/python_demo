# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        html_text = requests.get(url).text
    except Exception as e:
        print(e)
        return None
    return html_text

# 可以建立一个pages集合用来排重
pages = set()
def get_new_links(newurl):
    '''
    根据传入newurl打印本页一些信息
    取得跳转target_links，递归跳转
    '''
    global pages
    html = get_html('https://en.wikipedia.org' + newurl)
    soup = BeautifulSoup(html, 'lxml')
    # 打印每夜的信息
    try:
        print(soup.h1.get_text())
        print(soup.find(id="mw-content-text").findAll("p")[0])
        print(soup.find(id="ca-edit").find("span").find("a").attrs['href']) 
    except Exception as e:
        print('页面没有该属性！')
    target_links = soup.find('div', {"id": "bodyContent"}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    for i in target_links:
        if 'href' in i.attrs:
            if i.attrs['href'] not in pages:
                new_page_url = i.attrs['href']
                pages.add(new_page_url)
                # 递归
                get_new_links(new_page_url)


def main():
    get_new_links('')
    

if __name__ == '__main__':
    main()
    