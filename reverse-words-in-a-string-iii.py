'''
P.S: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

#Solution:
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_s=''
        res=[]
        s_array = s.split(' ')
        for word in s_array:
            res.append(word[::-1])
        for x in range(len(res)):
            if x+1 == len(res):
                final_s+=res[x]                
            else:
                final_s+=res[x]
                final_s+=' '
        return final_s
