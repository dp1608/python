# -*- coding: utf-8 -*-
# @StartTime : 2018/7/22 9:59
# @EndTime : 2018/7/22 9:59
# @Author  : Andy
# @Site    : 
# @File    : 875_koko_eating_banans_180722.py
# @Software: PyCharm


"""
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas,
and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead,
and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.



Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23


Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
"""


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        if not piles:
            return 0

        def can_eat(piles, k, h):
            if k < 1:
                return False
            res = 0
            for num in piles:
                res += num // k + int(num % k > 0)
            if res <= h:
                return True
            else:
                return False

        sum_banana = sum(piles)
        left = sum_banana // H
        right = max(piles)

        while 1:
            index = (left + right) // 2
            temp = can_eat(piles, index, H)
            temp2 = can_eat(piles, index - 1, H)
            if temp and not temp2:
                return index
            if temp and temp2:
                right = index - 1
            if not temp and not temp2:
                left = index + 1


print(Solution().minEatingSpeed([3,6,7,11], 8))
print(Solution().minEatingSpeed([30,11,23,4,20], 5))
