#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Foo(object):
    __count = 0 # 私有变量，无法在外部访问，Foo.__count会出错

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls, num):
        cls.__count = num

f1 = Foo()
f2 = Foo()
Foo.set_count(1)
print(f1.get_count(), f2.get_count())
# 结果:
