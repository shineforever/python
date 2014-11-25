#! /usr/bin/python
#coding:utf-8

import httplib

def check_webserver(address,port,resource):
    if not resource.startswith('/'):
        resource = '/' + resource
    try:
        conn = httplib.HTTPConnection(address,port)
        print "###############connected sucessfull..#####"
        req = conn.request('GET',resource)
        print "request ok!!!!"
        res = conn.getresponse()
        print "response ok! status: %s" % res.status
    except httplib.error,e:
        print "HTTP connection failed: %s" % e
        return False
    finally:
        conn.close()
        print "connection close sucessful"
    if res.status in [200,301]:
        return True
    else:
        return False

if __name__ == '__main__':
    check_webserver('www.baidu.com',80,'/index.html')




