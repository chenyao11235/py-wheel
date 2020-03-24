#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:32
# @Author     : chenyao

"""
混乱的继承：
                       鸟
            会飞                  不会飞
       会叫     不会叫         会叫      不会叫

    可以将飞和叫抽象成接口，针对不通种类的鸟把不同的接口组合就行了

推荐使用组合，少使用继承：
    继承可以提高代码的复用，但是随着代码的增多，不断的抽象出新的类，继承层次过深、继承关系过于复杂会影响到代码的可读性和可维护性。
    所以比较推荐接口的组合，但是python不支持接口，通过mixin的继承方式可以实现类似接口组合的效果
"""


class Fly:
    def fly(self):
        print("fly...")


class Swim:
    def swim(self):
        print("swim...")


class EatMeat:
    def eat_meat(self):
        print("eat meat...")


class Bird1Mixin:
    def swim(self):
        super().swim()

    def fly(self):
        super().fly()


class Bird2Mixin:
    def eat_meat(self):
        super().eat_meat()

    def fly(self):
        super().fly()


# 海鸥
class Seagull(Bird1Mixin, Fly, Swim):
    def fly(self):
        super().fly()

    def swim(self):
        super().swim()


# 老鹰
class Eagle(Bird2Mixin, Fly, EatMeat):
    def fly(self):
        super().fly()

    def eat_meat(self):
        super().eat_meat()


"""
多继承的时候形成一个继承链，通过super方法去不通的父类中寻找
"""

if __name__ == "__main__":
    s = Seagull()
    s.fly()

    e = Eagle()
    e.eat_meat()
