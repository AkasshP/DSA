# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # tree tracking by dfs start from root to leaf node.
        trg = 0
        node_count = 0
        def dfs(node,trg,targetSum,node_count):
            if node is None:
                print(trg,'trg-sum')
                if trg == targetSum and node_count > 1:
                    return True

            # process node here (e.g., print(node.val))
            if node:
                trg += node.val
                node_count += 1
                if node.left:
                    if dfs(node.left,trg,targetSum,node_count):
                        return True
                if node.right:
                    if dfs(node.right,trg, targetSum,node_count):
                        return True

                if node.left is None and node.right is None:
                    print(trg,'trg-sum')
                    if trg == targetSum and node_count > 1:
                        return True
            return False
        if root:
            if root.left is None and root.right is None:
                if root.val == targetSum: #additional edge case
                    return True
                else:
                    return False
            else:
                flag = dfs(root,trg,targetSum,node_count)
                return flag
        else:
            return False
        