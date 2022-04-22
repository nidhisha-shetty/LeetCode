'''
P.S: A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
'''

#Solution:
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        x=1
        li = []
        for char in arr:
            char = str(char)
            x+=1
            if char not in li:
                li.append(char)
            else:
                li.remove(char)
        if len(li) < k:
            return ''
        else:
            return li[k-1]

