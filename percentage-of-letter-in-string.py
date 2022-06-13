'''
P.S: Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
'''

#Solution:
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter = s.count(letter)
        string = len(s)
        percentage = (letter / string) * 100
        return floor(percentage)
