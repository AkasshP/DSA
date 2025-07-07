# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subtree(n,s):
            dn = deque([n])
            ds = deque([s])
            while dn:
                for i in range(len(dn)):
                    node1 = dn.popleft()
                    node2 = ds.popleft()
                    if node1.left and node2.left:
                        if node1.left.val != node2.left.val:
                            return False
                        dn.append(node1.left)
                        ds.append(node2.left)
                    elif node1.left or node2.left:
                        return False

                    if node1.right and node2.right:
                        if node1.right.val != node2.right.val:
                            return False
                        dn.append(node1.right)
                        ds.append(node2.right)

                    elif node1.right or node2.right:
                        return False

            return True
                    

                        
                    
        dq = deque()
        if root:
            dq.append(root)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.val == subRoot.val:
                    if subtree(node, subRoot):
                        return True
            
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return False
