# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root, float('-inf'), float('inf'))])
        
        #basic rule
        while q:
            node, low, high = q.popleft()

            # if this node ever violates its range, we can bail out
            if not (low < node.val < high):
                return False

            # left subtree must be in (low, node.val)
            if node.left:
                q.append((node.left, low, node.val))

            # right subtree must be in (node.val, high)
            if node.right:
                q.append((node.right, node.val, high))

        return True


        






