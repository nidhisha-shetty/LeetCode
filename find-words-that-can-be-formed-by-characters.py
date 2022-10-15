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
            i = 0
            for char in word:
                if char in chars:
                    if len(word)-1 == i:
                        res+=len(word)
                    else:
                        i += 1
                else:
                    break
        return res
