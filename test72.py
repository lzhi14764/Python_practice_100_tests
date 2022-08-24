#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    pr = []
    for i in range(3):
        num = int(raw_input('please input a number:\n'))
        pr.append(num)
    print pr
    pr.reverse()
    print pr