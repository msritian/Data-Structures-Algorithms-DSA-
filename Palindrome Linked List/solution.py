# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # print(head)
        # orig_head=head
        # prev=None
        # while orig_head:
        #     curr=orig_head
        #     orig_head=orig_head.next
        #     curr.next=prev
        #     prev=curr
        # head1=head
        # head2=prev
        # while head1 and head2:
        #     if head1.val==head2.val:
        #         head1=head1.next
        #         head2=head2.next
        # if head1==None and head2==None:
        #     return True
        # else:
        #     return False
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a == a[::-1]