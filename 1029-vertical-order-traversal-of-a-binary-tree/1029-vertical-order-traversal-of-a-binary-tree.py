# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_nodes=defaultdict(list)
        queue=deque([(root,0,0)])
        result=[]
        while queue:
            node,col,row=queue.popleft()
            col_nodes[col].append((row,node.val))
            if node.left:
                queue.append((node.left,col-1,row+1))
            if node.right:
                queue.append((node.right,col+1,row+1))
        for col in sorted(col_nodes):
            result.append([val for row,val in sorted(col_nodes[col])])
        return result