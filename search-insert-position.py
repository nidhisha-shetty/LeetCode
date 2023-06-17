'''
P.S; Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

#solution:
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            pos = nums.index(target)
        elif target<nums[0]:
            pos = nums.index(nums[0])
        elif target>nums[-1]:
            pos = nums.index(nums[-1])+1
        else:
            if target-1 in nums:
                pos = nums.index(target-1)+1
            elif target+1 in nums:
                pos = nums.index(target+1)
        return pos

