'''
P.S: 
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs
(nums[w], nums[x]) and (nums[y], nums[z]) is maximized. Return the maximum such product difference.
'''

#Solution: 
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sort_nums=sorted(nums)
        max_prod_dif=(sort_nums[-1]*sort_nums[-2]-sort_nums[0]*sort_nums[1])
        return max_prod_dif
