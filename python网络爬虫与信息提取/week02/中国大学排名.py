# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/9/2 23:27'


import requests
from bs4 import BeautifulSoup
import bs4
import pprint



def getHtml(url):
    """
    获得指定url的html页码数据
    :param url: 
    :return: html页码内容
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""



def fillUnivList(ulist,html):
    """
    解析html获得自定的字段，组成list结构返回
    :param ulist: 
    :param html: 
    :return: 
    """
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):   #过滤掉非标签类型的条件
            tds = tr('td')
            # print(tds)
            ulist.append((tds[0].string,tds[1].string,tds[3].string))

    return ulist

def printUnivlist(ulist,num):
    """
    打印指定行数的大学排名
    :param ulist: 
    :return: 
    """
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('排名','学校名称','分数',chr(12288)))  #使用中文的空格来填充，而不是英文字符，因为字符和中文字符赞扬
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))




def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    ulist = []
    html = getHtml(url)
    ulist = fillUnivList(ulist,html)

    # print(pprint.pprint(ulist))
    printUnivlist(ulist,20)

if __name__ == '__main__':
    main()
