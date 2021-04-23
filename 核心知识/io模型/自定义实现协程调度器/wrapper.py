#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wrapper.py
@Time    :   2021/04/20 22:20:03
@Desc    :   None
'''

# here put the import lib


class CoroutineWrapper:
    """生成器协程适配器
    重写生成器的方法：send，next
    使得生成器可以在调度器loop中执行
    """

    def __init__(self, loop, gen):
        # YieldLoop
        self.loop = loop
        # 生成器
        self.gen = gen
        # 生成器上下文
        self.context = None

    def send(self, val):
        val = self.gen.send(val)
        self.context = val
        self.loop.add_runables(self)

    def throw(self, tp, **rest):
        return self.gen.throw(tp, **rest)

    def close(self):
        return self.gen.close()

    def __next__(self):
        val = next(self.gen)
        self.context = val
        self.loop.add_runables(self)
    
    def __getattr__(self, name):
        """拦截生成器的其他方法
        保证原来生成器的所有方法可以被正确执行
        """
        return getattr(self.gen, name)

    def __str__(self):
        return "coroutinewrapper: {}, context:{}".format(self.gen, self.context)