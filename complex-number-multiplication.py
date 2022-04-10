'''
P.S: A complex number can be represented as a string on the form "real+imaginaryi" where:

- real is the real part and is an integer in the range [-100, 100].
- imaginary is the imaginary part and is an integer in the range [-100, 100].
- i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.
'''

#Solution:
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        check_sign=0
        num1 = [int(x) for x in num1.replace('i','').split('+')]
        num2 = [int(x) for x in num2.replace('i','').split('+')]
        res = str(num1[0] * num2[0] -  num1[1] * num2[1]) + "+" + str(num1[0] * num2[1] +  num1[1] * num2[0])+"i"
        return res
