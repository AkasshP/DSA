# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        result = []
        temp = []
        if root:
            dq.append(root)
            count = 0
        while dq:
            count += 1
            temp = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)  
                temp.append(node.val)
            if count % 2  == 0:
                temp.reverse()
            result.append(temp)
        return result

        