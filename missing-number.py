'''
P.S: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

#Solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        print(nums)
        min_num=min(nums)
        max_num=max(nums)
        for x in range(min_num, max_num):
            if x not in nums:
                return x
        else:
            if min_num==1:
                return 0
            return max_num+1
