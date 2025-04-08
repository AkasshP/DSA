from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level={}
        dq = deque()
        if root:
            level[1] = [root.val]
            dq.append(root)
        j = 2
        while dq:
            level[j]=[]
            for i in range(len(dq)):
                current_root = dq.popleft()
                
                if current_root.left:
                    dq.append(current_root.left)
                    if current_root.left.val is not None:
                        level[j].append(current_root.left.val)
                if current_root.right:
                    dq.append(current_root.right)
                    if current_root.right.val is not None:
                        level[j].append(current_root.right.val) 

            j += 1

        avg_lvl = []
        for keys,values in level.items():
            if values:
                avg_lvl.append((sum(values))/(len(values)))
        return avg_lvl
        



                

