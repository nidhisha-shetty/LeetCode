'''
P.S: A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.
For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right 
(i.e., other than the last number, each number is strictly smaller than the number on its right in s).
Return true if so, or false otherwise.
'''

#Solution:
class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums = s.split(' ')
        num1 = []
        for token in nums:
            if token.isdigit():
                num1.append(int(token))
        backup_num1 = num1
        num1.sort()
        if backup_num1==num1:
            return True
        else:
            return False
        
