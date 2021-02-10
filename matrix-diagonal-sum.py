# Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


#Solution:
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        prim_diag=[]
        sec_diag=[]
        prim_elem=0
        sec_elem=0
        for x in range(len(mat)):
            prim_diag.append(mat[x][prim_elem])
            prim_elem+=1
        for y in range(len(mat)-1,-1,-1):            
            sec_diag.append(mat[sec_elem][y])
            sec_elem+=1
        res=sum(prim_diag)+sum(sec_diag)
        print(prim_diag)
        print(sec_diag)
        if len(mat)%2==0:
            return res
        else:
            return res-mat[(len(mat)//2)][len(mat[0])/2]
