# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        count=1
        curr=head
        while curr.next:
            curr=curr.next
            count+=1
        curr.next=head
        n=count-k%count
        curr=head
        for i in range(n-1):
            curr=curr.next
        head=curr.next
        curr.next=None
        return head
        

        