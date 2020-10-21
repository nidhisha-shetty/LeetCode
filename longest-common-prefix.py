# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

#Solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        for x in range(len(strs[0])):
            temp=strs[0][x]
            for y in strs:
                if x>=len(y) or y[x] != temp:
                    return strs[0][:x]
        return strs[0]
