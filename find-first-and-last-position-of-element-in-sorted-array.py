'''
P.S: Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
'''
#Solution:
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li_values=[]
        li = [-1, -1]
 
        if target in nums:
            for x in range(len(nums)):
                if nums[x] == target:
                    li_values.append(x)
            if len(li_values)<2:
                li_values.append(li_values[0])
                return li_values
            elif len(li_values)>2:
                res = []
                res.append(li_values[0])
                res.append(li_values[-1])
                return res
            else:
                return li_values
        else:
            return li
