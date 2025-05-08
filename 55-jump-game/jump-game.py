class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        max_reach = 0
        for i,step in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach,i + step)
            # i + step secret here based on the iteration we are iterating
            if max_reach >= len(nums) - 1:
                return True
        