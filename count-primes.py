'''
P.S: Count the number of prime numbers less than a non-negative number, n.
'''

#Solution:
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        prime = [1]*n #creating a list of n length with 1 as elements in the list
        for x in range(2,n): 
            if prime[x] == 1:
                res += 1
                for x in range(x*x, n, x): #converting all multiples of x to 0
                    prime[x] = 0
        return res
