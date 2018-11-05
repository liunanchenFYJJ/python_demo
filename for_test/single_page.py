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
    target_url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
    target_html_text = get_html(target_url)
    soup = BeautifulSoup(target_html_text, 'lxml')
    a_list = soup.find('div', {"id": "bodyContent"}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    for i in a_list:
        print(i)

    # print(a_list)

if __name__ == '__main__':
    main()
    