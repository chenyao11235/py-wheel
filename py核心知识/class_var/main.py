#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/15 14:38
# @Author     : chenyao

'''类变量和实例变量
    类变量保存在类的命名空间中，
    通过类修改类变量的值，会影响所有的实例
    通过实例子修改类变量的值，只会影响该实例，不会影响其他的实例
'''


class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    a = A(2, 3)
    A.aa = 11
    a.aa = 100
    print(a.x, a.y, a.aa)
    print(A.aa)

    b = A(3, 5)
    print(b.aa)
