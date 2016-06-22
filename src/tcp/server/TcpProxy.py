#coding=utf-8
'''
Created on 2016年6月23日

@author: Administrator
'''
import socket
import threading

'''
this is a pretty hex dumping function directly taken from
http://code.activestate.com/recipes/142812-hex-dumper/
This function produce a classic 3 columns hex dump of a string. 
* The first column print the offset in hexadecimal. 
* The second colmun print the hexadecimal byte values. 
* The third column print ASCII values or a dot for non printable characters.
'''
def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
        result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) )

    print b'\n'.join(result)
    

