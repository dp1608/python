# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/28 17:14
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 101_symmetric_tree_180628.py


"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def pre_order(root, res):
            res.append(root.val)
            if root.left:
                pre_order(root.left, res)
            else:
                res.append('null')
            if root.right:
                pre_order(root.right, res)
            else:
                res.append('null')
            return res

        def re_pre_order(root, res):
            res.append(root.val)
            if root.right:
                re_pre_order(root.right, res)
            else:
                res.append('null')

            if root.left:
                re_pre_order(root.left, res)
            else:
                res.append('null')
            return res

        res1 = pre_order(root, [])
        res2 = re_pre_order(root, [])
        if res1 == res2:
            return True
        return False

