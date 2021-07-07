'''
P.S: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Return the first unique elements.
'''

#Solution:
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(1,len(nums)):
            if nums[j]==nums[i]:
                pass
            else:
                i+=1
                nums[i]=nums[j]
               
        return i+1
      
'''
Complexities:
Space Complexity: O(1) #only one extra variable, 'i' is used, hence O(1)
'''
