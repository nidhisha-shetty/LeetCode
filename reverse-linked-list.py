'''
P.S: Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Solution:
#using array
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr=[]
        while head!=None:
            
            arr.append(head.val)
            head=head.next
        arr=arr[::-1]
        curr = dummy = ListNode(0)
        
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        
        return dummy.next
      
#using linkedlist
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        cur=head
        while cur!=None:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        head=prev
        return head
