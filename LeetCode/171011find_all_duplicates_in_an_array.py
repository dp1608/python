# -*- coding: utf-8 -*-
# @StartTime : 10/11/2017 17:08
# @EndTime   : 10/11/2017 17:08
# @Author    : Andy
# @Site      : 
# @File      : 171011find_all_duplicates_in_an_array.py
# @Software  : PyCharm

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""

# 位置互换法，根据题目条件，可以知道，每个元素只出现一次或者两次，这个算法利用了
# 每个元素归位（x就放在第x位上），归位时相撞则append其到保存数组中。不撞则归位。
# 复杂度分析：
#   额外空间复杂度最坏情况分析：O（n/2），即所有元素都保存了一遍
#   时间复杂度分析：每个元素归位只进行了数据交换（n的整数倍），未归位元素取出来
#   保存，最多（n/2），实现了时间上的O（n）
#
#  参考网址：http://bookshadow.com/weblog/2016/10/25/
#           leetcode-find-all-duplicates-in-an-array/
# 对于网址中的另外一种做法正负号标记法中，仅仅有一遍遍历，更易理解。
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            while nums[i] and nums[i] != i + 1:
                n = nums[i]
                if nums[i] == nums[n - 1]:
                    ans.append(n)
                    nums[i] = 0
                else:
                    nums[i], nums[n - 1] = nums[n - 1], nums[i]
        return ans


# #  Time Limit Exceeded
# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         count = 0
#         # for i in range(len(nums)):
#         while(count+1 <= len(nums)):
#             if (count+1 < len(nums)) and (nums[count]) in nums[count+1:]:
#                 count += 1
#             else:
#                 # nums.remove(count)
#                 del nums[count]
#         return nums
#
So = Solution()
nums = [4,3,2,7,8,2,3,1]
print So.findDuplicates(nums)



# 正负号标记法
# 遍历nums，记当前数字为n（取绝对值），将数字n视为下标（因为a[i]∈[1, n]）
# 当n首次出现时，nums[n - 1]乘以-1。
# 当n再次出现时，则nums[n - 1]一定＜0，将n加入答案
# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         for n in nums:
#             if nums[abs(n) - 1] < 0:
#                 ans.append(abs(n))
#             else:
#                 nums[abs(n) - 1] *= -1
#         return ans




