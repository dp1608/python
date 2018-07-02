# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 14:36
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 114_flatten_binary_tree_to_linked_list_180702.py

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def flatten(self, root):
#         """
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#
#         head = root
#
#         def dfs(root):
#             if not root:
#                 return root
#             if root.left:
#                 temp = root.right
#                 root.right = root.left
#                 root.left = None
#                 tail = dfs(root.right)
#                 if tail:
#                     tail.right = temp
#                     return tail.right
#                 else:
#                     return tail
#             else:
#                 if root.right:
#                     root = root.right
#                     tail = dfs(root)
#                     return tail
#                 else:
#                     return root
#
#         dfs(head)
#         return root
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left.right = TreeNode(5)
# root.left.right = TreeNode(4)
# root.right = TreeNode(5)
# root.right.right = TreeNode(6)
a = Solution().flatten(root)
print(a.right.right.right.right.val)
