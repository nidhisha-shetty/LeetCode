def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    out = 0
    while x:
        out = out * 10 + x % 10
        x //= 10
    return out * sign
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 2 ** 31
        maxLimit = r - 1
        minLimit = r * -1
        if x<0:
            num=x*-1
        else:
            num=x
        rev=0
        while(num>0):
            q=num//10
            rem=num%10
            rev=(rev*10)+rem
            num=q
        if x<0:
            rev=rev * -1
        else:
            rev=rev
        if rev < minLimit or rev > maxLimit:
            return 0 #Return whatever you want. if overflows
        return rev
'''
