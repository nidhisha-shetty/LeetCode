'''
PS: Given a non-empty, singly linked list with head node 'head', return a middle node of linked list.
If there are two middle nodes, return the second middle node.
'''

#Solution:
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
'''Complexities:
Time complexity: O(n)
Space complexity: O(1)
'''
