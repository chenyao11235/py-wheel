#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2021/04/22 10:04:04
@Desc    :   None
'''

# here put the import lib
from const import CalcType

class BaseModule:
    def __init__(self):
        self.calc_type = CalcType.SingleThread

    def set_calc_type(self, type_):
        self.calc_type = type_

    def _process(self, url):
        raise NotImplementedError

    def _process_singlethread(self, list_):
        raise NotImplementedError

    def _process_multithread(self, list_):
        raise NotImplementedError

    def _process_multiprocess(self, list_):
        raise NotImplementedError
    
    def _process_coroutine(self, list_):
        raise NotImplementedError

    def process(self, list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_)
        elif self.calc_type == CalcType.MultiThread:
            return self._process_multithread(list_)
        elif self.calc_type == CalcType.MultiProcess:
            return self._process_multiprocess(list_)
        elif self.calc_type == CalcType.PyCoroutine:
            return self._process_coroutine(list_)