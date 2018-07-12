# -*- coding: utf-8 -*-
# @StartTime : 2018/7/12 22:28
# @EndTime : 2018/7/12 22:28
# @Author  : Andy
# @Site    : 
# @File    : 031_count_1_in_n_180712.py
# @Software: PyCharm

"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13
因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        m = 1
        while m <= n:
            a = n / m
            b = n % m
            res += (a + 8) / 10 * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return res

print(Solution().NumberOf1Between1AndN_Solution(10))