#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sub.py
@Time    :   2020/10/13 14:47:13
@Desc    :   None
'''

# here put the import lib
import redis

if __name__ == "__main__":
    client = redis.StrictRedis()
    client.publish("codehole", "python comes")
    client.publish("codehole", "java comes")
    client.publish("codehole", "golang comes")
