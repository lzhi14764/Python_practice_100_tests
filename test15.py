#!/usr/bin/python
# -*- coding: UTF-8 -*-

grade = int(raw_input('分数:'))
if grade > 90:
    score = 'A'
elif grade > 60:
    score = 'B'
else:
    score = 'C'
print '%d 属于 %s,'%(grade,score)
