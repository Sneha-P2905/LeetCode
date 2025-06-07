# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        temp1=head
        while temp1.next!=None:
            if temp1.next.next!=None:
                temp=temp.next
                temp1=temp1.next.next
            if temp1.next!=None and temp1.next.next==None:
                temp=temp.next
                temp1=temp1.next
        head=temp
        return head
        