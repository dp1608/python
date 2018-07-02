# -*- coding: utf-8 -*-
# @StartTime : 8/1/2017 22:02
# @EndTime   : 8/1/2017 22:02
# @Author    : Andy
# @Site      : 
# @File      : Array PartitionI.py
# @Software  : PyCharm


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=0
        for i in range(0,len(nums),2):
            ans=ans+nums[i]
        return ans

S=Solution()
ans=S.arrayPairSum([1,4,3,2])
print ans