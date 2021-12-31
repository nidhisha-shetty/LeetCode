'''
P.S: A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
'''

#Solution:
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result = 0
        for sentence in sentences:
            word_count = 0
            sentence = sentence.split(' ')
            for word in sentence:                
                word_count += 1
            if word_count > result:
                result = word_count
        return result

