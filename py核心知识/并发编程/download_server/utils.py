#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2021/04/22 09:52:55
@Desc    :   None
'''

# here put the import lib
import os


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    url_list = []
    with open(list_file, "r") as f:
        url_list = [line.strip() for line in f]
    return url_list

