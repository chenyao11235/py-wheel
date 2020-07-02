#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/6/14 23:50


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super.__new__(cls)


class IntField:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class User(metaclass=MetaClass):
    age = IntField()


if __name__ == "__main__":
    pass
