# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use the two list
        binary_tree = []
        def arr(pre,ino):
            if not pre or not ino:
                return
            root_val = pre[0]
            i = ino.index(root_val)
            left_ino  = ino[:i]    # everything before root
            right_ino = ino[i+1:]
            n_left = len(left_ino)
            left_pre  = pre[1 : 1 + n_left]
            right_pre = pre[1 + n_left : ]
            left_node  = arr(left_pre,  left_ino)
            right_node = arr(right_pre, right_ino)

            return TreeNode(root_val, left_node, right_node)

        return arr(preorder, inorder)