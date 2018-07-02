# -*- coding: utf-8 -*-
# @StartTime : 2018/5/15 21:05
# @EndTime : 2018/5/15 21:05
# @Author  : Andy
# @Site    : 
# @File    : 180515insert_interval.py
# @Software: PyCharm


"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        size = len(intervals)
        intervals.append(newInterval)
        i = 0
        while i < size:
            if newInterval.start < intervals[i].start:
                temp = intervals[i]
                intervals[i] = newInterval
                intervals[size] = temp
                break
            else:
                i = i + 1

        def merge(intervals):
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
            return intervals

        new_intervals = merge(intervals)
        return new_intervals


So = Solution()
a = Interval(1,3)
b = Interval(6,9)
A = [a,b]
c = Interval(2, 5)
B = So.insert(A, c)
print(B[0].start, B[0].end)
print(B[1].start, B[1].end)

