'''
P.S: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

#Solution:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res = sorted(res)
        if len(res) % 2 == 0:
            div = len(res) // 2
            med = (res[div]+res[div-1])/2
        else:
            div = (len(res)-1) // 2
            med = res[div]
        return med
