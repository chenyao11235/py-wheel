#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bsub.py
@Time    :   2020/10/13 14:48:45
@Desc    :   None
'''
 
import time
import redis

# here put the import lib
if __name__ == "__main__":
    client = redis.StrictRedis()
    p = client.pubsub()
    p.subscribe("codehole")
    for msg in p.listen():
        print(msg)