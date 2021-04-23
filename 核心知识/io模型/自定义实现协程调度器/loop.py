#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   loop.py
@Time    :   2021/04/20 22:01:23
@Desc    :   None
'''

# here put the import lib
import inspect
import functools
from queue import deque

from wrapper import CoroutineWrapper


class YieldLoop:
    """协程调度器
    """
    current = None 
    runnables = deque()

    # 单例模式
    @classmethod
    def instance(cls):
        if not YieldLoop.current:
            YieldLoop.current = YieldLoop()
        return YieldLoop.current
    
    def add_runables(self, coro):
        self.runnables.append(coro)

    def add_coroutine(self, coro):
        """添加协程到调度器
        """
        assert isinstance(coro, CoroutineWrapper), "coro is not CoroutineWrapper instance"
        self.add_runables(coro)

    def run_coroutine(self, coro):
        """执行协程
        """
        try:
            # print("run coro: ", coro)
            coro.send(coro.context)
        except StopIteration as e:
            print("coroutine {} stop".format(coro))

    def run_until_complete(self):
        """直到所有的协程都被执行完毕
        """
        while YieldLoop.runnables:
            # print("runables: ", YieldLoop.runnables)
            coro = YieldLoop.runnables.popleft()
            self.run_coroutine(coro)


def coroutine(func):
    """定义生成器协程适配器的装饰器
    被此装饰器装饰的普通生成器将会变成 生成器协程适配器 
    从而可以被协程调度器调度
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        if inspect.isgenerator(gen):
            coro = CoroutineWrapper(YieldLoop.instance(), gen)
            return coro
        else:
            raise RuntimeError('[CoroutineWrapper] error.\
                type({}) is not supported.'.format(type(gen)))
    return wrapper