#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

#Solution:
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)    
        nums1.sort()
        if len(nums1)>m+n:
            res=len(nums1)-(m+n)
            for x in range(res):
                nums1.remove(0)
        return nums1
