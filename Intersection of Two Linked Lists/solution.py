# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=headA
        l2=headB
        while l1 is not l2:
            l1=headB if l1 is None else l1.next
            l2=headA if l2 is None else l2.next
        return l1