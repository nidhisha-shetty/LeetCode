'''
P.S: Write a function that reverses a string. The input string is given as an array of characters s.
'''

#Solution:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=-1
        for x in range(len(s)//2):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
