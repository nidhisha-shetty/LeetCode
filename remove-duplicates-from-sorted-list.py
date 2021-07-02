'''
P.S: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

#Solution:
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        while current!=None and current.next!=None:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
