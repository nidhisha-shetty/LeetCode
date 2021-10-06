'''
P.S: You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

#Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_list_1=[]
        while l1:
            temp_list_1.append(l1.val)
            l1=l1.next
        temp_list_2=[]
        while l2:
            temp_list_2.append(l2.val)
            l2=l2.next
        temp_final=[]
        carry=0
        
        for x in range(len(temp_list_1)):
            res=temp_list_1[x]+temp_list_2[x]+int(carry)
            carry=0
            if res<9:
                temp_final.append(res)
            else:
                temp_final.append(int(str(res)[1]))
                carry=str(res)[0]
            
        print(temp_final)
