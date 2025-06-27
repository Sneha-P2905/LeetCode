# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            queue=[root]
            arr=[]
            while queue:
                n=len(queue)
                arr1=[]
                for i in range(n):
                    curr=queue.pop(0)
                    arr1.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                arr.append(arr1)
            print(arr)
            result=[]
            for i in range(len(arr)):
                if i%2==0:
                    result.append(arr[i])
                else:
                    j=arr[i]
                    result.append(j[::-1])
            return result