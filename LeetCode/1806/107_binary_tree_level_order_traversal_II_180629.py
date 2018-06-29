# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 15:02
# @EndTime : 2018/6/29 15:02
# @Author  : Andy
# @Site    : 
# @File    : 107_binary_tree_level_order_traversal_II_180629.py
# @Software: PyCharm

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        tree = []
        this = 1
        tree.append(root)
        while tree:
            next_num = 0
            temp = []
            while this:
                temp.append(tree[0].val)
                if tree[0].left:
                    next_num += 1
                    tree.append(tree[0].left)
                if tree[0].right:
                    next_num += 1
                    tree.append(tree[0].right)
                del tree[0]
                this -= 1
            this = next_num
            res.append(temp)
        return res[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right =TreeNode(7)

res = Solution().levelOrderBottom(root)
print(res)