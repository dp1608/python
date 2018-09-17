# -*- coding: utf-8 -*-
# @StartTime : 2018/9/16 10:27
# @EndTime : 2018/9/16 10:27
# @Author  : Andy
# @Site    : 
# @File    : 906_super_palindromes_180916.py
# @Software: PyCharm

"""
Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].



Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.


Note:

1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
"""

import math
class Solution(object):
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        left = int(math.floor(math.sqrt(L)))
        right = int(math.ceil(math.sqrt(R)))

        n1, n2 = len(str(left)), len(str(right))

        n1 = n1 // 2 if n1 % 2 == 0 else n1 // 2 + 1
        n2 = n2 // 2 if n2 % 2 == 0 else n2 // 2 + 1

        start = int('1' + '0' * (n1 - 1))
        end = int('9' * n2) + 1

        ans = 0
        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])
            num2 = int(x + x[:-1][::-1])
            for num in [num1, num2]:
                cand = num * num
                if cand >= L and cand <= R and str(cand) == str(cand)[::-1]:
                    ans += 1
        return ans

x = '12345'
print(x[:-1][::-1])