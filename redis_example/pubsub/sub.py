#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sub.py
@Time    :   2020/10/13 14:47:56
@Desc    :   None
'''

# here put the import lib
import time
import redis

if __name__ == "__main__":
    client = redis.StrictRedis()
    p = client.pubsub()
    p.subscribe("codehole")
    while True:
        msg = p.get_message()
        if not msg:
            time.sleep(1)
            continue
        print(msg)
