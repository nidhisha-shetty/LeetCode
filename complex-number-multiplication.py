class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_split = list(num1.split("+"))
        res = (int(str(num1_split[0])) ** 2 ) + (2 * (int(str(num1_split[0]))))
        print(res)
