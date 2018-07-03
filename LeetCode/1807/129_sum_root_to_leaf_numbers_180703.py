# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 11:33
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 129_sum_root_to_leaf_numbers_180703.py
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []

        def dfs(root, path):
            if not root.left and not root.right:
                path.append(root.val)
                res.append(path)
                path = []
                return
            if root.left:
                dfs(root.left, path + [root.val])
            if root.right:
                dfs(root.right, path + [root.val])

        dfs(root, [])
        # print(res)
        sum = 0
        for path in res:
            temp = int("".join(map(str, path)))
            sum += temp
        return sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print Solution().sumNumbers(root)