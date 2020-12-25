#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle. 
In Pascal's triangle, each number is the sum of the two numbers directly above it.

#Solution
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri=[]
        for x in range(numRows): 
            inner_tri=[]
            for y in range(x+1):  
                inner_tri.append(1)            
            for z in range(1, len(inner_tri)-1):
                inner_tri[z]=tri[-1][z-1]+tri[-1][z]
            tri.append(inner_tri)
        return tri      
