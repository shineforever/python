# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/9/11 22:40'

import requests
import re


def getHtmlText(url):
    """
    获取html里面内容
    :param url: 
    :return: 
    """
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt,html):
    """
    解析页面，获取商品的名称和价格，放入list
    :param ilt: 
    :param html: 
    :return: 
    """
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d+\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([title,price])
            #
    except:
        print("")

    return ilt

def printGoodList(ilt):
    """
    打印结果
    :param ilt: 
    :return: 
    """
    tp = '{:4}\t{:16}\t{:8}'
    count = 0
    for i in ilt:
        count = count +1
        print(tp.format(count,i[0],i[1]))

if __name__ == '__main__':
    keyword = '帆布鞋'
    start_url = 'https://s.taobao.com/search?q=' + keyword
    depth = 5
    info_list = []
    for i in range(depth):
        try:
            new_url = start_url  + "&s=" + str(44*i)
            html_context = getHtmlText(new_url)
            info_lists = parsePage(info_list,html_context)
        except:
            continue  #有异常，直接忽略，继续下面的任务
        printGoodList(info_lists)



