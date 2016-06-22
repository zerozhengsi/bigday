#coding=utf-8
'''
Created on 2016年6月23日

@author: Administrator
'''

import socket

target_host = "127.0.0.1"
target_port = 9000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

response  = client.recv(4096)

print response
