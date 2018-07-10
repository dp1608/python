# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 10:02
# @End_time:  2018/7/10 10:13
# @Author  : Andy
# @Site    : 
# @File    : 021_is_pop_order_180710.py

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""




# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False
        temp = []

        while pushV:
            if not temp:
                temp.append(pushV[0])
                del pushV[0]
            while pushV and temp[-1] != popV[0]:
                temp.append(pushV[0])
                del pushV[0]
            if temp[-1] != popV[0]:
                return False
            while temp and temp[-1] == popV[0]:
                del popV[0]
                temp.pop()
        if temp:
            return False
        else:
            return True

pushV = [1,2,3,4,5]
# popV = [4,5,3,2,1]
popV = [4,3,5,1,2]
print(Solution().IsPopOrder(pushV,popV))