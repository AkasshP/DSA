# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        h = 0
        def dfs(root):
            if root:
                nonlocal cnt,h
                cnt += 1
                dfs(root.left)
                h = max(h,cnt)
                # print(cnt,root.val,'cnt')
                dfs(root.right)
                cnt -= 1
                # print(cnt,'unwinding')
        dfs(root)
        return h
        # print(h,'updated')
                

