class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        if len(word1) < len(word2):
            for x in range(len(word1)):
                res += word1[x]
                res += word2[x]
            res += word2[x+1:]
        elif len(word1) > len(word2):
            for x in range(len(word2)):
                res += word1[x]
                res += word2[x]
            res += word1[x+1:]
        else:
            for x in range(len(word1)):
                res += word1[x]
                res += word2[x]
        return res
