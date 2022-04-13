'''
P.S: Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''

#Solution:
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        pos = []
        characters = [] 
        for x in range(len(s)):
            if s[x] in vowels:
                pos.append(x)
                characters.append(str(s[x]))
        characters.reverse()
        x=0
        for y in range(len(s)):
            if s[y] in vowels:
                s=s.replace(s[y], characters[x])
                x+=1
        return s
