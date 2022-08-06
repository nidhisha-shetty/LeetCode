'''
P.S: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
'''


#Solution:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res = ''
        if goal[0] in s:
            pos = s.index(goal[0])
            res += s[pos:] + s[:pos]
            if res == goal:
                return True
            else:
                return False
