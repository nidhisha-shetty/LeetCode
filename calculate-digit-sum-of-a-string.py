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
        while len(s) > k:
            rem  = len(s) % k
            div = s[:-rem]
            non_div = s[-rem:]
            div_sum=[]
            start = 0
            while start < len(div):
                num=0
                for elem in range(start, start+k):
                    num += int(div[elem])
                div_sum.append(num)
                start+=k

            print(div_sum)
            non_div_sum = 0
            for num in non_div:
                non_div_sum += int(num)
            div_sum.append(non_div_sum)
            s = div_sum
        return ''.join(str(x) for x in s) 
