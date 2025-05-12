from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq_updt = deque()
        dq.append(root)
        dq_updt.append(root)
        while True:
            for i in range(len(dq)):
                node =  dq.popleft()
                if node:
                    temp = None
                    if node.left:
                        temp = node.left
                        node.left = node.right
                        dq.append( node.left)
                    else:
                        temp = node.left
                        node.left = node.right
                        dq.append( node.left)
                    if node.right:
                        node.right = temp
                        dq.append(node.right)
                    else:
                        node.right = temp
                        dq.append(node.right)

            if not dq:
                return root
            
