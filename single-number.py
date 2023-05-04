'''
P.S: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

#Solution:
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        di_nums = dict(Counter(nums))
        for x in di_nums:
            if di_nums[x] == 1:
                return x
