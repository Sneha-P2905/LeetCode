# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width=0
        queue=deque([(root,0)])
        while queue:
            n=len(queue)
            first_node,first_index=queue[0]
            for i in range(n):
                curr_node,curr_index=queue.popleft()
                curr_index-=first_index
                if curr_node.left:
                    queue.append((curr_node.left,2*curr_index+1))
                if curr_node.right:
                    queue.append((curr_node.right,2*curr_index+2))
            width=curr_index+1
            max_width=max(max_width,width)
        return max_width