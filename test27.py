#!/usr/bin/python
# -*- coding: UTF-8 -*-

def output(s,l):
    if l == 0:
        return
    print (s[l - 1])
    output(s,l - 1)

s = raw_input('please input a test: \n')
l = len(s)
output(s,l)