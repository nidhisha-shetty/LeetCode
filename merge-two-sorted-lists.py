'''
P.S: Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
'''

#Solution:
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1=[]
        arr2=[]
        while l1:
            arr1.append(l1.val)
            l1=l1.next
        while l2:
            arr2.append(l2.val)
            l2=l2.next
        arr1.extend(arr2)
        arr1.sort()
        print(arr1)
        cur=dummy=ListNode(0)
        for node in arr1:
            cur.next=ListNode(node)
            cur=cur.next
        return dummy.next
