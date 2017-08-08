# -*- coding: utf-8 -*-
# @StartTime : 8/1/2017 22:17
# @EndTime   : 8/1/2017 22:17
# @Author    : Andy
# @Site      : 
# @File      : NumberComplement.py
# @Software  : PyCharm


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        思路：输入与其相同位数的最大数进行异或，例如，7和5异或
        """
        t=num
        n=1
        while num>0:
            n=n<<1
            num/=2
        return ((n-1)^t)

S=Solution()
ans=S.findComplement(5)
print ans

