#! /usr/bin/env python
# coding:utf-8

import platform

def getHostInfo():
    """
    获得系统的主机名，发行版本名称，版本；以及安装操作系统的32位或者64位；
    """
    pd = {}
    version = platform.dist()
    os_name = platform.node()
    os_release = platform.release()
    os_version = ' %s %s' % (version[0],version[1])
    pd['os_name'] = os_name
    pd['os_release'] = os_release
    pd['os_version'] = os_version
    return pd

if __name__ == '__main__':
    print getHostInfo()
    
