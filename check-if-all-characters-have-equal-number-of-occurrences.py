'''
P.S: Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

#Solution: 
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        di={}
        for char in s:
            if char in di:
                di[char]+=1
            else:
                di[char]=1
        res=set(di.values())
        if len(res)==1:
            return True
        else:
            return False
