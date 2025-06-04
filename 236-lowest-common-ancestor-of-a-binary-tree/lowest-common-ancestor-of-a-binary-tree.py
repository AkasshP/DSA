# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anchestor_node_height= {}
        nodes = {}
        anchesor_build_tree = {}
        count = 0
        if root:
            dq = deque()
            dq.append(root)
        while dq:
            count += 1
            for i in range(len(dq)):
                node = dq.popleft()
                anchestor_node_height[node.val] = count
                nodes[node.val] = node
                if node.left:
                    dq.append(node.left)
                    anchesor_build_tree[node.left.val] = node.val
                if node.right:
                    dq.append(node.right)
                    anchesor_build_tree[node.right.val] = node.val
        new_anchestor = {}
        # def dfs(i):
        #     result.append(i)
        #     if anchesor_build_tree.get(i) or anchesor_build_tree.get(i) == 0:
        #         return dfs(anchesor_build_tree[i])
        #     else:
        #         return result
        #Don't build anchestors for all the nodes
        # for keys,values in anchesor_build_tree.items():
        #     if anchesor_build_tree.get(values) == 0 or anchesor_build_tree.get(values):
        #         result = []
        #         new_anchestor[keys] = dfs(anchesor_build_tree[values]) + [values]
        #     else:
        #        new_anchestor[keys] = [values] 
        def build_chain(val):
            chain = []
            while val in anchesor_build_tree:
                chain.append(val)
                val = anchesor_build_tree[val]
            chain.append(val)  # add the root
            return chain

        chain_p = build_chain(p.val)
        chain_q = build_chain(q.val)

        if p.val in chain_q:
            return nodes[p.val]
        if q.val in chain_p:
            return nodes[q.val]

        common = set(chain_p).intersection(chain_q)
        if common:
            best = max(common, key=lambda x: anchestor_node_height[x])
            return nodes[best]
        # Fallback (should not happen in a valid tree)
        return None
                        
        
                