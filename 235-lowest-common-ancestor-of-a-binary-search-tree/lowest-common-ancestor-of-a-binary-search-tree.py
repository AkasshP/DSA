# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anchestor = {}
        node_map = {}
        dq =  deque()
        if root:
            dq.append(root)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                node_map[node.val] = node
                if node.left:
                    anchestor[node.left.val] = node.val
                    dq.append(node.left)
                if node.right:
                    anchestor[node.right.val] =  node.val
                    dq.append(node.right)

        seen = set()
        curr = p.val
        while True:
            seen.add(curr)
            if curr not in anchestor:
                break
            curr = anchestor[curr]

        curr =  q.val
        while curr not in seen:
            curr = anchestor[curr]
        return node_map[curr]

        # def dfs1(u,v):
        #     if u in anchestor and v in anchestor:
        #         if anchestor[u] == anchestor[v]:
        #             return node_map[anchestor[u]]
        #         return dfs1(anchestor[u],anchestor[v])

        # def dfs2(r):
        #     if not r:
        #         return None
        #     # initial encounter element of p.val or q.val thats enough
        #     if r.val in (p.val,q.val):
        #         return node_map[r.val]
        #      # search left subtree
        #     left_ans = dfs2(r.left)
        #     if left_ans is not None:
        #         return left_ans

        #     # otherwise search right subtree
        #     return dfs2(r.right)
        # #case 1: Means both are in different sub-trees common leveling we have to approach
        # if p.val <= root.val <= q.val:
        #     return dfs1(p.val,q.val)
        # #case 2: Means both are in the same subtree just find which one is comes first then that's the lca
        # if p.val <= root.val >= q.val:
        #     return dfs2(root)
