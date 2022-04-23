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
        new_li = []
        li = []
        for char in arr:
            li.append(arr.count(char))
        for x in range(len(li)):
            if li[x] == 1:
                new_li.append(arr[x])
        print(new_li)
        if len(new_li) < k:
            return ''
        else:
            return new_li[k-1]
