'''
P.S: We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

'''

#Solution:
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        if word.isupper() or word.islower():
            return True
        else:
            for letter in word:
                if letter.isupper() and count != 0:
                    return False
                else:
                    count+=1
        return True
