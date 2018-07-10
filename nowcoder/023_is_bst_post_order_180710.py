# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 10:27
# @End_time:   2018/7/10 10:39
# @Author  : Andy
# @Site    : 
# @File    : 023_is_bst_post_order_180710.py

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
5、7、6、9、11、10、8

"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        def verify_core(array):
            if not array:
                return True
            root = array[-1]
            for i in range(-1, len(array) - 1):
                if array[i + 1] > root:
                    break
            if array[0: i + 1] and max(array[0:i + 1]) >= root or array[i + 1:-1]and  min(array[i + 1:-1]) <= root:
                return False
            return verify_core(array[0:i + 1]) and verify_core(array[i + 1: -1])

        if verify_core(array=sequence):
            return True
        else:
            return False


print(Solution().VerifySquenceOfBST([7,4,6,5]))
# print(Solution().VerifySquenceOfBST([5,7,6,9,11,10,8]))
# print(Solution().VerifySquenceOfBST([5,7,12,9,11,10,8]))
