#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            temp=x
            rev=0
            while(temp>0):
                rev=rev*10+(temp%10)
                temp=temp//10
            return rev==x
