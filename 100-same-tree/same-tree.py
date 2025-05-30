# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque()
        dq2 = deque()
        if p:
            if q:
                if p.val == q.val:
                    dq.append(p)
                    dq2.append(q)
                else:
                    return False
            else:
                return False
        else:
            if q:
                return False
        
        while dq:
            for i in range(len(dq)):
                child = dq.popleft()
                child2 = dq2.popleft()
                if child.left:
                    if child2.left:
                        if child.left.val == child2.left.val:
                            dq.append(child.left)
                            dq2.append(child2.left)
                        else:
                            return False
                    else:
                        return False
                else:
                    if child2.left:
                        return False

                if child.right:
                    if child2.right:
                        if child.right.val == child2.right.val:
                            dq.append(child.right)
                            dq2.append(child2.right)
                        else:
                            return False
                    else:
                        return False
                else:
                    if child2.right:
                        return False
        return True
        # if q:
        #     dq2.append(q)
        #     print(dq2,'checking')
        # while dq2:
        #     for i in range(len(dq2)):
        #         child = dq2.popleft()
        #         print(child.val,'checking q')
        #         if child.left:
        #             dq2.append(child.left)
        #         if child.right:
        #             dq2.append(child.right)
        #bfs
        # for i in range(len()