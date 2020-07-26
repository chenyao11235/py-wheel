#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 16:56
# @Author     : chenyao

"""
java既支持接口，也支持抽象类。golang只支持接口，但是python这两者都不支持。

为什么要使用抽象类？
    抽象类是一种设计思想，抽象类不能实例化，它的子类可以，抽象类用来描述一组类通用的行为和特征, 强制抽象类的子类实现抽象方法
    即使python不支持我们也可以通过基础的面向对象语法实现和抽象类类似的功能，
"""


class CacheClass:
    def get(self):
        raise NotImplementedError

    def set(self):
        raise NotImplementedError


class RedisClass(CacheClass):
    pass


if __name__ == "__main__":
    redis_cache = RedisClass()
    redis_cache.get()  # 调用这个方法将会抛出异常
    redis_cache.set()  # 调用这个方法将会抛出异常

"""
依靠abc模块也可以实现抽象类的面向对象特性
"""
