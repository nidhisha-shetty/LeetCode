'''
P.S: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

#Solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)    
