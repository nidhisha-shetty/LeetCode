'''
P.S: You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''

#Solution:
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(nums)
        neg=[]
        pos=[]
        final=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        
        for x in range(len(pos)):
            final.append(pos[x])
            final.append(neg[x])
        return final
