# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        if root:
            dq.append(root)

        def val_conversion(tree):
            temp = []
            for i in tree:
                temp.append(i.val)
            print(temp,'temp')
            return temp

        while dq:
            main_arr = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    main_arr.append(node.left.val)
                else:
                    main_arr.append(None)
                if node.right:
                    dq.append(node.right)
                    main_arr.append(node.right.val)
                else:
                    main_arr.append(None)
            #once all the children are added        
            if len(main_arr) > 1:
                mid = len(main_arr) // 2
                left = main_arr[:mid]
                right = main_arr[mid:]
                print(left,right)
                left.reverse()
                if left == right:
                    pass
                else:
                    return False

        return True