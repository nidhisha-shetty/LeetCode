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
        res=[]
        res.append(s[0])
        s=list(s)
        x=1
        while x<len(s):
            print(x)
            if s[x]==res[-1]:
                del(s[x])
                del(res[-1])                
            else:
                res.append(s[x])
                x+=1
        return res
