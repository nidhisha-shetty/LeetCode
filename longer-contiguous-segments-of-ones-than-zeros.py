'''
PS: Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s.
Return false otherwise.
'''

#Solution:
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        present_1=0
        previous_1=0
        present_0=0
        previous_0=0
        for char in s:
            if char=="1":
                present_0=0
                present_1+=1
                previous_1=max(previous_1, present_1)
            else:
                present_1=0
                present_0+=1
                previous_0=max(previous_0, present_0)
        return previous_1>previous_0    
      
      '''
      Complexities:
      Time complexity: O(n)
      Space complexity: O(n)
      '''
