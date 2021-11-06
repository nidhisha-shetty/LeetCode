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
        for x in range(len(nums)):
            for y in range(x,len(nums)):
                if abs(x-y)==k:
                    res+=1
        return res
