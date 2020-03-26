#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:13
# @Author     : chenyao

"""
借助abc模块实现抽象类
"""
import abc


class CacheClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def set(self):
        pass


class RedisClass(CacheClass):
    pass


if __name__ == "__main__":
    rc = RedisClass()
