#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    n1 = int(raw_input('n1 = :\n'))
    n2 = int(raw_input('n2 = :\n'))
    n3 = int(raw_input('n3 = :\n'))

    def swap(n1,n2):
        return n2,n1

    if n1 > n2:n1,n2 = swap(n1,n2)
    if n1 > n3:n1,n3 = swap(n1,n3)
    if n2 > n3:n2,n3 = swap(n2,n3)

    print n1,n2,n3