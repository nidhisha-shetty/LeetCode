'''
P.S: Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

#Solution:
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        max_digit = max(nums)
        for x in range(1, len(nums)+1):
            if x not in nums:
                res.append(x)
        return res
