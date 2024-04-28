'''
You are given two 0-indexed integer arrays nums1 and nums2 of even length n.
You must remove n / 2 elements from nums1 and n / 2 elements from nums2. 
After the removals, you insert the remaining elements of nums1 and nums2 into a set s.
Return the maximum possible size of the set s.
'''

#Solution:
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        N = len(nums1)//2
        set_of_list1 = set(nums1)
        set_of_list2 = set(nums2)
        unique_list1 = []
        unique_list2 = []
        if len(set_of_list1) <=N and len(set_of_list2)<=N:
            res = len(set_of_list1.union(set_of_list2))
            return res

        if len(set_of_list1)> N:
            for x in set_of_list1:
                if x not in set_of_list2:
                    unique_list1.append(x)
            while len(unique_list1)>N:
                unique_list1.pop()
            if len(unique_list1)<N:
                for x in set_of_list1:
                    if x not in unique_list1 and x not in unique_list2 and len(unique_list1)<N:
                        unique_list1.append(x)
        else:
            unique_list1 = list(set_of_list1)

        if len(set_of_list2)> N:
            for x in set_of_list2:
                if x not in set_of_list1:
                    unique_list2.append(x)
            while len(unique_list2)>N:
                unique_list2.pop()
            if len(unique_list2)<N:
                for x in set_of_list2:
                    if x not in unique_list2 and x not in unique_list1 and len(unique_list2)<N:
                        unique_list2.append(x)
        else:
            unique_list2 = list(set_of_list2)

        
        
        if len(unique_list1)!=0 and  len(unique_list2)!=0:
            res = unique_list1+unique_list2
        
        return(len(set(res)))
