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
        def check(num):
            num = str(num)
            num_size = len(str(num))
            summ = 0            
            for x in range(num_size):
                summ += int(num[x]) ** 2
            if str(summ) != '1':
                return check(summ)
            else:
                return True
        return check(n) 
