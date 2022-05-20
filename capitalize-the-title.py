'''
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.
'''

#Solution:
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        res_li = []
        li_title = title.split(' ')
        for word in li_title:
            if len(word)<3:
                word = word.lower()
            else:
                word = word.capitalize()
            res_li.append(word)
        return ' '.join(res_li)
