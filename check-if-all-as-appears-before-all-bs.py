'''
P.S: Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. 
Otherwise, return false.
'''  

#Solution:
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b_check=False
        for char in s:
            if char=='a' and b_check==True:
                return False
            elif char=='b':
                 b_check=True
            else:
                pass
        else:
            return True
