'''
P.S: Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise.
If the array is already strictly increasing, return true. The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
'''

#Solution:
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        print(nums)
        for i in range(len(nums)) :
            if i+1<len(nums):
                if nums[i+1]<nums[i]:
                    count+=1
        print(nums)
        return count<=1
