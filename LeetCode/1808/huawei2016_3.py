# -*- coding: utf-8 -*-
# @StartTime : 2018/8/12 16:49
# @EndTime : 2018/8/12 16:49
# @Author  : Andy
# @Site    : 
# @File    : huawei2016_3.py
# @Software: PyCharm

"""
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（
其中，小写joker表示小王，大写JOKER表示大王）:)
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如：4 4 4 4-joker JOKER
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR

基本规则：
（1）输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）
（3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。

答案提示：
（1）除了炸弹和对王之外，其他必须同类型比较。
（2）输入已经保证合法性，不用检查输入是否是合法的牌。
（3）输入的顺子已经经过从小到大排序，因此不用再排序了.

输入描述:
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“
-”两边没有空格，如4 4 4 4-joker JOKER。


输出描述:
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开
；如果不存在比较关系则输出ERROR。

输入例子1:
4 4 4 4-joker JOKER

输出例子1:
joker JOKER
"""

import sys

s = sys.stdin.readline().strip().split('-')
s1 = s[0].split()
s2 = s[1].split()


def compare(a,b):
    temp = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
    index1 = temp.index(a)
    index2 = temp.index(b)
    if index1 > index2:
        return 1
    else:
        return 2


if len(s1) == 2 and 'joker' in s1:
    print(s[0])
    sys.exit()
elif len(s2) == 2 and 'joker' in s2:
    print(s[1])
elif len(s1) == 4 and len(s2) == 4:
    res = compare(s1[0], s2[0])
    if res == 1:
        print(s[0])
    else:
        print(s[1])

elif len(s1) == 1 and len(s2) == 4:
    print(s[1])
elif len(s1) == 2 and len(s2) == 4:
    print(s[1])
elif len(s1) == 3 and len(s2) == 4:
    print(s[1])
elif len(s1) == 5 and len(s2) == 4:
    print(s[1])

elif len(s2) == 1 and len(s1) == 4:
    print(s[0])
elif len(s2) == 2 and len(s1) == 4:
    print(s[0])
elif len(s2) == 3 and len(s1) == 4:
    print(s[0])
elif len(s2) == 5 and len(s1) == 4:
    print(s[0])
else:
    if len(s1) != len(s2):
        print("ERROR")
    else:
        res = compare(s1[0], s2[0])
        if res == 1:
            print(s[0])
        else:
            print(s[1])

