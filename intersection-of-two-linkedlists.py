'''
P.S: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
'''

#Solution:
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA=0
        countB=0
        
        temp_headA=headA
        temp_headB=headB
        
        while temp_headA:
            temp_headA=temp_headA.next
            countA+=1
        
        while temp_headB:
            temp_headB=temp_headB.next
            countB+=1
        
        if countA>countB:
            for _ in range(countA-countB):
                headA=headA.next
        if countB>countA:
            for _ in range(countB-countA):
                headB=headB.next
                
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None
            else:
                headA=headA.next
                headB=headB.next
        return None
