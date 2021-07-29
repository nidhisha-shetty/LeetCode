'''
P.S: Count the number of prime numbers less than a non-negative number, n.
'''

#Solution:
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for num in range(2,n):
            for x in range(2,num):
                if num%x==0:                    
                    # print("not a prime")
                    break
            else:
                print(num)
                count+=1                   
        return count
