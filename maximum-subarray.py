'''
PS: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

#Solution:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums_check=-999999
        sum_nums=0
        for pos in range(len(nums)):
            sum_nums+=nums[pos]
            if sum_nums>sum_nums_check:
                sum_nums_check=sum_nums
            if sum_nums<0:
                sum_nums=0
        return sum_nums_check     
        
'''
Complexities:
Time Complexity: O(n)
Space complexity: O(1)
'''
