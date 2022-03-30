'''
P.S: Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
'''

#Solution:
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        di1 = {}
        di2 = {}
        for word in words1:
            if word in di1:
                di1[word] += 1
            else:
                di1[word] = 1
        for word in words2:
            if str(word) in di2:
                di2[word]+=1
            else:
                di2[word]=1
        for key, value in list(di1.items()):
            if (value != 1):
                del di1[key] 

        for key, value in list(di2.items()):
            if (value != 1):
                del di2[key]
                
        final_count = 0

        for key in di1:
            if key in di2:
                final_count+=1
        return final_count
