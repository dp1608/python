# -*- coding: utf-8 -*-
# @StartTime : 2018/7/12 21:48
# @EndTime : 2018/7/12 21:48
# @Author  : Andy
# @Site    : 
# @File    : 047_1+n_180712.py
# @Software: PyCharm

"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        temp = ans and self.Sum_Solution(n - 1)
        ans = ans + temp
        return ans

print(Solution().Sum_Solution(4))