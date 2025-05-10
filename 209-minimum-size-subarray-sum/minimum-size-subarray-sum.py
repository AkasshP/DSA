import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_count = math.inf
        curr = 0
        while right < len(nums):
            curr += nums[right]
            while curr >= target:
                min_count = min(min_count,right - left + 1) #i'm instead of slicing the elements 
                curr -= nums[left]
                left = left + 1
            right = right + 1

        if min_count == inf:
            return 0
        else:
            return min_count

       
                
                    
            

        
