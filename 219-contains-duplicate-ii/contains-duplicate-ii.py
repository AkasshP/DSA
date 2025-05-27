class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            if duplicate.get(nums[i]) == 0 or duplicate.get(nums[i]):
                if abs(duplicate[nums[i]] - i) <= k:
                    return True
                else:
                    duplicate[nums[i]] = i
            else:
                duplicate[nums[i]] = i
        return False
                    