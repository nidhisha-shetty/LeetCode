'''
P.S: Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
- A letter 'a' appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
- s will contain at least one letter that appears twice.

For example: 
Input: s = "abccbaacz"
Output: "c"
'''

#Solution:
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for x in range(1, len(s)):
            if s[x] in s[:x]:
                return s[x]
