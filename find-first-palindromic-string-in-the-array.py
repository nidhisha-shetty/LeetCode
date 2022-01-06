'''
P.S: Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
'''

#Solution:
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for x in words:
            if x[::-1]==x:
                return x
        else: 
            return ""
