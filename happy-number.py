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
        str_num=str(n)
        if str_num > 9:
            len_size = len(str(str_num))
            num_sum=0
            for x in range(len_size):
                num=''
                
                sq_num = int(str_num[x]) ** 2
                num_sum+=sq_num
                
                print(num_sum)
                num=num_sum
                if num >9:
                    pass
