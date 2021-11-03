'''
P.S: Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

#Solution:
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        mismatch_indes=[]
        for x in range(len(s)):
            if s[x]!=goal[x]:
                mismatch_indes.append(x)
        if s!=goal:
            s[mismatch_indes[0]], s[mismatch_indes[1]]==s[mismatch_indes[1]], s[mismatch_indes[0]]     
