# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next

        if head==None:
            return head
        tmp=head
        while tmp:
            if tmp.next and tmp.next.val==val:
                tmp.next=tmp.next.next
            else:
                tmp=tmp.next
        return head