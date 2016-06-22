#coding=utf-8
'''
Created on 2016年6月23日

@author: Administrator
'''

import socket

target_host = "www.baidu.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("test",(target_host,target_port))

data,addr  = client.recvfrom(4096)

print data+addr
