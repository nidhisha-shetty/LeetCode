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
        if len(nums)>0:
            start=0
            end=0
            ranges=[]
            for i in range(len(nums)-1):
                if nums[i+1]-nums[i]==1:
                    end+=1
                else:
                    if start==end:
                        ranges.append(str(nums[start]))
                    else:
                        ranges.append(str(nums[start])+"->"+str(nums[end]))
                    end+=1
                    start=end
            if start!=end:
                ranges.append(str(nums[start])+"->"+str(nums[end]))
            else:
                ranges.append(str(nums[start]))
            return ranges
        else:
            return nums

