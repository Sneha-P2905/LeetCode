# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        count=0
        curr=head
        while count<k and curr:
            curr=curr.next
            count+=1
        if count<k:
            return head
        prev=None
        curr=head
        for i in range(k):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        head.next=self.reverseKGroup(curr,k)
        return prev