# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_order = []

        def preorder(root):
            if not root:
                return None
            pre_order.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        for i in pre_order:
            i.left = None
            i.right = None

        for i in range(len(pre_order)):
           if i + 1 < len(pre_order):
                pre_order[i].right = pre_order[i+1]
           else:
                pre_order[i].right = None