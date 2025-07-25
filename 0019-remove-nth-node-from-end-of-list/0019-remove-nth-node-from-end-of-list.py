# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        if head.next==None:
            head=None
            return head
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        for i in range(n):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
