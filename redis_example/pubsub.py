#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pubsub.py
@Time    :   2020/10/13 14:43:27
@Desc    :   None
'''

# here put the import lib

import time
import redis

if __name__ == "__main__":
    client = redis.StrictRedis()
    p = client.pubsub()
    p.subscribe("codehole")
    time.sleep(1)
    print(p.get_message())
    client.publish("codehole", "java comes")
    time.sleep(1)

    print(p.get_message())
    client.publish("codehole", "python comes")
    time.sleep(1)
    
    print(p.get_message())
    print(p.get_message())