#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = int(raw_input("please input a number:\n"))
x = str(a)
flag = True
for i in range(len(x)/2):
    if x[i] != x[-i-1]:
        flag = False
        break
if flag:
    print "%d is a 回文数"%a
else:
    print "%d not a 回文数"%a