# -*- coding: utf-8 -*-
# @StartTime : 9/21/2017 22:14
# @EndTime   : 9/21/2017 22:14
# @Author    : Andy
# @Site      : 
# @File      : test_for_ideas.py
# @Software  : PyCharm

# temp='abcde'
# print temp[4]
# revers=''
# for j in range(len(temp) - 1, -1, -1):
#     revers = revers[:len(temp) - j - 1] + temp[j]
# # print revers
#
# temp2='What a pity it is!'
# print len(temp2)
#
# nums = [[1,2,3], [3,4]]
# print len(nums)
# print len(nums[0])
# reshape_nums=[[0 for col in range(10)] for row in range(15)]
# # reshape_nums[0][0]=1
# row = len(reshape_nums[0])
# print row
# print reshape_nums
# for i in range(1,0):
#     print i
i  = 1
nums = [1,5,6,2,3,4,5]
nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
print  nums
# print 2 in nums[2:]
# nums = [4,3,2,7,8,2,3,1]
# print nums[1] in nums[1:]
# for i in nums:
#     print i
# nums = nums[1:4]
# print nums[1:3]
