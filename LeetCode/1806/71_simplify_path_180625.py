# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/25 16:28
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 71_simplify_path_180625.py

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        def valid_string(s):
            for char in s:
                if ord(char) < ord('z') and ord(char) > ord('a') or ord(char) < ord('Z') and ord(char) > ord('A'):
                    continue
                # else:
                #     return False
            return True


        path_indicat = []
        path_index = 0
        path_list = path.strip().split('/')
        res = ["" for _ in range(len(path_list))]
        for i in range(len(path_list)):
            if not path_list[i]:
                continue
            if path_list[i] == '.':
                continue
            if path_list[i] == '..':
                if path_index > 0:
                    path_index -= 1
                    continue
                continue

            # if valid_string(path_list[i]):
            if 1:
                if len(res) > path_index:
                    res[path_index] = (path_list[i])
                else:
                    res.append(path_list[i])
                path_index += 1

        ress = res[0:path_index]
        return "/" + "/".join(ress)


print(Solution().simplifyPath("/home/////.."))
print(Solution().simplifyPath("/a/./b/../../c/"))
print(Solution().simplifyPath("/..."))


