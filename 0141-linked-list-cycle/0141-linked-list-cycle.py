# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        temp1=head
        while temp1!=None and temp1.next!=None:
            temp=temp.next
            temp1=temp1.next.next
            if temp==temp1:
                return temp==temp1