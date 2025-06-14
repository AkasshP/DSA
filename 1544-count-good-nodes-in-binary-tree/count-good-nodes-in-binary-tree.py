# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        visited = []
        def dfs(node):
            if not node:
                return 
            if path:
                new_path = tuple(path + [node.val])
                path.append(node.val)
                visited.append(new_path)
            else:
                path.append(node.val)
                visited.append((node.val,))
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        print(visited,'visited')
        final_checklist = []
        for i in visited:
            if len(i) == 1:
                final_checklist.append(i)
            else:
                if max(i) <= i[-1]:
                    final_checklist.append(i)
        return len(final_checklist)