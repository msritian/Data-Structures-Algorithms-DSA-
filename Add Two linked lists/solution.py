# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None 
        l3=l3_final=ListNode(0)
        num1=num2=""
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        lis=str(int(num1[::-1])+int(num2[::-1]))[::-1]
        for i in lis:
            l3.next=ListNode(i)
            l3=l3.next
        return l3_final.next
