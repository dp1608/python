# -*- coding: utf-8 -*-
# @StartTime : 2018/8/20 10:39
# @EndTime : 2018/8/20 10:39
# @Author  : Andy
# @Site    : 
# @File    : offer_slide_windows.py
# @Software: PyCharm

"""
求解滑动窗口最大值

"""

class Solution(object):
    def max_in_slide_window(self, arr, windows_len):
        """
        :param arr:
        :param windows_len:
        :return: a list res
        """
        res = []
        support_index = []
        for i in range(len(arr)):
            if support_index:
                if support_index[0] <= i - windows_len:
                    del support_index[0]
                while support_index and arr[i] > arr[support_index[-1]]:
                    support_index.pop()
            support_index.append(i)
            res.append(arr[support_index[0]])
        return res[windows_len - 1:]


arr = [4,2,3,4,2,6,2,5,1]
size = 3
a = Solution()
print(a.max_in_slide_window(arr, size))