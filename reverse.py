#Given a 32-bit signed integer, reverse digits of an integer.

#Solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 2 ** 31
        maxLimit = r - 1
        minLimit = r * -1
        sign=-1 if x<0 else 1
        rev=0
        x=abs(x)
        while(x>0):
            rev=rev*10+(x%10)
            x=x//10  
        if rev < minLimit or rev > maxLimit:
            return 0 
        return rev*sign
