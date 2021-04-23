#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   producer-consumer-yield.py
@Time    :   2021/04/20 19:44:21
@Desc    :   None
'''

# here put the import lib
import time

# 消费者
def consumer():
    cnt = yield
    while True:
        if cnt <= 0:
            # 让出cpu
            cnt = yield cnt
        cnt -= 1
        time.sleep(1)
        print("consumer consum 1 cnt. cnt = ", cnt)


# 生产者
def producer(cnt):
    gen = consumer()
    next(gen)
    gen.send(cnt)
    while True:
        cnt += 5
        print("producer produce 5 cnt, cnt = ", cnt)
        cnt = gen.send(cnt)

if __name__ == "__main__":
    producer(0)