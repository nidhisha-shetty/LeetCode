#Given an integer 'n' and an integer 'start'. 
Define an array 'nums' where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

#Solution
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=0
        arr=[]
        for x in range(n):
            arr.append(start+(2*x))
        for y in arr:
            res=res ^ y
        return res
