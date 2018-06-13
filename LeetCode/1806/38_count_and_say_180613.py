# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/13 15:51
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 38_count_and_say_180613.py


"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        strr = "1"

        def count(string):
            size = len(string)
            res = []
            for i in range(len(string)):
                if i == 0:
                    res.append(1)
                    res.append(string[i])
                elif string[i] == string[i - 1]:
                    res[len(res) - 2] += 1
                else:
                    res.append(1)
                    res.append(string[i])
            res = map(str, res)
            return "".join(res)

        for i in range(2, n + 1):
            temp = strr
            strr = count(temp)
        return strr


# print(set("21"))
print(Solution().countAndSay(5))



