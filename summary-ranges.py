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
        res=[]
        begin=0
        for x in range(len(nums)):
            if x+1>=len(nums) or nums[x+1]-nums[x]!=1:
                print(x+1)
                if nums[begin]!=nums[x]: 
                    res.append(str(nums[begin])+"->"+str(nums[x]))
                else:
                    res.append(str(nums[begin]))

                begin = x+1
        return res

