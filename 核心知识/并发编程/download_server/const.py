#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   const.py
@Time    :   2021/04/22 09:44:41
@Desc    :   None
'''

# here put the import lib

from enum import Enum

class CalcType(Enum):
    SingleThread = 0
    MultiThread = 1
    MultiProcess = 2
    PyCoroutine = 3