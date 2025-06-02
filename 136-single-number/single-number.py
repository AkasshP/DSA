class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums,'checking')
        i = 0
        while i < len(nums):
            if i+1 < len(nums):
                if nums[i] ^ nums[i+1] == 0:
                    pass
                else:
                    return nums[i]
            if i  == len(nums) - 1:
                return nums[i]
            i += 2

       