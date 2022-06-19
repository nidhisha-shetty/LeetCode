'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

#Solution:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in range(len(s)):
            if s[x] in s[x+1:]:
                pass
            else:
                return x
        else:
            return -1
