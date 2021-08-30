'''
P.S: Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
'''

#Solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        di={}
        for x in range(0, len(numbers)):
            if target-numbers[x] in di:
                return di[target-numbers[x]], x+1
            else:
                di[numbers[x]]=x+1

