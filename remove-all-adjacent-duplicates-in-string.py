'''
P.S: You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
'''

#Solution:
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for x in s:
            if len(stack)==0:
                stack.append(x)
            elif stack[-1]!=x:
                stack.append(x)
            else:
                stack.pop()
        return ''.join(stack)
               
