#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   downloader.py
@Time    :   2021/04/22 09:38:19
@Desc    :   None
'''

# here put the import lib
import requests
from PIL import ImageFile
import numpy as np
import aiohttp

from const import CalcType
from modules.base import BaseModule
from modules.executors import thread_pool as tp
from modules.executors import process_pool as pp
from modules.executors import pycoroutines as co


class Downloader(BaseModule):

    def _process(self, url):
        print("download url: {}".format(url))
        response = requests.get(url)
        content = response.content
        # 图片转numpy数组
        parser = ImageFile.Parser()
        parser.feed(content)
        image = parser.close()
        img = np.array(image)
        return img

    def _process_singlethread(self, list_):
        response_list = []
        for url in list_:
            img = self._process(url)
            response_list.append(img)
        return response_list

    def _process_multithread(self, list_):
        response_list = []
        task_list = []
        for url in list_:
            task = tp.submit(self._process, (url))
            task_list.append(task)
        for task in task_list:
            image = task.result()
            response_list.append(image)
        return response_list
    
    def _process_multiprocess(self, list_):
        response_list = []
        task_list = []
        for url in list_:
            task = pp.submit(self._process, (url))
            task_list.append(task)
        for task in task_list:
            image = task.result()
            response_list.append(image)
        return response_list

    def _process_coroutine(self, list_):
        response_list = []
        aiohttp_session = aiohttp.ClientSession()

        async def main():
            for url in list_:
                async with aiohttp_session.get(url) as response:
                    content = await response.read()
                    # 图片转numpy数组
                    parser = ImageFile.Parser()
                    parser.feed(content)
                    image = parser.close()
                    img = np.array(image)
                    response_list.append(img)
        co.run_until_complete(main())
        return response_list
