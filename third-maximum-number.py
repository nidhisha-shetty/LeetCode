'''
P.S: Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

#Solution: 
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_sort = sorted(set(nums))       
        if len(nums_sort)>3:
            return nums_sort[-3]
        elif len(nums_sort) == 3:
            return nums_sort[0]
        else:
            return max(nums_sort)
 
'''
Complexities:
Space complexity: O(n) #the size of array, nums_sort is dependent on size of nums, hence O(n)
'''
