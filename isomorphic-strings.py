'''
P.S: Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

#Solution:
class Solution(object):
     def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        di={}
        if len(s)==len(t):
            for x in range(len(s)):
                if s[x] in di and di[s[x]]==t[x]:
                    pass
                elif s[x] in di and di[s[x]]!=t[x]:
                    return False
                else:   
                    di[s[x]]=t[x]
        return True
