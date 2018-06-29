# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 16:16
# @EndTime : 2018/6/29 16:16
# @Author  : Andy
# @Site    : 
# @File    : 109_convert_sorted_list_to_binary_search_tree_180629.py
# @Software: PyCharm

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
 subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        list_node = []
        indicate = head
        while indicate:
            list_node.append(indicate.val)
            indicate = indicate.next

        def bst(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            root_num = (len(nums) - 1) //2
            root = TreeNode(nums[root_num])
            root.left = bst(nums[0:root_num])
            root.right = bst(nums[root_num + 1:])
            return root
        return bst(list_node)




    # def sortedListToBST(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: TreeNode
    #     """
    #     if not head:
    #         return None
    #     if not head.next:
    #         return TreeNode(head.val)
    #
    #     slow = head
    #     fast = head.next.next
    #
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     root = TreeNode(slow.next.val)
    #     root.right = self.sortedListToBST(slow.next.next)
    #     slow.next = None
    #     root.left = self.sortedListToBST(head)
    #     return root
