'''
P.S: Given the head of a singly linked list, return true if it is a palindrome.
'''

#Solution:
#using array
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
    
#using linkedlist
class Solution(object):
    def isPalindrome(self, head):
        
        prev = ListNode(None,None)
        curr = head
        
        L = 0   # Get Length of Linked list
        while isinstance(head, ListNode):
            L+=1
            head = head.next
        
        for _ in range(L//2):
            nxt_node = curr.next    
            curr.next = prev    # Reversing first half linkedlist
            prev = curr     
            curr = nxt_node
        
        left = prev 
        right = curr if L%2==0 else curr.next
        while left and right:            
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True
