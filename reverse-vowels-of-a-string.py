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
        s=list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] not in vowels:
                i+=1
            elif s[j] not in vowels:
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return ''.join(s)
