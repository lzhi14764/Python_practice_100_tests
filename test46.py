#!/usr/bin/python
# -*- coding: UTF-8 -*-

True = 1
False = 0

def SQ(x):
    return x*x

again = 1
while(again):
    num = int(input("请输入数字："))
    print ("运算结果=%d"%SQ(num))
    if SQ(num) >= 50:
        again = True
    else:
        again = False