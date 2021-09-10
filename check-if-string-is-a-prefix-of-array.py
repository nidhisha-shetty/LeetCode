'''
P.S: Given a string s and an array of strings words, determine whether s is a prefix string of words.
A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise.
'''

#Solution:
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        str=''
        for x in words:
            str+=x
            if str==s:
                return True
        return False
