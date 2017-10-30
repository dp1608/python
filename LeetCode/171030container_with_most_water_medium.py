# -*- coding: utf-8 -*-
# @StartTime : 10/30/2017 14:01
# @EndTime   : 10/30/2017 14:38
# @Author    : Andy
# @Site      : 
# @File      : 171030container_with_most_water_medium.py
# @Software  : PyCharm

"""
Given n non-negative integers a1, a2, ..., an, where each
represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai)
 and (i, 0). Find two lines, which together with x-axis forms a
 container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

#思路： 首先判断，找到一个容器，放入可能的值。
# 从索引index零开始判断，最大的面积可能出现在最后一个索引上，如果最后一个索引小于height0，
# 则向前寻找，找到和其值一样大的索引位置，则最大面积一定在这个范围内，
# 如果index+1 小于 index的值，则不可能有更大的面积存在了。

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height2 = height[::-1]
        area_list = []
        col = len(height)
        i = 0
        # i = 0的时候，应该寻找此时的最大面积，并将其放进area_list
        j = 0
        area = (col - j - 1 - i) * min(height2[j], height[i])
        if height2[j] >= height[i]:
            area_list.append(area)
        else:
            while height2[j] < height[i] and i < col - j - 1:
                j += 1
                area = max((col - j - 1 - i) * min(height2[j], height[i]), area)
        area_list.append(area)
        i += 1

        while i < col:
            if height[i] < height[i - 1]:
                i += 1
                continue
            else:
                j = 0
                area = (col - j - 1 - i) * min(height2[j], height[i])
                if height2[j] >= height[i]:
                    area_list.append(area)
                else:
                    while height2[j] < height[i] and i < col - j - 1:
                        j += 1
                        area = max((col - j - 1 - i) * min(height2[j], height[i]), area)
                area_list.append(area)
                i += 1
        return max(area_list)

        # time execeeded
        # col = len(height)
        # area_list = []
        # area_max = 0
        # area = 0
        # for i in range(col - 1):
        #     for j in range(i + 1, col):
        #         area = (j - i) * min(height[i], height[j])
        #         area_max = max(area_max,area)
        #     area_list.append(area_max)
        # return max(area_list)

So = Solution()
# print So.maxArea([2,1,2,1,11,11])
# print So.maxArea([2,3,4,5,18,17,6])
print So.maxArea([10,9,8,7,6,5,4,3,2,1])

