'''
PS: Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

#Solution:
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_range=0
        ranges=0
        for num in nums:
            if num==1:
                ranges+=1
            else:
                max_range=max(ranges, max_range)
                ranges=0
        return max(ranges, max_range)
        
'''
Complexities:
Space complexity: n+2
Time complexity: O(n)
'''
