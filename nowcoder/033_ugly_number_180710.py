# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 11:39
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 033_ugly_number_180710.py

"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        res = [1]
        if index < 1:
            return 0
        if index == 1:
            return res[index - 1]

        temp1 = 0
        temp2 = 0
        temp3 = 0
        while len(res) != index:
            min_t = min(res[temp1] * 2, res[temp2] * 3, res[temp3] * 5)
            if res[temp1] * 2 == min_t:
                if min_t > res[-1]:
                    res.append(min_t)
                temp1 += 1
            elif res[temp2] * 3 == min_t:
                if min_t > res[-1]:
                    res.append(min_t)
                temp2 += 1
            else:
                if min_t > res[-1]:
                    res.append(min_t)
                temp3 += 1
        print(res)
        return res[-1]

print(Solution().GetUglyNumber_Solution(8))