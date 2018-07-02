# -*- coding: utf-8 -*-
# @StartTime : 10/23/2017 15:12
# @EndTime   : 10/23/2017 15:50
# @Author    : Andy
# @Site      : 
# @File      : 171023can_place_flowers.py
# @Software  : PyCharm


"""
Suppose you have a long flowerbed in which some of the plots are planted and
some are not. However, flowers cannot be planted in adjacent plots - they would
compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means
empty and 1 means not empty), and a number n, return if n new flowers can be
planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        index = -1
        if len(flowerbed) <= 2:
            if sum(flowerbed) == 0 :
                count += 1
        while i < len(flowerbed) - 2 :
            if flowerbed[i] == 1:
                i += 1
                index = 1
                continue
            if i == 0 and  flowerbed[i] == 0 and flowerbed[1] == 0:
                count += 1
                i += 1
                index = 1
                continue

            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                count += 1
                i += 2
                continue
            i += 1
            index = 0
        if index == 1 and i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            count += 1
        if count >= n:
            return True
        else:
            return False

So = Solution()
print So.canPlaceFlowers([1,0,0,0,1], 1)
print So.canPlaceFlowers([1,0,0,0,0,0,1], 2)
print So.canPlaceFlowers([0], 1)
print So.canPlaceFlowers([0,0,1,0,1], 1)
print So.canPlaceFlowers([0,0,0], 2)
