#! /usr/bin/env python
#coding:utf-8


import paramiko

paramiko.util.log_to_file('/home/guolt/paramiko_log.txt')

ssh=paramiko.SSHClient

ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())



ssh.connect('127.0.0.1',port=22,username='guolt',password='routon')


stdin,stdout,stderr=ssh.exec_command('hostname','uptime')
print stdout.read()


ssh.close()


