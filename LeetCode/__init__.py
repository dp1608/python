# -*- coding: utf-8 -*-
# @StartTime : 2018/5/8 15:38
# @EndTime : 2018/5/8 15:38
# @Author  : Andy
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


#!/usr/bin/env python
# coding=utf-8

class Foo(object):

    instance = None

    def __init__(self, name):
        self.name = name


    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls('hexm')
            cls.instance = obj
            return obj

obj = Foo.get_instance()
obj1 = Foo.get_instance()
print(obj.name)
print(obj1.name)
print(Foo.instance)
print(obj)