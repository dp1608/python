# -*- coding: utf-8 -*-
# @StartTime : 2018/8/22 12:55
# @EndTime : 2018/8/22 12:55
# @Author  : Andy
# @Site    : 
# @File    : 23_merge_k_sorter_listed_180822.py
# @Software: PyCharm


"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        i = 0
        while i < len(lists):
            if not lists[i]:
                del lists[i]
                continue
            i += 1
        k = len(lists)
        arr = lists[:]
        self.bulid_heap(arr, k)

        sentinel = ListNode(0)
        index = sentinel

        while len(arr) > 1:
            index.next = ListNode(arr[0].val)
            index = index.next
            arr[0] = arr[0].next
            if not arr[0]:
                self.swap(arr, 0, len(arr) - 1)
                del arr[-1]
            self.min_heap(arr, 0, len(arr))
        while arr and arr[0]:
            index.next = ListNode(arr[0].val)
            index = index.next
            arr[0] = arr[0].next
        return sentinel.next

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def min_heap(self, arr, i, arr_len):
        l = 2 * i
        r = 2 * i + 1
        if l < arr_len and arr[l].val < arr[i].val:
            minest = l
        else:
            minest = i
        if r < arr_len and arr[r].val < arr[minest].val:
            minest = r
        if minest != i:
            self.swap(arr, i, minest)
            self.min_heap(arr, minest, arr_len)

    def bulid_heap(self, arr, arr_len):
        for i in range(arr_len // 2, -1, -1):
            self.min_heap(arr, i, arr_len)


def creat_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    index = head
    for i in range(1, len(arr)):
        index.next = ListNode(arr[i])
        index = index.next
    return head

def print_list(arr):
    head = arr
    while head:
        print(head.val)
        head = head.next

arr = [[1,4,5], [1,3,4], []]
arr_list = []
for i in range(len(arr)):
    arr_list.append(creat_list(arr[i]))

a = Solution()
headd = a.mergeKLists(arr_list)

print_list(headd)







