'''
P.S: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

#Solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        di = {}
        for x in range(len(t)):
            di[t[x]] = x
        res = []
        for x in s:
            if x in di:
                res.append(di[x])
        if res == sorted(res) and len(res) == len(s):
            return True
        else:
            return False
