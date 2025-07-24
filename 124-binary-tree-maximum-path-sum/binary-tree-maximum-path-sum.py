# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dq = deque()
        # path = float('-inf')
        # if root:
        #     dq.append(root)
        # while dq:
        #     for i in range(len(dq)):
        #         node = dq.popleft()
        #         path = max(path,node.val) #hold the root value in the path and see
        #         if node.left:
        #             dq.append(node.left)

        #         if node.right:
        #             dq.append(node.right)
                
        #         #negative root
        #         if node.val < 0:
        #             if node.left and node.right:
        #                 if node.left.val < 0 and node.right.val < 0: #netative roots and children ateast find least maximum among negative
        #                     path = max(path, max(node.val,max(node.left.val,node.right.val)))
        #                 else:   #negative root and any positive children , don't wanna compare root because already negative waste of comapring
        #                     if node.left.val < 0 or node.right.val < 0:
        #                         path = max(path,max(node.left.val,node.right.val))
        #                     else: #both values are positive
        #                         if node.left.val > 0 and  node.right.val > 0:
        #                             path = max(path,max(node.left.val, node.right.val))
        #             else: # negative root and left or right alone don't wanna summ it decreases the optimal
        #                 if node.left:
        #                     if node.left.val < 0: #found left node but negative then, compare it with root
        #                         path = max(path, max(node.val,node.left.val))
        #                     else:  #positive then sum it up and see
        #                         path = max(path,(path + node.left.val))
        #                 if node.right:
        #                     if node.right.val < 0: #found right node but negative then, compare it with root
        #                         path = max(path, max(node.val,node.right.val))
        #                     else:  #positive then sum it up and see
        #                         path = max(path,(path + node.right.val))
        #         #positve root 
        #         else:
        #             if node.left and node.right: #both values present
        #                 if node.left.val < 0 and  node.right.val < 0: # both are negative
        #                     path = max(path, node.val) #directly compare the root
        #                 else:
        #                     if node.left.val < 0 or node.right.val < 0: #any one positive value so check that alone, and sum it up with root +ve value
        #                         path = max(path,path + max(node.left.val,node.right.val))
        #                     else:
        #                         if  node.left.val > 0 and node.right.val > 0: #both the children are positive then sum it up both with root maximises the path
        #                             path = max(path,(path + node.left.val + node.right.val))
        #             else:
        #                 #either left or right node alone
        #                 if node.left: 
        #                     if node.left.val < 0: #found left node but negative then, compare it with root
        #                         path = max(path, node.val) 
        #                     else:  #positive then sum it up and see
        #                         path = max(path,(path + node.left.val))
        #                 if node.right: 
        #                     if node.right.val < 0: #found right node but negative then, compare it with root
        #                         path = max(path, node.val) 
        #                     else:  #positive then sum it up and see
        #                         path = max(path,(path + node.right.val))
        # return path
        self.best = float('-inf')

        def dfs(rt):
            if not rt:
                return 0
            left_gain = max(dfs(rt.left),0)
            right_gain = max(dfs(rt.right),0)
            new_path = rt.val + left_gain + right_gain
            self.best = max(self.best,new_path)

            return rt.val + max(left_gain,right_gain)
        dfs(root)
        return self.best
