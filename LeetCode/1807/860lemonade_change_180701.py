# -*- coding: utf-8 -*-
# @StartTime : 2018/7/1 9:31
# @EndTime : 2018/7/1 9:31
# @Author  : Andy
# @Site    : 
# @File    : 860lemonade_change_180701.py
# @Software: PyCharm


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True

        def find_bills(res, n):
            if n == 5:
                return 4
            if n == 10:
                if 5 in res:
                    return 1
                else:
                    return 0
            if n == 20:
                if 10 in res and 5 in res:
                    return 2
                else:
                    mm = 0
                    for j in res:
                        if j == 5:
                            mm += 1
                    if mm >= 3:
                        return 3
                    return 0
        res = []
        count = 0
        for i in range(len(bills)):
            if count + 5 - bills[i] >= 0:
                m = find_bills(res, bills[i])
                count += 5
                if m == 0:
                    return False
                if m == 1:
                    j1 = res.index(5)
                    del res[j1]
                    res.append(bills[i])

                if m == 2:
                    j21 = res.index(5)
                    del res[j21]
                    j22 = res.index(10)
                    del res[j22]
                    res.append(bills[i])
                if m == 3:
                    j31 = res.index(5)
                    del res[j31]
                    j31 = res.index(5)
                    del res[j31]
                    j31 = res.index(5)
                    del res[j31]
                    res.append(bills[i])
                if m == 4:
                    res.append(bills[i])

            else:
                return False

        return True


# print(Solution().lemonadeChange([5,5,10, 10, 20]))
print(Solution().lemonadeChange([5,5,5,10,5,5,10,20,20,20]))