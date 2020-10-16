#Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'.

#Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp={}
        for x in range(len(nums)):
            if target-nums[x] in temp:
                return temp[target-nums[x]],x 
            else:
                temp[nums[x]]=x


