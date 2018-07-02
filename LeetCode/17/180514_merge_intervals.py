# -*- coding: utf-8 -*-
# @StartTime : 2018/5/14 10:56
# @EndTime : 2018/5/14 10:56
# @Author  : Andy
# @Site    : 
# @File    : 180514_merge_intervals.py
# @Software: PyCharm
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


a = Interval(1,3)
b = Interval(2,6)
A = [a,b]

# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         # size = len(intervals)
#         i = 0
#         while i < len(intervals) - 1:
#             if intervals[i].end >= intervals[i + 1].start and intervals[i].start > intervals[i + 1].start:
#                 i = i + 1
#             elif
#                 intervals[i].end = intervals[i + 1].end
#                 intervals[i].start = min(intervals[i].start, intervals[i + 1].start)
#                 del intervals[i + 1]
#             else:
#                 i = i + 1
#         return intervals


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # size = len(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].start == intervals[i + 1].start:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                del intervals[i + 1]
                continue

            if intervals[i].start < intervals[i + 1].start:
                if intervals[i].end >= intervals[i + 1].start:
                    intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                    del intervals[i + 1]
                    continue
                else:
                    i = i + 1
                    continue

            # if intervals[i].start > intervals[i + 1].start:
            #     if intervals[i].start <= intervals[i + 1].end:
            #         intervals[i].start = intervals[i + 1].start
            #         intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
            #     else:
            #         i = i + 1
            #         continue

        return intervals
So = Solution()
B = So.merge(A)
print(len(B))
print(B[0].start, B[0].end)


