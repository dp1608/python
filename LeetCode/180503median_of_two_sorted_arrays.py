# -*- coding: utf-8 -*-
# @StartTime : 2018/5/3 16:03
# @EndTime : 2018/5/3 20.45
# @Author  : Andy
# @Site    : 
# @File    : 180503median_of_two_sorted_arrays.py
# @Software: PyCharm

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 > len_nums2:
            return self.findMedianSortedArrays(nums2, nums1)
        len_sum = len_nums2 + len_nums1
        if len_nums1 < 1 and len_nums2 < 1:
            return ''
        if len_nums1 < 1:
            return (nums2[len_nums2 // 2] + nums2[(len_nums2 - 1) // 2]) / 2.0
        if len_nums2 < 1:
            return (nums1[len_nums1 // 2] + nums1[(len_nums1 - 1) // 2]) / 2.0

        cut_left = 0
        cut_right = len_nums1
        cut1 = int(len_nums1)
        cut2 = int(len_sum / 2 - cut1)

        while cut1 <= len_nums1:
            cut1 = (cut_left + cut_right) // 2
            cut2 = len_sum // 2 - cut1

            if cut1 <= 0:
                l1 = -999999999.0
            else:
                l1 = nums1[cut1 - 1]
            if cut1 >= len_nums1:
                r1 = 999999999
            else:
                r1 = nums1[cut1]

            if cut2 <= 0:
                l2 = -999999999.0
            else:
                l2 = nums2[cut2 - 1]
            if cut2 >= len_nums2:
                r2 = 999999999
            else:
                r2 = nums2[cut2]

            if l1 > r2:
                cut_right = cut1 - 1
            elif l2 > r1:
                cut_left = cut1 + 1
            else:
                if len_sum % 2 == 0:
                    l1 = max(l1, l2)
                    r1 = min(r1, r2)
                    return (l1 + r1) / 2.0
                else:
                    return min(r1, r2)


# nums1 = [1,2,3,5,6]
# nums2 = [4]
# nums1 = [1,2]
# nums2 = [3,4]
nums1 = [2,3,4,5]
nums2 = [1]
# print(0//2)
# print (nums2[1//2] + nums2[(1-1)//2]) / 2
So = Solution()
print(So.findMedianSortedArrays(nums1, nums2))





