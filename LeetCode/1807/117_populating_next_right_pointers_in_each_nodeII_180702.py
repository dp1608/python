# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 16:00
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 117_populating_next_right_pointers_in_each_nodeII_180702.py

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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = None
        prev = None
        cur = root

        while cur:

            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next

            cur = head
            head = None
            prev = None

