'''
P.S: You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
'''

#Solution:
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words:
            li=[]
            for char in word:
                if word.count(char) > chars.count(char):
                    li.append(char)
            if len(li)==0:
                res+=len(word)
        return res
