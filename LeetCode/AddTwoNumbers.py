# -*- coding: utf-8 -*-
# @StartTime : 2017/4/6 22:53
# @EndTime  :2017/4/8 22:17
# @Author   : Andy
# @File     : AddTwoNumbers.py
# @Software : PyCharm

# You are given two non-empty linked lists representing two
#   non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
#   except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        adds=n=ListNode(0)
        count=0
        while l1 or l2 or count:
            v1=0
            v2=0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            val=(v1+v2+count)%10
            if __name__ == '__main__':
                count=(v1+v2+count)/10   #This code cannot switch position with the front.
                                            # Because it's dangerous
            n.next=ListNode(val)
            n=n.next
        return adds.next


l1= ListNode([2,4,3])
l2= ListNode([5,6,4])

SOLU=Solution()
idx = ListNode(3)
n = idx
n.next = ListNode(4)
n = n.next
n.next = ListNode(5)
n = n.next
print idx.val

nm=SOLU.addTwoNumbers(idx,idx)
print nm.val
print nm.next.val
print nm.next.next.val
print 91/10


