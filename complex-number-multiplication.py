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
        num1_split = list(num1.split("+"))
        num2_split = list(num2.split("+"))

        a = int(num1_split[0])
        b = int(num1_split[1][0])
        x = int(num2_split[0])
        y = int(num2_split[1][0])

        res1 = (a*x)-(b*y)
        res2 = (a*y)+(b*x)
        res2 = "+"+str(res2)+"i"
       
        return str(res1)+str(res2)
