# -*- coding: utf-8 -*-
# @StartTime : 2018/7/16 14:51
# @EndTime : 2018/7/16 14:51
# @Author  : Andy
# @Site    : 
# @File    : 041_180716.py
# @Software: PyCharm


"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        import math
        res = []
        index = int(math.sqrt(tsum * 2))
        for i in range(index, 1, -1):
            if i & 1 == 1 and tsum % i == 0:
                mid = tsum / i
                res.append([jj for jj in range(mid - i // 2, mid + i // 2 + 1)])
            if i & 1 == 0 and (tsum % i) * 2 == i:
                mid = tsum // i
                # mid2 = tsum // i + 1
                res.append([jj for jj in range(mid - i / 2 + 1, mid + i / 2 + 1)])
        return res


print(Solution().FindContinuousSequence(100))
