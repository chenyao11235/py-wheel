#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   leetcode.py
@Time    :   2020/07/15 11:04:42
@Desc    :   刷的leetcode题目
'''

# here put the import lib

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==0:return -1
        if len(nums)==1:return 1
        numSum=[0]
        for i in range(len(nums)):
            numSum.append(numSum[i]+nums[i])
        for i in range(1,len(numSum)):
            if numSum[i-1]==numSum[-1]-numSum[i]:return i-1
        return -1