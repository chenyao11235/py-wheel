#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   storage.py
@Time    :   2021/04/22 10:23:10
@Desc    :   None
'''

# here put the import lib
from PIL import Image
from modules.base import BaseModule
from modules.executors import thread_pool as tp
from modules.executors import process_pool as pp


class Storage(BaseModule):
    """存储模块
    """
    
    def _process(self, item):
        content, path = item
        content = Image.fromarray(content.astype("uint8")).convert("RGB")
        content.save(path)
        print("save path: {}".format(path))

    def _process_singlethread(self, list_):
        for item in list_:
            self._process(item)

    def _process_multithread(self, list_):
        """存储是最后一个模块了，不需要返回了
        """
        task_list = []
        for item in list_:
            task = tp.submit(self._process, (item))
            task_list.append(task)
        for task in task_list:
            task.result()

    def _process_multiprocess(self, list_):
        """存储是最后一个模块了，不需要返回了
        """
        task_list = []
        for item in list_:
            task = pp.submit(self._process, (item))
            task_list.append(task)
        for task in task_list:
            task.result() 

    def _process_coroutine(self, list_):
        return self._process_multithread(list_)
