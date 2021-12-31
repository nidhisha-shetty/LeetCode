'''
P.S: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        d[0] = 0
        d[1] = 1
        d[2] = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3,n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]
