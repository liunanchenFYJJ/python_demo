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

def main():
    target_url = 'http://www.pythonscraping.com/pages/page3.html'
    target_html_text = get_html(target_url)
    soup = BeautifulSoup(target_html_text, 'lxml')
    # 这样获取所有的图片会有冗余
    # imglist  = soup.find_all('img')
    # 使用正则
    # 把属性值换成正则表达式
    regex_str = re.compile('\.\.\/img\/gifts\/img.\.jpg')
    imglist = soup.find_all('img', {"src": regex_str})
    for i in imglist:
        # attrs 获取属性
        print(i.attrs) 

    # print(namelist)

if __name__ == '__main__':
    main()
    