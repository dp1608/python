# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/13 17:23
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 40_find_number_2_180713.py

"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []

        res_xor = array[0]
        for i in range(1, len(array)):
            res_xor ^= array[i]
        xor = 1
        while res_xor:
            res_xor = res_xor >> 1
            xor = xor << 1
        xor = xor >> 1

        print(xor)

        l1 = []
        l2 = []
        for i in range(len(array)):
            if xor & array[i]:
                l1.append(array[i])
            else:
                l2.append(array[i])

        print(l1)
        print(l2)
        if not l1 or not l2:
            return []
        a1 = l1[0]
        a2 = l2[0]
        for j in range(1, len(l1)):
            a1 ^= l1[j]
        for j in range(1, len(l2)):
            a2 ^= l2[j]
        return [a1, a2]



print(Solution().FindNumsAppearOnce([2,4,3,6,3,2,5,5]))



# print(7 ^ 8 ^ 8 ^ 3)
# print(7 ^ 4)
# print(3 ^ 4)


