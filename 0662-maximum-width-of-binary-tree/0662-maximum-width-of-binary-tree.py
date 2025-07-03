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

        max_width = 0
        # Queue holds pairs of (node, index)
        queue = deque([(root, 1)])

        while queue:
            level_length = len(queue)
            first_node, first_index = queue[0]  # First node's index at this level

            for i in range(level_length):
                current_node, current_index = queue.popleft()
                # Normalize the index to prevent overflow
                current_index -= first_index

                if current_node.left:
                    queue.append((current_node.left, 2 * current_index + 1))
                if current_node.right:
                    queue.append((current_node.right, 2 * current_index + 2))

            # Width is the difference between last and first index + 1
            last_index = current_index  # current_index will be the last one after the loop
            width = last_index + 1
            max_width = max(max_width, width)

        return max_width

        