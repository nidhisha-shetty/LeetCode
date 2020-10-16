#my original solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x==y:
                    continue
                if nums[x]+nums[y]==target:
                 return x, y

#submitted solution
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


