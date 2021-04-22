#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   executors.py
@Time    :   2021/04/22 10:36:19
@Desc    :   None
'''

# here put the import lib
import asyncio
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

MULTI_NUM = 10

thread_pool = ThreadPoolExecutor(MULTI_NUM)
process_pool = ProcessPoolExecutor(MULTI_NUM)
pycoroutines = asyncio.get_event_loop()