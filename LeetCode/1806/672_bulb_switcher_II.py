# -*- coding: utf-8 -*-
# @StartTime : 2018/6/30 10:12
# @EndTime : 2018/6/30 10:12
# @Author  : Andy
# @Site    : 
# @File    : 672_bulb_switcher_II.py
# @Software: PyCharm

"""
There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
Example 1:
Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
Example 2:
Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]
Example 3:
Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
Note: n and m both fit in range [0, 1000].
"""


class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if not m:
            return 1
        if not n:
            return 0

        bulb = [0 for _ in range(n)]
        res = []

        def switcher_I(bulb):
            bulb1 = bulb[:]
            for i in range(len(bulb)):
                bulb1[i] = 1 - bulb1[i]
            return bulb1

        def switcher_II(bulb):
            bulb1 = bulb[:]
            for i in range(len(bulb)):
                if i & 0x1 == 0:
                    bulb1[i] = 1 - bulb1[i]
            # if bulb not in res:
                # res.append(bulb)
            return bulb1

        def switcher_III(bulb):
            bulb1 = bulb[:]
            for i in range(len(bulb)):
                if i & 0x1 == 1:
                    bulb1[i] = 1 - bulb1[i]
            return bulb1

        def switcher_IV(bulb):
            bulb1 = bulb[:]
            for i in range(0, len(bulb), 3):
                bulb1[i] = 1 - bulb1[i]
            return bulb1

        if m == 1:
            b1 = switcher_I(bulb)
            if b1 not in res:
                res.append(b1)
            b2 = switcher_II(bulb)
            if b2 not in res:
                res.append(b2)
            b3 = switcher_III(bulb)
            if b3 not in res:
                res.append(b3)
            b4 = switcher_IV(bulb)
            if b4 not in res:
                res.append(b4)
        elif m == 2:
            res.append(bulb)
            b1 = switcher_I(bulb)
            if b1 not in res:
                res.append(b1)
            b2 = switcher_II(bulb)
            if b2 not in res:
                res.append(b2)
            b3 = switcher_III(bulb)
            if b3 not in res:
                res.append(b3)
            b14 = switcher_IV(b1)
            b24 = switcher_IV(b2)
            b34 = switcher_IV(b3)
            if b14 not in res:
                res.append(b14)
            if b24 not in res:
                res.append(b24)
            if b34 not in res:
                res.append(b34)
        else:
            res.append(bulb)
            b1 = switcher_I(bulb)
            if b1 not in res:
                res.append(b1)
            b2 = switcher_II(bulb)
            if b2 not in res:
                res.append(b2)
            b3 = switcher_III(bulb)
            if b3 not in res:
                res.append(b3)
            b4 = switcher_IV(bulb)
            if b4 not in res:
                res.append(b4)
            b14 = switcher_IV(b1)
            b24 = switcher_IV(b2)
            b34 = switcher_IV(b3)
            if b14 not in res:
                res.append(b14)
            if b24 not in res:
                res.append(b24)
            if b34 not in res:
                res.append(b34)
        return len(res)


print(Solution().flipLights(3, 5))

