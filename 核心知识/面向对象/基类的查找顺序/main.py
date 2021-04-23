#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/15 14:56
# @Author     : chenyao

from threading import Thread

"""
1.新式类的基类查找顺序是： 广度优先
2.经典类的基类查找顺序是：从左往右，深度优先
"""


'''既然要重写父类的init方法为什么还要通过super调用父类的init方法？
        因为在某些场景下需要把一些参数传递给父类的init方法
'''


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)


# 既然我们重写B的构造函数， 为什么还要去调用super？
# super到底执行顺序是什么样的？


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == "__main__":
    print(D.__mro__)
    d = D()

