'''
P.S: You are given a 0-indexed integer array nums and a target element target. A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list.
The returned list must be sorted in increasing order.
'''

#Solution:
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        
        nums.sort()
        print(nums)
        for num in range(len(nums)):
            if nums[num] == target:
                res.append(num)
        return res

