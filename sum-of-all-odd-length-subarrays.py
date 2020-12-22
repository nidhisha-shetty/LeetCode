#Given an array of positive integers 'arr', calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of 'arr'.

#Solution:
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total=0
        for x in range(len(arr)):
            for y in range(x+1,len(arr)+1):
                if len(arr[x:y])%2!=0:
                    total+=sum((arr[x:y]))
        return total
