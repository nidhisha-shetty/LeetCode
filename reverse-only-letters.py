'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''

#Solution:
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=str(s)
        new_s=''
        li = s.split('-')
        for x in li:
            new_s += x
        new_s = new_s[::-1]
        return new_s
      
