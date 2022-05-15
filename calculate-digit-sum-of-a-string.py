'''
P.S: You are given a string s consisting of digits and an integer k.
A round can be completed if the length of s is greater than k. In one round, do the following:
1. Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
2. Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
3. Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.
Return s after all rounds have been completed.
'''

#Solution
class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rem = len(s) % 3 
        if rem != 0:
            div = s[:-rem]
            not_div = s[-rem:]
            x=0
            summ=0
            temp_sum = 0
            while x+3 <= len(div):
                add_three=x+3
                while x<add_three:
                    temp_sum += int(div[x])
                    x=x+1
                x=x+3
            for  num in range(len(not_div)):
                temp_sum += int(not_div[num])
            summ+=temp_sum
        return summ
