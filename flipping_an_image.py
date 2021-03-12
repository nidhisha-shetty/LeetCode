#Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image. 
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].

##Solution: 
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rev_list=[]
        for x in image[:]:
            rev_list.append(x[::-1])
        for sub_array in range(len(rev_list)):
            for elem in range(len(rev_list[0])):
                if rev_list[sub_array][elem]==0:
                    rev_list[sub_array][elem]=1
                else:
                    rev_list[sub_array][elem]=0
        return rev_list
