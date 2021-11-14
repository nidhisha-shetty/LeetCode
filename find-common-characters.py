'''
P.S: Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates).
You may return the answer in any order.
'''

#Solution
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        final=[]
        di={}
        combined_words=''
        for x in words:
            combined_words+=x
        for char in combined_words:
            res=0
            for word in words:
                if char in word:
                    res+=1   
            if res==3:
                final.append(char)
        return set(final)
