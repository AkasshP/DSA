from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        lvl = {}
        result = []
        if root:
            dq.append(root)
            lvl[0] = [root.val]
            result.append(lvl[0])
        j = 1
        while dq:
            lvl[j] = []
            for i in range(len(dq)):
                current_root = dq.popleft()
                if current_root.left:
                    dq.append(current_root.left)
                    if current_root.left.val is not None:
                        lvl[j].append(current_root.left.val)
                if current_root.right:
                    dq.append(current_root.right)
                    if current_root.right.val is not None:
                        lvl[j].append(current_root.right.val)
            
            if len(lvl[j]):
                result.append(lvl[j])
            j += 1
        return result
        
        
                
                        