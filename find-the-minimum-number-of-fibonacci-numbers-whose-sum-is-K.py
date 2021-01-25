#Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k.
The same Fibonacci number can be used multiple times.

Solution:
class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """ 
        a=0
        b=1
        arr=[0,1]
        for x in range(100):
            sum=a+b
            a=b
            b=sum
            arr.append(sum)       
        for y in range(len(arr)):
            if k==arr[y]:
                return 1
            elif arr[y] >=k:
                new_arr=arr[:y]
                sum=new_arr[-1]
                count=1
                for z in new_arr[::-1]:
                    if sum+z <= k:
                        sum+=z
                        count+=1
                    if sum==k:
                        return count
