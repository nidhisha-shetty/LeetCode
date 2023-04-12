'''
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.
'''

#Solution:
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        init = num
        num = str(num)
        for x in num:
            if init%int(x) == 0:
                res+=1
        return res
