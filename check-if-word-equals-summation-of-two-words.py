'''
P.S: The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.
'''

#Soltuion:
class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        summ=''
        for char in firstWord:
            summ+=str(ord(char) - ord('a'))
        
        sum1=''
        for char in secondWord:
            sum1+=str(ord(char)-ord('a'))
        sum2=''
        for char in targetWord:
            sum2+=str(ord(char)-ord('a'))
        if int(sum1)+int(summ) == int(sum2):
            return True
        return False
        
