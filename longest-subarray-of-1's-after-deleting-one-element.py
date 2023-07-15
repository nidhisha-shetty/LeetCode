class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
        ans = 0
        for x in nums:
            if x == 1:
                curr+=1
            else:
                ans=max(ans, prev+curr)
                prev=curr
                curr=0
        ans=max(ans, prev+curr)
        return ans-1 if ans==len(nums) else ans
