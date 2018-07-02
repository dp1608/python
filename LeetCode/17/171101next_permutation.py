# -*- coding: utf-8 -*-
# @StartTime : 11/1/2017 20:14
# @EndTime   : 11/1/2017 20:14
# @Author    : Andy
# @Site      : 
# @File      : 171101next_permutation.py
# @Software  : PyCharm


"""
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as
the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and
its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        col = len(nums)
        index_de = -1
        index_ws = col - 1
        for i in range(col - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index_de = i
                break
        for i in range(index_de + 1, col):
            if nums[i] <= nums[index_de]:
                index_ws = i - 1
                break
            # if nums[i] < nums[i + 1]:
            #     temp = nums[i]
            #     nums[i] = nums[i + 1]
            #     nums[i + 1] = temp
        temp = nums[index_de]
        nums[index_de] = nums[index_ws]
        nums[index_ws] = temp
        a = nums[index_de + 1 :]
        a.sort()
        for i in range(index_de + 1,col):
            nums[i] = a[i - index_de - 1]
        # nums[index_de:].sort()
            # if i < col - 2 and nums[i + 1] > nums[i + 2] :
            #     break
        print nums
So = Solution()
So.nextPermutation([1, 5, 1])
So.nextPermutation([1, 3, 2])
So.nextPermutation([1, 2, 3])
So.nextPermutation([3, 2, 1])
So.nextPermutation([1, 2])
So.nextPermutation([1])
So.nextPermutation([1, 2, 4, 6, 5, 3])

# 参考网址http://blog.csdn.net/qq575787460/article/details/41215475
# 最近刷leetcode的时候遇见next permutation这道题，感觉挺有意思的一个题目，递归的方法是较简单并且容易想到的，在网上搜了其余的解法，就是std::next_permutation非递归解法，但是让人不是很舒服的就是关于原理的部分，千篇一律的都是摘抄《STL源码剖析》，也就是这样的。
# 在当前序列中，从尾端往前寻找两个相邻元素，前一个记为*i，后一个记为*ii，并且满足*i < *ii。然后再从尾端寻找另一个元素*j，如果满足*i < *j，即将第i个元素与第j个元素对调，并将第ii个元素之后（包括ii）的所有元素颠倒排序，即求出下一个序列了。
# 想必有点C++功底的人都能看明白源码是这么个意思，但是这能算是原理么，这至多算是实现吧。相比之下老外就严谨多了，我找到了一篇文章，防止丢失，我保存在这里。http://blog.csdn.net/qq575787460/article/details/41206601，其中图片资源已经没了。看了这篇文章之后，我豁然开朗，在佩服老外严谨的态度之余，也把自己的理解纪律下来，希望能够帮助到一些人。
#
# 首先，关于什么是全排列不做解释。如果一个排列为A，下一个排列为A_NEXT，那么A_NEXT一定与A有尽可能长的公共前缀。
# 看具体例子，一个排列为124653，如何找到它的下一个排列，因为下一个排列一定与124653有尽可能长的前缀，所以，脑洞大开一下，从后面往前看这个序列，如果后面的若干个数字有下一个排列，问题就得到了解决。
# 第一步：找最后面1个数字的下一个全排列。
# 124653，显然最后1个数字3不具有下一个全排列。
# 第二步：找最后面2个数字的下一个全排列。
# 124653，显然最后2个数字53不具有下一个全排列。
# 第三步：找最后面3个数字的下一个全排列。
# 124653，显然最后3个数字653不具有下一个全排列。
#
# ------插曲：到这里相信大家已经看出来，如果一个序列是递减的，那么它不具有下一个排列。
#
# 第四步：找最后面4个数字的下一个全排列。
# 124653，我们发现显然最后4个数字4653具有下一个全排列。因为它不是递减的，例如6453，5643这些排列都在4653的后面。
#
# 我们总结上面的操作，并总结出重复上面操作的两种终止情况：
# 1：从后向前比较相邻的两个元素，直到前一个元素小于后一个元素，停止
# 2：如果已经没有了前一个元素，则说明这个排列是递减的，所以这个排列是没有下一个排列的。
#
# 124653这个排列终止情况是上面介绍的第一种，从后向前比较相邻的2个元素，遇到4<6的情况停止。
# 并且我们可以知道：
# 1：124653和它的下一个排列的公共前缀为12(因为4653存在下一个排列，所以前面的数字12保持不变)
# 2：4后面的元素是递减的(上面介绍的终止条件是前一个元素小于后一个元素，这里是4<6)
#
# 现在，我们开始考虑如何找到4653的下个排列，首先明确4后面的几个数字中至少有一个大于4.
# 4肯定要和653这3个数字中大于4的数字中(6，5)的某一个进行交换。这里就是4要和6，5中的某一个交换，很明显要和5交换，如果找到这样的元素呢，因为我们知道4后面的元素是递减的，所以在653中从后面往前查找，找到第一个大于4的数字，这就是需要和4进行交换的数字。这里我们找到了5，交换之后得到的临时序列为5643.，交换后得到的643也是一个递减序列。
#
# 所以得到的4653的下一个临时序列为5643，但是既然前面数字变大了(4653--->5643)，后面的自然要变为升序才行，变换5643得到5346.
# 所以124653的下一个序列为125346.
#
# ok，我的源码https://github.com/coderchen/leetcode/blob/master/Next%20Permutation.cpp



