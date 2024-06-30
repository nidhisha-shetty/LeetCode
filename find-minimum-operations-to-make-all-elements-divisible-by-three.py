"""
You are given an integer array "nums". In one operation, you can add or subtract 1 from any element of nums.
Return the minimum number of operations to make all elements of nums divisible by 3.
"""

#Solution:
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [1 for num in nums if num%3 == 0]
        return len(nums) - sum(res)
