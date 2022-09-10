'''
P.S: Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example: 
Input: arr = [10,2,5,3]
Output: true
'''

#Solution:
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2 * arr[j] or 2 * arr[i] == arr[j]:
                    return True
