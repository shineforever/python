#! /usr/bin/env python
#coding:utf-8
#通过paramiko模块，获得远程机器的指定进程相关信息；


import paramiko

host_lists=(
            ('node1','172.16.41.151'),
            ('node2','172.16.41.152'),
            ('node3','172.16.41.153'),
            ('node4','172.16.41.158')
        )



def getServerInfo(host,user,password,services):
     conn = paramiko.SSHClient()
     conn.load_system_host_keys()
     conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     conn.connect(host,22,user,password)
     stdin,stdout,stderr = conn.exec_command("ps aux|awk '{print $3,$4,$5,$6,$11}'|grep %s" % services)
     info = stdout.read()
     conn.close()

     return info

if __name__ == '__main__':
    print "hostname   %CPU   %MEM   VSZ   RSS   services"
    for host in host_lists:
        try:
            info = getServerInfo(host[1],'root','routon','cupsd')
            info_list = info.split()
            print "%s %s %s %s %s %s " % (host[0],info_list[0],info_list[1],info_list[2],info_list[3],info_list[4] )
        except:
            pass
