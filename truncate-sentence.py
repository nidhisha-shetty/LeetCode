'''
P.s: You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words. Return s after truncating it.
'''

#Solution:
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.split(" ")
        return join(s[:k])
