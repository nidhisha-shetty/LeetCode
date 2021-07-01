'''
P.S: Given the head of a singly linked list, return true if it is a palindrome.
'''

#Solution:
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr=[]
        while head!=None:
            
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]
