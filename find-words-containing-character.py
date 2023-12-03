'''
P.S: You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
'''

#Solution:
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        count = 0
        result = []
        for word in words:
            if x in word:
                result.append(count)
            count+=1
        return result
            
