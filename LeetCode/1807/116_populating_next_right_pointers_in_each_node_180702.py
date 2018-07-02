# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 15:30
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 116_populating_next_right_pointers_in_each_node_180702.py
"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# 不是常数空间，很尴尬，审题
# class Solution(object):
#     # @param root, a tree link node
#     # @return nothing
#     def connect(self, root):
#         if not root:
#             return
#         # tree = [[root]]
#         # tree.append(root)
#
#         if not root:
#             return []
#
#         to_print = 1
#         res = []
#         trees = []
#         trees.append(root)
#         while trees:
#             temp = []
#             next_nums = 0
#             while to_print:
#                 temp.append(trees[0])
#                 if trees[0].left:
#                     trees.append(trees[0].left)
#                     next_nums += 1
#                 if trees[0].right:
#                     trees.append(trees[0].right)
#                     next_nums += 1
#                 del[trees[0]]
#                 to_print -= 1
#             res.append(temp)
#             to_print = next_nums
#
#         size = len(res)
#         for i in range(size):
#             for j in range(0, len(res[i]) - 1):
#                 res[i][j].next = res[i][j + 1]

class Solution(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        else:
            return
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)




