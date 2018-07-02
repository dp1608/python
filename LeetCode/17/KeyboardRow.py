# -*- coding: utf-8 -*-
# @StartTime : 8/8/2017 22:48
# @EndTime   : 8/8/2017 23:12
# @Author    : Andy
# @Site      : 
# @File      : KeyboardRow.py
# @Software  : PyCharm

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1=['q','w','e','r','t','y','u','i','o','p']
        row_2=['a','s','d','f','g','h','j','k','l']
        row_3=['z','x','c','v','b','n','m']
        true_words=[]
        for i in range(len(words)):
            temp=words[i].lower()
            if temp[0] in row_1: mark=1
            if temp[0] in row_2: mark=2
            if temp[0] in row_3: mark=3

            for j in range(1,len(temp)):
                if mark==1 :
                    if temp[j] not in row_1:
                        mark=0
                        break
                elif mark==2:
                    if temp[j] not in row_2:
                        mark = 0
                        break
                elif mark==3:
                    if temp[j] not in row_3:
                        mark = 0
                        break
            if mark!=0:
                true_words.append(words[i])
        return true_words



