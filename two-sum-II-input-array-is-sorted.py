'''
P.S: Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
'''

#Solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in range(len(numbers)):
            for y in range(len(numbers)):
                if numbers[x]+numbers[y]==target:
                    return [x+1, y+1]

