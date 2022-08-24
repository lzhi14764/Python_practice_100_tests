#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = [1,4,3]
    b = [4,5,6]
    a.sort()
    print a
    c = (a + b)
    print c
    a.append(b)
    print a
