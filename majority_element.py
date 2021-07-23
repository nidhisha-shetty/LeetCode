'''
P.S: Given an array nums of size n, return the majority element.
'''

#Solution:
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        di={}
        for num in nums:
            if num in di:
                di[num]+=1
            else:
                di[num]=1
        print(di)
        ans=0
        for key in di:
            if di[key]>ans:
                ans=di[key]
                print(ans)
        final= [key for key,value in di.items() if value==ans]
        return int(final[0])

