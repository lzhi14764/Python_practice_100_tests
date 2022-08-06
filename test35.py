#!/usr/bin/python
# -*- coding: UTF-8 -*-

def hello_runoob():
    print 'runoob'

def hello_runoobs():
    for i in range(3):
        hello_runoob()
if __name__ == '__main__':
    hello_runoobs()