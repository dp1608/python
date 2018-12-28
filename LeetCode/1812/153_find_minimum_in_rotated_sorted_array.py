"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        mid = (l + r + 1) // 2

        while 1:
            if r - l <= 1:
                if nums[l] < nums[r]:
                    mid = l
                else:
                    mid = r
                break

            if nums[mid] < nums[r]:
                r = mid
                mid = (l + r + 1) // 2
            else:
                l = mid
                mid = (l + r + 1) // 2

        return nums[mid]