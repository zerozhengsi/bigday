#coding=utf-8
'''
Created on 2016年6月23日

@author: zeroz
'''
import unittest
from tcp.server import TcpProxy


class Test(unittest.TestCase):



    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testHexdump(self):
        s=("This 10 line function is just a sample of pyhton power "
           "for string manipulations.\n"
           "The code is \x07even\x08 quite readable!")
        TcpProxy.hexdump(s)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()