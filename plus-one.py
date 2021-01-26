# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

#Solution:
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        z=0
        arr=[]
        for elem in range(len(digits)):
            arr.append(0)
        arr[-1]=1
        new_arr=digits[:]
        for x in range(len(digits)-1,-1,-1):
           
            new_arr[x]=digits[x]+arr[x]+z
            if new_arr[x]>9:
                new_arr[x]=0
                z=1
            else:
                z=0
        if digits[0]==9 and z==1:
                
                new_arr.insert(0,1)
        return new_arr    
