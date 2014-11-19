#! /usr/bin/env python
#coding:utf-8


import paramiko


def get_hostname():
    paramiko.util.log_to_file('/tmp/paramiko_log.txt')

    ssh=paramiko.SSHClient()

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect('172.16.41.151',port=22,username='root',password='routon')
    stdin,stdout,stderr=ssh.exec_command('hostname;uptime')
    print stdout.read()


    ssh.close()


def scp():
    scp=paramiko.Transport(('172.16.41.151',22))
    scp.connect(username='root',password='routon')

    #建立一个sftp客户端对象，通过ssh transport操作远程文件
    sftp=paramiko.SFTPClient.from_transport(scp)

    #把远程文件下载到本地local machine
    sftp.get('/root/install.log','/tmp/node1_install.log')

    #把本地文件上传到远端remote
    sftp.put('/usr/local/python/README.md','/tmp/node29_readme.txt')
    scp.close()


if __name__ == '__main__':
#    get_hostname()
     scp()


