'''
P.S: Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''

#Solution: (Using two pointers)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0
        j = 0
        while i < j:
            if s[i] not in vowels:
                i+=1
            elif s[j] not in vowels:
                j+=1
            else:
                s[i], s[j] = s[j], s[i]
        return s
