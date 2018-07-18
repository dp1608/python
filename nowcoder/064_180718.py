# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/18 17:15
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 064_180718.py

"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
 {[2,3,4],2,6,2,5,1}，
  {2,[3,4,2],6,2,5,1}，
  {2,3,[4,2,6],2,5,1}，
  {2,3,4,[2,6,2],5,1}，
  {2,3,4,2,[6,2,5],1}，
  {2,3,4,2,6,[2,5,1]}。
"""

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return None
        if len(num) == size:
            return [max(num[:])]
        if len(num) < size:
            return []
        if not size:
            return []
        deque = []
        res = []
        for i in range(len(num)):
            if not deque:
                deque.append(i)
                res.append(num[i])
                continue
            if deque[0] < i - size + 1:
                del deque[0]
            while 1:
                if not deque:
                    deque.append(i)
                    res.append(num[deque[0]])
                    break
                if num[i] >= num[deque[-1]]:
                    deque.pop()
                    continue
                else:
                    deque.append(i)
                    res.append(num[deque[0]])
                    break
        return res[size - 1:]

a = [2, 3,4,2,6,2,5,1]
a = [10,14,12,11]
print(Solution().maxInWindows(a, 4))




