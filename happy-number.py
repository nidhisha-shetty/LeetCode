'''
P.S: Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
#Solution:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        num = str(n)
        num_size = len(str(num))
        sum = 0
        for x in range(num_size):
            sum += x ** 2
        if len(str(sum)) > 1:
            isHappy(sum)
        else:
            if sum != 1:
                return False
            else:
                return True  
