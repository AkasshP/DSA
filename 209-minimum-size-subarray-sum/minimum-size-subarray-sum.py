import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = left + 1
        min_count = math.inf
        curr = sum(nums[left:right])
        while right <= len(nums):
            if curr >= target:
                min_count = min(min_count,len(nums[left:right]))
                curr -= nums[left]
                left = left + 1
            else:
                if right < len(nums):
                    curr += nums[right]
                right = right + 1
        if min_count == inf:
            return 0
        else:
            return min_count

       
                
                    
            

        
