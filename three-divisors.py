'''
P.S: Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m.
'''

#Solution:
class Solution:
    def isThree(self, n: int) -> bool:
        sum=0
        for x in range(1,n+1):
            if n%x==0:
                sum+=1
        return sum==3
    
#Timecomplexity: O(n)
