# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/26 16:24
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 89_gray_code_180626.py

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

input 3
output
000  0
001  1
011  3
010  2

110  6
111  7
101  5
100  4

"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n < 0:
            return

        res = [[0, 1]]

        def recurrence(k):
            this = pre = res[k - 2]
            # middle = len(pre) >> 1
            for i in range(len(pre) - 1, -1, -1):
                this.append(pre[i] + (1 << (k - 1)))
            res.append(this)

        for i in range(2, n + 1):
            recurrence(i)
        return res[n - 1]

print(Solution().grayCode(3))