'''
P.S: Given a string s and a character c that occurs in s,
return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
'''

#Solution:

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions=[]
        for x in range(len(s)):
            if s[x]==c:
                positions.append(x)
        final=[]
        val=[]
        for x in range(len(s)):
            for y in range(len(positions)):
                diff=positions[y]-x
                if diff >0:
                    val.append(diff)
                
            final.append(min(val))   
            # print(final)
            # val.clear()
        return final
