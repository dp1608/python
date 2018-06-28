# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/28 11:47
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 96_unique_binary_search_trees.py

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

input 1
output 1

input 2
output 2

input 3
output f(2) + int(insert 3 in bst's child trees)
       = [root = 2] + [root = 1] + [root = 2]
       = f(2) + f(3 - 1) + f(3 - 2)
       = 5
intput 4
output f(3) + int(insert 4 in bst's child trees)
       = f(root = 4)+ f(root = 1) + f(root = 2) + f(root = 3)
       = f(3) + f(root = 1) + f(root = 2) + f(root = 3)
       = f(3) + f(0) * f(4 - 1) + f(1) * f(4 - 2)  + f(2) * f(4 - 3)
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1
        res = []
        res.append(1)
        res.append(1)

        def dynamic_programming(n):
            temp = 0
            for i in range(n):
                temp += res[i] * res[n - i - 1]
            res.append(temp)

        for j in range(2, n + 1):
            dynamic_programming(j)

        return res[n]


print(Solution().numTrees(3))
print(Solution().numTrees(4))



