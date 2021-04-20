#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   transaction.py
@Time    :   2020/10/13 14:40:19
@Desc    :   redis的事务怎么用
'''

# here put the import lib

import redis

def key_for(user_id):
    return "account_{}".format(user_id)

def double_account(client, user_id):
    key = key_for(user_id)
    while True:
        pipe = client.pipeline(transaction=True)
        pipe.watch(key)
        value = int(pipe.get(key))
        value *= 2  # 加倍
        pipe.multi()
        pipe.set(key, value)
        try:
            pipe.execute()
            break  # 总算成功了
        except redis.WatchError:
            continue  # 事务被打断了，重试, key在其他地方被修改了
    return int(client.get(key))  # 重新获取余额


if __name__ == "__main__":
    client = redis.StrictRedis(host="10.211.55.5", port=6379, db=0)

    user_id = "abc"
    client.setnx(key_for(user_id), 5)  # setnx 做初始化
    print(double_account(client, user_id))