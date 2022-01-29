'''
P.S Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
x mod y denotes the remainder when x is divided by y.
'''

#Solution:
class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for x in range(len(nums)):
            ans = x%10
            if ans == nums[x]:
                res.append(x)
        print(res)
        if len(res)>0:
            return min(res) 
        else:
            return -1
            
