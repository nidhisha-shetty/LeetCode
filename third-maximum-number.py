'''
P.S: Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

#Solution: 
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        for x in range(len(nums)):
            if nums[x] not in arr:
                arr.append(nums[x])
        if len(arr)>=3:
            for x in range(2):
                arr.remove(max(arr))
            return max(arr)
        else:
            return max(arr)
 
'''
Complexities:
Space complexity: O(n) #the size of array, arr is dependent on size of nums, hence O(n)
'''
