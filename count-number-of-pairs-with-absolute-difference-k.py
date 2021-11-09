'''
P.S: Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
'''

#Solution:
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j])==k:
                    res+=1
        return res
