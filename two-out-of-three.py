'''
P.S: Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays.
You may return the values in any order.
'''

#Solution:
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """    
        res=[]
        comb_list=nums1+nums2+nums3
        for x in list(comb_list):
            if (x in nums1 and x in nums2) or (x in nums2 and x in nums3) or (x in nums1 and x in nums3):
                res.append(x)
        return set(res)
