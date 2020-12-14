#Given an integer number n, return the difference between the product of its digits and the sum of its digits. 

#Solution:
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        mul=1
        summ=0
        while n!=0:
            rem=n%10
            n=n//10
            mul=mul*rem
            summ=summ+rem
        return mul-summ
