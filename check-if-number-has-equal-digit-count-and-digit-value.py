'''
P.S: You are given a 0-indexed string num of length n consisting of digits.
Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

Example: 
Input: num = "1210"
Output: true
'''

#Solution:
class Solution:
    def digitCount(self, num: str) -> bool:
        res = ''
        for x in range(len(num)):
            if str(num.count(str(x))) == num[x]:
                res += str(num.count(str(x)))
        if res == num:
            return True
        else:
            return False
