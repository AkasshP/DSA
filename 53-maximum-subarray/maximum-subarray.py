class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
           if len(nums) < 3:
                if len(nums) == 1:
                        return nums[0]
                elif len(nums) == 2:
                    return max(nums[0] + nums[1],max(nums))
                else:
                    return 0
           else:
                c_sum = b_sum = nums[0]
                for i in range(1,len(nums)):
                    c_sum = max(nums[i],c_sum + nums[i])
                    b_sum = max(b_sum,c_sum)
                return b_sum
                
