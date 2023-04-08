'''
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
'''

#Solution:
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=2
        while x < n*2:
            if x%2==0 and x%n==0:
                return x
            else:
                x+=2
        return x
