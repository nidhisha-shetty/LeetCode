
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for elem in range(len(nums)):
            if nums[elem]!=val:
                nums[index]=nums[elem]
                index+=1
        return index

        
