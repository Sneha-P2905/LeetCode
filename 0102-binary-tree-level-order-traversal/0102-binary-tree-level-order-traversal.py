# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        else:
            queue=[root]
            arr=[]
            while queue:
                size=len(queue)
                arr1=[]
                for i in range(size):
                    curr=queue.pop(0)
                    arr1.append(curr.val)
                    if curr.left!=None:
                        queue.append(curr.left)
                    if curr.right!=None:
                        queue.append(curr.right)
                arr.append(arr1)
            return arr