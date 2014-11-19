#! /usr/bin/env python
#coding:utf-8
#网络爬虫学习demo


import re
import urllib2
import MySQLdb
from BeautifulSoup import BeautifulSoup

url="http://www.baidu.com"
fp=urllib2.urlopen(url)
s=fp.read()
soup=BeautifulSoup(s)
polist=soup.findAll('span')
print polist[0].contents[0]



