# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        html_text = requests.get(url).text
    except Exception as e:
        print(e)
        return None
    return html_text

def main():
    target_url = 'http://www.pythonscraping.com/pages/warandpeace.html'
    target_html_text = get_html(target_url)
    soup = BeautifulSoup(target_html_text, 'lxml')
    namelist = soup.find_all('span', {"class": {"green", "red"}})
    for i in namelist:
        print(i.get_text())

    # print(namelist)

if __name__ == '__main__':
    main()
    