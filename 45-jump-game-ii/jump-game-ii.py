class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        end = 0
        farthest = 0
        if len(nums) < 2:
            return 0
        while end < len(nums) - 1:
                while i <= end:
                    farthest = max(farthest,i + nums[i])
                    i += 1
                count += 1
                end = farthest
        return count


