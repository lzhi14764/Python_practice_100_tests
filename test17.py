#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = raw_input('请输入字符:\n')
letters = 0
space = 0
digit = 0
others = 0
i = 0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d'%(letters,space,digit,others)
