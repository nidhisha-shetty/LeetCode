'''
P.S: You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
'''

#Solution:
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[str(nums[0])]
        for x in range(max(nums)+1):
            if x in nums:
                pass
            else:
                res.append("->"+str(x-1)+","+str(x+1))
        return res

