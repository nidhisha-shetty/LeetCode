'''
P.S: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''

#Solution:
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num=min(nums)
        max_num=max(nums)
        arr=[]
        for x in range(1, max_num+1):
            if max_num%x==0 and min_num%x==0:
                arr.append(x)
        if len(arr)==0:
            return 1
        else:
            return max(arr)
