'''
P.S: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

#Solution:
#using brute force attack algo
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]
