'''
P.S: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

#Solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums)==len(set(nums)) else True
