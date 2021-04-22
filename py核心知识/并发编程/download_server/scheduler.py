#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scheduler.py
@Time    :   2021/04/22 09:50:48
@Desc    :   None
'''

# here put the import lib
import os
import utils
import prettytable

from const import CalcType
from modules.downloader import Downloader
from modules.hasher import Hasher
from modules.storage import Storage

class Scheduler:
    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storage = Storage()

    def _wrap_path(self, md5):
        filename = "{}.jpg".format(md5)
        STORAGE_PATH = os.path.join(".", "images")
        path = os.path.join(STORAGE_PATH, filename)
        return path

    def set_calc_type(self, type_):
        self.downloader.set_calc_type(type_)
        self.hasher.set_calc_type(type_)
        self.storage.set_calc_type(type_)

    def process(self):
        # 1.加载图片列表
        url_list = utils.urllist()
        # 2.调度下载模块
        content_list = self.downloader.process(url_list)
        # 3. 计算哈希
        md5_list = self.hasher.process(content_list)
        for md5 in md5_list:
            print(md5)
        # 4.存储模块
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        self.storage.process(item_list)
    
    def statictics(self, log):
        table = prettytable.PrettyTable("类型", "线程总耗时")
        network_row = ["network"]
        cpu_row = ["cpu"]
        disk_row = ["disk"]
        network_row.append(log["network_time"][0])
        cpu_row.append(log["cpu_time"][0])
        disk_row.append(log["disk_time"][0])
        table.add_row(network_row)
        table.add_row(cpu_row)
        table.add_row(disk_row)
        print(table)


if __name__ == "__main__":
    scheduler = Scheduler()
    # 单线程运行
    # scheduler.set_calc_type(CalcType.SingleThread)
    # 多线程运行
    # scheduler.set_calc_type(CalcType.MultiThread)
    # 多进程运行
    # scheduler.set_calc_type(CalcType.MultiProcess)
    # 协程运行
    scheduler.set_calc_type(CalcType.PyCoroutine)
    scheduler.process()