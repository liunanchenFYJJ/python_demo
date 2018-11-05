# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import random
import datetime

# 作用？
# 根据系统时间生成随机数，保证每次程序运行时，维基百科词条都是一个全新的随机路径
random.seed(datetime.datetime.now())

def get_html(url):
    try:
        html_text = requests.get(url).text
    except Exception as e:
        print(e)
        return None
    return html_text

def get_new_links(newurl):
    html = get_html('https://en.wikipedia.org' + newurl)
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('div', {"id": "bodyContent"}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def main():
    target_url = '/wiki/Kevin_Bacon'
    target_links = get_new_links(target_url)
    while len(target_links) > 0:
        new_page_url = target_links[random.randint(0, len(target_links) - 1)].attrs['href']
        print(new_page_url)
        target_links = get_new_links(new_page_url)
    

if __name__ == '__main__':
    main()
    