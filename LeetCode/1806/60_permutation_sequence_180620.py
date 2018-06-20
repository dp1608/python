# -*- coding: utf-8 -*-
# @StartTime : 2018/6/20 20:58
# @EndTime : 2018/6/20 20:58
# @Author  : Andy
# @Site    : 
# @File    : 60_permutation_sequence_180620.py
# @Software: PyCharm

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_list = []
        for i in range(n):
            n_list.append(i + 1)
        if k == 1:
            return "".join(map(str, n_list))
        res = []
        n1 = 1
        for i in range(n):
            n1 *= i + 1
        if n1 < k:
            return ""

        def iter_n(res, arr, n, k):
            if k == 0:
                res = res[0:] + arr[0:]
                return res
            if k == 1:
                res = res[0:] + arr[0:]
                return res
                # for i in range(n):
                #     res.append(arr[i])
                # return
            n1 = 1
            for i in range(n):
                n1 *= i + 1
            n1 = n1 / n
            if (1.0 * k / n1 - int(k / n1)) > 0.00000001:
                index = int(k / n1) + 1
            else:
                index = k / n1
            res.append(arr[index - 1])
            # if k % n1 != 0:
            #     k %= n1
            k = k - n1 * (index -1)
            return iter_n(res, arr[0: index - 1] + arr[index:], n - 1, k)

        res = iter_n([], n_list, n, k)
        return "".join(map(str, res))

print(Solution().getPermutation(3, 2))
print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(3, 6))
print(Solution().getPermutation(4, 9))