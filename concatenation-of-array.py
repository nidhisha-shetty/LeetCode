'''
P.S: Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''

#Solution 1:
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums*2
      
#Solution 2:
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        ans=[0 for x in range(2*len(nums))]
        for x in range(len(nums)):
            ans[x]=ans[x+len(nums)]=nums[x]
        return ans

#Solution 3
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        ans=[]
        for x in nums:
          ans.append(x)
        for x in nums:
          ans.append(x)
        return ans
