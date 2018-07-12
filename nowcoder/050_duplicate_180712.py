# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/12 14:58
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 050_duplicate_180712.py

"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数
字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
"""

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        n = len(numbers)
        for i in range(n):
            if numbers[i] >= 2 * n:
                numbers[numbers[i] % n] += n
            elif numbers[i] >= n:
                numbers[numbers[i] - n] += n
            else:
                numbers[numbers[i]] += n
        for i in range(n):
            if numbers[i] >= 2 * n:
                duplication[0] = i
                break
        # print(numbers)
        # print(duplication)
        if not duplication:
            return False
        else:
            return True

print(Solution().duplicate([2,1,3,0,4],[]))
# print(Solution().duplicate([1,5,5,5,5,2,3,1,4],[]))
