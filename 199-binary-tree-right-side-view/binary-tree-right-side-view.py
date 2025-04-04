from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level={}
        rightView=[]
        dq = deque()
        dq.append(root)
        if root:
            level[1] = [root.val]
        j = 2
        while dq:
            level[j] = []
            for i in range(len(dq)):
                curr_root = dq.popleft()
                if curr_root:
                    if curr_root.left:
                        dq.append(curr_root.left)
                        if curr_root.left.val is not None:
                            level[j].append(curr_root.left.val)
                    if curr_root.right:
                        dq.append(curr_root.right)
                        if curr_root.right.val is not None:
                            level[j].append(curr_root.right.val)
            print(level,'dict')
            if not level.get(j):
                level.pop(j)
            j = j + 1
        for key,values in level.items():
            print(values)
            rightView.append(values.pop())
        # print(rightView,'right-view')
        return rightView
    
        

            