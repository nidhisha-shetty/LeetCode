'''
P.S: Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
'''

#Solution:
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for x in range(1, n+1):
            print(x)
            if x%3==0 and x%5==0:
                res.append("FizzBuzz")
            elif x%3==0:
                res.append("Fizz")
            elif x%5==0:
                res.append("Buzz")
            else:
                res.append(str(x))
        return res
