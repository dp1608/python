# -*- coding: utf-8 -*-
# @StartTime : 10/17/2017 12:52
# @EndTime   : 10/17/2017 13:52
# @Author    : Andy
# @Site      : 
# @File      : 171017merge_sorted_array.py
# @Software  : PyCharm

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal t
o m + n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
"""

class Solution(object):
     def merge(self, nums1, m, nums2, n):
         """
         :type nums1: List[int]
         :type m: int
         :type nums2: List[int]
         :type n: int
         :rtype: void Do not return anything, modify nums1 in-place instead.
         """
         while m > 0 and n > 0:
             if nums1[m - 1] >= nums2[n - 1]:
                 nums1[m + n - 1] = nums1[m - 1]
                 m -= 1
             else:
                 nums1[m + n - 1] = nums2[n - 1]
                 n -= 1
         if n > 0:
             nums1[:n] = nums2[:n]


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         # index of nums1 and nums 2
#         i = 0
#         j = 0
#         count = 0
#
#         if m == 0 :
#             for col in range(n):
#                 nums1.insert(col,nums2[col])
#             del nums1[n]
#
#             # print nums1
#             # return 0
#         while j < n and m != 0:
#             if count >= m:
#                 nums1.insert(i,nums2[j])
#                 i += 1
#                 j += 1
#                 continue
#             if nums2[j] <= nums1[i]:
#                 nums1.insert(i,nums2[j])
#                 j += 1
#                 i += 1
#                 continue
#             if nums2[j] > nums1[i] and count < m:
#                 i += 1
#                 count += 1
#         print nums1

So = Solution()
# So.merge([1,2,3,4,5],5,[0,2,4,6,8,10],6)
So.merge([1],1,[],0)
So.merge([0],0,[1],1)





