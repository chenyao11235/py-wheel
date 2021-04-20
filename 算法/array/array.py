#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   array.py
@Time    :   2020/07/15 11:08:35
@Desc    :   None
'''

class my_array:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    
    def _index_out_of_array(self):
        raise Exception("array is full, out of array")

    def _is_full(self):
        return len(self.data) >= self.capacity

    def insert(self, index: int, value: int):
        pass

    def find(self, index:int) ->int:
        return self.data[index]

    def delete(self, index:int) -> bool:
        pass