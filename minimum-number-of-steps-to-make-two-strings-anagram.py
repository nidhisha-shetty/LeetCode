'''
P.S: You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s. 
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
'''

#Solution:
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        di_s = {}
        for char in s:
            if char in di_s:
                di_s[char] += 1
            else:
                di_s[char] = 1
        di_t = {}
        for char in t:
            if char in di_t:
                di_t[char] += 1
            else:
                di_t[char] = 1
        res = 0
        for char in set(s):
            if char in t:
                if di_s[char] > di_t[char]:
                    diff = di_s[char] - di_t[char]
                    res += diff
            else:
                res += di_s[char]
        return res
