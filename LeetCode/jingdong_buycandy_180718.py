# -*- coding: utf-8 -*-
# @StartTime : 2018/7/18 21:00
# @EndTime :
# @Author  : Andy
# @Site    : 
# @File    : jingdong_buycandy_180718.py
# @Software: PyCharm


"""

某糖果公司专门生产儿童糖果，它最受儿童欢迎的糖果有A1、A2两个序列，均采用盒式包装。包装好的A1类糖果体积为一个存储单位，
而包装好的A2类糖果体积正好是A1类的两倍。



这两类糖果之所以广受儿童欢迎，是因为糖果中含有公司独家研发的魔幻因子。A1或A2序列中的糖果，看起来包装可能是一样的，
但因为其中的魔幻因子含量不同被细分为不同的产品。



临近传统节日，公司的糖果供不应求。作为一个精明的糖果分销商，小东希望能够借此大赚一笔，于是带着现金开着货车来公司提货。
货车的容量是确定的，小东希望采购的糖果能够尽可能装满货车，且糖果的魔幻因子总含量最高。只要不超出货车容量，糖果总可以装入货车中。



小东希望你能帮她解决这一问题。





输入
输入中有多组测试数据。每组测试数据的第一行有两个整数n和v，1<=n<=10^5, 1<=v<=10^9，n为可供选购糖果数量，v为货车的容量。
随后n行为糖果的具体信息，第一行编号为1，第二行编号为2，以此类推，最后一行编号为n。
每行包含两个整数ti和pi，1<=ti<=2, 1<=pi<=10^4，ti为糖果所属的序列，1为A1、2为A2，pi则是其中的魔幻因子含量。

样例输入
3 2

1 2

2 7

1 3



输出
对每组测试数据，先在单独的一行中输出能采购的糖果中的魔幻因子最高含量，
之后在单独的行中按编号从小到大的顺序输出以空格分隔的糖果编号，若有多组糖果组合均能满足要求，
输出编号最小的组。若没有糖果能够满足要求，则在第一行中输出0，第二行输出“No”。

样例输出
7

2



时间限制
C/C++语言：1000MS其它语言：3000MS
内存限制
C/C++语言：65536KB其它语言：589824KB
"""
while 1:
    s = raw_input()
    if not s:
        break
    [n, v] = map(int, s.split())
    greatest = []
    greatest_index = []
    t = []
    p = []

    def insert(greatest_index, greatest, num, index):
        size = len(greatest_index)
        if not size:
            greatest.insert(0, num)
            greatest_index.insert(0, index)
            return
        for i in range(size):
            if greatest[i] < num:
                greatest.insert(i, num)
                greatest_index.insert(i, index)
                return
        greatest.append(num)
        greatest_index.append(index)

    for _ in range(n):
        s = raw_input()
        ti, pi = map(int, s.split())
        danjia = pi * 1.0 / (ti * 1.0)
        t.append(ti)
        p.append(pi)
        insert(greatest_index, greatest, danjia, _)

        # print(greatest)
        # print(greatest_index)

    volume = v
    res = []
    count = 0
    while volume > 1:
        if not greatest_index:
            break
        this_t = t[greatest_index[0]]
        count += p[greatest_index[0]]
        res.append(greatest_index[0] + 1)
        volume -= this_t
        del greatest_index[0]
        del greatest[0]

    if volume == 1:
        for i in range(len(greatest_index)):
            if t[greatest_index[i]] == 1:
                count += p[greatest_index[0]]
                res.append(greatest_index[0] + 1)

    if not res:
        print(0)
        print("No")
    else:
        res.sort()
        print(count)
        print(" ".join(map(str, res)))

"""
3 2
1 2
2 7
1 3

5 3
1 9
2 9
1 9
2 10
1 6


10 10
1 14 
2 15 
2 11 
2 12 
2 9
1 14 
2 15
1 9
2 11
2 6

20 19
2 47
1 37
1 48
2 42
2 48
1 38
2 47
1 48
2 47
1 41
2 46
1 28
1 49
1 45
2 34
1 43
2 29
1 46
2 45
2 18

50 27
2 93
1 98
2 62
1 56
1 86
1 42
2 67
2 97
2 59
1 73
1 83
2 96
1 20
1 66
1 84
1 83
1 91
2 97
1 81
2 88
2 63
1 99
2 57
1 39
1 74
2 88
1 30
2 68
1 100
2 57
1 87
1 93
1 83
1 100
1 91
1 14
1 38
2 98
2 85
2 61
1 44
2 93
2 66
2 55
2 74
1 67
2 67
1 85
2 59
1 83
84 71
1 93
2 61
2 64
1 56
1 76
2 84
1 64
1 59
1 67
2 48
1 97
2 54
2 98
2 58
2 33
2 98
1 96
2 89
1 73
1 60
2 71
2 43
1 55
2 72
1 76
2 92
2 80
1 85
1 90
1 46
1 43
2 60
2 68
1 82
2 64
1 21
1 94
1 49
2 20
2 41
1 92
1 59
2 49
2 60
1 24
1 48
2 17
2 87
2 93
1 79
2 65
2 71
1 95
1 100
2 86
1 65
1 93
2 69
2 87
1 84
1 89
2 67
2 84
2 52
2 87
1 44
2 80
2 82
1 89
2 68
1 64
2 97
2 98
1 21
2 51
1 54
1 88
2 86
2 93
2 39
2 90
2 88
1 66
1 91
"""



