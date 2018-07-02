# -*- coding: utf-8 -*-
# @StartTime : 11/5/2017 23:16
# @EndTime   : 11/5/2017 23:16
# @Author    : Andy
# @Site      : 
# @File      : 171105search_in_rotated_sorted_array.py
# @Software  : PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def erfen(self,i,j,target):
            temp = (i + j) / 2
            if nums[temp] == target:
                return temp
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if temp == i:
                return -1
            if nums[temp] < target:
                return erfen(self,temp,j,target)
            else:
                return erfen(self,i,temp,target)


        if len(nums) == 0:
            return -1
        min_index = 0
        max_index = len(nums) - 1
        if target >= nums[min_index]:
            while 1:
                middle = (min_index + max_index) / 2
                if min_index >= max_index - 1 :
                    res = erfen(self, min_index, max_index, target)
                    return res
                if nums[middle] > nums[0] and nums[middle] >= target:
                    res = erfen(self, min_index, middle, target)
                    return res
                if nums[middle] > nums[0] and nums[middle] < target:
                    min_index = middle
                if nums[middle] < nums[0]:
                    max_index = middle
        if target < nums[min_index]:
            while 1:
                middle = (min_index + max_index) / 2
                if min_index >= max_index - 1 :
                    res = erfen(self, min_index, max_index, target)
                    return res
                if nums[middle] < nums[0] and nums[middle] <= target:
                    res = erfen(self,middle,max_index,target)
                    return res
                if nums[middle] < nums[0] and nums[middle] > target:
                    max_index = middle
                if nums[middle] > nums[0]:
                    min_index = middle


So = Solution()
print So.search([],5)
print So.search([1],0)
print So.search([5,1,3],5)
print So.search([4,5,6,7,0,1,2],5)
print So.search([4,5,6,7,0,1,2],0)
print So.search([4,5,6,7,0,1,2],2)
print So.search([4,5,6,7,0,1,2],6)
print So.search([216,221,222,225,228,231,234,244,245,246,249,251,259,262,264,265,268,271,276,277,278,281,282,286,289,294,295,296,298,299,0,4,9,10,13,18,23,25,26,33,34,38,39,42,43,45,48,49,51,52,53,55,58,60,61,62,63,65,66,70,72,74,78,79,82,85,89,90,91,95,104,109,112,113,117,118,120,122,123,126,127,128,133,134,138,140,142,144,147,148,149,152,156,164,165,168,169,174,177,185,191,192,193,194,195,197,204,211,215],0)















