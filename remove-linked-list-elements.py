'''
P.S: Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

#Solution:
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        temp=head
        while temp and temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
                
            else:
                temp=temp.next
        return head if head.val!=val else head.next     
