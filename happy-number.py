'''
Problem Statement: Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.
'''

#Solution:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        traversed = []
        def check_happy(num):
            num = str(num)
            num_size = len(str(num))
            new_num = 0
            for x in range(num_size):
                new_num += int(num[x]) ** 2
            if new_num != 1 and new_num not in traversed:
                traversed.append(new_num)
                return check_happy(new_num)
            elif new_num == 1 :
                return True
            else:
                return False
        return check_happy(n)
