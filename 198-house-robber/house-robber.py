class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #approach of like finding max value
        pocket_A = 0 #skipping
        pocket_B = 0 # taking
        rob = []
        for i in range(len(nums)):

            result = max(pocket_A,nums[i] + pocket_B)
            pocket_B = pocket_A
            pocket_A = result 
            rob.append(result)

        return rob[-1]
