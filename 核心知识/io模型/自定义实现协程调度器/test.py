#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2021/04/20 22:46:41
@Desc    :   None
'''

# here put the import lib
import time
import random
import string
from queue import deque
from loop import YieldLoop, coroutine


@coroutine
def test1():
    sum = 0
    for i in range(1, 11):
        if i % 2 == 1:
            sum += yield i 
    print('sum = ', sum)


@coroutine
def producer(q):
    while True:
        good = ".".join(random.sample(string.ascii_letters+string.digits, 8))
        q.append(good)
        cnt = len(q)
        print("producer produce good. cnt = ", cnt)
        if cnt > 0:
            yield

@coroutine
def consumer(q):
    while True:
        while len(q) <= 0:
            print("queue is empty")
            yield
        good = q.popleft()
        print("consumer consume good = {}, cnt = {}".format(good, len(q)))
        time.sleep(1)



# YieldLoop.instance().add_coroutine(test1())
# YieldLoop.instance().run_until_complete()

q = deque()

YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(consumer(q))
YieldLoop.instance().run_until_complete()

