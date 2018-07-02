# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 11:32
# @End_time:  2018/7/2 11:36
# @Author  : Andy
# @Site    : 
# @File    : 113_path_sumII_180702.py

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []
        res = []
        res_dict = {}

        def dfs(root, path):
            if not root.left and not root.right:
                path.append(root.val)
                temp_sum = sum(path)
                if temp_sum in res_dict.keys():
                    res_dict[temp_sum].append(path)
                else:
                    res_dict[temp_sum] = [path]
                res.append(temp_sum)
                return
            if root.left:
                dfs(root.left, path + [root.val])
            if root.right:
                dfs(root.right, path + [root.val])

        dfs(root, [])
        # print(res)
        if sum1 in res:
            return res_dict[sum1]
        else:
            return []