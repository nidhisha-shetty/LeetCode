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
        if n<2:
            return 0
        else:
            li=[1]*n
            li[0]=li[1]=0
            for i in range(2, int(n**0.5)+1):
                if li[i]:
                    for j in range(i*i,n,i):
                        li[j]=0
            return sum(li)
