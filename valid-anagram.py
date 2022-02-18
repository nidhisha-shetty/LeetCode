'''
P.S: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

#Solution:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        di1={}
        di2={}
        for letter in s:
            if letter in di1:
                di1[letter]+=1
            else:
                di1[letter]=1
        for letter in t:
            if letter in di2:
                di2[letter]+=1
            else:
                di2[letter]=1        
        print(di1)
        print(di2)
        if di1 == di2:
            return True
        else:
            return False
