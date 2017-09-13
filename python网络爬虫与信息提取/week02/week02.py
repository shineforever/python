# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/8/31 17:46'

import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://www.python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,'html.parser')

print(soup.original_encoding)
print(soup.find_all('a',class_="py2"))
tbody = soup.find('body')
# print(tbody)

print(soup.find_all('p',class_='py1'))
# print soup.prettify()
# print("8888888888888")
# for i in soup.body.children:
#     print(i)



#
# print soup.title.parent
#
# print(99999)
# print soup.a
#
# for i in soup.a.parents:
#     if i is None:
#         print i
#     else:
#         print i.name
#
# """
# 平行遍历
# """
# print('平行遍历')
#
# print('遍历a标签后续节点')
# for sibling in soup.a.next_siblings:
#     print(sibling)
#
#
# print('遍历a标签前续节点')
# for sibling in soup.a.previous_siblings:
#     print(sibling)