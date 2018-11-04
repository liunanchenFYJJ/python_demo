# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getelement(url):
    try:
        html = requests.get(url)
    except Exception as e:
        print(e)
        return None

    try:
      soup = BeautifulSoup(html.text, 'lxml')
      h1 = soup.h1
    except Exception as e:
      return None
    
    return h1

def main():
    h1 = getelement('http://www.pythonscraping.com/pages/page1.html')
    if h1 == None:
        print('element not found')
    else:
        print(h1)


if __name__ == '__main__':
    main()