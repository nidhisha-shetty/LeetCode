'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

#Solution:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        di = collections.Counter(s)
        li = []
        for x in di:
            if di[x] == 1:
                li.append(x)
        if len(li) == 0:
            return -1
        else:
            for x in range(len(s)):
                if s[x] == li[0]:
                    return x
