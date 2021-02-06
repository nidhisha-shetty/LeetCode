#Given a positive integer num consisting only of digits 6 and 9. Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

#Solution:
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        new_num=[x for x in str(num)]
        for x in range(len(new_num)):
            if new_num[x]=='6':
                new_num[x]='9'
                return int(''.join([y for y in new_num]))
        
        return int(''.join([y for y in new_num]))
