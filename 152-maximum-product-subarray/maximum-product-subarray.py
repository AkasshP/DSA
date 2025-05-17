class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #approach gonna be 
        if not nums:
            return 0

        max_ending = nums[0]
        min_ending = nums[0]
        result = nums[0]
        for n in nums[1:]:
            if n < 0:
                max_ending, min_ending = min_ending, max_ending
            max_ending = max(n, max_ending * n)
            min_ending = min(n, min_ending * n)
            result = max(result, max_ending)
        return result