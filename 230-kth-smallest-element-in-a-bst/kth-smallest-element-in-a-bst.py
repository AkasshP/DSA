# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, va l=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = set()
        result = []
        count = 0
        def inorder(root,count,k):
            if root:
                    print(root.val)
                    count = inorder(root.left,count,k) #updated count value i have to return
                    if root.val not in visited:
                        count += 1
                        print(count,'count-level')
                        visited.add(root.val)
                        if count == k:
                            result.append(root.val)
                            return count
                    count = inorder(root.right,count,k) #updated count value i  have to return
                    return count 
            else:
                return count
        v = inorder(root,count,k)
        print(visited)
        print(result)
        return result[-1] #last minimmum node val found
            

        