# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import requests

# 使用函数封装


def get_html(url):
    '''
    return 页面html
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    html = requests.get(url, headers=headers)
    return html


def get_img(html):
    '''
    处理html 得到想要的数据，图片
    return imglist
    '''
    imglist = []
    soup = BeautifulSoup(html.text, 'lxml')
    target_img = soup.find('div', class_="TypeList").find_all('img')
    for img in target_img:
        imglist.append(img.get('src'))
    return imglist

def empty_folder(path):
    '''
    写入之前先清空
    '''
    file_ls = os.listdir(path)
    for i in file_ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            empty_folder(c_path)
        else:
            os.remove(c_path)


if __name__ == '__main__':
    empty_folder('/Users/liunan/Desktop/python_demo/beauty_demo/beauty')
    print(100 * '=')
    print('目标网站:http://www.umei.cc/p/gaoqing/xiuren_VIP/')    
    print('作者:liunanchenFYJJ@github.com')    
    print(100 * '=')

    number = input('请输入页码:')
    while True:
        if number.isdigit():
            last_page_num = int(number)
            try:
                print('下载中——海量美女图片正在路上...') 
                for i in range(1, last_page_num + 1):
                    # 目标网站
                    target_url = 'http://www.umei.cc/p/gaoqing/xiuren_VIP/' + str(i) + '.htm'

                    target_html = get_html(target_url)
                    target_imglist = get_img(target_html)

                    for imgurl in target_imglist:
                        print(str(i) + '_' + str(target_imglist.index(imgurl) + 1))
                        # 存放路径
                        target_pathName = '/Users/liunan/Desktop/python_demo/beauty_demo/beauty/img' + str(i) + '_' + str(target_imglist.index(imgurl) + 1) + '.jpg'
                        # 设备图片下载路径 和 文件名称
                        with open(target_pathName, 'wb') as f:
                            f.write(requests.get(imgurl).content)
                print('下载完成!') 
            except Exception as e:
                print(e)
            break
        else:
            number = input('请重新输入页码:')
