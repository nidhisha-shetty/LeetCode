#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

#Solution
class Solution(object):
     def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        di={')':'(','}':'{',']':'['}
        stack=[]
        for x in range(len(s)):
            if s[x] == '{' or  s[x] == '[' or  s[x] == '(':
                stack.append(s[x])
            elif s[x] == '}' or  s[x] == ']' or  s[x] == ')':
                if len(stack)==0:
                    return False
                elif di[s[x]]==stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
