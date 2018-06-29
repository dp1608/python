# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 9:34
# @EndTime :2018/6/29 9:50
# @Author  : Andy
# @Site    : 
# @File    : 102_binary_tree_level_order_traversal_180629.py
# @Software: PyCharm

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        to_print = 1
        res = []
        trees = []
        trees.append(root)
        while trees:
            temp = []
            next_nums = 0
            while to_print:
                temp.append(trees[0].val)
                if trees[0].left:
                    trees.append(trees[0].left)
                    next_nums += 1
                if trees[0].right:
                    trees.append(trees[0].right)
                    next_nums += 1
                del[trees[0]]
                to_print -= 1
            res.append(temp)
            to_print = next_nums
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right =TreeNode(7)

res = Solution().levelOrder(root)
print(res)



















