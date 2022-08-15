'''
P.S: Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.
'''

#Solution:
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return ''.join(sorted(set(s)))
