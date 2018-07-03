# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 17:03
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 127_word_ladder_180702.py

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        def word_dist(word1, word2):
            return sum(word1[i] != word2[i] for i in range(len(word)))

        # def core(begin, end, word):
        from collections import deque, defaultdict
        queue = deque([beginWord, 1])
        visited = set([beginWord])
        neighbors = defaultdict(list)
        for word in wordList:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x + 1:]
                neighbors[token] .append(word)

        while queue:
            word = queue.popleft()
            length = queue.popleft()
            if word_dist(word, endWord) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x + 1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1]
        return 0

beginWord = "hit"
endWord = "hot"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
# from collections import deque, defaultdict
# queue = deque(([beginWord, 1]))
# a = queue.popleft()
# print(a)


