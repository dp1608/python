# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:55
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 006_xuanzhuan_180703.py
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最
小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，
若数组大小为0，请返回0。
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        def shunxu(array):
            min_a = array[0]
            for i in range(len(array)):
                if array[i] < min_a:
                    min_a = array[i]
            return min_a

        size = len(rotateArray)
        left = 0
        right = size - 1
        mid = left
        while rotateArray[right] <= rotateArray[left]:
            if right - left == 1:
                mid = right
                break

            mid = (right + left) // 2

            if rotateArray[mid] == rotateArray[left] and rotateArray[left] == rotateArray[right]:
                return shunxu(rotateArray)

            if rotateArray[mid] >= rotateArray[left]:
                left = mid
                continue
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
                continue
        return rotateArray[mid]


