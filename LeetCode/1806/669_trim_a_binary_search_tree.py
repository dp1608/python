# -*- coding: utf-8 -*-
# @StartTime : 2018/6/30 9:33
# @EndTime : 2018/6/30 9:33
# @Author  : Andy
# @Site    : 
# @File    : 669_trim_a_binary_search_tree.py
# @Software: PyCharm

"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def trimBST(self, root, L, R):
#         """
#         :type root: TreeNode
#         :type L: int
#         :type R: int
#         :rtype: TreeNode
#         """
#         inorder_l = []
#
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             inorder_l.append(root.val)
#             inorder(root.right)
#             return
#
#         new_bst = []
#         inorder(root)
#         for i in range(len(inorder_l)):
#             if L <= inorder_l[i] <= R:
#                 new_bst.append(inorder_l[i])
#         # print(new_bst)
#
#         def construt_bst(new_bst):
#             if not new_bst:
#                 return None
#             if len(new_bst) == 1:
#                 root = TreeNode(new_bst[0])
#                 return root
#             mid = (len(new_bst) - 1) // 2
#             root = TreeNode(new_bst[mid])
#             root.left = construt_bst(new_bst[0:mid])
#             root.right = construt_bst(new_bst[mid + 1:])
#             return root
#
#         root = construt_bst(new_bst)
#         return root

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if not root:
            return root
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        elif root.val < L:
            root = self.trimBST(root.right, L, R)
        else:
            root = self.trimBST(root.left, L, R)
        return root




root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
L = 1
R = 2
res = Solution().trimBST(root, L, R)
print(res.val)
print(res.left)
print(res.right.val)

